import { createRequire } from "node:module";
import { createServer } from "node:http";
import { basename, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { mkdir, mkdtemp, readFile, readdir, rm, stat, writeFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import { tmpdir } from "node:os";

const STATE_ROWS = [
  { id: "idle", frames: 6, fps: 10, prefs: ["idle", "stand", "room_idle", "ui_idle", "animation"] },
  { id: "running-right", frames: 8, fps: 12, prefs: ["move", "walk", "run", "posture", "idle", "animation"] },
  { id: "running-left", frames: 8, fps: 12, prefs: ["move", "walk", "run", "posture", "idle", "animation"] },
  { id: "waving", frames: 4, fps: 10, prefs: ["click", "giddy", "show", "touch", "skill", "attack", "idle", "animation"] },
  { id: "jumping", frames: 5, fps: 12, prefs: ["idle_birthday_up", "skill1", "skill", "attack", "move", "walk", "posture", "idle", "animation"] },
  { id: "failed", frames: 8, fps: 10, prefs: ["hit", "hurt", "die", "dead", "skill", "idle", "animation"] },
  { id: "waiting", frames: 6, fps: 10, prefs: ["sleep", "idle2", "room", "idle", "animation"] },
  { id: "running", frames: 6, fps: 12, prefs: ["idle_birthday_loop", "posture", "skill2", "skill", "attack", "move", "walk", "idle", "animation"] },
  { id: "review", frames: 6, fps: 10, prefs: ["unique", "click", "show", "idle", "animation"] },
];

function parseArgs(argv) {
  const args = {};
  for (let index = 2; index < argv.length; index += 1) {
    const token = argv[index];
    if (!token.startsWith("--")) continue;
    const key = token.slice(2);
    const next = argv[index + 1];
    if (!next || next.startsWith("--")) {
      args[key] = true;
    } else {
      args[key] = next;
      index += 1;
    }
  }
  return args;
}

function usage() {
  return [
    "Usage:",
    "  node tools/render_spine_frames.mjs --spine-dir <dir> --output <dir> --deps-dir <dir>",
    "",
    "Options:",
    "  --state <id|all>          Render one state or all Codex pet states. Default: all.",
    "  --skeleton <file>         Skeleton file. Default: first *_room.skel, then first *.skel.",
    "  --atlas <file>            Atlas file. Default: first *.atlas.",
    "  --motion-map <file>       JSON map of Codex state id to Spine animation name.",
    "  --list-animations         Print animation names and exit after loading.",
    "  --flip-running-left       Mirror only the running-left state horizontally.",
    "  --width <px>              Capture canvas width. Default: 1200.",
    "  --height <px>             Capture canvas height. Default: 1200.",
    "  --scale <number>          Spine container zoom. Default: 1.",
    "  --x <number>              Spine container x in pixels. Default: canvas center.",
    "  --y <number>              Spine container y in pixels. Default: canvas lower third.",
  ].join("\n");
}

function requirePathInside(child, parent) {
  const normalizedChild = resolve(child);
  const normalizedParent = resolve(parent);
  if (normalizedChild !== normalizedParent && !normalizedChild.startsWith(normalizedParent + "\\")) {
    throw new Error(`Refusing to serve path outside Spine directory: ${normalizedChild}`);
  }
  return normalizedChild;
}

async function findFirst(spineDir, requested, matcher, label) {
  if (requested) {
    const requestedPath = resolve(spineDir, requested);
    if (!existsSync(requestedPath)) throw new Error(`${label} not found: ${requestedPath}`);
    return requestedPath;
  }
  const files = await readdir(spineDir);
  const preferred = files.find((file) => matcher(file, true));
  const fallback = files.find((file) => matcher(file, false));
  const found = preferred || fallback;
  if (!found) throw new Error(`No ${label} found in ${spineDir}`);
  return join(spineDir, found);
}

function parseAtlasPages(atlasText) {
  const pages = [];
  let expectPage = true;
  for (const rawLine of atlasText.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line) {
      expectPage = true;
      continue;
    }
    if (expectPage && !line.includes(":")) {
      pages.push(line);
      expectPage = false;
    }
  }
  return pages;
}

function normalizeMotionName(name) {
  return String(name || "").trim();
}

async function loadMotionOverrides(path) {
  if (!path) return {};
  const motionMap = JSON.parse(await readFile(resolve(path), "utf8"));
  if (!motionMap || typeof motionMap !== "object" || Array.isArray(motionMap)) {
    throw new Error(`Motion map must be a JSON object: ${path}`);
  }
  return motionMap;
}

function chooseAnimation(animations, prefs) {
  const lowered = animations.map((name) => ({ name, key: name.toLowerCase() }));
  for (const pref of prefs) {
    const exact = lowered.find((entry) => entry.key === pref.toLowerCase());
    if (exact) return exact.name;
  }
  for (const pref of prefs) {
    const partial = lowered.find((entry) => entry.key.includes(pref.toLowerCase()));
    if (partial) return partial.name;
  }
  return animations[0] || "";
}

async function buildBrowserBundle(depsDir, workDir) {
  const requireFromDeps = createRequire(join(resolve(depsDir), "package.json"));
  const esbuild = requireFromDeps("esbuild");
  const entryPath = join(workDir, "entry.js");
  const bundlePath = join(workDir, "bundle.js");
  await writeFile(
    entryPath,
    `
      import { Application, Assets } from "pixi.js";
      import { Spine } from "@esotericsoftware/spine-pixi-v8";

      async function createSpine(job) {
        const app = new Application();
        await app.init({
          width: job.width,
          height: job.height,
          backgroundAlpha: 0,
          antialias: true,
          preserveDrawingBuffer: true,
        });
        document.body.replaceChildren(app.canvas);
        app.canvas.style.display = "block";
        Assets.add({ alias: "skeleton", src: job.skeletonUrl });
        Assets.add({ alias: "atlas", src: job.atlasUrl, data: { images: job.imageMap } });
        await Assets.load(["skeleton", "atlas"]);
        const spine = Spine.from({ skeleton: "skeleton", atlas: "atlas", scale: job.skeletonScale, autoUpdate: false });
        spine.x = job.x;
        spine.y = job.y;
        spine.scale.set(job.flipX ? -job.scale : job.scale, job.scale);
        app.stage.addChild(spine);
        return { app, spine };
      }

      window.listSpineAnimations = async (job) => {
        const { app, spine } = await createSpine(job);
        const names = spine.skeleton.data.animations.map((animation) => animation.name);
        app.destroy(true);
        return names;
      };

      function unionBoundingBox(a, b) {
        if (!a) return b;
        if (!b) return a;
        return {
          left: Math.min(a.left, b.left),
          top: Math.min(a.top, b.top),
          right: Math.max(a.right, b.right),
          bottom: Math.max(a.bottom, b.bottom),
        };
      }

      function paddedBoundingBox(box, width, height, padding) {
        if (!box) return { left: 0, top: 0, right: width, bottom: height };
        return {
          left: Math.max(0, box.left - padding),
          top: Math.max(0, box.top - padding),
          right: Math.min(width, box.right + padding),
          bottom: Math.min(height, box.bottom + padding),
        };
      }

      function spineBoundingBox(spine) {
        const bounds = spine.getBounds();
        const left = Math.floor(bounds.x);
        const top = Math.floor(bounds.y);
        const right = Math.ceil(bounds.x + bounds.width);
        const bottom = Math.ceil(bounds.y + bounds.height);
        return right > left && bottom > top ? { left, top, right, bottom } : null;
      }

      function prepareAnimation(spine, job) {
        spine.x = job.x;
        spine.y = job.y;
        spine.scale.set(job.flipX ? -job.scale : job.scale, job.scale);
        spine.state.clearTracks();
        spine.skeleton.setToSetupPose();
        spine.state.setAnimation(0, job.animationName, true);
      }

      async function captureStateBounds(app, spine, job) {
        prepareAnimation(spine, job);
        let union = null;
        for (let warmup = 0; warmup < 4; warmup += 1) {
          spine.update(1 / 60);
          app.renderer.render(app.stage);
        }
        for (let index = 0; index < job.frames; index += 1) {
          spine.update(job.intervalMs / 1000);
          app.renderer.render(app.stage);
          union = unionBoundingBox(union, spineBoundingBox(spine));
        }
        return union;
      }

      async function renderStateDataUrls(app, spine, job, crop) {
        const width = Math.max(1, crop.right - crop.left);
        const height = Math.max(1, crop.bottom - crop.top);
        const canvas = document.createElement("canvas");
        canvas.width = width;
        canvas.height = height;
        const context = canvas.getContext("2d", { willReadFrequently: true });
        const frames = [];
        prepareAnimation(spine, job);
        for (let warmup = 0; warmup < 4; warmup += 1) {
          spine.update(1 / 60);
          app.renderer.render(app.stage);
        }
        for (let index = 0; index < job.frames; index += 1) {
          spine.update(job.intervalMs / 1000);
          app.renderer.render(app.stage);
          context.clearRect(0, 0, width, height);
          context.drawImage(app.canvas, crop.left, crop.top, width, height, 0, 0, width, height);
          frames.push(canvas.toDataURL("image/png"));
        }
        return frames;
      }

      window.renderSpineFrames = async (job) => {
        const { app, spine } = await createSpine(job);
        const union = await captureStateBounds(app, spine, job);
        const crop = paddedBoundingBox(union, job.width, job.height, 8);
        const frames = await renderStateDataUrls(app, spine, job, crop);
        app.destroy(true);
        return frames;
      };

      window.renderSpineStates = async (job) => {
        const { app, spine } = await createSpine(job);
        let union = null;
        for (const stateJob of job.states) {
          union = unionBoundingBox(union, await captureStateBounds(app, spine, { ...job, ...stateJob }));
        }
        const crop = paddedBoundingBox(union, job.width, job.height, 8);
        const result = {};
        for (const stateJob of job.states) {
          result[stateJob.id] = await renderStateDataUrls(app, spine, { ...job, ...stateJob }, crop);
        }
        app.destroy(true);
        return result;
      };
    `,
    "utf8",
  );
  await esbuild.build({
    entryPoints: [entryPath],
    bundle: true,
    outfile: bundlePath,
    platform: "browser",
    format: "iife",
    target: "es2020",
    absWorkingDir: resolve(depsDir),
    nodePaths: [join(resolve(depsDir), "node_modules")],
  });
  return bundlePath;
}

function contentType(pathname) {
  if (pathname.endsWith(".js")) return "text/javascript";
  if (pathname.endsWith(".json")) return "application/json";
  if (pathname.endsWith(".png")) return "image/png";
  if (pathname.endsWith(".atlas")) return "text/plain";
  if (pathname.endsWith(".skel")) return "application/octet-stream";
  return "application/octet-stream";
}

async function startServer({ spineDir, bundlePath }) {
  const html = "<!doctype html><html><head><meta charset='utf-8'></head><body style='margin:0;background:transparent'><script src='/bundle.js'></script></body></html>";
  const server = createServer(async (request, response) => {
    try {
      const url = new URL(request.url, "http://127.0.0.1");
      if (url.pathname === "/") {
        response.writeHead(200, { "Content-Type": "text/html" });
        response.end(html);
        return;
      }
      if (url.pathname === "/bundle.js") {
        response.writeHead(200, { "Content-Type": "text/javascript" });
        response.end(await readFile(bundlePath));
        return;
      }
      if (url.pathname.startsWith("/model/")) {
        const relative = decodeURIComponent(url.pathname.slice("/model/".length));
        const filePath = requirePathInside(join(spineDir, relative), spineDir);
        const info = await stat(filePath);
        if (!info.isFile()) throw new Error(`Not a file: ${filePath}`);
        response.writeHead(200, { "Content-Type": contentType(filePath) });
        response.end(await readFile(filePath));
        return;
      }
      response.writeHead(404);
      response.end("Not found");
    } catch (error) {
      response.writeHead(500, { "Content-Type": "text/plain" });
      response.end(String(error.stack || error));
    }
  });
  await new Promise((resolvePromise) => server.listen(0, "127.0.0.1", resolvePromise));
  const address = server.address();
  return { server, baseUrl: `http://127.0.0.1:${address.port}` };
}

function dataUrlToBuffer(dataUrl) {
  const marker = "base64,";
  const index = dataUrl.indexOf(marker);
  if (index < 0) throw new Error("Unexpected frame data URL.");
  return Buffer.from(dataUrl.slice(index + marker.length), "base64");
}

async function main() {
  const args = parseArgs(process.argv);
  const spineDir = args["spine-dir"] ? resolve(args["spine-dir"]) : "";
  const outputDir = args.output ? resolve(args.output) : "";
  const depsDir = resolve(args["deps-dir"] || process.env.LIVE2D_RENDER_DEPS || join(tmpdir(), "9pets-live2d-test"));

  if (!spineDir || (!outputDir && !args["list-animations"])) {
    console.error(usage());
    process.exit(2);
  }
  if (!existsSync(spineDir)) throw new Error(`Spine directory not found: ${spineDir}`);
  if (!existsSync(depsDir)) throw new Error(`Renderer dependency directory not found: ${depsDir}`);

  const selectedState = args.state || "all";
  const states = selectedState === "all" ? STATE_ROWS : STATE_ROWS.filter((state) => state.id === selectedState);
  if (!states.length) throw new Error(`Unknown state: ${selectedState}`);

  const skeletonPath = await findFirst(
    spineDir,
    args.skeleton,
    (file, preferred) => file.endsWith(".skel") && (preferred ? file.includes("_room") : true),
    "skeleton",
  );
  const atlasPath = await findFirst(spineDir, args.atlas, (file) => file.endsWith(".atlas"), "atlas");
  const atlasText = await readFile(atlasPath, "utf8");
  const pages = parseAtlasPages(atlasText);
  if (!pages.length) throw new Error(`No atlas pages found in ${atlasPath}`);
  const imageMap = {};
  for (const page of pages) {
    imageMap[page] = `/model/${encodeURIComponent(page)}`;
  }

  const width = Number(args.width || 1200);
  const height = Number(args.height || 1200);
  const scale = Number(args.scale || 1);
  const skeletonScale = Number(args["skeleton-scale"] || 1);
  const x = Number(args.x || width / 2);
  const y = Number(args.y || height * 0.75);
  const flipRunningLeft = Boolean(args["flip-running-left"]);
  const motionOverrides = await loadMotionOverrides(args["motion-map"]);

  const workDir = await mkdtemp(join(tmpdir(), "9pets-spine-"));
  let server;

  try {
    const bundlePath = await buildBrowserBundle(depsDir, workDir);
    const serverInfo = await startServer({ spineDir, bundlePath });
    server = serverInfo.server;
    const requireFromDeps = createRequire(join(resolve(depsDir), "package.json"));
    const { chromium } = requireFromDeps("playwright");
    const browser = await chromium.launch();
    const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
    await page.goto(serverInfo.baseUrl, { waitUntil: "load" });
    const baseJob = {
      width,
      height,
      scale,
      x,
      y,
      skeletonScale,
      skeletonUrl: `/model/${encodeURIComponent(basename(skeletonPath))}`,
      atlasUrl: `/model/${encodeURIComponent(basename(atlasPath))}`,
      imageMap,
    };
    const animations = await page.evaluate((job) => window.listSpineAnimations(job), baseJob);
    console.log(`skeleton ${basename(skeletonPath)}`);
    console.log(`atlas ${basename(atlasPath)}`);
    console.log(`animations ${animations.join(", ")}`);
    if (args["list-animations"]) {
      await browser.close();
      return;
    }
    const renderJobs = [];
    for (const state of states) {
      const override = normalizeMotionName(motionOverrides[state.id] || "");
      let animationName = override && animations.includes(override) ? override : chooseAnimation(animations, state.prefs);
      if (override && !animations.includes(override)) {
        console.log(`${state.id} missing override ${override}; fallback ${animationName}`);
      }
      if (!animations.includes(animationName)) {
        throw new Error(`Animation not found for ${state.id}: ${animationName}`);
      }
      renderJobs.push({
        id: state.id,
        animationName,
        frames: state.frames,
        intervalMs: Math.round(1000 / state.fps),
        flipX: flipRunningLeft && state.id === "running-left",
      });
    }
    const renderedStates = await page.evaluate(
      (job) => window.renderSpineStates(job),
      { ...baseJob, states: renderJobs },
    );
    for (const job of renderJobs) {
      const frameData = renderedStates[job.id];
      const stateDir = join(outputDir, job.id);
      await rm(stateDir, { recursive: true, force: true });
      await mkdir(stateDir, { recursive: true });
      for (let index = 0; index < frameData.length; index += 1) {
        await writeFile(join(stateDir, `${String(index).padStart(2, "0")}.png`), dataUrlToBuffer(frameData[index]));
      }
      console.log(`${job.id} animation ${job.animationName}`);
      console.log(`rendered ${job.id} ${frameData.length} frames`);
    }
    await browser.close();
  } finally {
    if (server) await new Promise((resolvePromise) => server.close(resolvePromise));
    await rm(workDir, { recursive: true, force: true });
  }
}

main().catch((error) => {
  console.error(error.stack || error);
  process.exit(1);
});
