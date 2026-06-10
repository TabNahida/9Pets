const state = {
  pets: [],
  sourceFilter: "all",
  search: "",
};

const els = {
  grid: document.querySelector("#petGrid"),
  search: document.querySelector("#searchInput"),
  resultCount: document.querySelector("#resultCount"),
  totalCount: document.querySelector("#totalCount"),
  officialCount: document.querySelector("#officialCount"),
  prydwenCount: document.querySelector("#prydwenCount"),
  template: document.querySelector("#petCardTemplate"),
  filterButtons: [...document.querySelectorAll("[data-source-filter]")],
};

function formatBytes(bytes) {
  if (!Number.isFinite(bytes)) return "";
  return new Intl.NumberFormat("en", {
    maximumFractionDigits: bytes > 1_000_000 ? 1 : 0,
  }).format(bytes / 1_000_000) + " MB";
}

function sourceLabel(type) {
  if (type === "official-sourced") return "Official";
  if (type === "prydwen-sourced") return "Prydwen";
  return "Generated";
}

function filteredPets() {
  const query = state.search.trim().toLowerCase();
  return state.pets.filter((pet) => {
    const matchesSource = state.sourceFilter === "all" || pet.sourceType === state.sourceFilter;
    const matchesSearch = !query || pet.displayName.toLowerCase().includes(query) || pet.packageName.toLowerCase().includes(query);
    return matchesSource && matchesSearch;
  });
}

function renderStats() {
  const official = state.pets.filter((pet) => pet.sourceType === "official-sourced").length;
  const prydwen = state.pets.filter((pet) => pet.sourceType === "prydwen-sourced").length;
  els.totalCount.textContent = state.pets.length;
  els.officialCount.textContent = official;
  els.prydwenCount.textContent = prydwen;
}

function renderGrid() {
  const pets = filteredPets();
  els.grid.textContent = "";
  els.resultCount.textContent = `${pets.length} of ${state.pets.length} packages`;

  if (!pets.length) {
    const empty = document.createElement("div");
    empty.className = "empty";
    empty.textContent = "No packages match this search.";
    els.grid.append(empty);
    return;
  }

  const fragment = document.createDocumentFragment();
  for (const pet of pets) {
    const card = els.template.content.firstElementChild.cloneNode(true);
    const sprite = card.querySelector(".pet-sprite");
    const title = card.querySelector("h2");
    const meta = card.querySelector("p");
    const badge = card.querySelector(".badge");
    const download = card.querySelector(".download");

    sprite.style.backgroundImage = `url("${pet.spritesheet}")`;
    title.textContent = pet.displayName;
    meta.textContent = `${pet.packageName} · ${formatBytes(pet.packageBytes)}`;
    badge.textContent = sourceLabel(pet.sourceType);
    badge.classList.toggle("official", pet.sourceType === "official-sourced");
    badge.classList.toggle("prydwen", pet.sourceType === "prydwen-sourced");
    download.href = pet.download;
    download.download = `${pet.packageName}.zip`;
    download.setAttribute("aria-label", `Download ${pet.packageName}`);

    fragment.append(card);
  }
  els.grid.append(fragment);
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
    renderStats();
    renderGrid();
  } catch (error) {
    els.resultCount.textContent = "Catalog manifest failed to load.";
    els.grid.innerHTML = `<div class="empty">${error.message}</div>`;
  }
}

init();
