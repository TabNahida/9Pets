function readVariantMode() {
  const params = new URLSearchParams(window.location.search);
  return params.get("variant") === "cute" ? "cute" : "normal";
}

const state = {
  pets: [],
  cuteVariants: [],
  sourceFilter: "all",
  variantMode: readVariantMode(),
  search: "",
  renderToken: 0,
};

const els = {
  grid: document.querySelector("#petGrid"),
  search: document.querySelector("#searchInput"),
  resultCount: document.querySelector("#resultCount"),
  totalCount: document.querySelector("#totalCount"),
  officialCount: document.querySelector("#officialCount"),
  assetCount: document.querySelector("#assetCount"),
  cuteCount: document.querySelector("#cuteCount"),
  template: document.querySelector("#petCardTemplate"),
  filterButtons: [...document.querySelectorAll("[data-source-filter]")],
  variantButtons: [...document.querySelectorAll("[data-variant-mode]")],
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

function variantLabel(pet) {
  return pet.variantType === "cute" ? "Cute" : sourceLabel(pet.sourceType);
}

function petUrl(pet) {
  return `pet.html?id=${encodeURIComponent(pet.id)}`;
}

function syncVariantButtons() {
  for (const button of els.variantButtons) {
    button.classList.toggle("active", button.dataset.variantMode === state.variantMode);
  }
}

function updateVariantUrl() {
  const url = new URL(window.location.href);
  if (state.variantMode === "cute") {
    url.searchParams.set("variant", "cute");
  } else {
    url.searchParams.delete("variant");
  }
  window.history.replaceState(null, "", url);
}

function activePets() {
  return state.variantMode === "cute" ? state.cuteVariants : state.pets;
}

function filteredPets() {
  const query = state.search.trim().toLowerCase();
  return activePets().filter((pet) => {
    const matchesSource = state.sourceFilter === "all" || pet.sourceType === state.sourceFilter;
    const matchesSearch =
      !query ||
      pet.displayName.toLowerCase().includes(query) ||
      pet.packageName.toLowerCase().includes(query) ||
      String(pet.skinName || "").toLowerCase().includes(query);
    return matchesSource && matchesSearch;
  });
}

function renderStats() {
  const official = state.pets.filter((pet) => pet.sourceType === "official-sourced").length;
  const assetMapped = state.pets.filter((pet) => pet.assetId).length;
  els.totalCount.textContent = state.pets.length;
  els.officialCount.textContent = official;
  els.assetCount.textContent = assetMapped;
  els.cuteCount.textContent = state.cuteVariants.length;
}

function renderGrid() {
  const renderToken = ++state.renderToken;
  const pets = filteredPets();
  const allActivePets = activePets();
  els.grid.textContent = "";
  els.resultCount.textContent = `${pets.length} of ${allActivePets.length} ${state.variantMode === "cute" ? "cute " : ""}packages`;

  if (!pets.length) {
    const empty = document.createElement("div");
    empty.className = "empty";
    empty.textContent = "No packages match this search.";
    els.grid.append(empty);
    return;
  }

  let index = 0;
  const appendBatch = () => {
    if (renderToken !== state.renderToken) return;
    const fragment = document.createDocumentFragment();
    const end = Math.min(index + 24, pets.length);

    for (; index < end; index += 1) {
      const pet = pets[index];
      const card = els.template.content.firstElementChild.cloneNode(true);
      const preview = card.querySelector(".pet-preview");
      const title = card.querySelector("h2");
      const skin = card.querySelector(".skin-line");
      const meta = card.querySelector("p");
      const badge = card.querySelector(".badge");
      const details = card.querySelector(".details-link");
      const download = card.querySelector(".download");
      const detailsUrl = petUrl(pet);

      card.classList.toggle("cute-variant", pet.variantType === "cute");
      card.tabIndex = 0;
      card.setAttribute("role", "link");
      card.setAttribute("aria-label", `Open ${pet.displayName}`);
      preview.src = pet.preview;
      preview.alt = `${pet.displayName} pet preview`;
      title.textContent = pet.displayName;
      skin.textContent = pet.skinDisplayName || "";
      meta.textContent = `${pet.packageName} · ${formatBytes(pet.packageBytes)}`;
      badge.textContent = variantLabel(pet);
      badge.classList.toggle("official", pet.sourceType === "official-sourced" && pet.variantType !== "cute");
      badge.classList.toggle("cute", pet.variantType === "cute");
      details.href = detailsUrl;
      details.setAttribute("aria-label", `Open ${pet.displayName}`);
      download.href = pet.download;
      download.download = `${pet.packageName}.zip`;
      download.setAttribute("aria-label", `Download ${pet.packageName}`);
      card.addEventListener("click", (event) => {
        if (event.target.closest("a, button")) return;
        window.location.href = detailsUrl;
      });
      card.addEventListener("keydown", (event) => {
        if (event.key !== "Enter" && event.key !== " ") return;
        if (event.target.closest("a, button")) return;
        event.preventDefault();
        window.location.href = detailsUrl;
      });

      fragment.append(card);
    }

    els.grid.append(fragment);

    if (index < pets.length) {
      window.requestAnimationFrame(appendBatch);
    }
  };

  appendBatch();
}

function bindEvents() {
  els.search.addEventListener("input", (event) => {
    state.search = event.target.value;
    renderGrid();
  });

  for (const button of els.filterButtons) {
    button.addEventListener("click", () => {
      state.sourceFilter = button.dataset.sourceFilter;
      for (const other of els.filterButtons) {
        other.classList.toggle("active", other === button);
      }
      renderGrid();
    });
  }

  for (const button of els.variantButtons) {
    button.addEventListener("click", () => {
      state.variantMode = button.dataset.variantMode;
      syncVariantButtons();
      updateVariantUrl();
      renderGrid();
    });
  }
}

async function init() {
  bindEvents();
  try {
    let data = window.NINEPETS_DATA;
    if (!data) {
      const response = await fetch("data/pets.json");
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      data = await response.json();
    }
    if (!Array.isArray(data.pets)) throw new Error("Catalog data is missing pets.");
    state.pets = data.pets;
    state.cuteVariants = Array.isArray(data.cuteVariants) ? data.cuteVariants : [];
    syncVariantButtons();
    renderStats();
    renderGrid();
  } catch (error) {
    els.resultCount.textContent = "Catalog manifest failed to load.";
    els.grid.innerHTML = `<div class="empty">${error.message}</div>`;
  }
}

init();
