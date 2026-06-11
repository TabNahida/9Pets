# 9Pets

Fan-made Codex pet packages for Reverse: 1999 characters.

The generated GitHub Pages site lives in `docs/`. Each downloadable package uses the
`9Pets-Character-Name.zip` naming rule and contains a Codex-compatible `pet.json`
plus `spritesheet.webp`.

The catalog page uses lightweight static previews for scroll performance. Full
spritesheet animation is loaded only on per-character detail pages such as
`docs/pet.html?id=9pets-avgust`.

## Build

```powershell
python tools/build_pets_site.py
```

If a local Reverse-1999-CN-Asset checkout contains Live2D Cubism model folders,
the builder captures real motion frames and composes them into Codex pet atlases.
Set these paths when your cache differs from the defaults:

```powershell
$env:REVERSE_1999_ASSET_DIR = "C:\tmp\9pets-Reverse-1999-CN-Asset"
$env:LIVE2D_RENDER_DEPS = "C:\tmp\9pets-live2d-test"
$env:LIVE2D_CUBISM_CORE = "C:\tmp\9pets-live2d-test\live2dcubismcore.min.js"
python tools\build_pets_site.py
```

`tools/render_live2d_frames.mjs` expects temporary Node dependencies in
`LIVE2D_RENDER_DEPS` (`live2d-renderer`, `playwright@1.55.0`, `esbuild`, and
`path-browserify`) plus the official Live2D Cubism Core runtime. Set
`NINEPETS_RENDER_LIVE2D=0` to force the static official-art fallback.

The build reads `data/characters.json` and writes:

- `pets/9Pets-*/pet.json`
- `pets/9Pets-*/spritesheet.webp`
- `docs/data/pets.json`
- `docs/assets/source/*.png`
- `docs/assets/spritesheets/*.webp`
- `docs/downloads/9Pets-*.zip`

## Verify

```powershell
python tools\verify_build.py
python tools\smoke_site.py
```

The smoke test checks the catalog, mobile layout, direct `file://` loading, and
an interactive character detail page.

## Sources

- Bluepoch official home: https://re.bluepoch.com/home/
- Huiji Wiki target source: https://res1999.huijiwiki.com/wiki/
- Reverse-1999-CN-Asset dump: https://github.com/myssal/Reverse-1999-CN-Asset

## Asset Use Notice

This is a fan-made, non-commercial archive. Reverse: 1999 names and official
website artwork belong to Bluepoch and their respective rightsholders. The site
uses selected publicly exposed assets from the Bluepoch official home page for
visual framing, including the logo, home page panels, character thumbnails, and
the launch-site role artwork available from `character.js`.

Huiji returned automated 403 responses to direct script downloads in this build
environment. Character packages are built from official game assets mirrored in
`myssal/Reverse-1999-CN-Asset`, using Live2D Cubism motion capture when a usable
`.model3.json` folder is present in the local cache. When Cubism is unavailable,
the builder selects the cleanest official dump artwork candidate it can find.
Package metadata records the mapped Spine and Live2D asset paths, the selected
skin, birthday when available, and whether Live2D rendering was used. All
generated packages in this repository are marked `official-sourced`; future
community uploads should use a separate non-official source category.

`docs/data/pets-data.js` mirrors `docs/data/pets.json` so the catalog also works
when `docs/index.html` is opened directly from disk. GitHub Pages can use either
data file.
