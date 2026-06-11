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
  eyebrow: document.querySelector("#detailEyebrow"),
  summary: document.querySelector("#detailSummary"),
  sprite: document.querySelector("#detailSprite"),
  tabs: document.querySelector("#stateTabs"),
  download: document.querySelector("#downloadLink"),
  spritesheet: document.querySelector("#spritesheetLink"),
  source: document.querySelector("#sourceLink"),
  sourceImage: document.querySelector("#sourceImage"),
  infoGrid: document.querySelector("#infoGrid"),
};

function formatBytes(bytes) {
  if (!Number.isFinite(bytes)) return "";
  return new Intl.NumberFormat("en", {
    maximumFractionDigits: bytes > 1_000_000 ? 1 : 0,
  }).format(bytes / 1_000_000) + " MB";
}

function sourceLabel(type) {
  if (type === "official-sourced") return "Official";
  return "Community";
}

function normalize(value) {
  return String(value || "").trim().toLowerCase();
}

function findPet(pets) {
  const params = new URLSearchParams(window.location.search);
  const id = normalize(params.get("id") || params.get("pet"));
  if (!id) return null;
  return pets.find((pet) => {
    return [pet.id, pet.packageName, pet.displayName].some((value) => normalize(value) === id);
  });
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

function configureSprite(pet) {
  const atlasScale = Math.max(1, Number(pet.detailAtlasScale) || 1);
  atlasCellW = CELL_W * atlasScale;
  atlasCellH = CELL_H * atlasScale;
  els.sprite.style.width = `${atlasCellW}px`;
  els.sprite.style.height = `${atlasCellH}px`;
  els.sprite.style.backgroundSize = `${atlasCellW * COLS}px ${atlasCellH * ROWS}px`;
  els.sprite.style.backgroundImage = `url("${pet.detailSpritesheet || pet.spritesheet}")`;
  els.sprite.style.setProperty("--sprite-scale", atlasScale > 1 ? "1" : "2");
  els.sprite.style.setProperty("--sprite-mobile-scale", atlasScale > 1 ? "0.775" : "1.55");
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

function renderPet(pet) {
  const packageSize = formatBytes(pet.packageBytes);
  const source = sourceLabel(pet.sourceType);
  const animationMode = pet.animationModeLabel || pet.animationMode || "Official-art atlas";
  const summary = pet.characterSummary || `A Reverse: 1999 Codex pet package for ${pet.displayName}, built from official game asset-dump artwork and packaged for the fixed 9-state Codex pet atlas.`;

  document.title = `${pet.displayName} - 9Pets`;
  els.title.textContent = pet.displayName;
  els.eyebrow.textContent = `${source}-sourced package`;
  els.summary.textContent = summary;
  configureSprite(pet);
  els.download.href = pet.download;
  els.download.download = `${pet.packageName}.zip`;
  els.spritesheet.href = pet.spritesheet;
  els.source.href = pet.sourceImage || pet.sourceUrl || "#";
  els.sourceImage.src = pet.sourceImage || pet.preview;
  els.sourceImage.alt = `${pet.displayName} source art`;

  addInfo("Package", pet.packageName);
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
    if (!data) {
      const response = await fetch("data/pets.json");
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      data = await response.json();
    }
    const pet = findPet(data.pets || []);
    if (!pet) throw new Error("Pet package was not found.");
    renderPet(pet);
  } catch (error) {
    els.title.textContent = "Package not found";
    els.summary.textContent = error.message;
  }
}

init();
