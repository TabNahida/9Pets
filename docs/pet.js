const CELL_W = 192;
const CELL_H = 208;
const COLS = 8;
const ROWS = 9;

let atlasCellW = CELL_W;
let atlasCellH = CELL_H;

const STATES = [
  { id: "idle", label: "Idle", row: 0, frames: 6, duration: 1.15 },
  { id: "running-right", label: "Right", row: 1, frames: 8, duration: 0.92 },
  { id: "running-left", label: "Left", row: 2, frames: 8, duration: 0.92 },
  { id: "waving", label: "Wave", row: 3, frames: 4, duration: 0.92 },
  { id: "jumping", label: "Jump", row: 4, frames: 5, duration: 0.82 },
  { id: "failed", label: "Failed", row: 5, frames: 8, duration: 1.05 },
  { id: "waiting", label: "Waiting", row: 6, frames: 6, duration: 1.15 },
  { id: "running", label: "Working", row: 7, frames: 6, duration: 0.94 },
  { id: "review", label: "Review", row: 8, frames: 6, duration: 1.2 },
];

const els = {
  title: document.querySelector("#detailTitle"),
  skin: document.querySelector("#detailSkin"),
  eyebrow: document.querySelector("#detailEyebrow"),
  summary: document.querySelector("#detailSummary"),
  sprite: document.querySelector("#detailSprite"),
  tabs: document.querySelector("#stateTabs"),
  download: document.querySelector("#downloadLink"),
  spritesheet: document.querySelector("#spritesheetLink"),
  source: document.querySelector("#sourceLink"),
  sourceImage: document.querySelector("#sourceImage"),
  infoGrid: document.querySelector("#infoGrid"),
  variantSwitch: document.querySelector("#variantSwitch"),
  backLink: document.querySelector(".back-link"),
  catalogLinks: [...document.querySelectorAll('a[href="index.html#catalog"]')],
  homeLink: document.querySelector(".brand"),
};

function formatBytes(bytes) {
  if (!Number.isFinite(bytes)) return "";
  const megabytes = bytes / 1_000_000;
  return new Intl.NumberFormat("en", {
    minimumFractionDigits: megabytes < 1 ? 1 : 0,
    maximumFractionDigits: megabytes < 10 ? 1 : 0,
  }).format(megabytes) + " MB";
}

function sourceLabel(type) {
  if (type === "official-sourced") return "Official";
  return "Community";
}

function normalize(value) {
  return String(value || "").trim().toLowerCase();
}

function allPets(data) {
  return [...(data.pets || []), ...(data.cuteVariants || [])];
}

function findPet(data) {
  const params = new URLSearchParams(window.location.search);
  const id = normalize(params.get("id") || params.get("pet"));
  if (!id) return null;
  return allPets(data).find((pet) => {
    return [pet.id, pet.packageName, pet.displayName].some((value) => normalize(value) === id);
  });
}

function normalPetFor(data, pet) {
  if (pet.variantType === "cute") {
    return (data.pets || []).find((candidate) => candidate.id === pet.normalId || candidate.packageName === pet.normalPackageName);
  }
  return pet;
}

function cuteVariantFor(data, pet) {
  const normal = normalPetFor(data, pet);
  if (!normal) return null;
  return (data.cuteVariants || []).find((variant) => variant.normalId === normal.id || variant.normalPackageName === normal.packageName) || null;
}

function catalogUrlFor(pet) {
  return pet.variantType === "cute" ? "index.html?variant=cute#catalog" : "index.html#catalog";
}

function isLocalAssetUrl(url) {
  return Boolean(url) && !/^(?:[a-z][a-z\d+\-.]*:|#|\/\/)/i.test(String(url));
}

function versionedAssetUrl(url, data, pet) {
  if (!isLocalAssetUrl(url)) return url;
  const key = String(url).split("#", 1)[0].split("?", 1)[0];
  const assetVersion = pet.assetVersions && pet.assetVersions[key];
  const version = assetVersion || [data.generatedAt, pet.packageBytes].filter(Boolean).join("-");
  if (!version) return url;
  const value = String(url);
  const hashIndex = value.indexOf("#");
  const base = hashIndex >= 0 ? value.slice(0, hashIndex) : value;
  const hash = hashIndex >= 0 ? value.slice(hashIndex) : "";
  const separator = base.includes("?") ? "&" : "?";
  return `${base}${separator}v=${encodeURIComponent(version)}${hash}`;
}

function setState(state) {
  els.sprite.style.setProperty("--row-y", `${-state.row * atlasCellH}px`);
  els.sprite.style.setProperty("--frames", state.frames);
  els.sprite.style.setProperty("--end-x", `${-state.frames * atlasCellW}px`);
  els.sprite.style.setProperty("--duration", `${state.duration}s`);
  els.sprite.style.animationName = "none";
  window.requestAnimationFrame(() => {
    els.sprite.style.animationName = "atlas-state";
  });

  for (const button of els.tabs.querySelectorAll("button")) {
    button.classList.toggle("active", button.dataset.state === state.id);
  }
}

function configureSprite(data, pet) {
  const atlasScale = Math.max(1, Number(pet.detailAtlasScale) || 1);
  const spriteUrl = versionedAssetUrl(pet.detailSpritesheet || pet.spritesheet, data, pet);
  atlasCellW = CELL_W * atlasScale;
  atlasCellH = CELL_H * atlasScale;
  els.sprite.style.width = `${atlasCellW}px`;
  els.sprite.style.height = `${atlasCellH}px`;
  els.sprite.style.backgroundSize = `${atlasCellW * COLS}px ${atlasCellH * ROWS}px`;
  els.sprite.style.backgroundImage = `url("${spriteUrl}")`;
  els.sprite.style.setProperty("--sprite-scale", (2.05 / atlasScale).toFixed(3));
  els.sprite.style.setProperty("--sprite-mobile-scale", (1.45 / atlasScale).toFixed(3));
}

function createStateTabs() {
  const fragment = document.createDocumentFragment();
  for (const state of STATES) {
    const button = document.createElement("button");
    button.type = "button";
    button.dataset.state = state.id;
    button.textContent = state.label;
    button.addEventListener("click", () => setState(state));
    fragment.append(button);
  }
  els.tabs.append(fragment);
}

function addInfo(label, value, href) {
  if (!value) return;
  const item = document.createElement("div");
  item.className = "info-item";
  const labelEl = document.createElement("span");
  labelEl.textContent = label;
  const valueEl = href ? document.createElement("a") : document.createElement("strong");
  valueEl.textContent = value;
  if (href) {
    valueEl.href = href;
    valueEl.rel = "noreferrer";
  }
  item.append(labelEl, valueEl);
  els.infoGrid.append(item);
}

function addVariantLink(label, pet, active) {
  const link = document.createElement(active ? "span" : "a");
  link.className = "variant-link";
  link.textContent = label;
  if (active) {
    link.classList.add("active");
  } else if (pet) {
    link.href = `pet.html?id=${encodeURIComponent(pet.id)}`;
  } else {
    link.classList.add("disabled");
    link.setAttribute("aria-disabled", "true");
  }
  els.variantSwitch.append(link);
}

function renderVariantSwitch(data, pet) {
  els.variantSwitch.textContent = "";
  const normal = normalPetFor(data, pet);
  const cute = cuteVariantFor(data, pet);
  addVariantLink("Normal", normal, pet.variantType !== "cute");
  addVariantLink("Cute", cute, pet.variantType === "cute");
}

function renderPet(data, pet) {
  const packageSize = formatBytes(pet.packageBytes);
  const source = sourceLabel(pet.sourceType);
  const variant = pet.variantType === "cute" ? "Cute" : "Normal";
  const skinDisplay = pet.skinDisplayName || "";
  const animationMode = pet.animationModeLabel || pet.animationMode || "Official-art atlas";
  const summary = pet.characterSummary || `A Reverse: 1999 Codex pet package for ${pet.displayName}, built from official game asset-dump artwork and packaged for the fixed 9-state Codex pet atlas.`;

  document.title = `${pet.displayName}${skinDisplay ? ` ${skinDisplay}` : ""}${pet.variantType === "cute" ? " Cute" : ""} - 9Pets`;
  els.title.textContent = pet.displayName;
  els.skin.textContent = skinDisplay;
  els.eyebrow.textContent = pet.variantType === "cute" ? "Cute official-sourced package" : `${source}-sourced package`;
  els.summary.textContent = summary;
  const catalogUrl = catalogUrlFor(pet);
  els.backLink.href = catalogUrl;
  els.homeLink.href = catalogUrl;
  for (const link of els.catalogLinks) {
    link.href = catalogUrl;
  }
  renderVariantSwitch(data, pet);
  configureSprite(data, pet);
  els.download.href = versionedAssetUrl(pet.download, data, pet);
  els.download.download = `${pet.packageName}.zip`;
  els.spritesheet.href = versionedAssetUrl(pet.spritesheet, data, pet);
  els.source.href = versionedAssetUrl(pet.sourceImage || pet.sourceUrl || "#", data, pet);
  els.sourceImage.src = versionedAssetUrl(pet.sourceImage || pet.preview, data, pet);
  els.sourceImage.alt = `${pet.displayName} source art`;

  addInfo("Package", pet.packageName);
  addInfo("Version", variant);
  addInfo("Source", source);
  addInfo("Animation", animationMode);
  addInfo("Asset ID", pet.assetId);
  addInfo("Birthday", pet.birthday);
  addInfo("Skin", pet.skinName || "Default");
  addInfo("Download", packageSize);
  addInfo("Matched Name", pet.matchedName);
  addInfo("Source Image", pet.sourceRepoPath, pet.sourceUrl);
  addInfo("Live2D Assets", pet.cubismPath || "No mapped Live2D path", pet.cubismUrl);
  addInfo("Spine Assets", pet.spinePath || "No mapped Spine path", pet.spineUrl);
  addInfo("Asset Dump", "myssal/Reverse-1999-CN-Asset", pet.assetRepoUrl);

  setState(STATES[0]);
}

async function init() {
  createStateTabs();
  try {
    let data = window.NINEPETS_DATA;
    try {
      const response = await fetch(`data/pets.json?v=${Date.now()}`, { cache: "no-store" });
      if (response.ok) {
        data = await response.json();
      } else if (!data) {
        throw new Error(`HTTP ${response.status}`);
      }
    } catch (error) {
      if (!data) throw error;
    }
    const pet = findPet(data);
    if (!pet) throw new Error("Pet package was not found.");
    renderPet(data, pet);
  } catch (error) {
    els.title.textContent = "Package not found";
    els.summary.textContent = error.message;
  }
}

init();
