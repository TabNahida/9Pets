# 9Pets One-Character Rebuild Worklog

This file replaces the previous completion checklist. It is the durable guide for future agents after context compaction. Keep it in English so the repository remains English-only.

## Current Rule

Work on exactly one character at a time.

Do not mark a character done because a bulk script produced files. A character is done only after its own source audit, Live2D motion capture, crop/quality pass, package rebuild, site update, and visual QA have all passed.

## Active Character Slot

Only one character may be active here at a time. Fill this slot before touching generated assets, then clear it after the row is marked done.

- Active character: none
- Package: none
- Asset id: none
- Source folder audited: none
- Live2D model used: none
- Motion files selected: none
- Last QA artifact: none
- Blocker: none

## Acceptance Gates

For each character, complete these gates in order:

- [ ] Source audit: find the best available official Live2D/Cubism model in `myssal/Reverse-1999-CN-Asset`, including nearby versioned role folders when the current metadata points to a stale path.
- [ ] Motion audit: list the available motion groups and choose distinct motions for Codex states instead of reusing a tiny left-right sway.
- [ ] High-resolution capture: render from Live2D at a high enough source size to keep the detail page sharp. Avoid head, hair, weapon, and outfit clipping; fix camera scale and anchor before packaging.
- [ ] Atlas build: create the Codex pet atlas from the approved frames with transparent unused cells and normalized transparent pixels.
- [ ] Motion QA: verify `idle`, `running-right`, `running-left`, `waving`, `jumping`, `failed`, `waiting`, `running`, and `review` all show meaningful state-specific movement.
- [ ] Visual QA: inspect the package sprite, detail-page sprite, preview, and source image for blur, unexpected transparency, residue, cropping, and frame jitter.
- [ ] Site QA: verify the catalog card, detail page, download link, source links, and `file://` navigation for this single character.
- [ ] Package QA: verify `pets/<package>/pet.json`, `pets/<package>/spritesheet.webp`, `docs/downloads/<package>.zip`, and docs data for this character.

## Quality Targets

- Every finished pet should be official-sourced and preferably rendered from Live2D/Cubism assets.
- Official-art elastic fallback is not an acceptable final state unless a careful per-character audit proves that no usable Live2D/Cubism or equivalent official animated source exists.
- Detail-page sprites should be crisp enough to inspect at enlarged size.
- Do not accept one-image sway loops as final Live2D work.
- Do not accept clipped heads or hair. Character `37` is a known regression example and should be revisited before being marked done.
- Do not accept rows with unexplained transparent body parts, black hidden pixels, halos, or broken alpha cleanup.
- Rebuild and verify one character before moving to the next row.

## Allowed Automation

Automation is allowed only when it is scoped to the active character.

- OK: scripts that inspect one character, render one character, package one character, or verify one character.
- OK: whole-site smoke tests after one character is updated.
- Not OK: bulk rebuilding every pet and checking rows as done from script output alone.
- Not OK: regenerating all packages to hide one character's failure.

## Suggested Order

Start with known visual regressions, then convert fallback rows, then improve already-rendered rows with weak motion or low detail.

1. `9Pets-37`: fix crop, resolution, and motion variety.
2. Rows whose prior build mode is `official-art-elastic-rig`.
3. Rows whose prior build mode is `official-live2d-cubism` but fail motion, crop, or sharpness QA.

## Character Rebuild Table

`Prior mode` and `prior cache` describe the current repository state before the one-character rebuild pass. They do not mean the row is accepted.

| Done | Character | Package | Prior mode | Prior cache | Asset id | Rebuild note |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | 37 | `9Pets-37` | official-live2d-cubism | rendered | 306601 | Rebuilt one-character pass with audited Live2D source, 37-specific motion map, non-clipped capture, and 4x detail atlas. |
| [x] | 6 | `9Pets-6` | official-live2d-cubism | rendered | 307901 | Rebuilt one-character pass with audited Live2D source, 6-specific motion map, non-clipped capture, and 4x detail atlas. |
| [x] | A Knight | `9Pets-A-Knight` | official-live2d-cubism | rendered | 300731 | Rebuilt one-character pass with audited Live2D source, A Knight-specific motion map, non-clipped capture, and 4x detail atlas. |
| [x] | Aleph | `9Pets-Aleph` | official-live2d-cubism | rendered | 311301 | Rebuilt one-character pass with audited Live2D source, Aleph-specific motion map, non-clipped capture, and 4x detail atlas. |
| [x] | Alexios | `9Pets-Alexios` | official-live2d-cubism | rendered | 312201 | Rebuilt one-character pass with audited Live2D source, Alexios-specific motion map, non-clipped capture, and 4x detail atlas. |
| [x] | aliEn T | `9Pets-aliEn-T` | official-art-elastic-rig | mapped | 303401 | Rebuilt one-character pass from official Spine source, aliEn T-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | An-an Lee | `9Pets-An-an-Lee` | official-live2d-cubism | rendered | 303901 | Rebuilt one-character pass with audited Live2D source, An-an Lee-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Anjo Nala | `9Pets-Anjo-Nala` | official-live2d-cubism | rendered | 310001 | Rebuilt one-character pass with audited Live2D source, Anjo Nala-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | APPLe | `9Pets-APPLe` | official-art-elastic-rig | mapped | 302801 | Rebuilt one-character pass from official Spine source, APPLe-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [ ] | Argus | `9Pets-Argus` | official-live2d-cubism | rendered | 309701 | Needs one-character rebuild and visual QA. |
| [ ] | Avgust | `9Pets-Avgust` | official-live2d-cubism | rendered | 307801 | Needs one-character rebuild and visual QA. |
| [ ] | Baby Blue | `9Pets-Baby-Blue` | official-art-elastic-rig | mapped | 301601 | Prior fallback; find usable official animation before accepting. |
| [ ] | Balloon Party | `9Pets-Balloon-Party` | official-art-elastic-rig | mapped | 302401 | Prior fallback; find usable official animation before accepting. |
| [ ] | Barbara | `9Pets-Barbara` | official-live2d-cubism | rendered | 309901 | Needs one-character rebuild and visual QA. |
| [ ] | Barcarola | `9Pets-Barcarola` | official-live2d-cubism | rendered | 310801 | Needs one-character rebuild and visual QA. |
| [ ] | Beryl | `9Pets-Beryl` | official-live2d-cubism | rendered | 313401 | Needs one-character rebuild and visual QA. |
| [ ] | Bette | `9Pets-Bette` | official-art-elastic-rig | mapped | 304501 | Prior fallback; find usable official animation before accepting. |
| [ ] | Bkornblume | `9Pets-Bkornblume` | official-art-elastic-rig | mapped | 302001 | Prior fallback; find usable official animation before accepting. |
| [ ] | Blonney | `9Pets-Blonney` | official-live2d-cubism | rendered | 306001 | Needs one-character rebuild and visual QA. |
| [ ] | Brimley | `9Pets-Brimley` | official-live2d-cubism | rendered | 310601 | Needs one-character rebuild and visual QA. |
| [ ] | Brume | `9Pets-Brume` | official-live2d-cubism | rendered | 313501 | Needs one-character rebuild and visual QA. |
| [ ] | Buddy Fairchild | `9Pets-Buddy-Fairchild` | official-live2d-cubism | rendered | 311501 | Needs one-character rebuild and visual QA. |
| [ ] | Bunny Bunny | `9Pets-Bunny-Bunny` | official-art-elastic-rig | mapped | 301401 | Prior fallback; find usable official animation before accepting. |
| [ ] | Centurion | `9Pets-Centurion` | official-art-elastic-rig | mapped | 303201 | Prior fallback; find usable official animation before accepting. |
| [ ] | Charlie | `9Pets-Charlie` | official-art-elastic-rig | mapped | 301701 | Prior fallback; find usable official animation before accepting. |
| [ ] | Charon | `9Pets-Charon` | official-live2d-cubism | rendered | 312801 | Needs one-character rebuild and visual QA. |
| [ ] | Cheng Heguang | `9Pets-Cheng-Heguang` | official-live2d-cubism | rendered | 313701 | Needs one-character rebuild and visual QA. |
| [ ] | Click | `9Pets-Click` | official-live2d-cubism | rendered | 304901 | Needs one-character rebuild and visual QA. |
| [ ] | Coppelia | `9Pets-Coppelia` | official-live2d-cubism | rendered | 314401 | Needs one-character rebuild and visual QA. |
| [ ] | Corvus | `9Pets-Corvus` | official-live2d-cubism | rendered | 313201 | Needs one-character rebuild and visual QA. |
| [ ] | Cristallo | `9Pets-Cristallo` | official-art-elastic-rig | mapped | 303101 | Prior fallback; find usable official animation before accepting. |
| [ ] | Darley Clatter | `9Pets-Darley-Clatter` | official-art-elastic-rig | mapped | 305001 | Prior fallback; find usable official animation before accepting. |
| [ ] | Desert Flannel | `9Pets-Desert-Flannel` | official-live2d-cubism | rendered | 307501 | Needs one-character rebuild and visual QA. |
| [ ] | Diggers | `9Pets-Diggers` | official-live2d-cubism | rendered | 306401 | Needs one-character rebuild and visual QA. |
| [ ] | Dikke | `9Pets-Dikke` | official-live2d-cubism | rendered | 302201 | Needs one-character rebuild and visual QA. |
| [ ] | Door | `9Pets-Door` | official-art-elastic-rig | mapped | 305901 | Prior fallback; find usable official animation before accepting. |
| [ ] | Druvis III | `9Pets-Druvis-III` | official-live2d-cubism | rendered | 300301 | Needs one-character rebuild and visual QA. |
| [ ] | Eagle | `9Pets-Eagle` | official-art-elastic-rig | mapped | 300601 | Prior fallback; find usable official animation before accepting. |
| [ ] | Enigma | `9Pets-Enigma` | official-live2d-cubism | rendered | 314301 | Needs one-character rebuild and visual QA. |
| [ ] | Erick | `9Pets-Erick` | official-art-elastic-rig | mapped | 305801 | Prior fallback; find usable official animation before accepting. |
| [ ] | Eternity | `9Pets-Eternity` | official-live2d-cubism | rendered | 305101 | Needs one-character rebuild and visual QA. |
| [ ] | Ezio Auditore | `9Pets-Ezio-Auditore` | official-live2d-cubism | rendered | 312301 | Needs one-character rebuild and visual QA. |
| [ ] | Ezra Theodore | `9Pets-Ezra-Theodore` | official-live2d-cubism | rendered | 307401 | Needs one-character rebuild and visual QA. |
| [ ] | Fatutu | `9Pets-Fatutu` | official-live2d-cubism | rendered | 310901 | Needs one-character rebuild and visual QA. |
| [ ] | Flutterpage | `9Pets-Flutterpage` | official-live2d-cubism | rendered | 310501 | Needs one-character rebuild and visual QA. |
| [ ] | Getian | `9Pets-Getian` | official-live2d-cubism | rendered | 308401 | Needs one-character rebuild and visual QA. |
| [ ] | Hissabeth | `9Pets-Hissabeth` | official-live2d-cubism | rendered | 311601 | Needs one-character rebuild and visual QA. |
| [ ] | Horropedia | `9Pets-Horropedia` | official-live2d-cubism | rendered | 306101 | Needs one-character rebuild and visual QA. |
| [ ] | Igor | `9Pets-Igor` | official-live2d-cubism | rendered | 309201 | Needs one-character rebuild and visual QA. |
| [ ] | Isolde | `9Pets-Isolde` | official-live2d-cubism | rendered | 308101 | Needs one-character rebuild and visual QA. |
| [ ] | J | `9Pets-J` | official-live2d-cubism | rendered | 309401 | Needs one-character rebuild and visual QA. |
| [ ] | Jessica | `9Pets-Jessica` | official-live2d-cubism | rendered | 305601 | Needs one-character rebuild and visual QA. |
| [ ] | Jiu Niangzi | `9Pets-Jiu-Niangzi` | official-live2d-cubism | rendered | 308301 | Needs one-character rebuild and visual QA. |
| [ ] | John Titor | `9Pets-John-Titor` | official-art-elastic-rig | mapped | 303601 | Prior fallback; find usable official animation before accepting. |
| [ ] | Kaalaa Baunaa | `9Pets-Kaalaa-Baunaa` | official-live2d-cubism | rendered | 307001 | Needs one-character rebuild and visual QA. |
| [ ] | Kakania | `9Pets-Kakania` | official-live2d-cubism | rendered | 308001 | Needs one-character rebuild and visual QA. |
| [ ] | Kanjira | `9Pets-Kanjira` | official-live2d-cubism | rendered | 307101 | Needs one-character rebuild and visual QA. |
| [ ] | Kassandra | `9Pets-Kassandra` | official-live2d-cubism | rendered | 312401 | Needs one-character rebuild and visual QA. |
| [ ] | Kiperina | `9Pets-Kiperina` | official-live2d-cubism | rendered | 311701 | Needs one-character rebuild and visual QA. |
| [ ] | La Source | `9Pets-La-Source` | official-art-elastic-rig | mapped | 303001 | Prior fallback; find usable official animation before accepting. |
| [ ] | Leilani | `9Pets-Leilani` | official-art-elastic-rig | mapped | 303501 | Prior fallback; find usable official animation before accepting. |
| [ ] | Liang Yue | `9Pets-Liang-Yue` | official-live2d-cubism | rendered | 311001 | Needs one-character rebuild and visual QA. |
| [ ] | Lilya | `9Pets-Lilya` | official-live2d-cubism | rendered | 300401 | Needs one-character rebuild and visual QA. |
| [ ] | Loggerhead | `9Pets-Loggerhead` | official-live2d-cubism | rendered | 311201 | Needs one-character rebuild and visual QA. |
| [ ] | Lopera | `9Pets-Lopera` | official-live2d-cubism | rendered | 310201 | Needs one-character rebuild and visual QA. |
| [ ] | Lorelei | `9Pets-Lorelei` | official-live2d-cubism | rendered | 309101 | Needs one-character rebuild and visual QA. |
| [ ] | Lorentz Butterfly | `9Pets-Lorentz-Butterfly` | official-live2d-cubism | rendered | 313901 | Needs one-character rebuild and visual QA. |
| [ ] | Lucy | `9Pets-Lucy` | official-live2d-cubism | rendered | 308601 | Needs one-character rebuild and visual QA. |
| [ ] | Marcus | `9Pets-Marcus` | official-live2d-cubism | rendered | 306501 | Needs one-character rebuild and visual QA. |
| [ ] | Marsha | `9Pets-Marsha` | official-live2d-cubism | rendered | 312701 | Needs one-character rebuild and visual QA. |
| [ ] | Matilda | `9Pets-Matilda` | official-live2d-cubism | rendered | 304101 | Needs one-character rebuild and visual QA. |
| [ ] | Medicine Pocket | `9Pets-Medicine-Pocket` | official-live2d-cubism | rendered | 304701 | Needs one-character rebuild and visual QA. |
| [ ] | Melania | `9Pets-Melania` | official-live2d-cubism | rendered | 306201 | Needs one-character rebuild and visual QA. |
| [ ] | Mercuria | `9Pets-Mercuria` | official-live2d-cubism | rendered | 309501 | Needs one-character rebuild and visual QA. |
| [ ] | Mesmer Jr. | `9Pets-Mesmer-Jr` | official-art-elastic-rig | mapped | 305701 | Prior fallback; find usable official animation before accepting. |
| [ ] | Moldir | `9Pets-Moldir` | official-live2d-cubism | rendered | 312101 | Needs one-character rebuild and visual QA. |
| [ ] | Mondlicht | `9Pets-Mondlicht` | official-art-elastic-rig | mapped | 302601 | Prior fallback; find usable official animation before accepting. |
| [ ] | Mr. Duncan | `9Pets-Mr-Duncan` | official-live2d-cubism | rendered | 310301 | Needs one-character rebuild and visual QA. |
| [ ] | Ms. Moissan | `9Pets-Ms-Moissan` | official-art-elastic-rig | mapped | 304401 | Prior fallback; find usable official animation before accepting. |
| [ ] | Ms. NewBabel | `9Pets-Ms-NewBabel` | official-live2d-cubism | rendered | 305201 | Needs one-character rebuild and visual QA. |
| [ ] | Ms. Radio | `9Pets-Ms-Radio` | official-art-elastic-rig | mapped | 302701 | Prior fallback; find usable official animation before accepting. |
| [ ] | Ms. Stranger | `9Pets-Ms-Stranger` | official-live2d-cubism | rendered | 314701 | Needs one-character rebuild and visual QA. |
| [ ] | Name Day | `9Pets-Name-Day` | official-live2d-cubism | rendered | 311801 | Needs one-character rebuild and visual QA. |
| [ ] | Nautika | `9Pets-Nautika` | official-live2d-cubism | rendered | 312001 | Needs one-character rebuild and visual QA. |
| [ ] | Necrologist | `9Pets-Necrologist` | official-live2d-cubism | rendered | 303701 | Needs one-character rebuild and visual QA. |
| [ ] | Nick Bottom | `9Pets-Nick-Bottom` | official-art-elastic-rig | mapped | 300501 | Prior fallback; find usable official animation before accepting. |
| [ ] | Noire | `9Pets-Noire` | official-live2d-cubism | rendered | 311101 | Needs one-character rebuild and visual QA. |
| [ ] | Oliver Fog | `9Pets-Oliver-Fog` | official-art-elastic-rig | mapped | 301801 | Prior fallback; find usable official animation before accepting. |
| [ ] | ONiON | `9Pets-ONiON` | official-art-elastic-rig | mapped | 305401 | Prior fallback; find usable official animation before accepting. |
| [ ] | Paper Heron | `9Pets-Paper-Heron` | official-live2d-cubism | rendered | 314101 | Needs one-character rebuild and visual QA. |
| [ ] | Pavia | `9Pets-Pavia` | official-art-elastic-rig | mapped | 301501 | Prior fallback; find usable official animation before accepting. |
| [ ] | Pickles | `9Pets-Pickles` | official-live2d-cubism | rendered | 306301 | Needs one-character rebuild and visual QA. |
| [ ] | Pioneer | `9Pets-Pioneer` | official-art-elastic-rig | mapped | 309601 | Prior fallback; find usable official animation before accepting. |
| [ ] | Poltergeist | `9Pets-Poltergeist` | official-art-elastic-rig | mapped | 304601 | Prior fallback; find usable official animation before accepting. |
| [ ] | Rabies | `9Pets-Rabies` | official-art-elastic-rig | mapped | 304201 | Prior fallback; find usable official animation before accepting. |
| [ ] | Ramona | `9Pets-Ramona` | official-live2d-cubism | rendered | 314201 | Needs one-character rebuild and visual QA. |
| [ ] | Recoleta | `9Pets-Recoleta` | official-live2d-cubism | rendered | 311401 | Needs one-character rebuild and visual QA. |
| [ ] | Reed | `9Pets-Reed` | official-art-elastic-rig | mapped | 313801 | Prior fallback; find usable official animation before accepting. |
| [ ] | Regulus | `9Pets-Regulus` | official-live2d-cubism | rendered | 302504 | Needs one-character rebuild and visual QA. |
| [ ] | Rhiannon | `9Pets-Rhiannon` | official-live2d-cubism | rendered | 314601 | Needs one-character rebuild and visual QA. |
| [ ] | Rubuska | `9Pets-Rubuska` | official-live2d-cubism | rendered | 312501 | Needs one-character rebuild and visual QA. |
| [ ] | Satsuki | `9Pets-Satsuki` | official-live2d-cubism | rendered | 303801 | Needs one-character rebuild and visual QA. |
| [ ] | Semmelweis | `9Pets-Semmelweis` | official-live2d-cubism | rendered | 308801 | Needs one-character rebuild and visual QA. |
| [ ] | Sentinel | `9Pets-Sentinel` | official-live2d-cubism | rendered | 312601 | Needs one-character rebuild and visual QA. |
| [ ] | Shamane | `9Pets-Shamane` | official-live2d-cubism | rendered | 307201 | Needs one-character rebuild and visual QA. |
| [ ] | Silverwing Eagle | `9Pets-Silverwing-Eagle` | official-live2d-cubism | rendered | 315401 | Needs one-character rebuild and visual QA. |
| [ ] | Sonetto | `9Pets-Sonetto` | official-live2d-cubism | rendered | 302301 | Needs one-character rebuild and visual QA. |
| [ ] | Sotheby | `9Pets-Sotheby` | official-live2d-cubism | rendered | 300902 | Needs one-character rebuild and visual QA. |
| [ ] | Spathodea | `9Pets-Spathodea` | official-live2d-cubism | rendered | 307301 | Needs one-character rebuild and visual QA. |
| [ ] | Sputnik | `9Pets-Sputnik` | official-art-elastic-rig | mapped | 305501 | Prior fallback; find usable official animation before accepting. |
| [ ] | Sweetheart | `9Pets-Sweetheart` | official-art-elastic-rig | mapped | 301101 | Prior fallback; find usable official animation before accepting. |
| [ ] | Tennant | `9Pets-Tennant` | official-live2d-cubism | rendered | 304301 | Needs one-character rebuild and visual QA. |
| [ ] | The Fool | `9Pets-The-Fool` | official-art-elastic-rig | mapped | 301201 | Prior fallback; find usable official animation before accepting. |
| [ ] | Tooth Fairy | `9Pets-Tooth-Fairy` | official-live2d-cubism | rendered | 305301 | Needs one-character rebuild and visual QA. |
| [ ] | TTT | `9Pets-TTT` | official-art-elastic-rig | mapped | 303301 | Prior fallback; find usable official animation before accepting. |
| [ ] | Tuesday | `9Pets-Tuesday` | official-live2d-cubism | rendered | 309801 | Needs one-character rebuild and visual QA. |
| [ ] | Twins Sleep | `9Pets-Twins-Sleep` | official-art-elastic-rig | mapped | 304001 | Prior fallback; find usable official animation before accepting. |
| [ ] | Ulrich | `9Pets-Ulrich` | official-live2d-cubism | rendered | 310701 | Needs one-character rebuild and visual QA. |
| [ ] | Ulu | `9Pets-Ulu` | official-art-elastic-rig | mapped | 307601 | Prior fallback; find usable official animation before accepting. |
| [ ] | Vila | `9Pets-Vila` | official-live2d-cubism | rendered | 308701 | Needs one-character rebuild and visual QA. |
| [ ] | Voyager | `9Pets-Voyager` | official-live2d-cubism | rendered | 304801 | Needs one-character rebuild and visual QA. |
| [ ] | White Rum | `9Pets-White-Rum` | official-art-elastic-rig | mapped | 310101 | Prior fallback; find usable official animation before accepting. |
| [ ] | Willow | `9Pets-Willow` | official-live2d-cubism | rendered | 310401 | Needs one-character rebuild and visual QA. |
| [ ] | Windsong | `9Pets-Windsong` | official-live2d-cubism | rendered | 307701 | Needs one-character rebuild and visual QA. |
| [ ] | X | `9Pets-X` | official-live2d-cubism | rendered | 301001 | Needs one-character rebuild and visual QA. |
| [ ] | Yenisei | `9Pets-Yenisei` | official-live2d-cubism | rendered | 308201 | Needs one-character rebuild and visual QA. |
| [ ] | Zima | `9Pets-Zima` | official-art-elastic-rig | none | 301301 | Prior fallback; find usable official animation before accepting. |

## Per-Character Update Template

When a character is being worked, update the active slot and paste a short entry below:

```text
### YYYY-MM-DD - <Character> / <Package>
- Source audit:
- Live2D model:
- Motions selected:
- Capture settings:
- Files changed:
- QA artifacts:
- Verification:
- Decision:
```

## Work Notes

Add dated notes here as characters are rebuilt. Keep notes concise, factual, and tied to one package.

### 2026-06-11 - 37 / 9Pets-37
- Source audit: local official Cubism folder `live2d/roles/v1a4_306601_37`; related Spine folders `roles/v1a4_306601_37` and `roles/v1a4_306601_37_s` also exist.
- Live2D model: `v1a4_306601_37.model3.json` with 22 motion files and 6 expression files.
- Motions selected: `idle=b_idle`, `running-right=b_tiyi`, `running-left=b_tiyi`, `waving=b_guzhang`, `jumping=b_gongji`, `failed=b_xinxu`, `waiting=b_zhangshi`, `running=b_sisuo`, `review=b_diantou`.
- Capture settings: `1600x1800`, scale `0.75`, x `1000`, y `900`; raw frame minimum margins were left `132`, top `153`, right `595`, bottom `82`.
- Files changed: rebuilt `pets/9Pets-37`, `docs/assets/spritesheets/9Pets-37.webp`, `docs/assets/detail-spritesheets/9Pets-37.webp`, `docs/assets/previews/9Pets-37.png`, `docs/downloads/9Pets-37.zip`, and docs data for 37.
- QA artifacts: `C:\tmp\9pets-37-audit-profile1-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed and now checks the 37 detail spritesheet; targeted image QA found no cell-edge clipping and no transparent RGB residue.
- Decision: accepted for this pass.

### 2026-06-11 - 6 / 9Pets-6
- Source audit: local official Cubism folder `live2d/roles/v1a4_307901_6`; related Spine folder `roles/v1a4_307901_6` is referenced in site data.
- Live2D model: `v1a4_307901_6.model3.json` with 19 motion files and 6 expression files.
- Motions selected: `idle=b_idle`, `running-right=b_qianxun`, `running-left=b_qianxun`, `waving=b_taishou`, `jumping=b_yaotou`, `failed=t_nanguo`, `waiting=b_shalou`, `running=b_yuedu`, `review=b_diantou`.
- Capture settings: `1600x1800`, scale `0.72`, x `1000`, y `900`; raw frame minimum margins were left `262`, top `624`, right `958`, bottom `37`.
- Files changed: rebuilt `pets/9Pets-6`, `docs/assets/spritesheets/9Pets-6.webp`, `docs/assets/detail-spritesheets/9Pets-6.webp`, `docs/assets/previews/9Pets-6.png`, `docs/downloads/9Pets-6.zip`, and docs data for 6.
- QA artifacts: `C:\tmp\9pets-6-detail-qa.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: `python -m py_compile tools\build_pets_site.py` passed; `node --check tools\render_live2d_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed; targeted detail smoke for `pet.html?id=9pets-6` loaded `assets/detail-spritesheets/9Pets-6.webp`; targeted image QA found no cell-edge clipping and no transparent RGB residue.
- Decision: accepted for this pass.

### 2026-06-11 - A Knight / 9Pets-A-Knight
- Source audit: local official Cubism folder `live2d/roles/v3a1_300731_wxk`; no matching same-id Spine folder was found during the local audit.
- Live2D model: `v3a1_300731_wxk.model3.json` with 16 motion files and 1 expression file.
- Motions selected: `idle=b_idle`, `running-right=b_xingli`, `running-left=b_xingli`, `waving=b_shenshou`, `jumping=b_jujian`, `failed=b_shengqi`, `waiting=b_tanshou`, `running=b_cashi`, `review=b_sikao`.
- Capture settings: `1800x1800`, scale `0.68`, x `1050`, y `600`; raw frame minimum margins were left `455`, top `625`, right `729`, bottom `225`.
- Files changed: rebuilt `pets/9Pets-A-Knight`, `docs/assets/spritesheets/9Pets-A-Knight.webp`, `docs/assets/detail-spritesheets/9Pets-A-Knight.webp`, `docs/assets/previews/9Pets-A-Knight.png`, `docs/downloads/9Pets-A-Knight.zip`, and docs data for A Knight.
- QA artifacts: `C:\tmp\9pets-a-knight-detail-qa.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: `python -m py_compile tools\build_pets_site.py` passed; `node --check tools\render_live2d_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed; targeted detail smoke for `pet.html?id=9pets-a-knight` loaded `assets/detail-spritesheets/9Pets-A-Knight.webp`; targeted image QA found no raw-frame clipping, no cell-edge clipping, and no transparent RGB residue.
- Decision: accepted for this pass.

### 2026-06-11 - Aleph / 9Pets-Aleph
- Source audit: local official Cubism folder `live2d/roles/v2a6_311301_alf`; related Spine folders `roles/v2a6_311301_alf` and `roles/v2a6_311301_alf_s` also exist.
- Live2D model: `v2a6_311301_alf.model3.json` with 20 motion files and 1 expression file.
- Motions selected: `idle=b_idle`, `running-right=b_touzi2`, `running-left=b_touzi2`, `waving=b_yanshuo3`, `jumping=b_fenlie2`, `failed=b_tongku2`, `waiting=b_shoushu2`, `running=b_yanshuo2`, `review=b_diantou`.
- Capture settings: `1800x1800`, scale `0.68`, x `1050`, y `600`; raw frame minimum margins were left `509`, top `394`, right `718`, bottom `247`.
- Files changed: rebuilt `pets/9Pets-Aleph`, `docs/assets/spritesheets/9Pets-Aleph.webp`, `docs/assets/detail-spritesheets/9Pets-Aleph.webp`, `docs/assets/previews/9Pets-Aleph.png`, `docs/downloads/9Pets-Aleph.zip`, and docs data for Aleph.
- QA artifacts: `C:\tmp\9pets-aleph-detail-qa.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: `python -m py_compile tools\build_pets_site.py` passed; `node --check tools\render_live2d_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed; targeted detail smoke for `pet.html?id=9pets-aleph` loaded `assets/detail-spritesheets/9Pets-Aleph.webp`; targeted image QA found no raw-frame clipping, no cell-edge clipping, and no transparent RGB residue.
- Decision: accepted for this pass.

### 2026-06-11 - Alexios / 9Pets-Alexios
- Source audit: local official Cubism folder `live2d/roles/s01_312201_alexios`; related Spine folders `roles/s01_312201_alkxos` and `roles/s01_312201_alkxos_s` also exist.
- Live2D model: `s01_312201_alexios.model3.json` with 15 motion files and 4 expression files.
- Motions selected: `idle=b_idle`, `running-right=b_cajian`, `running-left=b_cajian`, `waving=b_tanshou`, `jumping=b_woquan`, `failed=b_baobi`, `waiting=b_yaotou`, `running=b_cajian`, `review=b_diantou`.
- Capture settings: `1800x1800`, scale `0.68`, x `1050`, y `600`; raw frame minimum margins were left `306`, top `422`, right `823`, bottom `312`.
- Files changed: rebuilt `pets/9Pets-Alexios`, `docs/assets/spritesheets/9Pets-Alexios.webp`, `docs/assets/detail-spritesheets/9Pets-Alexios.webp`, `docs/assets/previews/9Pets-Alexios.png`, `docs/downloads/9Pets-Alexios.zip`, and docs data for Alexios.
- QA artifacts: `C:\tmp\9pets-alexios-detail-qa.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: `python -m py_compile tools\build_pets_site.py` passed; `node --check tools\render_live2d_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed; targeted detail smoke for `pet.html?id=9pets-alexios` loaded `assets/detail-spritesheets/9Pets-Alexios.webp`; targeted image QA found no raw-frame clipping, no cell-edge clipping, and no transparent RGB residue.
- Decision: accepted for this pass.

### 2026-06-11 - aliEn T / 9Pets-aliEn-T
- Source audit: no matching Cubism folder was found under `live2d/roles`; official Spine folders `roles/303401_xingzhiyan` and `roles/303401_xingzhiyan_s` exist.
- Spine source: `roles/303401_xingzhiyan/303401_xingzhiyan_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture`, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=idle`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; raw frame margins after calibration were left `462`, top `91`, right `408`, bottom `364`.
- Files changed: added `tools/render_spine_frames.mjs`, added scoped Spine support/profile in `tools/build_pets_site.py`, rebuilt `pets/9Pets-aliEn-T`, `docs/assets/spritesheets/9Pets-aliEn-T.webp`, `docs/assets/detail-spritesheets/9Pets-aliEn-T.webp`, `docs/assets/previews/9Pets-aliEn-T.png`, `docs/downloads/9Pets-aliEn-T.zip`, and docs data for aliEn T.
- QA artifacts: `C:\tmp\9pets-alient-spine-final-contact-v2.png`; standard atlas is `1536x1872`, detail atlas is `6144x7488`.
- Verification: `python -m py_compile tools\build_pets_site.py tools\smoke_site.py` passed; `node --check tools\render_spine_frames.mjs` passed; `node --check tools\render_live2d_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed and now checks aliEn T's detail spritesheet; targeted image QA found no raw-frame clipping, no cell-edge clipping, and no transparent RGB residue.
- Decision: accepted for this pass.

### 2026-06-11 - An-an Lee / 9Pets-An-an-Lee
- Source audit: local official Cubism folder `live2d/roles/303901_nimengdishi`; no separate Spine source was needed because the Cubism model rendered correctly.
- Live2D model: `303901_nimengdishi.model3.json`.
- Motions selected: `idle=b_idle`, `running-right=b_kaiji`, `running-left=b_kaiji`, `waving=b_daiyanjing`, `jumping=b_kaiji`, `failed=b_yaotou`, `waiting=b_dahaqian`, `running=b_sikao`, `review=b_diantou`.
- Capture settings: `1800x1800`, scale `0.68`, x `1050`, y `600`; raw frame minimum margins were left `423`, top `424`, right `813`, bottom `297`.
- Files changed: added the scoped An-an Lee Live2D profile, rebuilt `pets/9Pets-An-an-Lee`, `docs/assets/spritesheets/9Pets-An-an-Lee.webp`, `docs/assets/detail-spritesheets/9Pets-An-an-Lee.webp`, `docs/assets/previews/9Pets-An-an-Lee.png`, `docs/downloads/9Pets-An-an-Lee.zip`, and docs data for An-an Lee.
- QA artifacts: `C:\tmp\9pets-anan-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: `python -m py_compile tools\build_pets_site.py tools\smoke_site.py` passed; `node --check tools\render_live2d_frames.mjs` passed; `node --check tools\render_spine_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed and now checks An-an Lee's detail spritesheet; targeted image QA found no cell-edge clipping and no transparent RGB residue.
- Decision: accepted for this pass.

### 2026-06-11 - Anjo Nala / 9Pets-Anjo-Nala
- Source audit: local official Cubism folder `live2d/roles/v2a2_310001_anjonala`; related official Spine folders `roles/v2a2_310001_tsnn` and `roles/v2a2_310001_tsnn_s` also exist.
- Live2D model: `v2a2_310001_anjonala.model3.json` with 15 body motions plus expression and mouth motions.
- Motions selected: `idle=b_idle`, `running-right=b_ruchang`, `running-left=b_ruchang`, `waving=b_fangkai`, `jumping=b_huizhua`, `failed=b_wuzui`, `waiting=b_qidao`, `running=b_tanhui`, `review=b_diantou`.
- Capture settings: `1800x1800`, scale `0.68`, x `1050`, y `600`; raw frame minimum margins were left `411`, top `455`, right `777`, bottom `307`.
- Files changed: added the scoped Anjo Nala Live2D profile, rebuilt `pets/9Pets-Anjo-Nala`, `docs/assets/spritesheets/9Pets-Anjo-Nala.webp`, `docs/assets/detail-spritesheets/9Pets-Anjo-Nala.webp`, `docs/assets/previews/9Pets-Anjo-Nala.png`, `docs/downloads/9Pets-Anjo-Nala.zip`, and docs data for Anjo Nala.
- QA artifacts: `C:\tmp\9pets-anjo-nala-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: `python -m py_compile tools\build_pets_site.py tools\smoke_site.py` passed; `node --check tools\render_live2d_frames.mjs` passed; `node --check tools\render_spine_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed and now checks Anjo Nala's detail spritesheet; targeted image QA found no cell-edge clipping, no static rows, and no transparent RGB residue.
- Decision: accepted for this pass.

### 2026-06-11 - APPLe / 9Pets-APPLe
- Source audit: no matching Cubism folder was found under `live2d/roles`; official Spine folders `roles/302801_apple` and `roles/302801_apple_s` exist.
- Spine source: `roles/302801_apple/302801_apple_fight.skel` with animations `born`, `die`, `die_special`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `skill3`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=skill3`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=posture`.
- Capture settings: `1600x1600`, scale `2.2`, x `800`, y `1150`; raw frame minimum margins were left `602`, top `173`, right `190`, bottom `559`.
- Files changed: added `--flip-running-left` support to `tools/render_spine_frames.mjs`, added the scoped APPLe Spine profile, rebuilt `pets/9Pets-APPLe`, `docs/assets/spritesheets/9Pets-APPLe.webp`, `docs/assets/detail-spritesheets/9Pets-APPLe.webp`, `docs/assets/previews/9Pets-APPLe.png`, `docs/downloads/9Pets-APPLe.zip`, and docs data for APPLe.
- QA artifacts: `C:\tmp\9pets-apple-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: `python -m py_compile tools\build_pets_site.py tools\smoke_site.py` passed; `node --check tools\render_live2d_frames.mjs` passed; `node --check tools\render_spine_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed and now checks APPLe's detail spritesheet; targeted image QA found no cell-edge clipping, no static rows, and no transparent RGB residue.
- Decision: accepted for this pass.
