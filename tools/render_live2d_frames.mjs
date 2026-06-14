import { createServer } from "node:http";
import { createRequire } from "node:module";
import { basename, dirname, join, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";
import { mkdir, mkdtemp, readFile, readdir, rm, stat, writeFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import { tmpdir } from "node:os";

const STATE_ROWS = [
  { id: "idle", group: "Idle", frames: 6, fps: 10, prefs: ["b_idle", "e_idle", "t_idle", "idle"] },
  { id: "running-right", group: "RunRight", frames: 8, fps: 12, prefs: ["b_ruchang", "b_xingli", "b_yaoqing", "b_baishou", "b_yangtou", "b_yaotou", "b_diantou", "b_idle"] },
  { id: "running-left", group: "RunLeft", frames: 8, fps: 12, prefs: ["b_ruchang", "b_xingli", "b_yaoqing", "b_baishou", "b_yangtou", "b_yaotou", "b_diantou", "b_idle"] },
  { id: "waving", group: "Wave", frames: 4, fps: 10, prefs: ["b_shenshou", "b_taishou", "b_jushou", "b_baishou", "b_tanshou", "b_yaoqing", "shenshou"] },
  { id: "jumping", group: "Jump", frames: 5, fps: 12, prefs: ["b_gongji", "b_ruchang", "b_xingli", "b_yangtou", "b_diantou", "b_idle"] },
  { id: "failed", group: "Failed", frames: 8, fps: 10, prefs: ["t_nanguo", "e_nanguo", "t_shengqi", "e_shengqi", "t_liulei", "t_zhaoji", "t_jinzhang"] },
  { id: "waiting", group: "Waiting", frames: 6, fps: 10, prefs: ["b_waitou", "b_tanshou", "b_qidao", "t_yihuo", "t_chensi", "b_diantou", "b_idle"] },
  { id: "running", group: "Working", frames: 6, fps: 12, prefs: ["b_sikao", "b_sisuo", "b_guancha", "b_yuedu", "b_zhengli", "b_moxiaba", "t_renzhen", "t_sikao", "t_haoqi", "b_diantou"] },
  { id: "review", group: "Review", frames: 6, fps: 10, prefs: ["b_sikao", "b_guancha", "b_yuedu", "t_renzhen", "t_sikao", "b_sisuo", "t_yansu", "b_diantou"] },
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
    "  node tools/render_live2d_frames.mjs --model-dir <dir> --output <dir> --deps-dir <dir> --cubism-core <file>",
    "",
    "Options:",
    "  --state <id|all>       Render one state or all Codex pet states. Default: all.",
    "  --model-json <file>    Model3 JSON filename. Default: first *.model3.json in model-dir.",
    "  --motion-map <file>    JSON map of Codex state id to motion filename.",
    "  --width <px>           Capture canvas width. Default: 1024.",
    "  --height <px>          Capture canvas height. Default: 1200.",
    "  --scale <number>       Live2D model zoom. Default: 0.56.",
    "  --x <number>           Live2D camera x in pixels. Default: 640.",
    "  --y <number>           Live2D camera y in pixels. Default: 140.",
    "  --primary-texture <path> Move this texture to the front of the patched model texture list.",
  ].join("\n");
}

function requirePathInside(child, parent) {
  const normalizedChild = resolve(child);
  const normalizedParent = resolve(parent);
  if (normalizedChild === normalizedParent) return normalizedChild;
  if (!normalizedChild.startsWith(normalizedParent + sep)) {
    throw new Error(`Path escapes root: ${child}`);
  }
  return normalizedChild;
}

async function findModelJson(modelDir, requested) {
  if (requested) {
    const requestedPath = resolve(modelDir, requested);
    if (!existsSync(requestedPath)) throw new Error(`Model JSON not found: ${requestedPath}`);
    return requestedPath;
  }
  const files = await readdir(modelDir);
  const model = files.find((file) => file.endsWith(".model3.json"));
  if (!model) throw new Error(`No *.model3.json found in ${modelDir}`);
  return join(modelDir, model);
}

async function listMotionFiles(modelDir) {
  const motionDir = join(modelDir, "motions");
  if (!existsSync(motionDir)) return [];
  const files = await readdir(motionDir);
  return files.filter((file) => file.endsWith(".motion3.json")).sort();
}

function chooseMotion(motionFiles, prefs) {
  const lowered = motionFiles.map((file) => ({ file, key: file.toLowerCase().replace(/\.motion3\.json$/, "") }));
  for (const pref of prefs) {
    const match = lowered.find((entry) => entry.key === pref || entry.key.includes(pref));
    if (match) return match.file;
  }
  return motionFiles[0] || "";
}

function normalizeMotionFilename(name) {
  if (!name) return "";
  return name.endsWith(".motion3.json") ? name : `${name}.motion3.json`;
}

async function loadMotionOverrides(path) {
  if (!path) return {};
  const motionMap = JSON.parse(await readFile(resolve(path), "utf8"));
  if (!motionMap || typeof motionMap !== "object" || Array.isArray(motionMap)) {
    throw new Error(`Motion map must be a JSON object: ${path}`);
  }
  return motionMap;
}

function prioritizeTexture(textures, primaryTexture) {
  if (!Array.isArray(textures)) return textures;
  if (!primaryTexture) {
    const first = String(textures[0] || "").replaceAll("\\", "/").toLowerCase();
    if (first.includes("bloom")) {
      const index = textures.findIndex((texture, textureIndex) => {
        if (textureIndex === 0) return false;
        const normalizedTexture = String(texture).replaceAll("\\", "/").toLowerCase();
        return normalizedTexture.endsWith(".png") && !normalizedTexture.includes("bloom");
      });
      if (index > 0) {
        const ordered = textures.slice();
        const [primary] = ordered.splice(index, 1);
        ordered.unshift(primary);
        console.log(`auto primary texture ${primary}`);
        return ordered;
      }
    }
    return textures;
  }
  const normalizedPrimary = primaryTexture.replaceAll("\\", "/").toLowerCase();
  const primaryBase = basename(normalizedPrimary);
  const index = textures.findIndex((texture) => {
    const normalizedTexture = String(texture).replaceAll("\\", "/").toLowerCase();
    return normalizedTexture === normalizedPrimary || basename(normalizedTexture) === primaryBase;
  });
  if (index <= 0) return textures;
  const ordered = textures.slice();
  const [primary] = ordered.splice(index, 1);
  ordered.unshift(primary);
  console.log(`primary texture ${primary}`);
  return ordered;
}

function textureWithoutBloom(texture) {
  return String(texture).replaceAll("\\", "/").replace(/_bloom(?=\.png$)/i, "").toLowerCase();
}

function filterRenderTextures(textures) {
  if (!Array.isArray(textures)) return textures;
  const canonical = new Set(textures.map((texture) => textureWithoutBloom(texture)));
  const filtered = textures.filter((texture) => {
    const value = String(texture).replaceAll("\\", "/").toLowerCase();
    if (!/_bloom(?=\.png$)/i.test(value)) return true;
    return !canonical.has(textureWithoutBloom(texture));
  });
  return filtered.length ? filtered : textures;
}

function countMotionSegments(curves) {
  let totalSegmentCount = 0;
  let totalPointCount = 0;
  for (const curve of curves || []) {
    const segments = curve.Segments || [];
    for (let position = 0; position < segments.length; ) {
      if (position === 0) {
        totalPointCount += 1;
        position += 2;
      }
      const segmentType = segments[position];
      if (segmentType === 1) {
        totalPointCount += 3;
        position += 7;
      } else {
        totalPointCount += 1;
        position += 3;
      }
      totalSegmentCount += 1;
    }
  }
  return { totalSegmentCount, totalPointCount };
}

async function patchMotionFile(modelDir, motionFile, patchedMotionPaths) {
  const originalPath = join(modelDir, "motions", motionFile);
  const motion = JSON.parse(await readFile(originalPath, "utf8"));
  motion.Meta = motion.Meta || {};
  motion.Meta.CurveCount = Array.isArray(motion.Curves) ? motion.Curves.length : 0;
  const counts = countMotionSegments(motion.Curves);
  motion.Meta.TotalSegmentCount = counts.totalSegmentCount;
  motion.Meta.TotalPointCount = counts.totalPointCount;
  if (!Array.isArray(motion.UserData)) {
    motion.UserData = [];
    motion.Meta.UserDataCount = 0;
    motion.Meta.TotalUserDataSize = 0;
  } else {
    motion.Meta.UserDataCount = motion.UserData.length;
    motion.Meta.TotalUserDataSize = motion.UserData.reduce((sum, item) => sum + String(item.Value || "").length, 0);
  }

  const patchedName = `.9pets-${Date.now()}-${motionFile}`;
  const patchedPath = join(modelDir, "motions", patchedName);
  await writeFile(patchedPath, JSON.stringify(motion), "utf8");
  patchedMotionPaths.push(patchedPath);
  return patchedName;
}

async function createPatchedModel(modelDir, modelJsonPath, states, motionOverrides = {}, options = {}) {
  const model = JSON.parse(await readFile(modelJsonPath, "utf8"));
  const motionFiles = await listMotionFiles(modelDir);
  if (!motionFiles.length) throw new Error(`No motion files found under ${join(modelDir, "motions")}`);
  const patchedTexturePaths = [];

  if (Array.isArray(model.FileReferences?.Textures)) {
    let placeholderTexture = "";
    const transparentPng = Buffer.from(
      "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNgYPgPAAEDAQDABJzQAAAAAElFTkSuQmCC",
      "base64",
    );
    model.FileReferences.Textures = filterRenderTextures(model.FileReferences.Textures);
    model.FileReferences.Textures = prioritizeTexture(model.FileReferences.Textures, options.primaryTexture);
    model.FileReferences.Textures = await Promise.all(
      model.FileReferences.Textures.map(async (texture) => {
        if (existsSync(join(modelDir, texture))) return texture;
        if (!placeholderTexture) {
          placeholderTexture = `.9pets-transparent-${Date.now()}.png`;
          const placeholderPath = join(modelDir, placeholderTexture);
          await writeFile(placeholderPath, transparentPng);
          patchedTexturePaths.push(placeholderPath);
        }
        return placeholderTexture;
      }),
    );
  }

  const motions = {};
  const patchedMotionPaths = [];
  const patchedMotionNames = new Map();
  for (const state of states) {
    const override = normalizeMotionFilename(motionOverrides[state.id] || motionOverrides[state.group] || "");
    const motionFile = override || chooseMotion(motionFiles, state.prefs);
    if (!motionFiles.includes(motionFile)) {
      throw new Error(`Motion override for ${state.id} not found: ${motionFile}`);
    }
    if (!patchedMotionNames.has(motionFile)) {
      patchedMotionNames.set(motionFile, await patchMotionFile(modelDir, motionFile, patchedMotionPaths));
    }
    motions[state.group] = [{ File: `motions/${patchedMotionNames.get(motionFile)}` }];
    console.log(`${state.id} motion ${motionFile}`);
  }

  model.FileReferences = model.FileReferences || {};
  model.FileReferences.Motions = motions;
  const patchedName = `.9pets-${Date.now()}-${basename(modelJsonPath)}`;
  const patchedPath = join(modelDir, patchedName);
  await writeFile(patchedPath, JSON.stringify(model, null, 2), "utf8");
  return { patchedModelPath: patchedPath, patchedMotionPaths, patchedTexturePaths };
}

async function buildBrowserBundle(depsDir, workDir) {
  const requireFromDeps = createRequire(join(resolve(depsDir), "package.json"));
  const esbuild = requireFromDeps("esbuild");
  const pathBrowserify = requireFromDeps.resolve("path-browserify");
  const entry = join(workDir, "capture-client.js");
  const bundle = join(workDir, "capture-bundle.js");
  await writeFile(
    entry,
    `
      import { Live2DCubismModel } from "live2d-renderer";

      const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

      window.renderLive2DFrames = async (job) => {
        const canvas = document.querySelector("#stage");
        canvas.width = job.width;
        canvas.height = job.height;
        const model = new Live2DCubismModel(canvas, {
          autoAnimate: false,
          autoInteraction: false,
          tapInteraction: false,
          randomMotion: false,
          cubismCorePath: job.cubismCoreUrl,
          keepAspect: false,
          premultipliedAlpha: true,
          checkMocConsistency: false,
          scale: job.scale,
          x: job.x,
          y: job.y,
          enablePhysics: true,
          enableEyeblink: true,
          enableBreath: true,
          enableLipsync: false,
          enableMotion: true,
          enableExpression: true,
          enableMovement: true,
          enablePose: true,
        });

        await model.load(job.modelUrl);
        model.centerModel();
        model.scale = job.scale;
        model.x = job.x;
        model.y = job.y;
        await model.startMotion(job.motionGroup, 0, 3);

        for (let i = 0; i < 8; i += 1) {
          await sleep(16);
          model.update();
        }

        const frames = [];
        for (let i = 0; i < job.frames; i += 1) {
          await sleep(job.intervalMs);
          model.update();
          frames.push(canvas.toDataURL("image/png"));
        }
        model.destroy(false);
        return frames;
      };
    `,
    "utf8",
  );

  await esbuild.build({
    entryPoints: [entry],
    bundle: true,
    outfile: bundle,
    platform: "browser",
    format: "iife",
    absWorkingDir: resolve(depsDir),
    nodePaths: [join(resolve(depsDir), "node_modules")],
    alias: {
      path: pathBrowserify,
    },
    logLevel: "silent",
  });
  return bundle;
}

function contentType(pathname) {
  if (pathname.endsWith(".js")) return "text/javascript";
  if (pathname.endsWith(".json")) return "application/json";
  if (pathname.endsWith(".png")) return "image/png";
  if (pathname.endsWith(".moc3")) return "application/octet-stream";
  return "application/octet-stream";
}

async function startServer({ modelDir, bundlePath, cubismCorePath }) {
  const html = `<!doctype html><html><body style="margin:0;background:transparent"><canvas id="stage"></canvas><script src="/bundle.js"></script></body></html>`;
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
      if (url.pathname === "/core/live2dcubismcore.min.js") {
        response.writeHead(200, { "Content-Type": "text/javascript" });
        response.end(await readFile(cubismCorePath));
        return;
      }
      if (url.pathname.startsWith("/model/")) {
        const relative = decodeURIComponent(url.pathname.slice("/model/".length));
        const filePath = requirePathInside(join(modelDir, relative), modelDir);
        await stat(filePath);
        response.writeHead(200, { "Content-Type": contentType(filePath) });
        response.end(await readFile(filePath));
        return;
      }
      response.writeHead(404);
      response.end("Not found");
    } catch (error) {
      response.writeHead(500);
      response.end(String(error.stack || error));
    }
  });

  await new Promise((resolveServer) => server.listen(0, "127.0.0.1", resolveServer));
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
  const modelDir = args["model-dir"] ? resolve(args["model-dir"]) : "";
  const outputDir = args.output ? resolve(args.output) : "";
  const depsDir = resolve(args["deps-dir"] || process.env.LIVE2D_RENDER_DEPS || join(tmpdir(), "9pets-live2d-test"));
  const cubismCore = resolve(args["cubism-core"] || process.env.LIVE2D_CUBISM_CORE || join(depsDir, "live2dcubismcore.min.js"));

  if (!modelDir || !outputDir) {
    console.error(usage());
    process.exit(2);
  }
  if (!existsSync(modelDir)) throw new Error(`Model directory not found: ${modelDir}`);
  if (!existsSync(depsDir)) throw new Error(`Renderer dependency directory not found: ${depsDir}`);
  if (!existsSync(cubismCore)) throw new Error(`Cubism Core not found: ${cubismCore}`);

  const selectedState = args.state || "all";
  const states = selectedState === "all" ? STATE_ROWS : STATE_ROWS.filter((state) => state.id === selectedState);
  if (!states.length) throw new Error(`Unknown state: ${selectedState}`);

  const width = Number(args.width || 1024);
  const height = Number(args.height || 1200);
  const scale = Number(args.scale || 0.56);
  const x = Number(args.x || 640);
  const y = Number(args.y || 140);

  const workDir = await mkdtemp(join(tmpdir(), "9pets-live2d-"));
  const modelJsonPath = await findModelJson(modelDir, args["model-json"]);
  const motionOverrides = await loadMotionOverrides(args["motion-map"]);
  const patched = await createPatchedModel(modelDir, modelJsonPath, states, motionOverrides, {
    primaryTexture: args["primary-texture"] || "",
  });
  let server;

  try {
    const bundlePath = await buildBrowserBundle(depsDir, workDir);
    const serverInfo = await startServer({ modelDir, bundlePath, cubismCorePath: cubismCore });
    server = serverInfo.server;
    const requireFromDeps = createRequire(join(resolve(depsDir), "package.json"));
    const { chromium } = requireFromDeps("playwright");
    const browser = await chromium.launch();
    const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
    await page.goto(serverInfo.baseUrl, { waitUntil: "load" });

    for (const state of states) {
      const frameData = await page.evaluate(
        (job) => window.renderLive2DFrames(job),
        {
          width,
          height,
          scale,
          x,
          y,
          modelUrl: `/model/${encodeURIComponent(basename(patched.patchedModelPath))}`,
          cubismCoreUrl: "/core/live2dcubismcore.min.js",
          motionGroup: state.group,
          frames: state.frames,
          intervalMs: Math.round(1000 / state.fps),
        },
      );
      const stateDir = join(outputDir, state.id);
      await rm(stateDir, { recursive: true, force: true });
      await mkdir(stateDir, { recursive: true });
      for (let index = 0; index < frameData.length; index += 1) {
        await writeFile(join(stateDir, `${String(index).padStart(2, "0")}.png`), dataUrlToBuffer(frameData[index]));
      }
      console.log(`rendered ${state.id} ${frameData.length} frames`);
    }

    await browser.close();
  } finally {
    if (server) {
      await new Promise((resolveClose) => server.close(resolveClose));
    }
    await rm(patched.patchedModelPath, { force: true });
    for (const motionPath of patched.patchedMotionPaths) {
      await rm(motionPath, { force: true });
    }
    for (const texturePath of patched.patchedTexturePaths) {
      await rm(texturePath, { force: true });
    }
    await rm(workDir, { recursive: true, force: true });
  }
}

main().catch((error) => {
  console.error(error.stack || error);
  process.exit(1);
});
