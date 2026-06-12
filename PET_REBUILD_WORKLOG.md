# 9Pets One-Character Rebuild Worklog

This file replaces the previous completion checklist. It is the durable guide for future agents after context compaction. Keep it in English so the repository remains English-only.

## Current Rule

Work on exactly one character at a time.

Official normal pets must use the character's normal Live2D/Cubism model or an equivalent normal animated source. Do not accept chibi/cartoon battle Spine assets as normal official rebuilds.

Cute/chibi variants are tracked separately and must use the package naming rule `9Pets-Cute-XXX`.

Do not mark a character done because a bulk script produced files. A character is done only after its own source audit, Live2D motion capture, crop/quality pass, package rebuild, site update, and visual QA have all passed.

## Active Character Slot

Only one character may be active here at a time. Fill this slot before touching generated assets, then clear it after the row is marked done.

- Active character: Cristallo
- Package: 9Pets-Cristallo
- Asset id: 303101
- Source folder audited: pending refreshed normal-source audit
- Live2D model used: pending
- Motion files selected: pending
- Last QA artifact: pending
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
| [x] | Argus | `9Pets-Argus` | official-live2d-cubism | rendered | 309701 | Rebuilt one-character pass with audited Live2D source, Argus-specific motion map, corrected primary texture capture, non-clipped motion frames, and 4x detail atlas. |
| [x] | Avgust | `9Pets-Avgust` | official-live2d-cubism | rendered | 307801 | Rebuilt one-character pass with audited Live2D source, Avgust-specific motion map, non-clipped motion frames, and 4x detail atlas. |
| [ ] | Baby Blue | `9Pets-Baby-Blue` | official-art-elastic-rig | mapped | 301601 | Room Spine package exists, but it is not accepted as the normal official rebuild; find a proper normal Live2D/Cubism or equivalent normal animated source before checking this row. |
| [ ] | Balloon Party | `9Pets-Balloon-Party` | official-art-elastic-rig | mapped | 302401 | Room Spine package exists, but it is not accepted as the normal official rebuild; find a proper normal Live2D/Cubism or equivalent normal animated source before checking this row. |
| [x] | Barbara | `9Pets-Barbara` | official-live2d-cubism | rendered | 309901 | Rebuilt one-character pass with audited Live2D source, Barbara-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Barcarola | `9Pets-Barcarola` | official-live2d-cubism | rendered | 310801 | Rebuilt one-character pass with audited Live2D source, Barcarola-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Beryl | `9Pets-Beryl` | official-live2d-cubism | rendered | 313401 | Rebuilt one-character pass with audited Live2D source, Beryl-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [ ] | Bette | `9Pets-Bette` | official-art-elastic-rig | mapped | 304501 | Prior fallback; find usable official animation before accepting. |
| [ ] | Bkornblume | `9Pets-Bkornblume` | official-art-elastic-rig | mapped | 302001 | Prior fallback; find usable official animation before accepting. |
| [x] | Blonney | `9Pets-Blonney` | official-live2d-cubism | rendered | 306001 | Rebuilt one-character pass with audited Live2D source, Blonney-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Brimley | `9Pets-Brimley` | official-live2d-cubism | rendered | 310601 | Rebuilt one-character pass with audited Live2D source, Brimley-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Brume | `9Pets-Brume` | official-live2d-cubism | rendered | 313501 | Rebuilt one-character pass with audited Live2D source, Brume-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Buddy Fairchild | `9Pets-Buddy-Fairchild` | official-live2d-cubism | rendered | 311501 | Rebuilt one-character pass with audited Live2D source, Buddy Fairchild-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [ ] | Bunny Bunny | `9Pets-Bunny-Bunny` | official-art-elastic-rig | mapped | 301401 | Prior fallback; find usable official animation before accepting. |
| [ ] | Centurion | `9Pets-Centurion` | official-art-elastic-rig | mapped | 303201 | Prior fallback; find usable official animation before accepting. |
| [x] | Charlie | `9Pets-Charlie` | official-art-elastic-rig | mapped | 301701 | Rebuilt one-character pass from audited official room Spine source, avoiding the battle/cute track, with state-specific room motions and 4x detail atlas. |
| [x] | Charon | `9Pets-Charon` | official-live2d-cubism | rendered | 312801 | Rebuilt one-character pass with audited Live2D source, Charon-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Cheng Heguang | `9Pets-Cheng-Heguang` | official-live2d-cubism | rendered | 313701 | Rebuilt one-character pass with audited Live2D source, Cheng Heguang-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Click | `9Pets-Click` | official-live2d-cubism | rendered | 304901 | Rebuilt one-character pass with audited Live2D source, Click-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Coppelia | `9Pets-Coppelia` | official-live2d-cubism | rendered | 314401 | Rebuilt one-character pass with audited Live2D source, Coppelia-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Corvus | `9Pets-Corvus` | official-live2d-cubism | rendered | 313201 | Rebuilt one-character pass with audited normal Live2D source, Corvus-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
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

## Cute Character Variant Todo Table

Cute/chibi variants are separate from the official normal rebuild table. Build them one character at a time after auditing the chibi/cartoon source, and name each package `9Pets-Cute-XXX`.

| Done | Character | Cute package | Asset id | Cute rebuild note |
| --- | --- | --- | --- | --- |
| [ ] | 37 | `9Pets-Cute-37` | 306601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | 6 | `9Pets-Cute-6` | 307901 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | A Knight | `9Pets-Cute-A-Knight` | 300731 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Aleph | `9Pets-Cute-Aleph` | 311301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Alexios | `9Pets-Cute-Alexios` | 312201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | aliEn T | `9Pets-Cute-aliEn-T` | 303401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | An-an Lee | `9Pets-Cute-An-an-Lee` | 303901 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Anjo Nala | `9Pets-Cute-Anjo-Nala` | 310001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | APPLe | `9Pets-Cute-APPLe` | 302801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Argus | `9Pets-Cute-Argus` | 309701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Avgust | `9Pets-Cute-Avgust` | 307801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [x] | Baby Blue | `9Pets-Cute-Baby-Blue` | 301601 | Rebuilt from audited official chibi Spine source with a reproducible scoped profile and 4x detail atlas. |
| [x] | Balloon Party | `9Pets-Cute-Balloon-Party` | 302401 | Rebuilt from audited official chibi Spine source with a reproducible scoped profile and 4x detail atlas. |
| [ ] | Barbara | `9Pets-Cute-Barbara` | 309901 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Barcarola | `9Pets-Cute-Barcarola` | 310801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Beryl | `9Pets-Cute-Beryl` | 313401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Bette | `9Pets-Cute-Bette` | 304501 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Bkornblume | `9Pets-Cute-Bkornblume` | 302001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Blonney | `9Pets-Cute-Blonney` | 306001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [x] | Brimley | `9Pets-Cute-Brimley` | 310601 | Built from audited official chibi Spine source with detached-piece motions rejected and replaced. |
| [x] | Brume | `9Pets-Cute-Brume` | 313501 | Built from audited official chibi Spine source with state-specific motions and 4x detail atlas. |
| [x] | Buddy Fairchild | `9Pets-Cute-Buddy-Fairchild` | 311501 | Built from audited official chibi Spine source with state-specific motions and 4x detail atlas. |
| [x] | Bunny Bunny | `9Pets-Cute-Bunny-Bunny` | 301401 | Built from audited official chibi Spine source with state-specific motions and 4x detail atlas. |
| [x] | Centurion | `9Pets-Cute-Centurion` | 303201 | Built from audited official chibi Spine source; rejected detached-piece motions and rebuilt with stable state-specific motions and 4x detail atlas. |
| [x] | Charlie | `9Pets-Cute-Charlie` | 301701 | Built from audited official chibi Spine source with a reproducible scoped profile and 4x detail atlas. |
| [x] | Charon | `9Pets-Cute-Charon` | 312801 | Built from audited official chibi Spine source with a reproducible scoped profile and 4x detail atlas. |
| [x] | Cheng Heguang | `9Pets-Cute-Cheng-Heguang` | 313701 | Built from audited official chibi Spine source with state-specific motions and 4x detail atlas. |
| [x] | Click | `9Pets-Cute-Click` | 304901 | Built from audited official chibi Spine source; rejected empty or faded jump motions and rebuilt with stable state-specific motions plus 4x detail atlas. |
| [ ] | Coppelia | `9Pets-Cute-Coppelia` | 314401 | Blocked for now; no matching local official chibi Spine folder was found under `roles`, so do not fake a cute variant from normal Live2D or static art. |
| [x] | Corvus | `9Pets-Cute-Corvus` | 313201 | Built from audited official chibi Spine source with state-specific motions and 4x detail atlas. |
| [ ] | Cristallo | `9Pets-Cute-Cristallo` | 303101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Darley Clatter | `9Pets-Cute-Darley-Clatter` | 305001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Desert Flannel | `9Pets-Cute-Desert-Flannel` | 307501 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Diggers | `9Pets-Cute-Diggers` | 306401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Dikke | `9Pets-Cute-Dikke` | 302201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Door | `9Pets-Cute-Door` | 305901 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Druvis III | `9Pets-Cute-Druvis-III` | 300301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Eagle | `9Pets-Cute-Eagle` | 300601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Enigma | `9Pets-Cute-Enigma` | 314301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Erick | `9Pets-Cute-Erick` | 305801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Eternity | `9Pets-Cute-Eternity` | 305101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Ezio Auditore | `9Pets-Cute-Ezio-Auditore` | 312301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Ezra Theodore | `9Pets-Cute-Ezra-Theodore` | 307401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Fatutu | `9Pets-Cute-Fatutu` | 310901 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Flutterpage | `9Pets-Cute-Flutterpage` | 310501 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Getian | `9Pets-Cute-Getian` | 308401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Hissabeth | `9Pets-Cute-Hissabeth` | 311601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Horropedia | `9Pets-Cute-Horropedia` | 306101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Igor | `9Pets-Cute-Igor` | 309201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Isolde | `9Pets-Cute-Isolde` | 308101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | J | `9Pets-Cute-J` | 309401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Jessica | `9Pets-Cute-Jessica` | 305601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Jiu Niangzi | `9Pets-Cute-Jiu-Niangzi` | 308301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | John Titor | `9Pets-Cute-John-Titor` | 303601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Kaalaa Baunaa | `9Pets-Cute-Kaalaa-Baunaa` | 307001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Kakania | `9Pets-Cute-Kakania` | 308001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Kanjira | `9Pets-Cute-Kanjira` | 307101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Kassandra | `9Pets-Cute-Kassandra` | 312401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Kiperina | `9Pets-Cute-Kiperina` | 311701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | La Source | `9Pets-Cute-La-Source` | 303001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Leilani | `9Pets-Cute-Leilani` | 303501 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Liang Yue | `9Pets-Cute-Liang-Yue` | 311001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Lilya | `9Pets-Cute-Lilya` | 300401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Loggerhead | `9Pets-Cute-Loggerhead` | 311201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Lopera | `9Pets-Cute-Lopera` | 310201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Lorelei | `9Pets-Cute-Lorelei` | 309101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Lorentz Butterfly | `9Pets-Cute-Lorentz-Butterfly` | 313901 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Lucy | `9Pets-Cute-Lucy` | 308601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Marcus | `9Pets-Cute-Marcus` | 306501 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Marsha | `9Pets-Cute-Marsha` | 312701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Matilda | `9Pets-Cute-Matilda` | 304101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Medicine Pocket | `9Pets-Cute-Medicine-Pocket` | 304701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Melania | `9Pets-Cute-Melania` | 306201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Mercuria | `9Pets-Cute-Mercuria` | 309501 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Mesmer Jr. | `9Pets-Cute-Mesmer-Jr` | 305701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Moldir | `9Pets-Cute-Moldir` | 312101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Mondlicht | `9Pets-Cute-Mondlicht` | 302601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Mr. Duncan | `9Pets-Cute-Mr-Duncan` | 310301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Ms. Moissan | `9Pets-Cute-Ms-Moissan` | 304401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Ms. NewBabel | `9Pets-Cute-Ms-NewBabel` | 305201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Ms. Radio | `9Pets-Cute-Ms-Radio` | 302701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Ms. Stranger | `9Pets-Cute-Ms-Stranger` | 314701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Name Day | `9Pets-Cute-Name-Day` | 311801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Nautika | `9Pets-Cute-Nautika` | 312001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Necrologist | `9Pets-Cute-Necrologist` | 303701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Nick Bottom | `9Pets-Cute-Nick-Bottom` | 300501 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Noire | `9Pets-Cute-Noire` | 311101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Oliver Fog | `9Pets-Cute-Oliver-Fog` | 301801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | ONiON | `9Pets-Cute-ONiON` | 305401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Paper Heron | `9Pets-Cute-Paper-Heron` | 314101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Pavia | `9Pets-Cute-Pavia` | 301501 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Pickles | `9Pets-Cute-Pickles` | 306301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Pioneer | `9Pets-Cute-Pioneer` | 309601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Poltergeist | `9Pets-Cute-Poltergeist` | 304601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Rabies | `9Pets-Cute-Rabies` | 304201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Ramona | `9Pets-Cute-Ramona` | 314201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Recoleta | `9Pets-Cute-Recoleta` | 311401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Reed | `9Pets-Cute-Reed` | 313801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Regulus | `9Pets-Cute-Regulus` | 302504 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Rhiannon | `9Pets-Cute-Rhiannon` | 314601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Rubuska | `9Pets-Cute-Rubuska` | 312501 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Satsuki | `9Pets-Cute-Satsuki` | 303801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Semmelweis | `9Pets-Cute-Semmelweis` | 308801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Sentinel | `9Pets-Cute-Sentinel` | 312601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Shamane | `9Pets-Cute-Shamane` | 307201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Silverwing Eagle | `9Pets-Cute-Silverwing-Eagle` | 315401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Sonetto | `9Pets-Cute-Sonetto` | 302301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Sotheby | `9Pets-Cute-Sotheby` | 300902 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Spathodea | `9Pets-Cute-Spathodea` | 307301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Sputnik | `9Pets-Cute-Sputnik` | 305501 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Sweetheart | `9Pets-Cute-Sweetheart` | 301101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Tennant | `9Pets-Cute-Tennant` | 304301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | The Fool | `9Pets-Cute-The-Fool` | 301201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Tooth Fairy | `9Pets-Cute-Tooth-Fairy` | 305301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | TTT | `9Pets-Cute-TTT` | 303301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Tuesday | `9Pets-Cute-Tuesday` | 309801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Twins Sleep | `9Pets-Cute-Twins-Sleep` | 304001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Ulrich | `9Pets-Cute-Ulrich` | 310701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Ulu | `9Pets-Cute-Ulu` | 307601 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Vila | `9Pets-Cute-Vila` | 308701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Voyager | `9Pets-Cute-Voyager` | 304801 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | White Rum | `9Pets-Cute-White-Rum` | 310101 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Willow | `9Pets-Cute-Willow` | 310401 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Windsong | `9Pets-Cute-Windsong` | 307701 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Zima | `9Pets-Cute-Zima` | 301301 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | X | `9Pets-Cute-X` | 301001 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |
| [ ] | Yenisei | `9Pets-Cute-Yenisei` | 308201 | Todo; audit the official chibi/cartoon source and rebuild this cute variant one character at a time. |

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

### 2026-06-11 - Argus / 9Pets-Argus
- Source audit: local official Cubism folder `live2d/roles/v2a1_309701_aegs`; related official Spine folders `roles/v2a1_309701_aegs` and `roles/v2a1_309701_aegs_s` also exist.
- Live2D model: `v2a1_309701_aegs.model3.json` with 25 motion files and 7 expression files. The model lists a bloom texture before the main color texture, so the renderer now supports scoped `--primary-texture` and the Argus profile uses `textures/309701_aegs.png`.
- Motions selected: `idle=b_idle`, `running-right=b_baqiang1`, `running-left=b_baqiang2`, `waving=b_shenshou1`, `jumping=b_baqiang3`, `failed=b_yaotou`, `waiting=b_baoxiong`, `running=b_maoyan`, `review=b_diantou`.
- Capture settings: `1800x1800`, scale `0.84`, x `1050`, y `560`; raw frame minimum margins were left `414`, top `133`, right `742`, bottom `379`.
- Files changed: added scoped Argus Live2D profile and renderer primary texture support, rebuilt `pets/9Pets-Argus`, `docs/assets/spritesheets/9Pets-Argus.webp`, `docs/assets/detail-spritesheets/9Pets-Argus.webp`, `docs/assets/previews/9Pets-Argus.png`, `docs/downloads/9Pets-Argus.zip`, and docs data for Argus.
- QA artifacts: `C:\tmp\9pets-argus-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: `python -m py_compile tools\build_pets_site.py tools\smoke_site.py` passed; `node --check tools\render_live2d_frames.mjs` passed; `node --check tools\render_spine_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed and now checks Argus's detail spritesheet plus detail sprite frame bounds; targeted image QA found no cell-edge clipping, no static rows, and no transparent RGB residue.
- Decision: accepted for this pass.

### 2026-06-11 - Avgust / 9Pets-Avgust
- Source audit: local official Cubism folder `live2d/roles/v1a8_307801_afuxiwei`; related official Spine folder `roles/v1a8_307801_afuxiwei` also exists.
- Live2D model: `v1a8_307801_afuxiwei.model3.json` with 26 motion files and 6 expression files.
- Motions selected: `idle=b_idle`, `running-right=b_xiangrikui`, `running-left=b_diaozhui`, `waving=b_shenshou`, `jumping=b_xiangrikui`, `failed=b_yaotou`, `waiting=b_waitou`, `running=b_diaozhui`, `review=b_diantou`.
- Capture settings: `1800x1800`, scale `0.84`, x `1050`, y `560`; raw frame minimum margins were left `306`, top `164`, right `746`, bottom `375`.
- Files changed: added the scoped Avgust Live2D profile, rebuilt `pets/9Pets-Avgust`, `docs/assets/spritesheets/9Pets-Avgust.webp`, `docs/assets/detail-spritesheets/9Pets-Avgust.webp`, `docs/assets/previews/9Pets-Avgust.png`, `docs/downloads/9Pets-Avgust.zip`, and docs data for Avgust.
- QA artifacts: `C:\tmp\9pets-avgust-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: `python -m py_compile tools\build_pets_site.py tools\smoke_site.py` passed; `node --check tools\render_live2d_frames.mjs` passed; `node --check tools\render_spine_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed and now checks Avgust's detail spritesheet plus detail sprite frame bounds; targeted image QA found no cell-edge clipping, no static rows, and no transparent RGB residue.
- Decision: accepted for this pass.

### 2026-06-11 - Baby Blue / 9Pets-Baby-Blue
- Source audit: no matching normal Cubism folder was found under `live2d/roles`; official chibi Spine folders `roles/301601_yingerlan` and `roles/301601_yingerlan_s` exist.
- Spine source: `roles/301601_yingerlan/301601_yingerlan_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill1_1`, `skill2`, `sleep`, `unique`, and `victory`.
- Correction: this source is a chibi/cartoon battle model, not the normal character Live2D requested for the official normal table.
- Files changed: preserved the generated chibi output as `pets/9Pets-Cute-Baby-Blue`, `docs/assets/spritesheets/9Pets-Cute-Baby-Blue.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Baby-Blue.webp`, `docs/assets/previews/9Pets-Cute-Baby-Blue.png`, and `docs/downloads/9Pets-Cute-Baby-Blue.zip`; removed the scoped normal Baby Blue Spine profile and rebuilt `9Pets-Baby-Blue` as fallback.
- QA artifacts: prior chibi QA remains `C:\tmp\9pets-baby-blue-final-contact.png`; normal rebuild now has no accepted detail atlas.
- Verification: `python -m py_compile tools\build_pets_site.py tools\smoke_site.py` passed; `node --check tools\render_live2d_frames.mjs` passed; `node --check tools\render_spine_frames.mjs` passed; `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed; English-only text scan passed; cute zip prefix check passed; cute snapshot preservation check passed.
- Decision: not accepted as a normal official rebuild; tracked as completed cute variant `9Pets-Cute-Baby-Blue`.

### 2026-06-12 - Baby Blue Normal / 9Pets-Baby-Blue
- Source audit: local asset cache is at the same HEAD as `myssal/Reverse-1999-CN-Asset`; no Baby Blue Cubism `*.model3.json` or `*.motion3.json` was found under `live2d`. The available official animated source is `roles/301601_yingerlan`.
- Normal source decision: selected `301601_yingerlan_room.skel` as the normal equivalent source instead of the battle/cute `301601_yingerlan_fight.skel`; the separate cute package continues to use the chibi/battle track.
- Spine source: `301601_yingerlan_room.skel` with animations `click`, `hit`, `idle`, `idle_birthday_loop`, `idle_birthday_up`, `sleep`, and `walk`.
- Motions selected: `idle=idle`, `running-right=walk`, `running-left=walk` with renderer flip, `waving=click`, `jumping=idle_birthday_up`, `failed=hit`, `waiting=sleep`, `running=idle_birthday_loop`, `review=click`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `10`, top `4`, right `9`, bottom `6`.
- Files changed: added the scoped Baby Blue normal room Spine profile, rebuilt `pets/9Pets-Baby-Blue`, `docs/assets/spritesheets/9Pets-Baby-Blue.webp`, `docs/assets/detail-spritesheets/9Pets-Baby-Blue.webp`, `docs/assets/previews/9Pets-Baby-Blue.png`, `docs/downloads/9Pets-Baby-Blue.zip`, and docs data for Baby Blue.
- QA artifacts: `C:\tmp\9pets-baby-blue-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas. The official cat/head and birthday wand elements are attached motion elements, not detached render fragments.
- Decision: not accepted as the normal official rebuild after user review. The package files are preserved, but this room Spine source still reads as a cute/room model rather than the requested normal Live2D/Cubism character source.

### 2026-06-12 - Baby Blue Cute / 9Pets-Cute-Baby-Blue
- Source audit: local official chibi Spine folder `roles/301601_yingerlan`; alternate smaller folder `roles/301601_yingerlan_s` also exists but was not used for this cute pass.
- Spine source: `301601_yingerlan_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill1_1`, `skill2`, `sleep`, `unique`, and `victory`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=victory`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `7`, top `47`, right `7`, bottom `6`.
- Files changed: added the scoped Baby Blue cute Spine profile, rebuilt `pets/9Pets-Cute-Baby-Blue`, `docs/assets/spritesheets/9Pets-Cute-Baby-Blue.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Baby-Blue.webp`, `docs/assets/previews/9Pets-Cute-Baby-Blue.png`, `docs/downloads/9Pets-Cute-Baby-Blue.zip`, and docs cute data for Baby Blue.
- QA artifacts: `C:\tmp\9pets-cute-baby-blue-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-11 - Cute variant correction / 9Pets-Cute-Baby-Blue and 9Pets-Cute-Balloon-Party
- Correction: Baby Blue and Balloon Party chibi/cartoon battle Spine outputs were moved out of the official normal track.
- Files changed: created `pets/9Pets-Cute-Baby-Blue`, `pets/9Pets-Cute-Balloon-Party`, matching docs spritesheets, detail spritesheets, previews, and downloads; removed their normal-track Spine profiles; rebuilt `9Pets-Baby-Blue` and `9Pets-Balloon-Party` as official fallback packages; full site builds now preserve existing `9Pets-Cute-*` outputs.
- Rule update: future cute variants use `9Pets-Cute-XXX` and are tracked in the Cute Character Variant Todo Table.
- Verification: `python tools\verify_build.py` passed; `python tools\smoke_site.py` passed; English-only text scan passed; cute zip prefix check passed; cute snapshot preservation check passed.
- Decision at the time: normal Baby Blue and Balloon Party remained unchecked until a normal Live2D/Cubism or equivalent animated source was found.

### 2026-06-12 - Balloon Party Normal / 9Pets-Balloon-Party
- Source audit: local asset cache is at the same HEAD as `myssal/Reverse-1999-CN-Asset`; no Balloon Party Cubism `*.model3.json` was found under `live2d`. The available official animated source is `roles/302401_qiqiupaidui`.
- Normal source decision: selected `302401_qiqiupaidui_room.skel` as the normal equivalent source instead of the battle/cute `302401_qiqiupaidui_fight.skel`; the separate cute package continues to use the chibi/battle track.
- Spine source: `302401_qiqiupaidui_room.skel` with animations `click`, `hit`, `idle`, `sleep`, and `walk`.
- Motions selected: `idle=idle`, `running-right=walk`, `running-left=walk` with renderer flip, `waving=click`, `jumping=walk`, `failed=hit`, `waiting=sleep`, `running=walk`, `review=idle`. A temporary `running=click` candidate was rejected because the 6-frame capture included a detached pink effect.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `19`, top `4`, right `12`, bottom `6`.
- Files changed: added the scoped Balloon Party normal room Spine profile, rebuilt `pets/9Pets-Balloon-Party`, `docs/assets/spritesheets/9Pets-Balloon-Party.webp`, `docs/assets/detail-spritesheets/9Pets-Balloon-Party.webp`, `docs/assets/previews/9Pets-Balloon-Party.png`, `docs/downloads/9Pets-Balloon-Party.zip`, and docs data for Balloon Party.
- QA artifacts: `C:\tmp\9pets-balloon-party-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: not accepted as the normal official rebuild after user review. The package files are preserved, but this room Spine source still reads as a cute/room model rather than the requested normal Live2D/Cubism character source.

### 2026-06-12 - Balloon Party Cute / 9Pets-Cute-Balloon-Party
- Source audit: local official chibi Spine folder `roles/302401_qiqiupaidui`; alternate smaller folder `roles/302401_qiqiupaidui_s` also exists but was not used for this cute pass.
- Spine source: `302401_qiqiupaidui_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `23`, top `4`, right `23`, bottom `6`.
- Files changed: added the scoped Balloon Party cute Spine profile, rebuilt `pets/9Pets-Cute-Balloon-Party`, `docs/assets/spritesheets/9Pets-Cute-Balloon-Party.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Balloon-Party.webp`, `docs/assets/previews/9Pets-Cute-Balloon-Party.png`, `docs/downloads/9Pets-Cute-Balloon-Party.zip`, and docs cute data for Balloon Party.
- QA artifacts: `C:\tmp\9pets-cute-balloon-party-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas. The balloon remains connected by its string during the `unique` review motion.
- Decision: accepted for this cute pass.

### 2026-06-12 - Normal-source correction / Baby Blue and Balloon Party
- Correction: normal table completion was revoked for Baby Blue and Balloon Party. Local audit found no `*.model3.json` under `live2d/roles` for asset ids `301601` or `302401`; available animated sources are `roles/301601_yingerlan` and `roles/302401_qiqiupaidui`.
- Source comparison: `*_ui.skel` renders the same room-scale character but only has `idle` and `sleep`; `*_room.skel` has more state coverage but still reads as a cute/room model; `*_fight.skel` remains reserved for the Cute packages.
- Files changed: no generated packages were removed. Existing `9Pets-Baby-Blue` and `9Pets-Balloon-Party` room-Spine packages are preserved as produced artifacts, but their normal rebuild rows are unchecked until a proper normal Live2D/Cubism or equivalent normal animated source is found.
- QA artifacts reviewed: `C:\tmp\9pets-audit-baby-ui-frames\idle\00.png`, `C:\tmp\9pets-audit-baby-room-frames\idle\00.png`, `C:\tmp\9pets-audit-balloon-ui-frames`, and `C:\tmp\9pets-audit-balloon-room-frames`.
- Decision: leave Baby Blue and Balloon Party normal rows unchecked; keep `9Pets-Cute-Baby-Blue` and `9Pets-Cute-Balloon-Party` checked.

### 2026-06-12 - Barbara / 9Pets-Barbara
- Source audit: local official Cubism folder `live2d/roles/v2a1_309901_syg`; related official chibi Spine folder `roles/v2a1_309901_syg` also exists but was not used for the normal package.
- Live2D model: `v2a1_309901_syg.model3.json` with 19 motion files.
- Motions selected: `idle=b_idle`, `running-right=b_zhaierji`, `running-left=b_waitou`, `waving=b_zhaierji`, `jumping=b_zhaierji`, `failed=b_yaotou`, `waiting=b_fuxiong`, `running=b_sikao`, `review=b_diantou`.
- Capture settings: `1800x1800`, scale `0.84`, x `1050`, y `560`; final standard atlas minimum cell margins were left `56`, top `4`, right `55`, bottom `6`.
- Files changed: added the scoped Barbara Live2D profile, rebuilt `pets/9Pets-Barbara`, `docs/assets/spritesheets/9Pets-Barbara.webp`, `docs/assets/detail-spritesheets/9Pets-Barbara.webp`, `docs/assets/previews/9Pets-Barbara.png`, `docs/downloads/9Pets-Barbara.zip`, and docs data for Barbara.
- QA artifacts: `C:\tmp\9pets-barbara-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames and no transparent RGB residue in either the standard or detail atlas. This entry was added to close the missing detailed-worklog gap for a row already marked complete.
- Decision: accepted for this pass.

### 2026-06-11 - Barcarola / 9Pets-Barcarola
- Source audit: local official Cubism folder `live2d/roles/v2a4_310801_bkle`; nearby folders `live2d/roles/v2a4_310802_bkle` and `live2d/roles/v2a7_310803_bkle` were checked, and the default `310801` folder was kept for normal asset consistency.
- Live2D model: `v2a4_310801_bkle.model3.json` with 22 motion files.
- Motions selected: `idle=b_idle`, `running-right=b_zhihui`, `running-left=b_tanshou`, `waving=b_tanshou`, `jumping=b_tietie`, `failed=b_wuzui`, `waiting=b_chayao`, `running=b_zhihui`, `review=b_diantou`. A temporary `t_*` expression-motion candidate was rendered and rejected because it did not improve small-size readability.
- Capture settings: `1800x1800`, scale `0.78`, x `1050`, y `600`; final standard atlas minimum cell margins were left `44`, top `4`, right `44`, bottom `6`.
- Files changed: added the scoped Barcarola Live2D profile, rebuilt `pets/9Pets-Barcarola`, `docs/assets/spritesheets/9Pets-Barcarola.webp`, `docs/assets/detail-spritesheets/9Pets-Barcarola.webp`, `docs/assets/previews/9Pets-Barcarola.png`, `docs/downloads/9Pets-Barcarola.zip`, and docs data for Barcarola.
- QA artifacts: `C:\tmp\9pets-barcarola-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames and no transparent RGB residue in either the standard or detail atlas. The final contact sheet showed no head, hair, outfit, or instrument clipping.
- Decision: accepted for this pass.

### 2026-06-11 - Beryl / 9Pets-Beryl
- Source audit: local official Cubism folder `live2d/roles/v3a2_313401_ble`; related official chibi Spine folders `roles/v3a2_313401_ble` and `roles/v3a2_313401_ble_s` also exist but were not used for the normal package.
- Live2D model: `v3a2_313401_ble.model3.json` with 39 motion files.
- Motions selected: `idle=b_idle`, `running-right=b_liyi`, `running-left=b_bukan`, `waving=b_taishou`, `jumping=b_lingbai`, `failed=b_yaotou`, `waiting=b_fuxiong`, `running=b_bukan2`, `review=b_diantou`.
- Capture settings: `1800x1800`, scale `0.72`, x `1050`, y `640`; raw `idle/00` frame showed a complete head and full-body normal Live2D render.
- Files changed: added the scoped Beryl Live2D profile, rebuilt `pets/9Pets-Beryl`, `docs/assets/spritesheets/9Pets-Beryl.webp`, `docs/assets/detail-spritesheets/9Pets-Beryl.webp`, `docs/assets/previews/9Pets-Beryl.png`, `docs/downloads/9Pets-Beryl.zip`, and docs data for Beryl.
- QA artifacts: `C:\tmp\9pets-beryl-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames and no transparent RGB residue in either the standard or detail atlas. The final contact sheet showed a complete normal model with readable state-specific motion.
- Decision: accepted for this pass.

### 2026-06-11 - Bette / 9Pets-Bette
- Source audit: no matching normal Cubism folder was found under `live2d/roles`.
- Chibi source found: official Spine folders `roles/304501_beidi` and `roles/304501_beidi_s`.
- Decision: not accepted as a normal official rebuild because the available animated source is chibi battle Spine. Leave `9Pets-Bette` unchecked until a normal Live2D/Cubism or equivalent normal animated source is found. The chibi source can be used later for `9Pets-Cute-Bette`.

### 2026-06-11 - Bkornblume / 9Pets-Bkornblume
- Source audit: no matching normal Cubism folder was found under `live2d/roles`.
- Chibi source found: official Spine folders `roles/302001_bolinyidong` and `roles/302001_bolinyidong_s`.
- Decision: not accepted as a normal official rebuild because the available animated source is chibi battle Spine. Leave `9Pets-Bkornblume` unchecked until a normal Live2D/Cubism or equivalent normal animated source is found. The chibi source can be used later for `9Pets-Cute-Bkornblume`.

### 2026-06-11 - Blonney / 9Pets-Blonney
- Source audit: local official Cubism folder `live2d/roles/306001_jinmier`; related official chibi Spine folders `roles/306001_jinmier` and `roles/306001_jinmier_s` also exist but were not used for the normal package.
- Live2D model: `306001_jinmier.model3.json` with 20 motion files.
- Motions selected: `idle=b_idle`, `running-right=b_bijiben`, `running-left=b_motoufa`, `waving=b_motoufa`, `jumping=b_yaotou`, `failed=t_kongju`, `waiting=b_bijiben`, `running=b_bijiben`, `review=b_diantou`. A `b_sheyingji` candidate was rejected because it added a detached floating camera prop in several rows.
- Capture settings: `1800x1800`, scale `0.78`, x `1050`, y `900`; the initial y `620` candidate clipped the raw frame top and was rejected.
- Files changed: added the scoped Blonney Live2D profile, rebuilt `pets/9Pets-Blonney`, `docs/assets/spritesheets/9Pets-Blonney.webp`, `docs/assets/detail-spritesheets/9Pets-Blonney.webp`, `docs/assets/previews/9Pets-Blonney.png`, `docs/downloads/9Pets-Blonney.zip`, and docs data for Blonney.
- QA artifacts: `C:\tmp\9pets-blonney-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames and no transparent RGB residue in either the standard or detail atlas. The final contact sheet showed no raw capture clipping and no detached camera artifact.
- Decision: accepted for this pass.

### 2026-06-12 - Brimley / 9Pets-Brimley
- Source audit: local official Cubism folder `live2d/roles/v2a3_310601_kym`; related official chibi Spine folders `roles/v2a3_310601_kym` and `roles/v2a3_310601_kym_s` also exist but were not used for the normal package.
- Live2D model: `v2a3_310601_kym.model3.json` with 9 motion files and 1 expression file.
- Motions selected: `idle=b_idle`, `running-right=b_xingli`, `running-left=b_feizou`, `waving=b_xingfen`, `jumping=b_tiaoyue`, `failed=b_shoushang`, `waiting=b_shiluo`, `running=b_feizou`, `review=b_shiluo`.
- Capture settings: `1800x1800`, scale `0.78`, x `1050`, y `900`; final standard atlas minimum cell margins were left `10`, top `4`, right `10`, bottom `6`.
- Files changed: added the scoped Brimley Live2D profile, rebuilt `pets/9Pets-Brimley`, `docs/assets/spritesheets/9Pets-Brimley.webp`, `docs/assets/detail-spritesheets/9Pets-Brimley.webp`, `docs/assets/previews/9Pets-Brimley.png`, `docs/downloads/9Pets-Brimley.zip`, and docs data for Brimley.
- QA artifacts: `C:\tmp\9pets-brimley-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames and no transparent RGB residue in either the standard or detail atlas. The final contact sheet showed visible state-specific motion without clipped head, coat, or wheel.
- Decision: accepted for this pass.

### 2026-06-12 - Brimley Cute / 9Pets-Cute-Brimley
- Source audit: local official chibi Spine folder `roles/v2a3_310601_kym`; alternate smaller folder `roles/v2a3_310601_kym_s` also exists but was not used for this cute pass.
- Spine source: `310601_kym_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=idle`, `running=skill1`, `review=posture`. Earlier `sleep`, `unique`, and `skill2` candidates were rejected because they produced detached hat/body fragments.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `12`, top `4`, right `12`, bottom `6`.
- Files changed: added one-character cute build support with `--cute-only`, added the scoped Brimley cute Spine profile, built `pets/9Pets-Cute-Brimley`, `docs/assets/spritesheets/9Pets-Cute-Brimley.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Brimley.webp`, `docs/assets/previews/9Pets-Cute-Brimley.png`, `docs/downloads/9Pets-Cute-Brimley.zip`, and docs cute data for Brimley.
- QA artifacts: `C:\tmp\9pets-cute-brimley-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Brume / 9Pets-Brume
- Source audit: local official Cubism folder `live2d/roles/v3a2_313501_hdl`; related official chibi Spine folders `roles/v3a2_313501_hdl` and `roles/v3a2_313501_hdl_s` also exist but were not used for the normal package.
- Live2D model: `v3a2_313501_hdl.model3.json` with 30 motion files and 10 expression files.
- Motions selected: `idle=b_idle`, `running-right=b_xiaolong`, `running-left=b_fue`, `waving=b_tanshou`, `jumping=b_wuli`, `failed=b_yaotou`, `waiting=b_jinzhang`, `running=b_xiaolong`, `review=b_diantou`.
- Capture settings: `1800x2200`, scale `0.68`, x `1050`, y `760`; final standard atlas minimum cell margins were left `48`, top `4`, right `48`, bottom `6`.
- Files changed: added the scoped Brume Live2D profile, rebuilt `pets/9Pets-Brume`, `docs/assets/spritesheets/9Pets-Brume.webp`, `docs/assets/detail-spritesheets/9Pets-Brume.webp`, `docs/assets/previews/9Pets-Brume.png`, `docs/downloads/9Pets-Brume.zip`, and docs data for Brume.
- QA artifacts: `C:\tmp\9pets-brume-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames and no transparent RGB residue in either the standard or detail atlas. The final contact sheet showed visible state-specific Live2D motion without head, clothing, or prop clipping.
- Decision: accepted for this pass.

### 2026-06-12 - Brume Cute / 9Pets-Cute-Brume
- Source audit: local official chibi Spine folder `roles/v3a2_313501_hdl`; alternate smaller folder `roles/v3a2_313501_hdl_s` also exists but was not used for this cute pass.
- Spine source: `313501_hdl_fight.skel` with animations `born`, `channel_idle`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `skill2_1`, `skill2_2`, `skill3`, `skill3_1`, `sleep`, `unique`, `unique_2`, `unique_3`, `unique_4`, `unique_5`, and `unique_6`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=channel_idle`, `running=skill2`, `review=channel_idle`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `23`, top `4`, right `23`, bottom `6`.
- Files changed: added the scoped Brume cute Spine profile, built `pets/9Pets-Cute-Brume`, `docs/assets/spritesheets/9Pets-Cute-Brume.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Brume.webp`, `docs/assets/previews/9Pets-Cute-Brume.png`, `docs/downloads/9Pets-Cute-Brume.zip`, and docs cute data for Brume.
- QA artifacts: `C:\tmp\9pets-cute-brume-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Buddy Fairchild / 9Pets-Buddy-Fairchild
- Source audit: local official Cubism folder `live2d/roles/v2a8_311501_jjsg`; related official chibi Spine folders `roles/v2a8_311501_jjsg` and `roles/v2a8_311501_jjsg_s` also exist but were not used for the normal package.
- Live2D model: `v2a8_311501_jjsg.model3.json` with 27 motion files and 4 expression files.
- Motions selected: `idle=b_idle`, `running-right=b_huiqi1`, `running-left=b_huiqi2`, `waving=b_zhi1`, `jumping=b_wulian`, `failed=b_yaotou1`, `waiting=b_sikao1`, `running=b_sikao2`, `review=b_diantou1`.
- Capture settings: `1800x1800`, scale `0.78`, x `1050`, y `860`; final standard atlas minimum cell margins were left `8`, top `4`, right `8`, bottom `6`.
- Files changed: added the scoped Buddy Fairchild Live2D profile, rebuilt `pets/9Pets-Buddy-Fairchild`, `docs/assets/spritesheets/9Pets-Buddy-Fairchild.webp`, `docs/assets/detail-spritesheets/9Pets-Buddy-Fairchild.webp`, `docs/assets/previews/9Pets-Buddy-Fairchild.png`, `docs/downloads/9Pets-Buddy-Fairchild.zip`, and docs data for Buddy Fairchild.
- QA artifacts: `C:\tmp\9pets-buddy-fairchild-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames and no transparent RGB residue in either the standard or detail atlas. The final contact sheet showed visible state-specific Live2D motion without character, crate, or paper clipping.
- Decision: accepted for this pass.

### 2026-06-12 - Buddy Fairchild Cute / 9Pets-Cute-Buddy-Fairchild
- Source audit: local official chibi Spine folder `roles/v2a8_311501_jjsg`; alternate smaller folder `roles/v2a8_311501_jjsg_s` also exists but was not used for this cute pass.
- Spine source: `311501_jjsg_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=posture`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `18`, top `4`, right `11`, bottom `6`.
- Files changed: added the scoped Buddy Fairchild cute Spine profile, built `pets/9Pets-Cute-Buddy-Fairchild`, `docs/assets/spritesheets/9Pets-Cute-Buddy-Fairchild.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Buddy-Fairchild.webp`, `docs/assets/previews/9Pets-Cute-Buddy-Fairchild.png`, `docs/downloads/9Pets-Cute-Buddy-Fairchild.zip`, and docs cute data for Buddy Fairchild.
- QA artifacts: `C:\tmp\9pets-cute-buddy-fairchild-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Bunny Bunny / 9Pets-Bunny-Bunny
- Source audit: no matching normal Cubism folder was found under `live2d/roles` during a broad local search for asset id `301401`.
- Chibi source found: official Spine folders `roles/301401_banibani` and `roles/301401_banibani_s`.
- Decision: not accepted as a normal official rebuild because the available animated source is chibi battle Spine. Leave `9Pets-Bunny-Bunny` unchecked until a normal Live2D/Cubism or equivalent normal animated source is found. The chibi source is being used for `9Pets-Cute-Bunny-Bunny`.

### 2026-06-12 - Bunny Bunny Cute / 9Pets-Cute-Bunny-Bunny
- Source audit: local official chibi Spine folder `roles/301401_banibani`; alternate smaller folder `roles/301401_banibani_s` also exists but was not used for this cute pass.
- Spine source: `301401_banibani_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `innate1`, `posture`, `skill1`, `skill2`, `sleep`, `unique`, and `victory`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=victory`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `14`, top `4`, right `14`, bottom `6`.
- Files changed: added the scoped Bunny Bunny cute Spine profile, built `pets/9Pets-Cute-Bunny-Bunny`, `docs/assets/spritesheets/9Pets-Cute-Bunny-Bunny.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Bunny-Bunny.webp`, `docs/assets/previews/9Pets-Cute-Bunny-Bunny.png`, `docs/downloads/9Pets-Cute-Bunny-Bunny.zip`, and docs cute data for Bunny Bunny.
- QA artifacts: `C:\tmp\9pets-cute-bunny-bunny-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Centurion / 9Pets-Centurion
- Source audit: no matching normal Cubism folder was found under `live2d/roles` during a broad local search for asset id `303201`.
- Chibi source found: official Spine folders `roles/303201_baifuzhang` and `roles/303201_baifuzhang_s`.
- Decision: not accepted as a normal official rebuild because the available animated source is chibi battle Spine. Leave `9Pets-Centurion` unchecked until a normal Live2D/Cubism or equivalent normal animated source is found. The chibi source is being used for `9Pets-Cute-Centurion`.

### 2026-06-12 - Centurion Cute / 9Pets-Cute-Centurion
- Source audit: local official chibi Spine folder `roles/303201_baifuzhang`; alternate smaller folder `roles/303201_baifuzhang_s` also exists but was not used for this cute pass.
- Spine source: `303201_baifuzhang_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `idle_special1`, `posture`, `skill1`, `skill1_1`, `skill2`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=giddy`, `waiting=posture`, `running=skill1`, `review=posture`. Earlier `idle_special1` and `skill1_1` candidates were rejected because they produced detached fragments.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `40`, top `4`, right `41`, bottom `6`.
- Files changed: added the scoped Centurion cute Spine profile, built `pets/9Pets-Cute-Centurion`, `docs/assets/spritesheets/9Pets-Cute-Centurion.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Centurion.webp`, `docs/assets/previews/9Pets-Cute-Centurion.png`, `docs/downloads/9Pets-Cute-Centurion.zip`, and docs cute data for Centurion.
- QA artifacts: `C:\tmp\9pets-cute-centurion-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Charlie Normal / 9Pets-Charlie
- Source audit: no matching Charlie Cubism `*.model3.json` was found under `live2d`; the only matching local official animated source is `roles/301701_xiali`.
- Normal source decision: selected `301701_xiali_room.skel` as the normal equivalent source instead of the battle/cute `301701_xiali_fight.skel`; the separate cute package uses the chibi/battle track.
- Spine source: `301701_xiali_room.skel` with animations `click`, `hit`, `idle`, `sleep`, and `walk`.
- Motions selected: `idle=idle`, `running-right=walk`, `running-left=walk` with renderer flip, `waving=click`, `jumping=walk`, `failed=hit`, `waiting=sleep`, `running=walk`, `review=idle`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `17`, top `4`, right `17`, bottom `6`.
- Files changed: added the scoped Charlie normal room Spine profile, rebuilt `pets/9Pets-Charlie`, `docs/assets/spritesheets/9Pets-Charlie.webp`, `docs/assets/detail-spritesheets/9Pets-Charlie.webp`, `docs/assets/previews/9Pets-Charlie.png`, `docs/downloads/9Pets-Charlie.zip`, and docs data for Charlie.
- QA artifacts: `C:\tmp\9pets-charlie-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this pass.

### 2026-06-12 - Charlie Cute / 9Pets-Cute-Charlie
- Source audit: local official chibi Spine folder `roles/301701_xiali`; alternate smaller folder `roles/301701_xiali_s` also exists but was not used for this cute pass.
- Spine source: `301701_xiali_fight.skel` with animations `born`, `change`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, `unique`, and `victory`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=victory`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `7`, top `15`, right `7`, bottom `6`.
- Files changed: added the scoped Charlie cute Spine profile, rebuilt `pets/9Pets-Cute-Charlie`, `docs/assets/spritesheets/9Pets-Cute-Charlie.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Charlie.webp`, `docs/assets/previews/9Pets-Cute-Charlie.png`, `docs/downloads/9Pets-Cute-Charlie.zip`, and docs cute data for Charlie.
- QA artifacts: `C:\tmp\9pets-cute-charlie-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Charon / 9Pets-Charon
- Source audit: local official Cubism folder `live2d/roles/v3a0_312801_kr`; unrelated Barcarola folders also matched loose text searches and were rejected.
- Live2D model: `v3a0_312801_kr.model3.json` with 13 motion files and 1 expression file.
- Motions selected: `idle=b_idle`, `running-right=b_goupai`, `running-left=b_fanshu`, `waving=b_xianhua`, `jumping=b_fanshu3`, `failed=b_yaotou`, `waiting=b_fuxiong`, `running=b_goupai`, `review=b_diantou`.
- Capture settings: `1800x2200`, scale `0.68`, x `1050`, y `760`; final standard atlas minimum cell margins were left `44`, top `4`, right `45`, bottom `6`.
- Files changed: added the scoped Charon Live2D profile, rebuilt `pets/9Pets-Charon`, `docs/assets/spritesheets/9Pets-Charon.webp`, `docs/assets/detail-spritesheets/9Pets-Charon.webp`, `docs/assets/previews/9Pets-Charon.png`, `docs/downloads/9Pets-Charon.zip`, and docs data for Charon.
- QA artifacts: `C:\tmp\9pets-charon-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas. The final contact sheet showed visible state-specific Live2D motion without head, hair, hand, or red ground-effect clipping.
- Decision: accepted for this pass.

### 2026-06-12 - Charon Cute / 9Pets-Cute-Charon
- Source audit: local official chibi Spine folder `roles/v3a0_312801_kr`; no alternate `_s` folder was needed for this cute pass.
- Spine source: `312801_kr_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `skill3`, `sleep`, and `unique`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `16`, top `4`, right `16`, bottom `6`.
- Files changed: added the scoped Charon cute Spine profile, rebuilt `pets/9Pets-Cute-Charon`, `docs/assets/spritesheets/9Pets-Cute-Charon.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Charon.webp`, `docs/assets/previews/9Pets-Cute-Charon.png`, `docs/downloads/9Pets-Cute-Charon.zip`, and docs cute data for Charon.
- QA artifacts: `C:\tmp\9pets-cute-charon-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Cheng Heguang / 9Pets-Cheng-Heguang
- Source audit: local official Cubism folder `live2d/roles/v3a4_313701_chg`; related official chibi Spine folders `roles/v3a4_313701_chg` and `roles/v3a4_313701_chg_s` also exist but were not used for the normal package.
- Live2D model: `v3a4_313701_chg.model3.json` with 26 motion files and 8 expression files.
- Motions selected: `idle=b_idle`, `running-right=b_baoquan`, `running-left=b_zuanquan`, `waving=b_qing`, `jumping=b_zuanquan`, `failed=b_yaotou`, `waiting=b_cazui`, `running=b_baoquan2`, `review=b_diantou`.
- Capture settings: `1800x2200`, scale `0.68`, x `1050`, y `760`; final standard atlas minimum cell margins were left `30`, top `4`, right `31`, bottom `6`.
- Files changed: added the scoped Cheng Heguang Live2D profile, rebuilt `pets/9Pets-Cheng-Heguang`, `docs/assets/spritesheets/9Pets-Cheng-Heguang.webp`, `docs/assets/detail-spritesheets/9Pets-Cheng-Heguang.webp`, `docs/assets/previews/9Pets-Cheng-Heguang.png`, `docs/downloads/9Pets-Cheng-Heguang.zip`, and docs data for Cheng Heguang.
- QA artifacts: `C:\tmp\9pets-cheng-heguang-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas. The final contact sheet showed visible state-specific Live2D motion without head, hair, outfit, or weapon clipping.
- Decision: accepted for this pass.

### 2026-06-12 - Cheng Heguang Cute / 9Pets-Cute-Cheng-Heguang
- Source audit: local official chibi Spine folder `roles/v3a4_313701_chg`; alternate smaller folder `roles/v3a4_313701_chg_s` also exists but was not used for this cute pass.
- Spine source: `313701_chg_fight.skel` with animations `born`, `channel_idle`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `skill3`, `sleep`, `unique`, `unique2`, and `unique3`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=channel_idle`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `20`, top `4`, right `21`, bottom `6`.
- Files changed: added the scoped Cheng Heguang cute Spine profile, built `pets/9Pets-Cute-Cheng-Heguang`, `docs/assets/spritesheets/9Pets-Cute-Cheng-Heguang.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Cheng-Heguang.webp`, `docs/assets/previews/9Pets-Cute-Cheng-Heguang.png`, `docs/downloads/9Pets-Cute-Cheng-Heguang.zip`, and docs cute data for Cheng Heguang.
- QA artifacts: `C:\tmp\9pets-cute-cheng-heguang-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Click / 9Pets-Click
- Source audit: local official Cubism folder `live2d/roles/304901_kachakacha`; related official chibi Spine folders `roles/304901_kachakacha` and `roles/304901_kachakacha_s` also exist but were not used for the normal package.
- Live2D model: `304901_kachakacha.model3.json` with 19 motion files and 6 expression files.
- Motions selected: `idle=b_idle`, `running-right=b_xiangji`, `running-left=b_paizhao`, `waving=b_naotou`, `jumping=b_paizhao`, `failed=b_yaotou`, `waiting=b_jiaojuan`, `running=b_xiangji`, `review=b_diantou`.
- Capture settings: `1800x1800`, scale `0.84`, x `1050`, y `560`; final standard atlas minimum cell margins were left `56`, top `4`, right `55`, bottom `6`.
- Files changed: added the scoped Click Live2D profile, rebuilt `pets/9Pets-Click`, `docs/assets/spritesheets/9Pets-Click.webp`, `docs/assets/detail-spritesheets/9Pets-Click.webp`, `docs/assets/previews/9Pets-Click.png`, `docs/downloads/9Pets-Click.zip`, and docs data for Click.
- QA artifacts: `C:\tmp\9pets-click-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas. The final contact sheet showed normal Live2D character proportions with attached camera and bag elements.
- Decision: accepted for this pass.

### 2026-06-12 - Click Cute / 9Pets-Cute-Click
- Source audit: local official chibi Spine folder `roles/304901_kachakacha`; alternate smaller folder `roles/304901_kachakacha_s` also exists but was not used for this cute pass.
- Spine source: `304901_kachakacha_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `innate`, `posture`, `skill1`, `skill1_1`, `skill2`, `skill2_1`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=giddy`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Rejected motions: `skill1` produced empty and semi-transparent jump frames; `skill1_1` and `skill2_1` produced empty frames; `unique_1` rendered a separate plane-only asset instead of Click. The final `jumping=giddy` choice avoids the transparent/empty-frame failure.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `50`, top `4`, right `37`, bottom `6`.
- Files changed: added the scoped Click cute Spine profile, built `pets/9Pets-Cute-Click`, `docs/assets/spritesheets/9Pets-Cute-Click.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Click.webp`, `docs/assets/previews/9Pets-Cute-Click.png`, `docs/downloads/9Pets-Cute-Click.zip`, and docs cute data for Click.
- QA artifacts: rejected candidate contact `C:\tmp\9pets-cute-click-reject-contact.png`; accepted final contact `C:\tmp\9pets-cute-click-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Coppelia / 9Pets-Coppelia
- Source audit: local official Cubism folder `live2d/roles/v3a7_314401_fly`; no matching local official chibi Spine folder was found under `roles` for asset id `314401`.
- Live2D model: `v3a7_314401_fly.model3.json` with 28 motion files and 7 expression files.
- Motions selected: `idle=b_idle`, `running-right=b_yincha`, `running-left=b_tanshou`, `waving=b_tanshou`, `jumping=b_yincha`, `failed=b_kuqi`, `waiting=b_kuqi1`, `running=b_sikao`, `review=b_diantou`.
- Capture settings: `1800x2200`, scale `0.68`, x `1050`, y `760`; final standard atlas minimum cell margins were left `54`, top `4`, right `55`, bottom `6`.
- Files changed: added the scoped Coppelia Live2D profile, rebuilt `pets/9Pets-Coppelia`, `docs/assets/spritesheets/9Pets-Coppelia.webp`, `docs/assets/detail-spritesheets/9Pets-Coppelia.webp`, `docs/assets/previews/9Pets-Coppelia.png`, `docs/downloads/9Pets-Coppelia.zip`, and docs data for Coppelia.
- QA artifacts: `C:\tmp\9pets-coppelia-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, and no edge clipping in either the standard or detail atlas. The final contact sheet showed visible state-specific Live2D motion without hair, dress, or blue effect clipping.
- Decision: accepted for this normal pass.

### 2026-06-12 - Coppelia Cute / 9Pets-Cute-Coppelia
- Source audit: local search found `live2d/roles/v3a7_314401_fly` for the normal model, but no matching `roles/v3a7_314401_fly`, `roles/314401_*`, or other local chibi Spine folder under `roles`.
- Decision: blocked for now. Do not build `9Pets-Cute-Coppelia` from the normal Live2D model or static artwork; wait until a proper official chibi/cartoon source is found.

### 2026-06-12 - Corvus / 9Pets-Corvus
- Source audit: local official Cubism folder `live2d/roles/v3a1_313201_gsn`; related official chibi Spine folders `roles/v3a1_313201_gsn` and `roles/v3a1_313201_gsn_s` also exist but were not used for the normal package.
- Live2D model: `v3a1_313201_gsn.model3.json` with 31 motion files and texture set `313201_gsn`.
- Motions selected: `idle=b_idle`, `running-right=b_chakan`, `running-left=b_chiqiang`, `waving=b_taishou`, `jumping=b_yamao`, `failed=b_yaotou`, `waiting=b_zhiweijin_loop`, `running=b_chakan_loop`, `review=b_diantou`.
- Capture settings: `1800x2200`, scale `0.68`, x `1050`, y `760`; final standard atlas minimum cell margins were left `44`, top `4`, right `43`, bottom `6`.
- Files changed: added the scoped Corvus Live2D profile, rebuilt `pets/9Pets-Corvus`, `docs/assets/spritesheets/9Pets-Corvus.webp`, `docs/assets/detail-spritesheets/9Pets-Corvus.webp`, `docs/assets/previews/9Pets-Corvus.png`, `docs/downloads/9Pets-Corvus.zip`, and docs data for Corvus.
- QA artifacts: `C:\tmp\9pets-corvus-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas. The final contact sheet showed the normal Live2D character proportions with visible state-specific motion and no head, hair, outfit, or prop clipping.
- Decision: accepted for this normal pass.

### 2026-06-12 - Corvus Cute / 9Pets-Cute-Corvus
- Source audit: local official chibi Spine folder `roles/v3a1_313201_gsn`; alternate smaller folder `roles/v3a1_313201_gsn_s` also exists but was not used for this cute pass.
- Spine source: `313201_gsn_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `skill3`, `sleep`, `unique`, `unique_1`, `unique_2`, `unique_3`, and `unique_4`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `7`, top `18`, right `7`, bottom `6`.
- Files changed: added the scoped Corvus cute Spine profile, built `pets/9Pets-Cute-Corvus`, `docs/assets/spritesheets/9Pets-Cute-Corvus.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Corvus.webp`, `docs/assets/previews/9Pets-Cute-Corvus.png`, `docs/downloads/9Pets-Cute-Corvus.zip`, and docs cute data for Corvus.
- QA artifacts: `C:\tmp\9pets-cute-corvus-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas. The final contact sheet used the chibi/cute proportions and did not replace the normal package source.
- Decision: accepted for this cute pass.
