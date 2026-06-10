# 9Pets

Fan-made Codex pet packages for Reverse: 1999 characters.

The generated GitHub Pages site lives in `docs/`. Each downloadable package uses the
`9Pets-Character-Name.zip` naming rule and contains a Codex-compatible `pet.json`
plus `spritesheet.webp`.

## Build

```powershell
python tools/build_pets_site.py
```

The build reads `data/characters.json` and writes:

- `pets/9Pets-*/pet.json`
- `pets/9Pets-*/spritesheet.webp`
- `docs/data/pets.json`
- `docs/assets/spritesheets/*.webp`
- `docs/downloads/9Pets-*.zip`

## Sources

- Bluepoch official home: https://re.bluepoch.com/home/
- Huiji Wiki target source: https://res1999.huijiwiki.com/wiki/
- Prydwen character catalog: https://www.prydwen.gg/re1999/characters

## Asset Use Notice

This is a fan-made, non-commercial archive. Reverse: 1999 names and official
website artwork belong to Bluepoch and their respective rightsholders. The site
uses selected publicly exposed assets from the Bluepoch official home page for
visual framing, including the logo, home page panels, character thumbnails, and
the launch-site role artwork available from `character.js`.

Huiji and Prydwen returned automated 403 responses to direct script downloads in
this build environment. Bluepoch's official home script exposed 10 downloadable
launch-site character assets; packages created from those files are marked
`official-sourced`. The remaining packages use deterministic generated cards
based on the English character catalog and are marked `generated-card`.

`docs/data/pets-data.js` mirrors `docs/data/pets.json` so the catalog also works
when `docs/index.html` is opened directly from disk. GitHub Pages can use either
data file.
