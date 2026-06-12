# 9Pets One-Character Rebuild Worklog

This file replaces the previous completion checklist. It is the durable guide for future agents after context compaction. Keep it in English so the repository remains English-only.

## Current Rule

Work on exactly one character at a time.

Official normal pets must use the character's normal Live2D/Cubism model or an equivalent normal animated source. Do not accept chibi/cartoon battle Spine assets as normal official rebuilds.

Cute/chibi variants are tracked separately and must use the package naming rule `9Pets-Cute-XXX`.

Do not mark a character done because a bulk script produced files. A character is done only after its own source audit, Live2D motion capture, crop/quality pass, package rebuild, site update, and visual QA have all passed.

## Active Character Slot

Only one character may be active here at a time. Fill this slot before touching generated assets, then clear it after the row is marked done.

- Active character: none
- Package: none
- Asset id: none
- Source folder audited: complete through Yenisei, plus A Knight and Coppelia cute unblocks
- Live2D model used: n/a
- Motion files selected: n/a
- Last QA artifact: final verification pending after worklog cleanup
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
| [x] | A Knight | `9Pets-A-Knight` | official-live2d-cubism | rendered | 300731 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
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
| [x] | Bette | `9Pets-Bette` | official-art-elastic-rig | mapped | 304501 | Rebuilt one-character pass from audited official room Spine source, avoiding the battle/cute track, with state-specific room motions and 4x detail atlas. |
| [x] | Bkornblume | `9Pets-Bkornblume` | official-art-elastic-rig | mapped | 302001 | Rebuilt one-character pass from audited official room Spine source, avoiding the battle/cute track, with state-specific room motions and 4x detail atlas. |
| [x] | Blonney | `9Pets-Blonney` | official-live2d-cubism | rendered | 306001 | Rebuilt one-character pass with audited Live2D source, Blonney-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Brimley | `9Pets-Brimley` | official-live2d-cubism | rendered | 310601 | Rebuilt one-character pass with audited Live2D source, Brimley-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Brume | `9Pets-Brume` | official-live2d-cubism | rendered | 313501 | Rebuilt one-character pass with audited Live2D source, Brume-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Buddy Fairchild | `9Pets-Buddy-Fairchild` | official-live2d-cubism | rendered | 311501 | Rebuilt one-character pass with audited Live2D source, Buddy Fairchild-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Bunny Bunny | `9Pets-Bunny-Bunny` | official-art-elastic-rig | mapped | 301401 | Rebuilt one-character pass from audited official room Spine source, avoiding the battle/cute track, with state-specific room motions and 4x detail atlas. |
| [x] | Centurion | `9Pets-Centurion` | official-art-elastic-rig | mapped | 303201 | Rebuilt one-character pass from audited official room Spine source, avoiding the battle/cute track, with state-specific room motions and 4x detail atlas. |
| [x] | Charlie | `9Pets-Charlie` | official-art-elastic-rig | mapped | 301701 | Rebuilt one-character pass from audited official room Spine source, avoiding the battle/cute track, with state-specific room motions and 4x detail atlas. |
| [x] | Charon | `9Pets-Charon` | official-live2d-cubism | rendered | 312801 | Rebuilt one-character pass with audited Live2D source, Charon-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Cheng Heguang | `9Pets-Cheng-Heguang` | official-live2d-cubism | rendered | 313701 | Rebuilt one-character pass with audited Live2D source, Cheng Heguang-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Click | `9Pets-Click` | official-live2d-cubism | rendered | 304901 | Rebuilt one-character pass with audited Live2D source, Click-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Coppelia | `9Pets-Coppelia` | official-live2d-cubism | rendered | 314401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Corvus | `9Pets-Corvus` | official-live2d-cubism | rendered | 313201 | Rebuilt one-character pass with audited normal Live2D source, Corvus-specific motion map, non-clipped capture, visible state motion, and 4x detail atlas. |
| [x] | Cristallo | `9Pets-Cristallo` | official-art-elastic-rig | mapped | 303101 | Rebuilt one-character pass from audited official room Spine source, avoiding the battle/cute track, with state-specific room motions and 4x detail atlas. |
| [x] | Darley Clatter | `9Pets-Darley-Clatter` | official-art-elastic-rig | mapped | 305001 | Rebuilt one-character pass from audited official room Spine source, keeping the fight/cute track separate, with state-specific room motions and 4x detail atlas. |
| [x] | Desert Flannel | `9Pets-Desert-Flannel` | official-live2d-cubism | rendered | 307501 | Rebuilt one-character pass with audited Live2D normal source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Diggers | `9Pets-Diggers` | official-live2d-cubism | rendered | 306401 | Rebuilt one-character pass with audited Live2D normal source, repaired official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Dikke | `9Pets-Dikke` | official-live2d-cubism | rendered | 302201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Door | `9Pets-Door` | official-art-elastic-rig | mapped | 305901 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Druvis III | `9Pets-Druvis-III` | official-live2d-cubism | rendered | 300301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Eagle | `9Pets-Eagle` | official-art-elastic-rig | mapped | 300601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Enigma | `9Pets-Enigma` | official-live2d-cubism | rendered | 314301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Erick | `9Pets-Erick` | official-art-elastic-rig | mapped | 305801 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Eternity | `9Pets-Eternity` | official-live2d-cubism | rendered | 305101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Ezio Auditore | `9Pets-Ezio-Auditore` | official-live2d-cubism | rendered | 312301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Ezra Theodore | `9Pets-Ezra-Theodore` | official-live2d-cubism | rendered | 307401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Fatutu | `9Pets-Fatutu` | official-live2d-cubism | rendered | 310901 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Flutterpage | `9Pets-Flutterpage` | official-live2d-cubism | rendered | 310501 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Getian | `9Pets-Getian` | official-live2d-cubism | rendered | 308401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Hissabeth | `9Pets-Hissabeth` | official-live2d-cubism | rendered | 311601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Horropedia | `9Pets-Horropedia` | official-live2d-cubism | rendered | 306101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Igor | `9Pets-Igor` | official-live2d-cubism | rendered | 309201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Isolde | `9Pets-Isolde` | official-live2d-cubism | rendered | 308101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | J | `9Pets-J` | official-live2d-cubism | rendered | 309401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Jessica | `9Pets-Jessica` | official-live2d-cubism | rendered | 305601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Jiu Niangzi | `9Pets-Jiu-Niangzi` | official-live2d-cubism | rendered | 308301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | John Titor | `9Pets-John-Titor` | official-art-elastic-rig | mapped | 303601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Kaalaa Baunaa | `9Pets-Kaalaa-Baunaa` | official-live2d-cubism | rendered | 307001 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Kakania | `9Pets-Kakania` | official-live2d-cubism | rendered | 308001 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Kanjira | `9Pets-Kanjira` | official-live2d-cubism | rendered | 307101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Kassandra | `9Pets-Kassandra` | official-live2d-cubism | rendered | 312401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Kiperina | `9Pets-Kiperina` | official-live2d-cubism | rendered | 311701 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | La Source | `9Pets-La-Source` | official-art-elastic-rig | mapped | 303001 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Leilani | `9Pets-Leilani` | official-art-elastic-rig | mapped | 303501 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Liang Yue | `9Pets-Liang-Yue` | official-live2d-cubism | rendered | 311001 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Lilya | `9Pets-Lilya` | official-live2d-cubism | rendered | 300401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Loggerhead | `9Pets-Loggerhead` | official-live2d-cubism | rendered | 311201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Lopera | `9Pets-Lopera` | official-live2d-cubism | rendered | 310201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Lorelei | `9Pets-Lorelei` | official-live2d-cubism | rendered | 309101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Lorentz Butterfly | `9Pets-Lorentz-Butterfly` | official-live2d-cubism | rendered | 313901 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Lucy | `9Pets-Lucy` | official-live2d-cubism | rendered | 308601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Marcus | `9Pets-Marcus` | official-live2d-cubism | rendered | 306501 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Marsha | `9Pets-Marsha` | official-live2d-cubism | rendered | 312701 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Matilda | `9Pets-Matilda` | official-live2d-cubism | rendered | 304101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Medicine Pocket | `9Pets-Medicine-Pocket` | official-live2d-cubism | rendered | 304701 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Melania | `9Pets-Melania` | official-live2d-cubism | rendered | 306201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Mercuria | `9Pets-Mercuria` | official-live2d-cubism | rendered | 309501 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Mesmer Jr. | `9Pets-Mesmer-Jr` | official-art-elastic-rig | mapped | 305701 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Moldir | `9Pets-Moldir` | official-live2d-cubism | rendered | 312101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Mondlicht | `9Pets-Mondlicht` | official-art-elastic-rig | mapped | 302601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Mr. Duncan | `9Pets-Mr-Duncan` | official-live2d-cubism | rendered | 310301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Ms. Moissan | `9Pets-Ms-Moissan` | official-art-elastic-rig | mapped | 304401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Ms. NewBabel | `9Pets-Ms-NewBabel` | official-live2d-cubism | rendered | 305201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Ms. Radio | `9Pets-Ms-Radio` | official-art-elastic-rig | mapped | 302701 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Ms. Stranger | `9Pets-Ms-Stranger` | official-live2d-cubism | rendered | 314701 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Name Day | `9Pets-Name-Day` | official-live2d-cubism | rendered | 311801 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Nautika | `9Pets-Nautika` | official-live2d-cubism | rendered | 312001 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Necrologist | `9Pets-Necrologist` | official-live2d-cubism | rendered | 303701 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Nick Bottom | `9Pets-Nick-Bottom` | official-art-elastic-rig | mapped | 300501 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Noire | `9Pets-Noire` | official-live2d-cubism | rendered | 311101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Oliver Fog | `9Pets-Oliver-Fog` | official-art-elastic-rig | mapped | 301801 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | ONiON | `9Pets-ONiON` | official-art-elastic-rig | mapped | 305401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Paper Heron | `9Pets-Paper-Heron` | official-live2d-cubism | rendered | 314101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Pavia | `9Pets-Pavia` | official-art-elastic-rig | mapped | 301501 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Pickles | `9Pets-Pickles` | official-live2d-cubism | rendered | 306301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Pioneer | `9Pets-Pioneer` | official-art-elastic-rig | mapped | 309601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Poltergeist | `9Pets-Poltergeist` | official-art-elastic-rig | mapped | 304601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Rabies | `9Pets-Rabies` | official-art-elastic-rig | mapped | 304201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Ramona | `9Pets-Ramona` | official-live2d-cubism | rendered | 314201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Recoleta | `9Pets-Recoleta` | official-live2d-cubism | rendered | 311401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Reed | `9Pets-Reed` | official-art-elastic-rig | mapped | 313801 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Regulus | `9Pets-Regulus` | official-live2d-cubism | rendered | 302504 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Rhiannon | `9Pets-Rhiannon` | official-live2d-cubism | rendered | 314601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Rubuska | `9Pets-Rubuska` | official-live2d-cubism | rendered | 312501 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Satsuki | `9Pets-Satsuki` | official-live2d-cubism | rendered | 303801 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Semmelweis | `9Pets-Semmelweis` | official-live2d-cubism | rendered | 308801 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Sentinel | `9Pets-Sentinel` | official-live2d-cubism | rendered | 312601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Shamane | `9Pets-Shamane` | official-live2d-cubism | rendered | 307201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Silverwing Eagle | `9Pets-Silverwing-Eagle` | official-live2d-cubism | rendered | 315401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Sonetto | `9Pets-Sonetto` | official-live2d-cubism | rendered | 302301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Sotheby | `9Pets-Sotheby` | official-live2d-cubism | rendered | 300902 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Spathodea | `9Pets-Spathodea` | official-live2d-cubism | rendered | 307301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Sputnik | `9Pets-Sputnik` | official-art-elastic-rig | mapped | 305501 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Sweetheart | `9Pets-Sweetheart` | official-art-elastic-rig | mapped | 301101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Tennant | `9Pets-Tennant` | official-live2d-cubism | rendered | 304301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | The Fool | `9Pets-The-Fool` | official-art-elastic-rig | mapped | 301201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Tooth Fairy | `9Pets-Tooth-Fairy` | official-live2d-cubism | rendered | 305301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | TTT | `9Pets-TTT` | official-art-elastic-rig | mapped | 303301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Tuesday | `9Pets-Tuesday` | official-live2d-cubism | rendered | 309801 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Twins Sleep | `9Pets-Twins-Sleep` | official-art-elastic-rig | mapped | 304001 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Ulrich | `9Pets-Ulrich` | official-live2d-cubism | rendered | 310701 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Ulu | `9Pets-Ulu` | official-art-elastic-rig | mapped | 307601 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Vila | `9Pets-Vila` | official-live2d-cubism | rendered | 308701 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Voyager | `9Pets-Voyager` | official-live2d-cubism | rendered | 304801 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | White Rum | `9Pets-White-Rum` | official-art-elastic-rig | mapped | 310101 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Willow | `9Pets-Willow` | official-live2d-cubism | rendered | 310401 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Windsong | `9Pets-Windsong` | official-live2d-cubism | rendered | 307701 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | X | `9Pets-X` | official-live2d-cubism | rendered | 301001 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Yenisei | `9Pets-Yenisei` | official-live2d-cubism | rendered | 308201 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |
| [x] | Zima | `9Pets-Zima` | official-art-elastic-rig | none | 301301 | Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, visible state motion, and 4x detail atlases. |

## Cute Character Variant Todo Table

Cute/chibi variants are separate from the official normal rebuild table. Build them one character at a time after auditing the chibi/cartoon source, and name each package `9Pets-Cute-XXX`.

| Done | Character | Cute package | Asset id | Cute rebuild note |
| --- | --- | --- | --- | --- |
| [x] | 37 | `9Pets-Cute-37` | 306601 | Built from audited official chibi Spine source with detached-effect candidate motions rejected and a 4x detail atlas. |
| [x] | 6 | `9Pets-Cute-6` | 307901 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | A Knight | `9Pets-Cute-A-Knight` | 300731 | Built from audited official chibi Spine source `roles/300701_weixiukai` during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Aleph | `9Pets-Cute-Aleph` | 311301 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | Alexios | `9Pets-Cute-Alexios` | 312201 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | aliEn T | `9Pets-Cute-aliEn-T` | 303401 | Built from audited official chibi Spine source; smaller `_s` source was rejected because it had too few animations. |
| [x] | An-an Lee | `9Pets-Cute-An-an-Lee` | 303901 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | Anjo Nala | `9Pets-Cute-Anjo-Nala` | 310001 | Built from audited official chibi Spine source with non-transition motions and a 4x detail atlas. |
| [x] | APPLe | `9Pets-Cute-APPLe` | 302801 | Built from audited official chibi Spine source; smaller `_s` source was rejected because it had too few animations. |
| [x] | Argus | `9Pets-Cute-Argus` | 309701 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | Avgust | `9Pets-Cute-Avgust` | 307801 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | Baby Blue | `9Pets-Cute-Baby-Blue` | 301601 | Rebuilt from audited official chibi Spine source with a reproducible scoped profile and 4x detail atlas. |
| [x] | Balloon Party | `9Pets-Cute-Balloon-Party` | 302401 | Rebuilt from audited official chibi Spine source with a reproducible scoped profile and 4x detail atlas. |
| [x] | Barbara | `9Pets-Cute-Barbara` | 309901 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | Barcarola | `9Pets-Cute-Barcarola` | 310801 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | Beryl | `9Pets-Cute-Beryl` | 313401 | Built from audited official chibi Spine source with detached-effect candidate motion rejected and a 4x detail atlas. |
| [x] | Bette | `9Pets-Cute-Bette` | 304501 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | Bkornblume | `9Pets-Cute-Bkornblume` | 302001 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | Blonney | `9Pets-Cute-Blonney` | 306001 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | Brimley | `9Pets-Cute-Brimley` | 310601 | Built from audited official chibi Spine source with detached-piece motions rejected and replaced. |
| [x] | Brume | `9Pets-Cute-Brume` | 313501 | Built from audited official chibi Spine source with state-specific motions and 4x detail atlas. |
| [x] | Buddy Fairchild | `9Pets-Cute-Buddy-Fairchild` | 311501 | Built from audited official chibi Spine source with state-specific motions and 4x detail atlas. |
| [x] | Bunny Bunny | `9Pets-Cute-Bunny-Bunny` | 301401 | Built from audited official chibi Spine source with state-specific motions and 4x detail atlas. |
| [x] | Centurion | `9Pets-Cute-Centurion` | 303201 | Built from audited official chibi Spine source; rejected detached-piece motions and rebuilt with stable state-specific motions and 4x detail atlas. |
| [x] | Charlie | `9Pets-Cute-Charlie` | 301701 | Built from audited official chibi Spine source with a reproducible scoped profile and 4x detail atlas. |
| [x] | Charon | `9Pets-Cute-Charon` | 312801 | Built from audited official chibi Spine source with a reproducible scoped profile and 4x detail atlas. |
| [x] | Cheng Heguang | `9Pets-Cute-Cheng-Heguang` | 313701 | Built from audited official chibi Spine source with state-specific motions and 4x detail atlas. |
| [x] | Click | `9Pets-Cute-Click` | 304901 | Built from audited official chibi Spine source; rejected empty or faded jump motions and rebuilt with stable state-specific motions plus 4x detail atlas. |
| [x] | Coppelia | `9Pets-Cute-Coppelia` | 314401 | Built from audited official chibi Spine source `roles/v3a7_314401_fly` during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Corvus | `9Pets-Cute-Corvus` | 313201 | Built from audited official chibi Spine source with state-specific motions and 4x detail atlas. |
| [x] | Cristallo | `9Pets-Cute-Cristallo` | 303101 | Built from audited official chibi Spine source with state-specific motions and a 4x detail atlas. |
| [x] | Darley Clatter | `9Pets-Cute-Darley-Clatter` | 305001 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Desert Flannel | `9Pets-Cute-Desert-Flannel` | 307501 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Diggers | `9Pets-Cute-Diggers` | 306401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Dikke | `9Pets-Cute-Dikke` | 302201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Door | `9Pets-Cute-Door` | 305901 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Druvis III | `9Pets-Cute-Druvis-III` | 300301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Eagle | `9Pets-Cute-Eagle` | 300601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Enigma | `9Pets-Cute-Enigma` | 314301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Erick | `9Pets-Cute-Erick` | 305801 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Eternity | `9Pets-Cute-Eternity` | 305101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Ezio Auditore | `9Pets-Cute-Ezio-Auditore` | 312301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Ezra Theodore | `9Pets-Cute-Ezra-Theodore` | 307401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Fatutu | `9Pets-Cute-Fatutu` | 310901 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Flutterpage | `9Pets-Cute-Flutterpage` | 310501 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Getian | `9Pets-Cute-Getian` | 308401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Hissabeth | `9Pets-Cute-Hissabeth` | 311601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Horropedia | `9Pets-Cute-Horropedia` | 306101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Igor | `9Pets-Cute-Igor` | 309201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Isolde | `9Pets-Cute-Isolde` | 308101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | J | `9Pets-Cute-J` | 309401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Jessica | `9Pets-Cute-Jessica` | 305601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Jiu Niangzi | `9Pets-Cute-Jiu-Niangzi` | 308301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | John Titor | `9Pets-Cute-John-Titor` | 303601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Kaalaa Baunaa | `9Pets-Cute-Kaalaa-Baunaa` | 307001 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Kakania | `9Pets-Cute-Kakania` | 308001 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Kanjira | `9Pets-Cute-Kanjira` | 307101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Kassandra | `9Pets-Cute-Kassandra` | 312401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Kiperina | `9Pets-Cute-Kiperina` | 311701 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | La Source | `9Pets-Cute-La-Source` | 303001 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Leilani | `9Pets-Cute-Leilani` | 303501 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Liang Yue | `9Pets-Cute-Liang-Yue` | 311001 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Lilya | `9Pets-Cute-Lilya` | 300401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Loggerhead | `9Pets-Cute-Loggerhead` | 311201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Lopera | `9Pets-Cute-Lopera` | 310201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Lorelei | `9Pets-Cute-Lorelei` | 309101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Lorentz Butterfly | `9Pets-Cute-Lorentz-Butterfly` | 313901 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Lucy | `9Pets-Cute-Lucy` | 308601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Marcus | `9Pets-Cute-Marcus` | 306501 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Marsha | `9Pets-Cute-Marsha` | 312701 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Matilda | `9Pets-Cute-Matilda` | 304101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Medicine Pocket | `9Pets-Cute-Medicine-Pocket` | 304701 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Melania | `9Pets-Cute-Melania` | 306201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Mercuria | `9Pets-Cute-Mercuria` | 309501 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Mesmer Jr. | `9Pets-Cute-Mesmer-Jr` | 305701 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Moldir | `9Pets-Cute-Moldir` | 312101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Mondlicht | `9Pets-Cute-Mondlicht` | 302601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Mr. Duncan | `9Pets-Cute-Mr-Duncan` | 310301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Ms. Moissan | `9Pets-Cute-Ms-Moissan` | 304401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Ms. NewBabel | `9Pets-Cute-Ms-NewBabel` | 305201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Ms. Radio | `9Pets-Cute-Ms-Radio` | 302701 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Ms. Stranger | `9Pets-Cute-Ms-Stranger` | 314701 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Name Day | `9Pets-Cute-Name-Day` | 311801 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Nautika | `9Pets-Cute-Nautika` | 312001 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Necrologist | `9Pets-Cute-Necrologist` | 303701 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Nick Bottom | `9Pets-Cute-Nick-Bottom` | 300501 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Noire | `9Pets-Cute-Noire` | 311101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Oliver Fog | `9Pets-Cute-Oliver-Fog` | 301801 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | ONiON | `9Pets-Cute-ONiON` | 305401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Paper Heron | `9Pets-Cute-Paper-Heron` | 314101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Pavia | `9Pets-Cute-Pavia` | 301501 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Pickles | `9Pets-Cute-Pickles` | 306301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Pioneer | `9Pets-Cute-Pioneer` | 309601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Poltergeist | `9Pets-Cute-Poltergeist` | 304601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Rabies | `9Pets-Cute-Rabies` | 304201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Ramona | `9Pets-Cute-Ramona` | 314201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Recoleta | `9Pets-Cute-Recoleta` | 311401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Reed | `9Pets-Cute-Reed` | 313801 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Regulus | `9Pets-Cute-Regulus` | 302504 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Rhiannon | `9Pets-Cute-Rhiannon` | 314601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Rubuska | `9Pets-Cute-Rubuska` | 312501 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Satsuki | `9Pets-Cute-Satsuki` | 303801 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Semmelweis | `9Pets-Cute-Semmelweis` | 308801 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Sentinel | `9Pets-Cute-Sentinel` | 312601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Shamane | `9Pets-Cute-Shamane` | 307201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Silverwing Eagle | `9Pets-Cute-Silverwing-Eagle` | 315401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Sonetto | `9Pets-Cute-Sonetto` | 302301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Sotheby | `9Pets-Cute-Sotheby` | 300902 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Spathodea | `9Pets-Cute-Spathodea` | 307301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Sputnik | `9Pets-Cute-Sputnik` | 305501 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Sweetheart | `9Pets-Cute-Sweetheart` | 301101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Tennant | `9Pets-Cute-Tennant` | 304301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | The Fool | `9Pets-Cute-The-Fool` | 301201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Tooth Fairy | `9Pets-Cute-Tooth-Fairy` | 305301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | TTT | `9Pets-Cute-TTT` | 303301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Tuesday | `9Pets-Cute-Tuesday` | 309801 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Twins Sleep | `9Pets-Cute-Twins-Sleep` | 304001 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Ulrich | `9Pets-Cute-Ulrich` | 310701 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Ulu | `9Pets-Cute-Ulu` | 307601 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Vila | `9Pets-Cute-Vila` | 308701 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Voyager | `9Pets-Cute-Voyager` | 304801 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | White Rum | `9Pets-Cute-White-Rum` | 310101 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Willow | `9Pets-Cute-Willow` | 310401 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Windsong | `9Pets-Cute-Windsong` | 307701 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Zima | `9Pets-Cute-Zima` | 301301 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | X | `9Pets-Cute-X` | 301001 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |
| [x] | Yenisei | `9Pets-Cute-Yenisei` | 308201 | Built from audited official chibi Spine source during the one-character rebuild pass, with package/site QA passing and a 4x detail atlas. |

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
- Superseded: the 2026-06-12 Bette Normal pass accepted the primary `304501_beidi_room.skel` room source as normal-equivalent, while keeping battle Spine for `9Pets-Cute-Bette`.
- Source audit: no matching normal Cubism folder was found under `live2d/roles`.
- Chibi source found: official Spine folders `roles/304501_beidi` and `roles/304501_beidi_s`.
- Decision: not accepted as a normal official rebuild because the available animated source is chibi battle Spine. Leave `9Pets-Bette` unchecked until a normal Live2D/Cubism or equivalent normal animated source is found. The chibi source can be used later for `9Pets-Cute-Bette`.

### 2026-06-11 - Bkornblume / 9Pets-Bkornblume
- Superseded: the 2026-06-12 Bkornblume Normal pass accepted the primary `302001_bolinyidong_room.skel` room source as normal-equivalent, while keeping battle Spine for `9Pets-Cute-Bkornblume`.
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

### 2026-06-12 - 37 Cute / 9Pets-Cute-37
- Source audit: local official chibi Spine folder `roles/v1a4_306601_37`; alternate smaller folder `roles/v1a4_306601_37_s` also exists but was not used for this cute pass.
- Spine source: `306601_37_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `idle_special1`, `posture`, `skill1`, `skill1_1`, `skill2`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=idle_special1`, `running-left=idle_special1` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=idle_special1`.
- Rejected motions: first `posture` directional candidate showed a detached yellow effect beside the sprite, and `review=unique_1` produced empty review frames after atlas composition.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `14`, top `32`, right `7`, bottom `6`.
- Files changed: added the scoped 37 cute Spine profile, built `pets/9Pets-Cute-37`, `docs/assets/spritesheets/9Pets-Cute-37.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-37.webp`, `docs/assets/previews/9Pets-Cute-37.png`, `docs/downloads/9Pets-Cute-37.zip`, and docs cute data for 37.
- QA artifacts: rejected candidate contact `C:\tmp\9pets-cute-37-candidate-contact.png`; accepted final contact `C:\tmp\9pets-cute-37-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - 6 Cute / 9Pets-Cute-6
- Source audit: local official chibi Spine folder `roles/v1a4_307901_6`; alternate smaller folder `roles/v1a4_307901_6_s` also exists but was not used for this cute pass.
- Spine source: `307901_6_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `idle_special1`, `posture`, `skill1`, `skill2`, `sleep`, and `unique`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `35`, top `4`, right `35`, bottom `6`.
- Files changed: added the scoped 6 cute Spine profile, built `pets/9Pets-Cute-6`, `docs/assets/spritesheets/9Pets-Cute-6.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-6.webp`, `docs/assets/previews/9Pets-Cute-6.png`, `docs/downloads/9Pets-Cute-6.zip`, and docs cute data for 6.
- QA artifacts: `C:\tmp\9pets-cute-6-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - A Knight Cute / 9Pets-Cute-A-Knight
- Source audit: no matching local official chibi Spine folder was found under `roles` for asset id `300731`, internal name `wxk`, or likely A Knight name variants.
- Normal source found: `live2d/roles/v3a1_300731_wxk` with `v3a1_300731_wxk.model3.json`, `v3a1_300731_wxk.moc3`, and normal Live2D textures.
- Decision: blocked for now. Do not build `9Pets-Cute-A-Knight` from the normal Live2D model or static artwork; wait until a proper official chibi/cartoon source is found.

### 2026-06-12 - Aleph Cute / 9Pets-Cute-Aleph
- Source audit: local official chibi Spine folder `roles/v2a6_311301_alf`; alternate smaller folder `roles/v2a6_311301_alf_s` also exists but was not used for this cute pass.
- Spine source: `311301_alf_fight.skel` with animations `born`, `change`, `channel_idle`, `channel_start`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `sleep`, `unique`, and `unique_3`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=channel_idle`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `26`, top `4`, right `26`, bottom `6`.
- Files changed: added the scoped Aleph cute Spine profile, built `pets/9Pets-Cute-Aleph`, `docs/assets/spritesheets/9Pets-Cute-Aleph.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Aleph.webp`, `docs/assets/previews/9Pets-Cute-Aleph.png`, `docs/downloads/9Pets-Cute-Aleph.zip`, and docs cute data for Aleph.
- QA artifacts: `C:\tmp\9pets-cute-aleph-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Alexios Cute / 9Pets-Cute-Alexios
- Source audit: local official chibi Spine folder `roles/s01_312201_alkxos`; alternate smaller folder `roles/s01_312201_alkxos_s` also exists but was not used for this cute pass.
- Spine source: `312201_alkxos_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, and `unique`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `7`, top `78`, right `58`, bottom `6`.
- Files changed: added the scoped Alexios cute Spine profile, built `pets/9Pets-Cute-Alexios`, `docs/assets/spritesheets/9Pets-Cute-Alexios.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Alexios.webp`, `docs/assets/previews/9Pets-Cute-Alexios.png`, `docs/downloads/9Pets-Cute-Alexios.zip`, and docs cute data for Alexios.
- QA artifacts: `C:\tmp\9pets-cute-alexios-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - aliEn T Cute / 9Pets-Cute-aliEn-T
- Source audit: local official chibi Spine folder `roles/303401_xingzhiyan`; alternate smaller folder `roles/303401_xingzhiyan_s` exists but was rejected because its fight skeleton only exposed `born`, `idle`, and `jump`.
- Spine source: `303401_xingzhiyan_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Source limitation: the normal package also uses the primary Spine source because no normal Cubism source was found for this character; the cute package remains separately named and packaged.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `54`, top `4`, right `55`, bottom `6`.
- Files changed: added the scoped aliEn T cute Spine profile, built `pets/9Pets-Cute-aliEn-T`, `docs/assets/spritesheets/9Pets-Cute-aliEn-T.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-aliEn-T.webp`, `docs/assets/previews/9Pets-Cute-aliEn-T.png`, `docs/downloads/9Pets-Cute-aliEn-T.zip`, and docs cute data for aliEn T.
- QA artifacts: `C:\tmp\9pets-cute-alien-t-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - An-an Lee Cute / 9Pets-Cute-An-an-Lee
- Source audit: local official chibi Spine folder `roles/303901_nimengdishi`; alternate smaller folder `roles/303901_nimengdishi_s` also exists but was not used for this cute pass.
- Spine source: `303901_nimengdishi_fight.skel` with animations `born`, `change`, `change2`, `die`, `freeze`, `giddy`, `hit`, `idle`, `idle_special1`, `innate`, `innate_1`, `posture`, `skill1`, `skill1_1`, `skill2`, `sleep`, and `unique`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `20`, top `4`, right `20`, bottom `6`.
- Files changed: added the scoped An-an Lee cute Spine profile, built `pets/9Pets-Cute-An-an-Lee`, `docs/assets/spritesheets/9Pets-Cute-An-an-Lee.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-An-an-Lee.webp`, `docs/assets/previews/9Pets-Cute-An-an-Lee.png`, `docs/downloads/9Pets-Cute-An-an-Lee.zip`, and docs cute data for An-an Lee.
- QA artifacts: `C:\tmp\9pets-cute-an-an-lee-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Anjo Nala Cute / 9Pets-Cute-Anjo-Nala
- Source audit: local official chibi Spine folder `roles/v2a2_310001_tsnn`; alternate smaller folder `roles/v2a2_310001_tsnn_s` also exists but was not used for this cute pass.
- Spine source: `310001_tsnn_fight.skel` with animations `born`, `channel_idle`, `channel_start`, `die`, `freeze`, `giddy`, `giddy_trans`, `hit`, `hit_trans`, `idle`, `idle_trans`, `posture`, `posture_trans`, `skill1`, `skill1_1`, `skill2`, `skill3`, `skill3_1`, `sleep`, `sleep_trans`, and `unique`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Rejected motion family: `_trans` transition motions were not used because they are not needed for the Codex state loops and can introduce unwanted transparent transition states.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `16`, top `4`, right `15`, bottom `6`.
- Files changed: added the scoped Anjo Nala cute Spine profile, built `pets/9Pets-Cute-Anjo-Nala`, `docs/assets/spritesheets/9Pets-Cute-Anjo-Nala.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Anjo-Nala.webp`, `docs/assets/previews/9Pets-Cute-Anjo-Nala.png`, `docs/downloads/9Pets-Cute-Anjo-Nala.zip`, and docs cute data for Anjo Nala.
- QA artifacts: `C:\tmp\9pets-cute-anjo-nala-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - APPLe Cute / 9Pets-Cute-APPLe
- Source audit: local official chibi Spine folder `roles/302801_apple`; alternate smaller folder `roles/302801_apple_s` exists but was rejected because its fight skeleton only exposed `born`, `idle`, and `jump`.
- Spine source: `302801_apple_fight.skel` with animations `born`, `die`, `die_special`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `skill3`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=skill3`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=posture`.
- Source limitation: the normal package also uses the primary Spine source because no normal Cubism source was found for this character; the cute package remains separately named and packaged.
- Capture settings: `1600x1600`, scale `2.2`, x `800`, y `1150`; final standard atlas minimum cell margins were left `7`, top `8`, right `7`, bottom `6`.
- Files changed: added the scoped APPLe cute Spine profile, built `pets/9Pets-Cute-APPLe`, `docs/assets/spritesheets/9Pets-Cute-APPLe.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-APPLe.webp`, `docs/assets/previews/9Pets-Cute-APPLe.png`, `docs/downloads/9Pets-Cute-APPLe.zip`, and docs cute data for APPLe.
- QA artifacts: `C:\tmp\9pets-cute-apple-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Argus Cute / 9Pets-Cute-Argus
- Source audit: local official chibi Spine folder `roles/v2a1_309701_aegs`; alternate smaller folder `roles/v2a1_309701_aegs_s` also exists but was not used for this cute pass.
- Spine source: `309701_aegs_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `skill3`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `27`, top `4`, right `27`, bottom `6`.
- Files changed: added the scoped Argus cute Spine profile, built `pets/9Pets-Cute-Argus`, `docs/assets/spritesheets/9Pets-Cute-Argus.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Argus.webp`, `docs/assets/previews/9Pets-Cute-Argus.png`, `docs/downloads/9Pets-Cute-Argus.zip`, and docs cute data for Argus.
- QA artifacts: `C:\tmp\9pets-cute-argus-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Avgust Cute / 9Pets-Cute-Avgust
- Source audit: local official chibi Spine folder `roles/v1a8_307801_afuxiwei`; no alternate `_s` folder was found for this cute pass.
- Spine source: `307801_afuxiwei_fight.skel` with animations `born`, `change2`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, `unique`, `unique_2`, `unique_3`, and `unique_4`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `7`, top `4`, right `8`, bottom `6`.
- Files changed: added the scoped Avgust cute Spine profile, built `pets/9Pets-Cute-Avgust`, `docs/assets/spritesheets/9Pets-Cute-Avgust.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Avgust.webp`, `docs/assets/previews/9Pets-Cute-Avgust.png`, `docs/downloads/9Pets-Cute-Avgust.zip`, and docs cute data for Avgust.
- QA artifacts: `C:\tmp\9pets-cute-avgust-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Bunny Bunny Normal / 9Pets-Bunny-Bunny
- Source audit: no matching normal Cubism `*.model3.json` was found under `live2d` for asset id `301401` or internal name `banibani`.
- Normal source decision: selected `roles/301401_banibani/301401_banibani_room.skel` as the normal-equivalent animated source instead of the battle/cute `301401_banibani_fight.skel`.
- Spine source: `301401_banibani_room.skel` with animations `click`, `hit`, `idle`, `idle_birthday_loop`, `idle_birthday_up`, `sleep`, and `walk`.
- Motions selected: `idle=idle`, `running-right=walk`, `running-left=walk` with renderer flip, `waving=click`, `jumping=idle_birthday_up`, `failed=hit`, `waiting=sleep`, `running=idle_birthday_loop`, `review=click`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `7`, top `34`, right `7`, bottom `6`.
- Files changed: added the scoped Bunny Bunny normal room Spine profile, rebuilt `pets/9Pets-Bunny-Bunny`, `docs/assets/spritesheets/9Pets-Bunny-Bunny.webp`, `docs/assets/detail-spritesheets/9Pets-Bunny-Bunny.webp`, `docs/assets/previews/9Pets-Bunny-Bunny.png`, `docs/downloads/9Pets-Bunny-Bunny.zip`, and docs data for Bunny Bunny.
- QA artifacts: `C:\tmp\9pets-bunny-bunny-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Centurion Normal / 9Pets-Centurion
- Source audit: no matching normal Cubism `*.model3.json` was found under `live2d` for asset id `303201` or internal name `baifuzhang`.
- Normal source decision: selected `roles/303201_baifuzhang/303201_baifuzhang_room.skel` as the normal-equivalent animated source instead of the battle/cute `303201_baifuzhang_fight.skel`.
- Spine source: `303201_baifuzhang_room.skel` with animations `click`, `hit`, `idle`, `idle_birthday_loop`, `idle_birthday_up`, `idle_room`, `sleep`, and `walk`.
- Motions selected: `idle=idle`, `running-right=walk`, `running-left=walk` with renderer flip, `waving=click`, `jumping=idle_birthday_up`, `failed=hit`, `waiting=sleep`, `running=idle_birthday_loop`, `review=idle_room`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `7`, top `11`, right `7`, bottom `6`.
- Files changed: added the scoped Centurion normal room Spine profile, rebuilt `pets/9Pets-Centurion`, `docs/assets/spritesheets/9Pets-Centurion.webp`, `docs/assets/detail-spritesheets/9Pets-Centurion.webp`, `docs/assets/previews/9Pets-Centurion.png`, `docs/downloads/9Pets-Centurion.zip`, and docs data for Centurion.
- QA artifacts: `C:\tmp\9pets-centurion-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Baby Blue and Balloon Party Normal Final Audit
- Baby Blue audit: no matching normal Cubism `*.model3.json` or `*.motion3.json` was found under `live2d` for asset id `301601` or internal name `yingerlan`.
- Baby Blue available animation: `roles/301601_yingerlan/301601_yingerlan_room.skel` with animations `click`, `hit`, `idle`, `idle_birthday_loop`, `idle_birthday_up`, `sleep`, and `walk`; existing generated package is preserved but remains unaccepted for the normal table.
- Balloon Party audit: no matching normal Cubism `*.model3.json` or `*.motion3.json` was found under `live2d` for asset id `302401` or internal name `qiqiupaidui`.
- Balloon Party available animation: `roles/302401_qiqiupaidui/302401_qiqiupaidui_room.skel` with animations `click`, `hit`, `idle`, `sleep`, and `walk`; existing generated package is preserved but remains unaccepted for the normal table.
- Decision: keep both normal rows unchecked. Do not mark Baby Blue or Balloon Party normal complete unless a proper normal Cubism source or a user-approved normal-equivalent source is found.

### 2026-06-12 - Baby Blue Normal Re-Audit / 9Pets-Baby-Blue
- Source audit: checked local `live2d/roles` and the GitHub `live2d/roles` tree for asset id `301601` and internal name `yingerlan`; no normal Cubism folder, `*.model3.json`, `*.moc3`, or `*.motion3.json` source was found.
- Available animation: local official Spine folders `roles/301601_yingerlan` and `roles/301601_yingerlan_s` exist. The primary folder exposes `301601_yingerlan_room.skel`, `301601_yingerlan_ui.skel`, and `301601_yingerlan_fight.skel`; the `_s` folder is a smaller chibi source.
- Decision: blocked for Normal. Keep the table row unchecked and preserve existing files until a proper normal Cubism source or explicitly accepted normal-equivalent source is found.

### 2026-06-12 - Balloon Party Normal Re-Audit / 9Pets-Balloon-Party
- Source audit: checked local `live2d/roles` and the GitHub `live2d/roles` tree for asset id `302401` and internal name `qiqiupaidui`; no normal Cubism folder, `*.model3.json`, `*.moc3`, or `*.motion3.json` source was found.
- Available animation: local official Spine folders `roles/302401_qiqiupaidui` and `roles/302401_qiqiupaidui_s` exist. The primary folder exposes `302401_qiqiupaidui_room.skel`, `302401_qiqiupaidui_ui.skel`, and `302401_qiqiupaidui_fight.skel`; the `_s` folder is a smaller chibi source.
- Decision: blocked for Normal. Keep the table row unchecked and preserve existing files until a proper normal Cubism source or explicitly accepted normal-equivalent source is found.

### 2026-06-12 - Bette Normal / 9Pets-Bette
- Source audit: no matching normal Cubism source was found under `live2d/roles` for asset id `304501` or internal name `beidi`.
- Normal source decision: selected `roles/304501_beidi/304501_beidi_room.skel` as the normal-equivalent animated source instead of the battle/cute `304501_beidi_fight.skel` or `_s` folder.
- Spine source: `304501_beidi_room.skel` with animations `click`, `hit`, `idle`, `idle_birthday_loop`, `idle_birthday_up`, `sleep`, and `walk`.
- Motions selected: `idle=idle`, `running-right=walk`, `running-left=walk` with renderer flip, `waving=click`, `jumping=idle_birthday_up`, `failed=hit`, `waiting=sleep`, `running=idle_birthday_loop`, `review=click`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `20`, top `4`, right `20`, bottom `6`.
- Files changed: added the scoped Bette normal room Spine profile, rebuilt `pets/9Pets-Bette`, `docs/assets/spritesheets/9Pets-Bette.webp`, `docs/assets/detail-spritesheets/9Pets-Bette.webp`, `docs/assets/previews/9Pets-Bette.png`, `docs/downloads/9Pets-Bette.zip`, and docs data for Bette.
- QA artifacts: `C:\tmp\9pets-bette-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Bkornblume Normal / 9Pets-Bkornblume
- Source audit: no matching normal Cubism source was found under `live2d/roles` for asset id `302001` or internal name `bolinyidong`.
- Normal source decision: selected `roles/302001_bolinyidong/302001_bolinyidong_room.skel` as the normal-equivalent animated source instead of the battle/cute `302001_bolinyidong_fight.skel` or `_s` folder.
- Spine source: `302001_bolinyidong_room.skel` with animations `click`, `hit`, `idle`, `sleep`, and `walk`.
- Motions selected: `idle=idle`, `running-right=walk`, `running-left=walk` with renderer flip, `waving=click`, `jumping=walk`, `failed=hit`, `waiting=sleep`, `running=walk`, `review=click`.
- Source limitation: the room skeleton exposes only five motions, so several Codex states reuse `walk` or `click`; no battle or cute Spine actions were mixed into the Normal package.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `17`, top `4`, right `17`, bottom `6`.
- Files changed: added the scoped Bkornblume normal room Spine profile, rebuilt `pets/9Pets-Bkornblume`, `docs/assets/spritesheets/9Pets-Bkornblume.webp`, `docs/assets/detail-spritesheets/9Pets-Bkornblume.webp`, `docs/assets/previews/9Pets-Bkornblume.png`, `docs/downloads/9Pets-Bkornblume.zip`, and docs data for Bkornblume.
- QA artifacts: `C:\tmp\9pets-bkornblume-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Barbara Cute / 9Pets-Cute-Barbara
- Source audit: local official chibi Spine folder `roles/v2a1_309901_syg`; alternate smaller folder `roles/v2a1_309901_syg_s` also exists but was not used for this cute pass.
- Spine source: `309901_syg_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `40`, top `4`, right `39`, bottom `6`.
- Files changed: added the scoped Barbara cute Spine profile, built `pets/9Pets-Cute-Barbara`, `docs/assets/spritesheets/9Pets-Cute-Barbara.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Barbara.webp`, `docs/assets/previews/9Pets-Cute-Barbara.png`, `docs/downloads/9Pets-Cute-Barbara.zip`, and docs cute data for Barbara.
- QA artifacts: `C:\tmp\9pets-cute-barbara-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Barcarola Cute / 9Pets-Cute-Barcarola
- Source audit: local official chibi Spine folder `roles/v2a4_310801_bkle`; alternate smaller folder `roles/v2a4_310801_bkle_s` also exists but was not used for this cute pass.
- Spine source: `310801_bkle_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, `unique`, `unique_1`, `unique_2`, and `unique_3`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `7`, top `11`, right `15`, bottom `6`.
- Files changed: added the scoped Barcarola cute Spine profile, built `pets/9Pets-Cute-Barcarola`, `docs/assets/spritesheets/9Pets-Cute-Barcarola.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Barcarola.webp`, `docs/assets/previews/9Pets-Cute-Barcarola.png`, `docs/downloads/9Pets-Cute-Barcarola.zip`, and docs cute data for Barcarola.
- QA artifacts: `C:\tmp\9pets-cute-barcarola-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Beryl Cute / 9Pets-Cute-Beryl
- Source audit: local official chibi Spine folder `roles/v3a2_313401_ble`; alternate smaller folder `roles/v3a2_313401_ble_s` also exists but was not used for this cute pass.
- Spine source: `313401_ble_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `skill3`, `sleep`, `unique`, and `unique2`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill3`, `review=unique`.
- Rejected motion: first `running=skill2` candidate produced detached small effect fragments in the running row, so it was replaced with the cleaner `skill3` candidate.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `24`, top `4`, right `25`, bottom `6`.
- Files changed: added the scoped Beryl cute Spine profile, built `pets/9Pets-Cute-Beryl`, `docs/assets/spritesheets/9Pets-Cute-Beryl.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Beryl.webp`, `docs/assets/previews/9Pets-Cute-Beryl.png`, `docs/downloads/9Pets-Cute-Beryl.zip`, and docs cute data for Beryl.
- QA artifacts: rejected visual observation from the first Beryl contact sheet before the motion fix, candidate comparison `C:\tmp\9pets-beryl-running-candidates.png`, and accepted final contact `C:\tmp\9pets-cute-beryl-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas after the `skill3` rebuild.
- Decision: accepted for this cute pass.

### 2026-06-12 - Bette Cute / 9Pets-Cute-Bette
- Source audit: local official chibi Spine folder `roles/304501_beidi`; alternate smaller folder `roles/304501_beidi_s` also exists but was not used for this cute pass.
- Spine source: `304501_beidi_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill1_1`, `skill2`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `15`, top `4`, right `15`, bottom `6`.
- Files changed: added the scoped Bette cute Spine profile, built `pets/9Pets-Cute-Bette`, `docs/assets/spritesheets/9Pets-Cute-Bette.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Bette.webp`, `docs/assets/previews/9Pets-Cute-Bette.png`, `docs/downloads/9Pets-Cute-Bette.zip`, and docs cute data for Bette.
- QA artifacts: `C:\tmp\9pets-cute-bette-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Bkornblume Cute / 9Pets-Cute-Bkornblume
- Source audit: local official chibi Spine folder `roles/302001_bolinyidong`; alternate smaller folder `roles/302001_bolinyidong_s` also exists but was not used for this cute pass.
- Spine source: `302001_bolinyidong_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `skill2_1`, `skill2_2`, `sleep`, `unique`, `unique_1`, `unique_2`, and `victory`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `16`, top `4`, right `16`, bottom `6`.
- Files changed: added the scoped Bkornblume cute Spine profile, built `pets/9Pets-Cute-Bkornblume`, `docs/assets/spritesheets/9Pets-Cute-Bkornblume.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Bkornblume.webp`, `docs/assets/previews/9Pets-Cute-Bkornblume.png`, `docs/downloads/9Pets-Cute-Bkornblume.zip`, and docs cute data for Bkornblume.
- QA artifacts: `C:\tmp\9pets-cute-bkornblume-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Blonney Cute / 9Pets-Cute-Blonney
- Source audit: local official chibi Spine folder `roles/306001_jinmier`; alternate smaller folder `roles/306001_jinmier_s` also exists but was not used for this cute pass.
- Spine source: `306001_jinmier_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill1_1`, `skill2`, `sleep`, `unique`, and `unique_1`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; final standard atlas minimum cell margins were left `7`, top `10`, right `7`, bottom `6`.
- Files changed: added the scoped Blonney cute Spine profile, built `pets/9Pets-Cute-Blonney`, `docs/assets/spritesheets/9Pets-Cute-Blonney.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Blonney.webp`, `docs/assets/previews/9Pets-Cute-Blonney.png`, `docs/downloads/9Pets-Cute-Blonney.zip`, and docs cute data for Blonney.
- QA artifacts: `C:\tmp\9pets-cute-blonney-final-contact.png`; detail atlas is `6144x7488` with 4x atlas scale.
- Verification: targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas. Visual QA accepted the attached weapon effect in the review row because it stays connected to the sprite.
- Decision: accepted for this cute pass.

### 2026-06-12 - Site Normal/Cute Visibility Correction
- Scope: site and generator metadata correction, not a new Normal acceptance for Baby Blue or Balloon Party.
- Normal visibility rule: `9Pets-Baby-Blue` and `9Pets-Balloon-Party` are now hidden from the exported Normal catalog because their Normal rows remain blocked. Existing local package files are preserved, but `docs/data/pets.json` no longer lists them under `pets`.
- Cute independence rule: Cute variants are now built from `9Pets-Cute-*` package data instead of copying the normal source-art fields. This keeps `9Pets-Cute-Baby-Blue` and `9Pets-Cute-Balloon-Party` visible even while their Normal entries are hidden.
- Source art correction: Cute detail pages now use generated `docs/assets/source/9Pets-Cute-*.png` frame images from the Cute spritesheets, and their source links point to the relevant official Spine asset folder instead of the standard character portrait.
- Navigation correction: `docs/app.js` accepts `?variant=cute`, and `docs/pet.js` rewrites Back, Catalog, and logo links so Cute detail pages return to `index.html?variant=cute#catalog` in both hosted and `file://` modes.
- Files changed: updated `tools/build_pets_site.py`, `docs/app.js`, `docs/pet.js`, `tools/verify_build.py`, `tools/smoke_site.py`, rebuilt `9Pets-Cute-Baby-Blue`, regenerated docs data, and added Cute source art images for existing Cute packages.
- Verification: `python -m py_compile tools\build_pets_site.py tools\smoke_site.py tools\verify_build.py`, `node --check docs\app.js`, `node --check docs\pet.js`, `python tools\verify_build.py`, and `python tools\smoke_site.py` passed. Build verifier now reports `pets=125 official=125`; Cute total remains `28`.
- Decision: accepted as the current site-data contract. Do not re-add Baby Blue or Balloon Party to the Normal catalog unless their blocked Normal rows are explicitly accepted later.

### 2026-06-12 - Cristallo Normal / 9Pets-Cristallo
- Source audit: no matching normal Cubism `*.model3.json` was found under `live2d/roles` for asset id `303101`; unrelated Matilda motions named `b_shuijingqiu.motion3.json` were not used.
- Normal source decision: selected `roles/303101_qianboli/303101_qianboli_room.skel` as the normal-equivalent animated source instead of `303101_qianboli_fight.skel` or the smaller `_s` folder.
- Spine source: `303101_qianboli_room.skel` with animations `click`, `hit`, `idle`, `idle_birthday_loop`, `idle_birthday_up`, `sleep`, and `walk`.
- Motions selected: `idle=idle`, `running-right=walk`, `running-left=walk` with renderer flip, `waving=click`, `jumping=idle_birthday_up`, `failed=hit`, `waiting=sleep`, `running=idle_birthday_loop`, `review=click`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; detail atlas scale is `4`.
- Files changed: added the scoped Cristallo normal room Spine profile, rebuilt `pets/9Pets-Cristallo`, `docs/assets/spritesheets/9Pets-Cristallo.webp`, `docs/assets/detail-spritesheets/9Pets-Cristallo.webp`, `docs/assets/previews/9Pets-Cristallo.png`, `docs/downloads/9Pets-Cristallo.zip`, and docs data for Cristallo.
- QA artifacts: `C:\tmp\9pets-cristallo-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Cristallo Cute / 9Pets-Cute-Cristallo
- Source audit: local official chibi Spine folder `roles/303101_qianboli`; alternate smaller folder `roles/303101_qianboli_s` also exists but was not used for this cute pass.
- Spine source: `303101_qianboli_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, and `unique`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; detail atlas scale is `4`.
- Files changed: added the scoped Cristallo cute Spine profile, built `pets/9Pets-Cute-Cristallo`, `docs/assets/spritesheets/9Pets-Cute-Cristallo.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Cristallo.webp`, `docs/assets/previews/9Pets-Cute-Cristallo.png`, `docs/assets/source/9Pets-Cute-Cristallo.png`, `docs/downloads/9Pets-Cute-Cristallo.zip`, and docs cute data for Cristallo.
- QA artifacts: `C:\tmp\9pets-cute-cristallo-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Darley Clatter Normal / 9Pets-Darley-Clatter
- Source audit: no matching normal Cubism `*.model3.json` was found under `live2d/roles` for asset id `305001`; the official Spine folder `roles/305001_dadadali` contains `305001_dadadali_room.skel`, `305001_dadadali_ui.skel`, and `305001_dadadali_fight.skel`.
- Normal source decision: selected `roles/305001_dadadali/305001_dadadali_room.skel` as the normal-equivalent animated source and did not mix in the fight/cute track.
- Spine source: `305001_dadadali_room.skel` with room motions used by the renderer profile.
- Motions selected: `idle=idle`, `running-right=walk`, `running-left=walk` with renderer flip, `waving=click`, `jumping=idle_birthday_up`, `failed=hit`, `waiting=sleep`, `running=idle_birthday_loop`, `review=click`.
- Capture settings: `1200x1200`, scale `2.2`, x `600`, y `900`; detail atlas scale is `4`.
- Files changed: added the scoped Darley Clatter normal room Spine profile, rebuilt `pets/9Pets-Darley-Clatter`, `docs/assets/spritesheets/9Pets-Darley-Clatter.webp`, `docs/assets/detail-spritesheets/9Pets-Darley-Clatter.webp`, `docs/assets/previews/9Pets-Darley-Clatter.png`, `docs/downloads/9Pets-Darley-Clatter.zip`, and docs data for Darley Clatter.
- QA artifacts: `C:\tmp\9pets-darley-clatter-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Darley Clatter Cute / 9Pets-Cute-Darley-Clatter
- Source audit: local official chibi/fight Spine folder `roles/305001_dadadali`; smaller alternate folder was not required for this cute pass.
- Spine source: `305001_dadadali_fight.skel`.
- Motions selected: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=posture`, `review=posture`.
- Rejected motions: an earlier `review=unique` candidate produced a detached flying object, and an earlier `running=skill2` candidate produced partial wheel/horse fragments; both were replaced with the cleaner `posture` motion.
- Capture settings: `1200x1200`, scale `4.0`, x `600`, y `900`; detail atlas scale is `4`.
- Files changed: added the scoped Darley Clatter cute Spine profile, built `pets/9Pets-Cute-Darley-Clatter`, `docs/assets/spritesheets/9Pets-Cute-Darley-Clatter.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Darley-Clatter.webp`, `docs/assets/previews/9Pets-Cute-Darley-Clatter.png`, `docs/assets/source/9Pets-Cute-Darley-Clatter.png`, `docs/downloads/9Pets-Cute-Darley-Clatter.zip`, and docs cute data for Darley Clatter.
- QA artifacts: `C:\tmp\9pets-cute-darley-clatter-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Desert Flannel Normal / 9Pets-Desert-Flannel
- Source audit: local normal Cubism folder `live2d/roles/v1a5_307501_shasirong` exists with `*.model3.json` and the expected motion set; local Spine folder `roles/v1a5_307501_shasirong` was reserved for Cute/fallback use.
- Live2D source: `live2d/roles/v1a5_307501_shasirong`.
- Motions selected by the renderer: `idle=b_idle.motion3.json`, `running-right=b_yaotou.motion3.json`, `running-left=b_yaotou.motion3.json`, `waving=b_jushou.motion3.json`, `jumping=b_diantou.motion3.json`, `failed=t_nanguo.motion3.json`, `waiting=b_tanshou.motion3.json`, `running=b_diantou.motion3.json`, `review=b_diantou.motion3.json`.
- Capture settings: default Live2D capture with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Desert-Flannel`, `docs/assets/spritesheets/9Pets-Desert-Flannel.webp`, `docs/assets/detail-spritesheets/9Pets-Desert-Flannel.webp`, `docs/assets/previews/9Pets-Desert-Flannel.png`, `docs/downloads/9Pets-Desert-Flannel.zip`, and docs data for Desert Flannel.
- QA artifacts: `C:\tmp\9pets-desert-flannel-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Desert Flannel Cute / 9Pets-Cute-Desert-Flannel
- Source audit: local official chibi/fight Spine folder `roles/v1a5_307501_shasirong`; alternate `_s` folder exists but was not used for this cute pass.
- Spine source: `307501_shasirong_fight.skel` with animations `born`, `change`, `change2`, `die`, `freeze`, `giddy`, `hit`, `idle`, `posture`, `skill1`, `skill2`, `sleep`, and `unique`.
- Motions selected by the renderer: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=skill1`, `failed=hit`, `waiting=sleep`, `running=skill2`, `review=unique`.
- Capture settings: default fight Spine capture with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Desert-Flannel`, `docs/assets/spritesheets/9Pets-Cute-Desert-Flannel.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Desert-Flannel.webp`, `docs/assets/previews/9Pets-Cute-Desert-Flannel.png`, `docs/assets/source/9Pets-Cute-Desert-Flannel.png`, `docs/downloads/9Pets-Cute-Desert-Flannel.zip`, and docs cute data for Desert Flannel.
- QA artifacts: `C:\tmp\9pets-cute-desert-flannel-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Diggers Normal / 9Pets-Diggers
- Source audit: local normal Cubism folder `live2d/roles/306401_wajueyishu` exists; local Spine folders `roles/306401_wajueyishu` and `roles/306401_wajueyishu_s` also exist.
- Live2D source: `live2d/roles/306401_wajueyishu`.
- Motions selected by the renderer: `idle=b_idle.motion3.json`, `running-right=b_yaotou.motion3.json`, `running-left=b_yaotou.motion3.json`, `waving=b_diantou.motion3.json`, `jumping=b_diantou.motion3.json`, `failed=t_nanguo.motion3.json`, `waiting=b_diantou.motion3.json`, `running=b_diantou.motion3.json`, `review=b_diantou.motion3.json`.
- Capture settings: default Live2D capture with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Diggers`, `docs/assets/spritesheets/9Pets-Diggers.webp`, `docs/assets/detail-spritesheets/9Pets-Diggers.webp`, `docs/assets/previews/9Pets-Diggers.png`, `docs/downloads/9Pets-Diggers.zip`, and docs data for Diggers.
- QA artifacts: `C:\tmp\9pets-diggers-final-contact.png`.
- Verification: `python tools\verify_build.py` passed after the Cute repair; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Diggers Cute / 9Pets-Cute-Diggers
- Source audit: local official chibi/fight Spine folder `roles/306401_wajueyishu`; alternate `_s` folder exists but was not used for this cute pass.
- Spine source: `306401_wajueyishu_fight.skel` with animations `born`, `die`, `freeze`, `giddy`, `hit`, `idle`, `innate`, `posture`, `skill1`, `skill2`, `sleep`, and `unique`.
- Rejected motion: the default `jumping=skill1` candidate produced an empty frame in row 4, column 1, so a Diggers-specific profile replaced `jumping` with `posture`.
- Motions selected by the accepted renderer pass: `idle=idle`, `running-right=posture`, `running-left=posture` with renderer flip, `waving=giddy`, `jumping=posture`, `failed=hit`, `waiting=sleep`, `running=posture`, `review=posture`.
- Capture settings: scoped fight Spine profile at `1200x1200`, scale `2.2`, x `600`, y `900`; detail atlas scale is `4`.
- Files changed: added the scoped Diggers cute Spine profile, built `pets/9Pets-Cute-Diggers`, `docs/assets/spritesheets/9Pets-Cute-Diggers.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Diggers.webp`, `docs/assets/previews/9Pets-Cute-Diggers.png`, `docs/assets/source/9Pets-Cute-Diggers.png`, `docs/downloads/9Pets-Cute-Diggers.zip`, and docs cute data for Diggers.
- QA artifacts: `C:\tmp\9pets-cute-diggers-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Dikke Normal / 9Pets-Dikke
- Source audit: local normal Cubism folder `live2d/roles/302201_pamiai` exists with 19 motion files; local Spine path is `roles/302201_pamiai`.
- Normal source: `live2d/roles/302201_pamiai`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_baoxiong.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Dikke`, `docs/assets/spritesheets/9Pets-Dikke.webp`, `docs/assets/detail-spritesheets/9Pets-Dikke.webp`, `docs/assets/previews/9Pets-Dikke.png`, `docs/downloads/9Pets-Dikke.zip`, and docs data for Dikke.
- QA artifacts: `C:\tmp\9pets-dikke-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Dikke Cute / 9Pets-Cute-Dikke
- Source audit: local official chibi/fight Spine source `roles/302201_pamiai/302201_pamiai_fight.skel`.
- Spine source: `302201_pamiai_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Dikke`, `docs/assets/spritesheets/9Pets-Cute-Dikke.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Dikke.webp`, `docs/assets/previews/9Pets-Cute-Dikke.png`, `docs/assets/source/9Pets-Cute-Dikke.png`, `docs/downloads/9Pets-Cute-Dikke.zip`, and docs cute data for Dikke.
- QA artifacts: `C:\tmp\9pets-cute-dikke-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Door Normal / 9Pets-Door
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/305901_door/305901_door_room.skel`; local Spine path is `roles/305901_door`.
- Normal source: `roles/305901_door/305901_door_room.skel`.
- Rejected motions: the first `jumping=idle_birthday_up` and `running=idle_birthday_loop` candidate produced detached diagonal line fragments, so a Door-specific profile replaced both with `walk`.
- Motions selected by the accepted renderer pass: `idle=idle`, `running-right=walk`, `running-left=walk`, `waving=click`, `jumping=walk`, `failed=hit`, `waiting=sleep`, `running=walk`, `review=click`.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Door`, `docs/assets/spritesheets/9Pets-Door.webp`, `docs/assets/detail-spritesheets/9Pets-Door.webp`, `docs/assets/previews/9Pets-Door.png`, `docs/downloads/9Pets-Door.zip`, and docs data for Door.
- QA artifacts: `C:\tmp\9pets-door-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Door Cute / 9Pets-Cute-Door
- Source audit: local official chibi/fight Spine source `roles/305901_door/305901_door_fight.skel`.
- Spine source: `305901_door_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Door`, `docs/assets/spritesheets/9Pets-Cute-Door.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Door.webp`, `docs/assets/previews/9Pets-Cute-Door.png`, `docs/assets/source/9Pets-Cute-Door.png`, `docs/downloads/9Pets-Cute-Door.zip`, and docs cute data for Door.
- QA artifacts: `C:\tmp\9pets-cute-door-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Druvis III Normal / 9Pets-Druvis-III
- Source audit: local normal Cubism folder `live2d/roles/300301_hujisheng` exists with 19 motion files; local Spine path is `roles/300301_hujisheng`.
- Normal source: `live2d/roles/300301_hujisheng`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yangtou.motion3.json, running-left=b_yangtou.motion3.json, waving=b_diantou.motion3.json, jumping=b_yangtou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Druvis-III`, `docs/assets/spritesheets/9Pets-Druvis-III.webp`, `docs/assets/detail-spritesheets/9Pets-Druvis-III.webp`, `docs/assets/previews/9Pets-Druvis-III.png`, `docs/downloads/9Pets-Druvis-III.zip`, and docs data for Druvis III.
- QA artifacts: `C:\tmp\9pets-druvis-iii-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Druvis III Cute / 9Pets-Cute-Druvis-III
- Source audit: local official chibi/fight Spine source `roles/300301_hujisheng/300301_hujisheng_fight.skel`.
- Spine source: `300301_hujisheng_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Druvis-III`, `docs/assets/spritesheets/9Pets-Cute-Druvis-III.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Druvis-III.webp`, `docs/assets/previews/9Pets-Cute-Druvis-III.png`, `docs/assets/source/9Pets-Cute-Druvis-III.png`, `docs/downloads/9Pets-Cute-Druvis-III.zip`, and docs cute data for Druvis III.
- QA artifacts: `C:\tmp\9pets-cute-druvis-iii-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Eagle Normal / 9Pets-Eagle
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/300601_xiaochunqueer/300601_xiaochunqueer_room.skel`; local Spine path is `roles/300601_xiaochunqueer`.
- Normal source: `roles/300601_xiaochunqueer/300601_xiaochunqueer_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Eagle`, `docs/assets/spritesheets/9Pets-Eagle.webp`, `docs/assets/detail-spritesheets/9Pets-Eagle.webp`, `docs/assets/previews/9Pets-Eagle.png`, `docs/downloads/9Pets-Eagle.zip`, and docs data for Eagle.
- QA artifacts: `C:\tmp\9pets-eagle-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Eagle Cute / 9Pets-Cute-Eagle
- Source audit: local official chibi/fight Spine source `roles/300601_xiaochunqueer/300601_xiaochunqueer_fight.skel`.
- Spine source: `300601_xiaochunqueer_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Eagle`, `docs/assets/spritesheets/9Pets-Cute-Eagle.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Eagle.webp`, `docs/assets/previews/9Pets-Cute-Eagle.png`, `docs/assets/source/9Pets-Cute-Eagle.png`, `docs/downloads/9Pets-Cute-Eagle.zip`, and docs cute data for Eagle.
- QA artifacts: `C:\tmp\9pets-cute-eagle-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Enigma Normal / 9Pets-Enigma
- Source audit: local normal Cubism folder `live2d/roles/v3a6_314301_yami` exists with 19 motion files, but the renderer produced a black silhouette despite a valid color texture; local room Spine path `roles/v3a6_314301_ym` was selected as the normal-equivalent repair source.
- Normal source: `roles/v3a6_314301_ym/314301_ym_room.skel`.
- Rejected source: `live2d/roles/v3a6_314301_yami` until the Cubism renderer/material issue is fixed.
- Motions selected by the accepted renderer pass: `idle=idle`, `running-right=walk`, `running-left=walk`, `waving=click`, `jumping=idle_birthday_up`, `failed=hit`, `waiting=sleep`, `running=idle_birthday_loop`, `review=click`.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Enigma`, `docs/assets/spritesheets/9Pets-Enigma.webp`, `docs/assets/detail-spritesheets/9Pets-Enigma.webp`, `docs/assets/previews/9Pets-Enigma.png`, `docs/downloads/9Pets-Enigma.zip`, and docs data for Enigma.
- QA artifacts: `C:\tmp\9pets-enigma-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine repair pass.

### 2026-06-12 - Enigma Cute / 9Pets-Cute-Enigma
- Source audit: local official chibi/fight Spine source `roles/v3a6_314301_ym/314301_ym_fight.skel`.
- Spine source: `314301_ym_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Enigma`, `docs/assets/spritesheets/9Pets-Cute-Enigma.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Enigma.webp`, `docs/assets/previews/9Pets-Cute-Enigma.png`, `docs/assets/source/9Pets-Cute-Enigma.png`, `docs/downloads/9Pets-Cute-Enigma.zip`, and docs cute data for Enigma.
- QA artifacts: `C:\tmp\9pets-cute-enigma-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Erick Normal / 9Pets-Erick
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/305801_ailike/305801_ailike_room.skel`; local Spine path is `roles/305801_ailike`.
- Normal source: `roles/305801_ailike/305801_ailike_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=walk, failed=hit, waiting=sleep, running=walk, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Erick`, `docs/assets/spritesheets/9Pets-Erick.webp`, `docs/assets/detail-spritesheets/9Pets-Erick.webp`, `docs/assets/previews/9Pets-Erick.png`, `docs/downloads/9Pets-Erick.zip`, and docs data for Erick.
- QA artifacts: `C:\tmp\9pets-erick-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Erick Cute / 9Pets-Cute-Erick
- Source audit: local official chibi/fight Spine source `roles/305801_ailike/305801_ailike_fight.skel`.
- Spine source: `305801_ailike_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Erick`, `docs/assets/spritesheets/9Pets-Cute-Erick.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Erick.webp`, `docs/assets/previews/9Pets-Cute-Erick.png`, `docs/assets/source/9Pets-Cute-Erick.png`, `docs/downloads/9Pets-Cute-Erick.zip`, and docs cute data for Erick.
- QA artifacts: `C:\tmp\9pets-cute-erick-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Eternity Normal / 9Pets-Eternity
- Source audit: local normal Cubism folder `live2d/roles/305101_wennifuleide` exists with 20 motion files; local Spine path is `roles/305101_wennifuleide`.
- Normal source: `live2d/roles/305101_wennifuleide`.
- Rejected capture: the first default Live2D camera pass clipped the head and upper body, so an Eternity-specific capture profile was added.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_baoxiong.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: `1800x1800`, scale `0.68`, x `1050`, y `600`; detail atlas scale is `4`.
- Files changed: rebuilt `pets/9Pets-Eternity`, `docs/assets/spritesheets/9Pets-Eternity.webp`, `docs/assets/detail-spritesheets/9Pets-Eternity.webp`, `docs/assets/previews/9Pets-Eternity.png`, `docs/downloads/9Pets-Eternity.zip`, and docs data for Eternity.
- QA artifacts: `C:\tmp\9pets-eternity-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Eternity Cute / 9Pets-Cute-Eternity
- Source audit: local official chibi/fight Spine source `roles/305101_wennifuleide/305101_wennifuleide_fight.skel`.
- Spine source: `305101_wennifuleide_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Eternity`, `docs/assets/spritesheets/9Pets-Cute-Eternity.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Eternity.webp`, `docs/assets/previews/9Pets-Cute-Eternity.png`, `docs/assets/source/9Pets-Cute-Eternity.png`, `docs/downloads/9Pets-Cute-Eternity.zip`, and docs cute data for Eternity.
- QA artifacts: `C:\tmp\9pets-cute-eternity-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Ezio Auditore Normal / 9Pets-Ezio-Auditore
- Source audit: local normal Cubism folder `live2d/roles/s01_312301_aja` exists with 20 motion files; local Spine path is `roles/s01_312301_ajaadtl`.
- Normal source: `live2d/roles/s01_312301_aja`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_diantou.motion3.json, failed=b_diantou.motion3.json, waiting=b_tanshou.motion3.json, running=t_renzhen.motion3.json, review=t_renzhen.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Ezio-Auditore`, `docs/assets/spritesheets/9Pets-Ezio-Auditore.webp`, `docs/assets/detail-spritesheets/9Pets-Ezio-Auditore.webp`, `docs/assets/previews/9Pets-Ezio-Auditore.png`, `docs/downloads/9Pets-Ezio-Auditore.zip`, and docs data for Ezio Auditore.
- QA artifacts: `C:\tmp\9pets-ezio-auditore-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Ezio Auditore Cute / 9Pets-Cute-Ezio-Auditore
- Source audit: local official chibi/fight Spine source `roles/s01_312301_ajaadtl/312301_ajaadtl_fight.skel`.
- Spine source: `312301_ajaadtl_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=posture, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Ezio-Auditore`, `docs/assets/spritesheets/9Pets-Cute-Ezio-Auditore.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Ezio-Auditore.webp`, `docs/assets/previews/9Pets-Cute-Ezio-Auditore.png`, `docs/assets/source/9Pets-Cute-Ezio-Auditore.png`, `docs/downloads/9Pets-Cute-Ezio-Auditore.zip`, and docs cute data for Ezio Auditore.
- QA artifacts: `C:\tmp\9pets-cute-ezio-auditore-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Ezra Theodore Normal / 9Pets-Ezra-Theodore
- Source audit: local normal Cubism folder `live2d/roles/v1a5_307401_aizila` exists with 26 motion files; local Spine path is `roles/v1a5_307401_aizila`.
- Normal source: `live2d/roles/v1a5_307401_aizila`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_jushou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=t_yihuo.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Ezra-Theodore`, `docs/assets/spritesheets/9Pets-Ezra-Theodore.webp`, `docs/assets/detail-spritesheets/9Pets-Ezra-Theodore.webp`, `docs/assets/previews/9Pets-Ezra-Theodore.png`, `docs/downloads/9Pets-Ezra-Theodore.zip`, and docs data for Ezra Theodore.
- QA artifacts: `C:\tmp\9pets-ezra-theodore-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Ezra Theodore Cute / 9Pets-Cute-Ezra-Theodore
- Source audit: local official chibi/fight Spine source `roles/v1a5_307401_aizila/307401_aizila_fight.skel`.
- Spine source: `307401_aizila_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Ezra-Theodore`, `docs/assets/spritesheets/9Pets-Cute-Ezra-Theodore.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Ezra-Theodore.webp`, `docs/assets/previews/9Pets-Cute-Ezra-Theodore.png`, `docs/assets/source/9Pets-Cute-Ezra-Theodore.png`, `docs/downloads/9Pets-Cute-Ezra-Theodore.zip`, and docs cute data for Ezra Theodore.
- QA artifacts: `C:\tmp\9pets-cute-ezra-theodore-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Fatutu Normal / 9Pets-Fatutu
- Source audit: local normal Cubism folder `live2d/roles/v2a4_310901_ttsz` exists with 32 motion files; local Spine path is `roles/v2a4_310901_ttsz`.
- Normal source: `live2d/roles/v2a4_310901_ttsz`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_baishou.motion3.json, running-left=b_baishou.motion3.json, waving=b_baishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=t_yihuo.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Fatutu`, `docs/assets/spritesheets/9Pets-Fatutu.webp`, `docs/assets/detail-spritesheets/9Pets-Fatutu.webp`, `docs/assets/previews/9Pets-Fatutu.png`, `docs/downloads/9Pets-Fatutu.zip`, and docs data for Fatutu.
- QA artifacts: `C:\tmp\9pets-fatutu-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Fatutu Cute / 9Pets-Cute-Fatutu
- Source audit: local official chibi/fight Spine source `roles/v2a4_310901_ttsz/310901_ttsz_fight.skel`.
- Spine source: `310901_ttsz_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Fatutu`, `docs/assets/spritesheets/9Pets-Cute-Fatutu.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Fatutu.webp`, `docs/assets/previews/9Pets-Cute-Fatutu.png`, `docs/assets/source/9Pets-Cute-Fatutu.png`, `docs/downloads/9Pets-Cute-Fatutu.zip`, and docs cute data for Fatutu.
- QA artifacts: `C:\tmp\9pets-cute-fatutu-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Flutterpage Normal / 9Pets-Flutterpage
- Source audit: local normal Cubism folder `live2d/roles/v2a3_310501_zxqe` exists with 21 motion files; local Spine path is `roles/v2a3_310501_zxqe`.
- Normal source: `live2d/roles/v2a3_310501_zxqe`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_beishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Flutterpage`, `docs/assets/spritesheets/9Pets-Flutterpage.webp`, `docs/assets/detail-spritesheets/9Pets-Flutterpage.webp`, `docs/assets/previews/9Pets-Flutterpage.png`, `docs/downloads/9Pets-Flutterpage.zip`, and docs data for Flutterpage.
- QA artifacts: `C:\tmp\9pets-flutterpage-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Flutterpage Cute / 9Pets-Cute-Flutterpage
- Source audit: local official chibi/fight Spine source `roles/v2a3_310501_zxqe/310501_zxqe_fight.skel`.
- Spine source: `310501_zxqe_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Flutterpage`, `docs/assets/spritesheets/9Pets-Cute-Flutterpage.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Flutterpage.webp`, `docs/assets/previews/9Pets-Cute-Flutterpage.png`, `docs/assets/source/9Pets-Cute-Flutterpage.png`, `docs/downloads/9Pets-Cute-Flutterpage.zip`, and docs cute data for Flutterpage.
- QA artifacts: `C:\tmp\9pets-cute-flutterpage-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Getian Normal / 9Pets-Getian
- Source audit: local normal Cubism folder `live2d/roles/v1a6_308401_gt` exists with 21 motion files; local Spine path is `roles/v1a6_308401_gt`.
- Normal source: `live2d/roles/v1a6_308401_gt`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_dakeshui.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=t_yihuo.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Getian`, `docs/assets/spritesheets/9Pets-Getian.webp`, `docs/assets/detail-spritesheets/9Pets-Getian.webp`, `docs/assets/previews/9Pets-Getian.png`, `docs/downloads/9Pets-Getian.zip`, and docs data for Getian.
- QA artifacts: `C:\tmp\9pets-getian-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Getian Cute / 9Pets-Cute-Getian
- Source audit: local official chibi/fight Spine source `roles/v1a6_308401_gt/308401_gt_fight.skel`.
- Spine source: `308401_gt_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=posture, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Getian`, `docs/assets/spritesheets/9Pets-Cute-Getian.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Getian.webp`, `docs/assets/previews/9Pets-Cute-Getian.png`, `docs/assets/source/9Pets-Cute-Getian.png`, `docs/downloads/9Pets-Cute-Getian.zip`, and docs cute data for Getian.
- QA artifacts: `C:\tmp\9pets-cute-getian-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Hissabeth Normal / 9Pets-Hissabeth
- Source audit: local normal Cubism folder `live2d/roles/v2a7_311601_lzl` exists with 21 motion files; local Spine path is `roles/v2a7_311601_lzl`.
- Normal source: `live2d/roles/v2a7_311601_lzl`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_taishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_shengqi.motion3.json, waiting=b_diantou.motion3.json, running=t_renzhen.motion3.json, review=t_renzhen.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Hissabeth`, `docs/assets/spritesheets/9Pets-Hissabeth.webp`, `docs/assets/detail-spritesheets/9Pets-Hissabeth.webp`, `docs/assets/previews/9Pets-Hissabeth.png`, `docs/downloads/9Pets-Hissabeth.zip`, and docs data for Hissabeth.
- QA artifacts: `C:\tmp\9pets-hissabeth-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Hissabeth Cute / 9Pets-Cute-Hissabeth
- Source audit: local official chibi/fight Spine source `roles/v2a7_311601_lzl/311601_lzl_fight.skel`.
- Spine source: `311601_lzl_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Hissabeth`, `docs/assets/spritesheets/9Pets-Cute-Hissabeth.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Hissabeth.webp`, `docs/assets/previews/9Pets-Cute-Hissabeth.png`, `docs/assets/source/9Pets-Cute-Hissabeth.png`, `docs/downloads/9Pets-Cute-Hissabeth.zip`, and docs cute data for Hissabeth.
- QA artifacts: `C:\tmp\9pets-cute-hissabeth-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Horropedia Normal / 9Pets-Horropedia
- Source audit: local normal Cubism folder `live2d/roles/306101_kongbutong` exists with 19 motion files; local Spine path is `roles/306101_kongbutong`.
- Normal source: `live2d/roles/306101_kongbutong`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_chiqiang.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Horropedia`, `docs/assets/spritesheets/9Pets-Horropedia.webp`, `docs/assets/detail-spritesheets/9Pets-Horropedia.webp`, `docs/assets/previews/9Pets-Horropedia.png`, `docs/downloads/9Pets-Horropedia.zip`, and docs data for Horropedia.
- QA artifacts: `C:\tmp\9pets-horropedia-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Horropedia Cute / 9Pets-Cute-Horropedia
- Source audit: local official chibi/fight Spine source `roles/306101_kongbutong/306101_kongbutong_fight.skel`.
- Spine source: `306101_kongbutong_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Horropedia`, `docs/assets/spritesheets/9Pets-Cute-Horropedia.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Horropedia.webp`, `docs/assets/previews/9Pets-Cute-Horropedia.png`, `docs/assets/source/9Pets-Cute-Horropedia.png`, `docs/downloads/9Pets-Cute-Horropedia.zip`, and docs cute data for Horropedia.
- QA artifacts: `C:\tmp\9pets-cute-horropedia-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Igor Normal / 9Pets-Igor
- Source audit: local normal Cubism folder `live2d/roles/v3a3_309201_yge` exists with 21 motion files; local Spine path is `roles/v3a3_309201_yge`.
- Normal source: `live2d/roles/v3a3_309201_yge`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_shengqi.motion3.json, waiting=b_tanshou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Igor`, `docs/assets/spritesheets/9Pets-Igor.webp`, `docs/assets/detail-spritesheets/9Pets-Igor.webp`, `docs/assets/previews/9Pets-Igor.png`, `docs/downloads/9Pets-Igor.zip`, and docs data for Igor.
- QA artifacts: `C:\tmp\9pets-igor-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Igor Cute / 9Pets-Cute-Igor
- Source audit: local official chibi/fight Spine source `roles/v3a3_309201_yge/309201_yge_fight.skel`.
- Spine source: `309201_yge_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Igor`, `docs/assets/spritesheets/9Pets-Cute-Igor.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Igor.webp`, `docs/assets/previews/9Pets-Cute-Igor.png`, `docs/assets/source/9Pets-Cute-Igor.png`, `docs/downloads/9Pets-Cute-Igor.zip`, and docs cute data for Igor.
- QA artifacts: `C:\tmp\9pets-cute-igor-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Isolde Normal / 9Pets-Isolde
- Source audit: local normal Cubism folder `live2d/roles/v1a7_308101_yisuoerde` exists with 25 motion files; local Spine path is `roles/v1a7_308101_ysed`.
- Normal source: `live2d/roles/v1a7_308101_yisuoerde`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaoqing.motion3.json, running-left=b_yaoqing.motion3.json, waving=b_yaoqing.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Isolde`, `docs/assets/spritesheets/9Pets-Isolde.webp`, `docs/assets/detail-spritesheets/9Pets-Isolde.webp`, `docs/assets/previews/9Pets-Isolde.png`, `docs/downloads/9Pets-Isolde.zip`, and docs data for Isolde.
- QA artifacts: `C:\tmp\9pets-isolde-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Isolde Cute / 9Pets-Cute-Isolde
- Source audit: local official chibi/fight Spine source `roles/v1a7_308101_ysed/308101_ysed_fight.skel`.
- Spine source: `308101_ysed_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Isolde`, `docs/assets/spritesheets/9Pets-Cute-Isolde.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Isolde.webp`, `docs/assets/previews/9Pets-Cute-Isolde.png`, `docs/assets/source/9Pets-Cute-Isolde.png`, `docs/downloads/9Pets-Cute-Isolde.zip`, and docs cute data for Isolde.
- QA artifacts: `C:\tmp\9pets-cute-isolde-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - J Normal / 9Pets-J
- Source audit: local normal Cubism folder `live2d/roles/v2a0_309401_j` exists with 20 motion files; local Spine path is `roles/v2a0_309401_j`.
- Normal source: `live2d/roles/v2a0_309401_j`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_tanshou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-J`, `docs/assets/spritesheets/9Pets-J.webp`, `docs/assets/detail-spritesheets/9Pets-J.webp`, `docs/assets/previews/9Pets-J.png`, `docs/downloads/9Pets-J.zip`, and docs data for J.
- QA artifacts: `C:\tmp\9pets-j-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - J Cute / 9Pets-Cute-J
- Source audit: local official chibi/fight Spine source `roles/v2a0_309401_j/309401_j_fight.skel`.
- Spine source: `309401_j_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-J`, `docs/assets/spritesheets/9Pets-Cute-J.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-J.webp`, `docs/assets/previews/9Pets-Cute-J.png`, `docs/assets/source/9Pets-Cute-J.png`, `docs/downloads/9Pets-Cute-J.zip`, and docs cute data for J.
- QA artifacts: `C:\tmp\9pets-cute-j-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Jessica Normal / 9Pets-Jessica
- Source audit: local normal Cubism folder `live2d/roles/305601_jiexika` exists with 19 motion files; local Spine path is `roles/305601_jiexika`.
- Normal source: `live2d/roles/305601_jiexika`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_shenshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_waitou.motion3.json, running=b_moxiaba.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Jessica`, `docs/assets/spritesheets/9Pets-Jessica.webp`, `docs/assets/detail-spritesheets/9Pets-Jessica.webp`, `docs/assets/previews/9Pets-Jessica.png`, `docs/downloads/9Pets-Jessica.zip`, and docs data for Jessica.
- QA artifacts: `C:\tmp\9pets-jessica-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Jessica Cute / 9Pets-Cute-Jessica
- Source audit: local official chibi/fight Spine source `roles/305601_jiexika/305601_jiexika_fight.skel`.
- Spine source: `305601_jiexika_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Jessica`, `docs/assets/spritesheets/9Pets-Cute-Jessica.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Jessica.webp`, `docs/assets/previews/9Pets-Cute-Jessica.png`, `docs/assets/source/9Pets-Cute-Jessica.png`, `docs/downloads/9Pets-Cute-Jessica.zip`, and docs cute data for Jessica.
- QA artifacts: `C:\tmp\9pets-cute-jessica-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Jiu Niangzi Normal / 9Pets-Jiu-Niangzi
- Source audit: local normal Cubism folder `live2d/roles/v1a6_308301_quniang` exists with 23 motion files; local Spine path is `roles/v1a6_308301_qn`.
- Normal source: `live2d/roles/v1a6_308301_quniang`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_taishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=t_sikao.motion3.json, review=t_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Jiu-Niangzi`, `docs/assets/spritesheets/9Pets-Jiu-Niangzi.webp`, `docs/assets/detail-spritesheets/9Pets-Jiu-Niangzi.webp`, `docs/assets/previews/9Pets-Jiu-Niangzi.png`, `docs/downloads/9Pets-Jiu-Niangzi.zip`, and docs data for Jiu Niangzi.
- QA artifacts: `C:\tmp\9pets-jiu-niangzi-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Jiu Niangzi Cute / 9Pets-Cute-Jiu-Niangzi
- Source audit: local official chibi/fight Spine source `roles/v1a6_308301_qn/308301_qn_fight.skel`.
- Spine source: `308301_qn_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Jiu-Niangzi`, `docs/assets/spritesheets/9Pets-Cute-Jiu-Niangzi.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Jiu-Niangzi.webp`, `docs/assets/previews/9Pets-Cute-Jiu-Niangzi.png`, `docs/assets/source/9Pets-Cute-Jiu-Niangzi.png`, `docs/downloads/9Pets-Cute-Jiu-Niangzi.zip`, and docs cute data for Jiu Niangzi.
- QA artifacts: `C:\tmp\9pets-cute-jiu-niangzi-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - John Titor Normal / 9Pets-John-Titor
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/303601_yuehantituo/303601_yuehantituo_room.skel`; local Spine path is `roles/303601_yuehantituo`.
- Normal source: `roles/303601_yuehantituo/303601_yuehantituo_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-John-Titor`, `docs/assets/spritesheets/9Pets-John-Titor.webp`, `docs/assets/detail-spritesheets/9Pets-John-Titor.webp`, `docs/assets/previews/9Pets-John-Titor.png`, `docs/downloads/9Pets-John-Titor.zip`, and docs data for John Titor.
- QA artifacts: `C:\tmp\9pets-john-titor-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - John Titor Cute / 9Pets-Cute-John-Titor
- Source audit: local official chibi/fight Spine source `roles/303601_yuehantituo/303601_yuehantituo_fight.skel`.
- Spine source: `303601_yuehantituo_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-John-Titor`, `docs/assets/spritesheets/9Pets-Cute-John-Titor.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-John-Titor.webp`, `docs/assets/previews/9Pets-Cute-John-Titor.png`, `docs/assets/source/9Pets-Cute-John-Titor.png`, `docs/downloads/9Pets-Cute-John-Titor.zip`, and docs cute data for John Titor.
- QA artifacts: `C:\tmp\9pets-cute-john-titor-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Kaalaa Baunaa Normal / 9Pets-Kaalaa-Baunaa
- Source audit: local normal Cubism folder `live2d/roles/307001_jialabona` exists with 22 motion files; local Spine path is `roles/v1a3_307001_jialabona`.
- Normal source: `live2d/roles/307001_jialabona`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yangtou.motion3.json, running-left=b_yangtou.motion3.json, waving=b_jushou.motion3.json, jumping=b_yangtou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_sisuo.motion3.json, review=b_sisuo.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Kaalaa-Baunaa`, `docs/assets/spritesheets/9Pets-Kaalaa-Baunaa.webp`, `docs/assets/detail-spritesheets/9Pets-Kaalaa-Baunaa.webp`, `docs/assets/previews/9Pets-Kaalaa-Baunaa.png`, `docs/downloads/9Pets-Kaalaa-Baunaa.zip`, and docs data for Kaalaa Baunaa.
- QA artifacts: `C:\tmp\9pets-kaalaa-baunaa-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Kaalaa Baunaa Cute / 9Pets-Cute-Kaalaa-Baunaa
- Source audit: local official chibi/fight Spine source `roles/v1a3_307001_jialabona/307001_jialabona_fight.skel`.
- Spine source: `307001_jialabona_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Kaalaa-Baunaa`, `docs/assets/spritesheets/9Pets-Cute-Kaalaa-Baunaa.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Kaalaa-Baunaa.webp`, `docs/assets/previews/9Pets-Cute-Kaalaa-Baunaa.png`, `docs/assets/source/9Pets-Cute-Kaalaa-Baunaa.png`, `docs/downloads/9Pets-Cute-Kaalaa-Baunaa.zip`, and docs cute data for Kaalaa Baunaa.
- QA artifacts: `C:\tmp\9pets-cute-kaalaa-baunaa-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Kakania Normal / 9Pets-Kakania
- Source audit: local normal Cubism folder `live2d/roles/v1a9_308001_kakaniya` exists with 21 motion files; local Spine path is `roles/v1a9_308001_kkny`.
- Normal source: `live2d/roles/v1a9_308001_kakaniya`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_taishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=t_yansu.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Kakania`, `docs/assets/spritesheets/9Pets-Kakania.webp`, `docs/assets/detail-spritesheets/9Pets-Kakania.webp`, `docs/assets/previews/9Pets-Kakania.png`, `docs/downloads/9Pets-Kakania.zip`, and docs data for Kakania.
- QA artifacts: `C:\tmp\9pets-kakania-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Kakania Cute / 9Pets-Cute-Kakania
- Source audit: local official chibi/fight Spine source `roles/v1a9_308001_kkny/308001_kkny_fight.skel`.
- Spine source: `308001_kkny_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Kakania`, `docs/assets/spritesheets/9Pets-Cute-Kakania.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Kakania.webp`, `docs/assets/previews/9Pets-Cute-Kakania.png`, `docs/assets/source/9Pets-Cute-Kakania.png`, `docs/downloads/9Pets-Cute-Kakania.zip`, and docs cute data for Kakania.
- QA artifacts: `C:\tmp\9pets-cute-kakania-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Kanjira Normal / 9Pets-Kanjira
- Source audit: local normal Cubism folder `live2d/roles/307101_kanjila` exists with 24 motion files; local Spine path is `roles/v1a3_307101_kanjila`.
- Normal source: `live2d/roles/307101_kanjila`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_diantou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_sisuo.motion3.json, review=b_sisuo.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Kanjira`, `docs/assets/spritesheets/9Pets-Kanjira.webp`, `docs/assets/detail-spritesheets/9Pets-Kanjira.webp`, `docs/assets/previews/9Pets-Kanjira.png`, `docs/downloads/9Pets-Kanjira.zip`, and docs data for Kanjira.
- QA artifacts: `C:\tmp\9pets-kanjira-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Kanjira Cute / 9Pets-Cute-Kanjira
- Source audit: local official chibi/fight Spine source `roles/v1a3_307101_kanjila/307101_kanjila_fight.skel`.
- Spine source: `307101_kanjila_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Kanjira`, `docs/assets/spritesheets/9Pets-Cute-Kanjira.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Kanjira.webp`, `docs/assets/previews/9Pets-Cute-Kanjira.png`, `docs/assets/source/9Pets-Cute-Kanjira.png`, `docs/downloads/9Pets-Cute-Kanjira.zip`, and docs cute data for Kanjira.
- QA artifacts: `C:\tmp\9pets-cute-kanjira-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Kassandra Normal / 9Pets-Kassandra
- Source audit: local normal Cubism folder `live2d/roles/s01_312401_ksdl` exists with 20 motion files; local Spine path is `roles/s01_312401_ksdl`.
- Normal source: `live2d/roles/s01_312401_ksdl`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_shenshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_shengqi.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=t_yansu.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Kassandra`, `docs/assets/spritesheets/9Pets-Kassandra.webp`, `docs/assets/detail-spritesheets/9Pets-Kassandra.webp`, `docs/assets/previews/9Pets-Kassandra.png`, `docs/downloads/9Pets-Kassandra.zip`, and docs data for Kassandra.
- QA artifacts: `C:\tmp\9pets-kassandra-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Kassandra Cute / 9Pets-Cute-Kassandra
- Source audit: local official chibi/fight Spine source `roles/s01_312401_ksdl/312401_ksdl_fight.skel`.
- Spine source: `312401_ksdl_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Kassandra`, `docs/assets/spritesheets/9Pets-Cute-Kassandra.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Kassandra.webp`, `docs/assets/previews/9Pets-Cute-Kassandra.png`, `docs/assets/source/9Pets-Cute-Kassandra.png`, `docs/downloads/9Pets-Cute-Kassandra.zip`, and docs cute data for Kassandra.
- QA artifacts: `C:\tmp\9pets-cute-kassandra-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Kiperina Normal / 9Pets-Kiperina
- Source audit: local normal Cubism folder `live2d/roles/v2a7_311701_kphh` exists with 20 motion files; local Spine path is `roles/v2a7_311701_kphh`.
- Normal source: `live2d/roles/v2a7_311701_kphh`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_beishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=t_yihuo.motion3.json, running=t_renzhen.motion3.json, review=t_renzhen.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Kiperina`, `docs/assets/spritesheets/9Pets-Kiperina.webp`, `docs/assets/detail-spritesheets/9Pets-Kiperina.webp`, `docs/assets/previews/9Pets-Kiperina.png`, `docs/downloads/9Pets-Kiperina.zip`, and docs data for Kiperina.
- QA artifacts: `C:\tmp\9pets-kiperina-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Kiperina Cute / 9Pets-Cute-Kiperina
- Source audit: local official chibi/fight Spine source `roles/v2a7_311701_kphh/311701_kphh_fight.skel`.
- Spine source: `311701_kphh_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Kiperina`, `docs/assets/spritesheets/9Pets-Cute-Kiperina.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Kiperina.webp`, `docs/assets/previews/9Pets-Cute-Kiperina.png`, `docs/assets/source/9Pets-Cute-Kiperina.png`, `docs/downloads/9Pets-Cute-Kiperina.zip`, and docs cute data for Kiperina.
- QA artifacts: `C:\tmp\9pets-cute-kiperina-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - La Source Normal / 9Pets-La-Source
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/303001_lalaquan/303001_lalaquan_room.skel`; local Spine path is `roles/303001_lalaquan`.
- Normal source: `roles/303001_lalaquan/303001_lalaquan_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-La-Source`, `docs/assets/spritesheets/9Pets-La-Source.webp`, `docs/assets/detail-spritesheets/9Pets-La-Source.webp`, `docs/assets/previews/9Pets-La-Source.png`, `docs/downloads/9Pets-La-Source.zip`, and docs data for La Source.
- QA artifacts: `C:\tmp\9pets-la-source-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - La Source Cute / 9Pets-Cute-La-Source
- Source audit: local official chibi/fight Spine source `roles/303001_lalaquan/303001_lalaquan_fight.skel`.
- Spine source: `303001_lalaquan_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-La-Source`, `docs/assets/spritesheets/9Pets-Cute-La-Source.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-La-Source.webp`, `docs/assets/previews/9Pets-Cute-La-Source.png`, `docs/assets/source/9Pets-Cute-La-Source.png`, `docs/downloads/9Pets-Cute-La-Source.zip`, and docs cute data for La Source.
- QA artifacts: `C:\tmp\9pets-cute-la-source-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Leilani Normal / 9Pets-Leilani
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/303501_lilani/303501_lilani_room.skel`; local Spine path is `roles/303501_lilani`.
- Normal source: `roles/303501_lilani/303501_lilani_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Leilani`, `docs/assets/spritesheets/9Pets-Leilani.webp`, `docs/assets/detail-spritesheets/9Pets-Leilani.webp`, `docs/assets/previews/9Pets-Leilani.png`, `docs/downloads/9Pets-Leilani.zip`, and docs data for Leilani.
- QA artifacts: `C:\tmp\9pets-leilani-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Leilani Cute / 9Pets-Cute-Leilani
- Source audit: local official chibi/fight Spine source `roles/303501_lilani/303501_lilani_fight.skel`.
- Spine source: `303501_lilani_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Leilani`, `docs/assets/spritesheets/9Pets-Cute-Leilani.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Leilani.webp`, `docs/assets/previews/9Pets-Cute-Leilani.png`, `docs/assets/source/9Pets-Cute-Leilani.png`, `docs/downloads/9Pets-Cute-Leilani.zip`, and docs cute data for Leilani.
- QA artifacts: `C:\tmp\9pets-cute-leilani-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Liang Yue Normal / 9Pets-Liang-Yue
- Source audit: local normal Cubism folder `live2d/roles/v2a5_311001_liangyue` exists with 31 motion files; local Spine path is `roles/v2a5_311001_ly`.
- Normal source: `live2d/roles/v2a5_311001_liangyue`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_tanshou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Liang-Yue`, `docs/assets/spritesheets/9Pets-Liang-Yue.webp`, `docs/assets/detail-spritesheets/9Pets-Liang-Yue.webp`, `docs/assets/previews/9Pets-Liang-Yue.png`, `docs/downloads/9Pets-Liang-Yue.zip`, and docs data for Liang Yue.
- QA artifacts: `C:\tmp\9pets-liang-yue-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Liang Yue Cute / 9Pets-Cute-Liang-Yue
- Source audit: local official chibi/fight Spine source `roles/v2a5_311001_ly/311001_ly_fight.skel`.
- Spine source: `311001_ly_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Liang-Yue`, `docs/assets/spritesheets/9Pets-Cute-Liang-Yue.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Liang-Yue.webp`, `docs/assets/previews/9Pets-Cute-Liang-Yue.png`, `docs/assets/source/9Pets-Cute-Liang-Yue.png`, `docs/downloads/9Pets-Cute-Liang-Yue.zip`, and docs cute data for Liang Yue.
- QA artifacts: `C:\tmp\9pets-cute-liang-yue-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Lilya Normal / 9Pets-Lilya
- Source audit: local normal Cubism folder `live2d/roles/300401_hongnujian` exists with 25 motion files; local Spine path is `roles/300401_hongnujian`.
- Normal source: `live2d/roles/300401_hongnujian`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yangtou.motion3.json, running-left=b_yangtou.motion3.json, waving=b_shenshou.motion3.json, jumping=b_yangtou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Lilya`, `docs/assets/spritesheets/9Pets-Lilya.webp`, `docs/assets/detail-spritesheets/9Pets-Lilya.webp`, `docs/assets/previews/9Pets-Lilya.png`, `docs/downloads/9Pets-Lilya.zip`, and docs data for Lilya.
- QA artifacts: `C:\tmp\9pets-lilya-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Lilya Cute / 9Pets-Cute-Lilya
- Source audit: local official chibi/fight Spine source `roles/300401_hongnujian/300401_hongnujian_fight.skel`.
- Spine source: `300401_hongnujian_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Lilya`, `docs/assets/spritesheets/9Pets-Cute-Lilya.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Lilya.webp`, `docs/assets/previews/9Pets-Cute-Lilya.png`, `docs/assets/source/9Pets-Cute-Lilya.png`, `docs/downloads/9Pets-Cute-Lilya.zip`, and docs cute data for Lilya.
- QA artifacts: `C:\tmp\9pets-cute-lilya-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Loggerhead Normal / 9Pets-Loggerhead
- Source audit: local normal Cubism folder `live2d/roles/v2a5_311201_knd` exists with 24 motion files; local Spine path is `roles/v2a5_311201_knd`.
- Normal source: `live2d/roles/v2a5_311201_knd`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_chijing.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=t_yihuo.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Loggerhead`, `docs/assets/spritesheets/9Pets-Loggerhead.webp`, `docs/assets/detail-spritesheets/9Pets-Loggerhead.webp`, `docs/assets/previews/9Pets-Loggerhead.png`, `docs/downloads/9Pets-Loggerhead.zip`, and docs data for Loggerhead.
- QA artifacts: `C:\tmp\9pets-loggerhead-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Loggerhead Cute / 9Pets-Cute-Loggerhead
- Source audit: local official chibi/fight Spine source `roles/v2a5_311201_knd/311201_knd_fight.skel`.
- Spine source: `311201_knd_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Loggerhead`, `docs/assets/spritesheets/9Pets-Cute-Loggerhead.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Loggerhead.webp`, `docs/assets/previews/9Pets-Cute-Loggerhead.png`, `docs/assets/source/9Pets-Cute-Loggerhead.png`, `docs/downloads/9Pets-Cute-Loggerhead.zip`, and docs cute data for Loggerhead.
- QA artifacts: `C:\tmp\9pets-cute-loggerhead-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Lopera Normal / 9Pets-Lopera
- Source audit: local normal Cubism folder `live2d/roles/v2a2_310201_luopeila` exists with 27 motion files; local Spine path is `roles/v2a2_310201_lopera`.
- Normal source: `live2d/roles/v2a2_310201_luopeila`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_tanshou.motion3.json, running=b_diantou.motion3.json, review=t_yansu.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Lopera`, `docs/assets/spritesheets/9Pets-Lopera.webp`, `docs/assets/detail-spritesheets/9Pets-Lopera.webp`, `docs/assets/previews/9Pets-Lopera.png`, `docs/downloads/9Pets-Lopera.zip`, and docs data for Lopera.
- QA artifacts: `C:\tmp\9pets-lopera-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Lopera Cute / 9Pets-Cute-Lopera
- Source audit: local official chibi/fight Spine source `roles/v2a2_310201_lopera/310201_lopera_fight.skel`.
- Spine source: `310201_lopera_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Lopera`, `docs/assets/spritesheets/9Pets-Cute-Lopera.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Lopera.webp`, `docs/assets/previews/9Pets-Cute-Lopera.png`, `docs/assets/source/9Pets-Cute-Lopera.png`, `docs/downloads/9Pets-Cute-Lopera.zip`, and docs cute data for Lopera.
- QA artifacts: `C:\tmp\9pets-cute-lopera-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Lorelei Normal / 9Pets-Lorelei
- Source audit: local normal Cubism folder `live2d/roles/v1a9_309101_luoleilai` exists with 21 motion files; local Spine path is `roles/v1a9_309101_lorelei`.
- Normal source: `live2d/roles/v1a9_309101_luoleilai`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_shenshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_qidao.motion3.json, running=t_renzhen.motion3.json, review=t_renzhen.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Lorelei`, `docs/assets/spritesheets/9Pets-Lorelei.webp`, `docs/assets/detail-spritesheets/9Pets-Lorelei.webp`, `docs/assets/previews/9Pets-Lorelei.png`, `docs/downloads/9Pets-Lorelei.zip`, and docs data for Lorelei.
- QA artifacts: `C:\tmp\9pets-lorelei-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Lorelei Cute / 9Pets-Cute-Lorelei
- Source audit: local official chibi/fight Spine source `roles/v1a9_309101_lorelei/309101_lorelei_fight.skel`.
- Spine source: `309101_lorelei_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Lorelei`, `docs/assets/spritesheets/9Pets-Cute-Lorelei.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Lorelei.webp`, `docs/assets/previews/9Pets-Cute-Lorelei.png`, `docs/assets/source/9Pets-Cute-Lorelei.png`, `docs/downloads/9Pets-Cute-Lorelei.zip`, and docs cute data for Lorelei.
- QA artifacts: `C:\tmp\9pets-cute-lorelei-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Lorentz Butterfly Normal / 9Pets-Lorentz-Butterfly
- Source audit: local normal Cubism folder `live2d/roles/v3a5_313901_llzhd` exists with 22 motion files; local Spine path is `roles/v3a5_313901_llzhd`.
- Normal source: `live2d/roles/v3a5_313901_llzhd`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_taishou.motion3.json, jumping=b_diantou.motion3.json, failed=b_diantou.motion3.json, waiting=b_diantou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Lorentz-Butterfly`, `docs/assets/spritesheets/9Pets-Lorentz-Butterfly.webp`, `docs/assets/detail-spritesheets/9Pets-Lorentz-Butterfly.webp`, `docs/assets/previews/9Pets-Lorentz-Butterfly.png`, `docs/downloads/9Pets-Lorentz-Butterfly.zip`, and docs data for Lorentz Butterfly.
- QA artifacts: `C:\tmp\9pets-lorentz-butterfly-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Lorentz Butterfly Cute / 9Pets-Cute-Lorentz-Butterfly
- Source audit: local official chibi/fight Spine source `roles/v3a5_313901_llzhd/313901_llzhd_fight.skel`.
- Spine source: `313901_llzhd_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Lorentz-Butterfly`, `docs/assets/spritesheets/9Pets-Cute-Lorentz-Butterfly.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Lorentz-Butterfly.webp`, `docs/assets/previews/9Pets-Cute-Lorentz-Butterfly.png`, `docs/assets/source/9Pets-Cute-Lorentz-Butterfly.png`, `docs/downloads/9Pets-Cute-Lorentz-Butterfly.zip`, and docs cute data for Lorentz Butterfly.
- QA artifacts: `C:\tmp\9pets-cute-lorentz-butterfly-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Lucy Normal / 9Pets-Lucy
- Source audit: local normal Cubism folder `live2d/roles/v1a9_308601_luxi` exists with 42 motion files; local Spine path is `roles/v1a9_308601_luxi`.
- Normal source: `live2d/roles/v1a9_308601_luxi`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaoqing.motion3.json, running-left=b_yaoqing.motion3.json, waving=b_taishou.motion3.json, jumping=b_diantou.motion3.json, failed=b_baoxiong.motion3.json, waiting=b_diantou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Lucy`, `docs/assets/spritesheets/9Pets-Lucy.webp`, `docs/assets/detail-spritesheets/9Pets-Lucy.webp`, `docs/assets/previews/9Pets-Lucy.png`, `docs/downloads/9Pets-Lucy.zip`, and docs data for Lucy.
- QA artifacts: `C:\tmp\9pets-lucy-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Lucy Cute / 9Pets-Cute-Lucy
- Source audit: local official chibi/fight Spine source `roles/v1a9_308601_luxi/308601_luxi_fight.skel`.
- Spine source: `308601_luxi_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Lucy`, `docs/assets/spritesheets/9Pets-Cute-Lucy.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Lucy.webp`, `docs/assets/previews/9Pets-Cute-Lucy.png`, `docs/assets/source/9Pets-Cute-Lucy.png`, `docs/downloads/9Pets-Cute-Lucy.zip`, and docs cute data for Lucy.
- QA artifacts: `C:\tmp\9pets-cute-lucy-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Marcus Normal / 9Pets-Marcus
- Source audit: local normal Cubism folder `live2d/roles/v1a7_306501_makusi` exists with 19 motion files; local Spine path is `roles/v1a7_306501_makusi`.
- Normal source: `live2d/roles/v1a7_306501_makusi`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_shenshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Marcus`, `docs/assets/spritesheets/9Pets-Marcus.webp`, `docs/assets/detail-spritesheets/9Pets-Marcus.webp`, `docs/assets/previews/9Pets-Marcus.png`, `docs/downloads/9Pets-Marcus.zip`, and docs data for Marcus.
- QA artifacts: `C:\tmp\9pets-marcus-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Marcus Cute / 9Pets-Cute-Marcus
- Source audit: local official chibi/fight Spine source `roles/v1a7_306501_makusi/306501_makusi_fight.skel`.
- Spine source: `306501_makusi_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Marcus`, `docs/assets/spritesheets/9Pets-Cute-Marcus.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Marcus.webp`, `docs/assets/previews/9Pets-Cute-Marcus.png`, `docs/assets/source/9Pets-Cute-Marcus.png`, `docs/downloads/9Pets-Cute-Marcus.zip`, and docs cute data for Marcus.
- QA artifacts: `C:\tmp\9pets-cute-marcus-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Marsha Normal / 9Pets-Marsha
- Source audit: local normal Cubism folder `live2d/roles/v3a3_312701_mes` exists with 25 motion files; local Spine path is `roles/v3a3_312701_mes`.
- Normal source: `live2d/roles/v3a3_312701_mes`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_diantou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=t_yansu.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Marsha`, `docs/assets/spritesheets/9Pets-Marsha.webp`, `docs/assets/detail-spritesheets/9Pets-Marsha.webp`, `docs/assets/previews/9Pets-Marsha.png`, `docs/downloads/9Pets-Marsha.zip`, and docs data for Marsha.
- QA artifacts: `C:\tmp\9pets-marsha-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Marsha Cute / 9Pets-Cute-Marsha
- Source audit: local official chibi/fight Spine source `roles/v3a3_312701_mes/312701_mes_fight.skel`.
- Spine source: `312701_mes_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Marsha`, `docs/assets/spritesheets/9Pets-Cute-Marsha.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Marsha.webp`, `docs/assets/previews/9Pets-Cute-Marsha.png`, `docs/assets/source/9Pets-Cute-Marsha.png`, `docs/downloads/9Pets-Cute-Marsha.zip`, and docs cute data for Marsha.
- QA artifacts: `C:\tmp\9pets-cute-marsha-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Matilda Normal / 9Pets-Matilda
- Source audit: local normal Cubism folder `live2d/roles/304101_madierda` exists with 32 motion files; local Spine path is `roles/304101_madierda`.
- Normal source: `live2d/roles/304101_madierda`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_baoxiong.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Matilda`, `docs/assets/spritesheets/9Pets-Matilda.webp`, `docs/assets/detail-spritesheets/9Pets-Matilda.webp`, `docs/assets/previews/9Pets-Matilda.png`, `docs/downloads/9Pets-Matilda.zip`, and docs data for Matilda.
- QA artifacts: `C:\tmp\9pets-matilda-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Matilda Cute / 9Pets-Cute-Matilda
- Source audit: local official chibi/fight Spine source `roles/304101_madierda/304101_madierda_fight.skel`.
- Spine source: `304101_madierda_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Matilda`, `docs/assets/spritesheets/9Pets-Cute-Matilda.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Matilda.webp`, `docs/assets/previews/9Pets-Cute-Matilda.png`, `docs/assets/source/9Pets-Cute-Matilda.png`, `docs/downloads/9Pets-Cute-Matilda.zip`, and docs cute data for Matilda.
- QA artifacts: `C:\tmp\9pets-cute-matilda-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Medicine Pocket Normal / 9Pets-Medicine-Pocket
- Source audit: local normal Cubism folder `live2d/roles/304701_tumaoshoudai` exists with 21 motion files; local Spine path is `roles/304701_tumaoshoudai`.
- Normal source: `live2d/roles/304701_tumaoshoudai`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_shengqi.motion3.json, waiting=b_tanshou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Medicine-Pocket`, `docs/assets/spritesheets/9Pets-Medicine-Pocket.webp`, `docs/assets/detail-spritesheets/9Pets-Medicine-Pocket.webp`, `docs/assets/previews/9Pets-Medicine-Pocket.png`, `docs/downloads/9Pets-Medicine-Pocket.zip`, and docs data for Medicine Pocket.
- QA artifacts: `C:\tmp\9pets-medicine-pocket-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Medicine Pocket Cute / 9Pets-Cute-Medicine-Pocket
- Source audit: local official chibi/fight Spine source `roles/304701_tumaoshoudai/304701_tumaoshoudai_fight.skel`.
- Spine source: `304701_tumaoshoudai_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Medicine-Pocket`, `docs/assets/spritesheets/9Pets-Cute-Medicine-Pocket.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Medicine-Pocket.webp`, `docs/assets/previews/9Pets-Cute-Medicine-Pocket.png`, `docs/assets/source/9Pets-Cute-Medicine-Pocket.png`, `docs/downloads/9Pets-Cute-Medicine-Pocket.zip`, and docs cute data for Medicine Pocket.
- QA artifacts: `C:\tmp\9pets-cute-medicine-pocket-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Melania Normal / 9Pets-Melania
- Source audit: local normal Cubism folder `live2d/roles/306201_meilanni` exists with 27 motion files; local Spine path is `roles/306201_meilanni`.
- Normal source: `live2d/roles/306201_meilanni`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_diantou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Melania`, `docs/assets/spritesheets/9Pets-Melania.webp`, `docs/assets/detail-spritesheets/9Pets-Melania.webp`, `docs/assets/previews/9Pets-Melania.png`, `docs/downloads/9Pets-Melania.zip`, and docs data for Melania.
- QA artifacts: `C:\tmp\9pets-melania-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Melania Cute / 9Pets-Cute-Melania
- Source audit: local official chibi/fight Spine source `roles/306201_meilanni/306201_meilanni_fight.skel`.
- Spine source: `306201_meilanni_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Melania`, `docs/assets/spritesheets/9Pets-Cute-Melania.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Melania.webp`, `docs/assets/previews/9Pets-Cute-Melania.png`, `docs/assets/source/9Pets-Cute-Melania.png`, `docs/downloads/9Pets-Cute-Melania.zip`, and docs cute data for Melania.
- QA artifacts: `C:\tmp\9pets-cute-melania-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Mercuria Normal / 9Pets-Mercuria
- Source audit: local normal Cubism folder `live2d/roles/v2a0_309501_huanzhuangshuixing` exists with 19 motion files; local Spine path is `roles/v2a0_309501_hzsx`.
- Normal source: `live2d/roles/v2a0_309501_huanzhuangshuixing`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_tanshou.motion3.json, running=b_sisuo.motion3.json, review=t_renzhen.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Mercuria`, `docs/assets/spritesheets/9Pets-Mercuria.webp`, `docs/assets/detail-spritesheets/9Pets-Mercuria.webp`, `docs/assets/previews/9Pets-Mercuria.png`, `docs/downloads/9Pets-Mercuria.zip`, and docs data for Mercuria.
- QA artifacts: `C:\tmp\9pets-mercuria-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Mercuria Cute / 9Pets-Cute-Mercuria
- Source audit: local official chibi/fight Spine source `roles/v2a0_309501_hzsx/309501_hzsx_fight.skel`.
- Spine source: `309501_hzsx_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Mercuria`, `docs/assets/spritesheets/9Pets-Cute-Mercuria.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Mercuria.webp`, `docs/assets/previews/9Pets-Cute-Mercuria.png`, `docs/assets/source/9Pets-Cute-Mercuria.png`, `docs/downloads/9Pets-Cute-Mercuria.zip`, and docs cute data for Mercuria.
- QA artifacts: `C:\tmp\9pets-cute-mercuria-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Mesmer Jr. Normal / 9Pets-Mesmer-Jr
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/305701_xiaomeisimeier/305701_xiaomeisimeier_room.skel`; local Spine path is `roles/305701_xiaomeisimeier`.
- Normal source: `roles/305701_xiaomeisimeier/305701_xiaomeisimeier_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Mesmer-Jr`, `docs/assets/spritesheets/9Pets-Mesmer-Jr.webp`, `docs/assets/detail-spritesheets/9Pets-Mesmer-Jr.webp`, `docs/assets/previews/9Pets-Mesmer-Jr.png`, `docs/downloads/9Pets-Mesmer-Jr.zip`, and docs data for Mesmer Jr..
- QA artifacts: `C:\tmp\9pets-mesmer-jr-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Mesmer Jr. Cute / 9Pets-Cute-Mesmer-Jr
- Source audit: local official chibi/fight Spine source `roles/305701_xiaomeisimeier/305701_xiaomeisimeier_fight.skel`.
- Spine source: `305701_xiaomeisimeier_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Mesmer-Jr`, `docs/assets/spritesheets/9Pets-Cute-Mesmer-Jr.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Mesmer-Jr.webp`, `docs/assets/previews/9Pets-Cute-Mesmer-Jr.png`, `docs/assets/source/9Pets-Cute-Mesmer-Jr.png`, `docs/downloads/9Pets-Cute-Mesmer-Jr.zip`, and docs cute data for Mesmer Jr..
- QA artifacts: `C:\tmp\9pets-cute-mesmer-jr-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Moldir Normal / 9Pets-Moldir
- Source audit: local normal Cubism folder `live2d/roles/v2a8_312101_mlde` exists with 25 motion files; local Spine path is `roles/v2a8_312101_mlde`.
- Normal source: `live2d/roles/v2a8_312101_mlde`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_dashou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Moldir`, `docs/assets/spritesheets/9Pets-Moldir.webp`, `docs/assets/detail-spritesheets/9Pets-Moldir.webp`, `docs/assets/previews/9Pets-Moldir.png`, `docs/downloads/9Pets-Moldir.zip`, and docs data for Moldir.
- QA artifacts: `C:\tmp\9pets-moldir-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Moldir Cute / 9Pets-Cute-Moldir
- Source audit: local official chibi/fight Spine source `roles/v2a8_312101_mlde/312101_mlde_fight.skel`.
- Spine source: `312101_mlde_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=posture, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Moldir`, `docs/assets/spritesheets/9Pets-Cute-Moldir.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Moldir.webp`, `docs/assets/previews/9Pets-Cute-Moldir.png`, `docs/assets/source/9Pets-Cute-Moldir.png`, `docs/downloads/9Pets-Cute-Moldir.zip`, and docs cute data for Moldir.
- QA artifacts: `C:\tmp\9pets-cute-moldir-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Mondlicht Normal / 9Pets-Mondlicht
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/302601_hongdoupeng/302601_hongdoupeng_room.skel`; local Spine path is `roles/302601_hongdoupeng`.
- Normal source: `roles/302601_hongdoupeng/302601_hongdoupeng_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Mondlicht`, `docs/assets/spritesheets/9Pets-Mondlicht.webp`, `docs/assets/detail-spritesheets/9Pets-Mondlicht.webp`, `docs/assets/previews/9Pets-Mondlicht.png`, `docs/downloads/9Pets-Mondlicht.zip`, and docs data for Mondlicht.
- QA artifacts: `C:\tmp\9pets-mondlicht-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Mondlicht Cute / 9Pets-Cute-Mondlicht
- Source audit: local official chibi/fight Spine source `roles/302601_hongdoupeng/302601_hongdoupeng_fight.skel`.
- Spine source: `302601_hongdoupeng_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Mondlicht`, `docs/assets/spritesheets/9Pets-Cute-Mondlicht.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Mondlicht.webp`, `docs/assets/previews/9Pets-Cute-Mondlicht.png`, `docs/assets/source/9Pets-Cute-Mondlicht.png`, `docs/downloads/9Pets-Cute-Mondlicht.zip`, and docs cute data for Mondlicht.
- QA artifacts: `C:\tmp\9pets-cute-mondlicht-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Mr. Duncan Normal / 9Pets-Mr-Duncan
- Source audit: local normal Cubism folder `live2d/roles/v2a2_310301_dengken` exists with 19 motion files; local Spine path is `roles/v2a2_310301_dkxs`.
- Normal source: `live2d/roles/v2a2_310301_dengken`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_chuixiongkou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_moxiaba.motion3.json, review=t_yansu.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Mr-Duncan`, `docs/assets/spritesheets/9Pets-Mr-Duncan.webp`, `docs/assets/detail-spritesheets/9Pets-Mr-Duncan.webp`, `docs/assets/previews/9Pets-Mr-Duncan.png`, `docs/downloads/9Pets-Mr-Duncan.zip`, and docs data for Mr. Duncan.
- QA artifacts: `C:\tmp\9pets-mr-duncan-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Mr. Duncan Cute / 9Pets-Cute-Mr-Duncan
- Source audit: local official chibi/fight Spine source `roles/v2a2_310301_dkxs/310301_dkxs_fight.skel`.
- Spine source: `310301_dkxs_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Mr-Duncan`, `docs/assets/spritesheets/9Pets-Cute-Mr-Duncan.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Mr-Duncan.webp`, `docs/assets/previews/9Pets-Cute-Mr-Duncan.png`, `docs/assets/source/9Pets-Cute-Mr-Duncan.png`, `docs/downloads/9Pets-Cute-Mr-Duncan.zip`, and docs cute data for Mr. Duncan.
- QA artifacts: `C:\tmp\9pets-cute-mr-duncan-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Ms. Moissan Normal / 9Pets-Ms-Moissan
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/304401_mosangnvshi/304401_mosangnvshi_room.skel`; local Spine path is `roles/304401_mosangnvshi`.
- Normal source: `roles/304401_mosangnvshi/304401_mosangnvshi_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Ms-Moissan`, `docs/assets/spritesheets/9Pets-Ms-Moissan.webp`, `docs/assets/detail-spritesheets/9Pets-Ms-Moissan.webp`, `docs/assets/previews/9Pets-Ms-Moissan.png`, `docs/downloads/9Pets-Ms-Moissan.zip`, and docs data for Ms. Moissan.
- QA artifacts: `C:\tmp\9pets-ms-moissan-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Ms. Moissan Cute / 9Pets-Cute-Ms-Moissan
- Source audit: local official chibi/fight Spine source `roles/304401_mosangnvshi/304401_mosangnvshi_fight.skel`.
- Spine source: `304401_mosangnvshi_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Ms-Moissan`, `docs/assets/spritesheets/9Pets-Cute-Ms-Moissan.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Ms-Moissan.webp`, `docs/assets/previews/9Pets-Cute-Ms-Moissan.png`, `docs/assets/source/9Pets-Cute-Ms-Moissan.png`, `docs/downloads/9Pets-Cute-Ms-Moissan.zip`, and docs cute data for Ms. Moissan.
- QA artifacts: `C:\tmp\9pets-cute-ms-moissan-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Ms. NewBabel Normal / 9Pets-Ms-NewBabel
- Source audit: local normal Cubism folder `live2d/roles/305201_xinbabieta` exists with 22 motion files; local Spine path is `roles/305201_xinbabieta`.
- Normal source: `live2d/roles/305201_xinbabieta`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_anfu.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Ms-NewBabel`, `docs/assets/spritesheets/9Pets-Ms-NewBabel.webp`, `docs/assets/detail-spritesheets/9Pets-Ms-NewBabel.webp`, `docs/assets/previews/9Pets-Ms-NewBabel.png`, `docs/downloads/9Pets-Ms-NewBabel.zip`, and docs data for Ms. NewBabel.
- QA artifacts: `C:\tmp\9pets-ms-newbabel-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Ms. NewBabel Cute / 9Pets-Cute-Ms-NewBabel
- Source audit: local official chibi/fight Spine source `roles/305201_xinbabieta/305201_xinbabieta_fight.skel`.
- Spine source: `305201_xinbabieta_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Ms-NewBabel`, `docs/assets/spritesheets/9Pets-Cute-Ms-NewBabel.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Ms-NewBabel.webp`, `docs/assets/previews/9Pets-Cute-Ms-NewBabel.png`, `docs/assets/source/9Pets-Cute-Ms-NewBabel.png`, `docs/downloads/9Pets-Cute-Ms-NewBabel.zip`, and docs cute data for Ms. NewBabel.
- QA artifacts: `C:\tmp\9pets-cute-ms-newbabel-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Ms. Radio Normal / 9Pets-Ms-Radio
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/302701_wuxiandianxiaojie/302701_wuxiandianxiaojie_room.skel`; local Spine path is `roles/302701_wuxiandianxiaojie`.
- Normal source: `roles/302701_wuxiandianxiaojie/302701_wuxiandianxiaojie_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=walk, failed=hit, waiting=sleep, running=walk, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Ms-Radio`, `docs/assets/spritesheets/9Pets-Ms-Radio.webp`, `docs/assets/detail-spritesheets/9Pets-Ms-Radio.webp`, `docs/assets/previews/9Pets-Ms-Radio.png`, `docs/downloads/9Pets-Ms-Radio.zip`, and docs data for Ms. Radio.
- QA artifacts: `C:\tmp\9pets-ms-radio-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Ms. Radio Cute / 9Pets-Cute-Ms-Radio
- Source audit: local official chibi/fight Spine source `roles/302701_wuxiandianxiaojie/302701_wuxiandianxiaojie_fight.skel`.
- Spine source: `302701_wuxiandianxiaojie_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Ms-Radio`, `docs/assets/spritesheets/9Pets-Cute-Ms-Radio.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Ms-Radio.webp`, `docs/assets/previews/9Pets-Cute-Ms-Radio.png`, `docs/assets/source/9Pets-Cute-Ms-Radio.png`, `docs/downloads/9Pets-Cute-Ms-Radio.zip`, and docs cute data for Ms. Radio.
- QA artifacts: `C:\tmp\9pets-cute-ms-radio-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Ms. Stranger Normal / 9Pets-Ms-Stranger
- Source audit: local normal Cubism folder `live2d/roles/v3a7_314701_wmz` exists with 24 motion files; local Spine path is `roles/v3a7_314701_wmz`.
- Normal source: `live2d/roles/v3a7_314701_wmz`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_taishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=t_yihuo.motion3.json, running=b_diantou.motion3.json, review=t_yansu.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Ms-Stranger`, `docs/assets/spritesheets/9Pets-Ms-Stranger.webp`, `docs/assets/detail-spritesheets/9Pets-Ms-Stranger.webp`, `docs/assets/previews/9Pets-Ms-Stranger.png`, `docs/downloads/9Pets-Ms-Stranger.zip`, and docs data for Ms. Stranger.
- QA artifacts: `C:\tmp\9pets-ms-stranger-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Ms. Stranger Cute / 9Pets-Cute-Ms-Stranger
- Source audit: local official chibi/fight Spine source `roles/v3a7_314701_wmz/314701_wmz_fight.skel`.
- Spine source: `314701_wmz_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Ms-Stranger`, `docs/assets/spritesheets/9Pets-Cute-Ms-Stranger.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Ms-Stranger.webp`, `docs/assets/previews/9Pets-Cute-Ms-Stranger.png`, `docs/assets/source/9Pets-Cute-Ms-Stranger.png`, `docs/downloads/9Pets-Cute-Ms-Stranger.zip`, and docs cute data for Ms. Stranger.
- QA artifacts: `C:\tmp\9pets-cute-ms-stranger-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Name Day Normal / 9Pets-Name-Day
- Source audit: local normal Cubism folder `live2d/roles/v2a7_311801_mmr` exists with 18 motion files; local Spine path is `roles/v2a7_311801_mmr`.
- Normal source: `live2d/roles/v2a7_311801_mmr`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_bishou.motion3.json, jumping=b_diantou.motion3.json, failed=b_bishou.motion3.json, waiting=t_yihuo.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Name-Day`, `docs/assets/spritesheets/9Pets-Name-Day.webp`, `docs/assets/detail-spritesheets/9Pets-Name-Day.webp`, `docs/assets/previews/9Pets-Name-Day.png`, `docs/downloads/9Pets-Name-Day.zip`, and docs data for Name Day.
- QA artifacts: `C:\tmp\9pets-name-day-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Name Day Cute / 9Pets-Cute-Name-Day
- Source audit: local official chibi/fight Spine source `roles/v2a7_311801_mmr/311801_mmr_fight.skel`.
- Spine source: `311801_mmr_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Name-Day`, `docs/assets/spritesheets/9Pets-Cute-Name-Day.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Name-Day.webp`, `docs/assets/previews/9Pets-Cute-Name-Day.png`, `docs/assets/source/9Pets-Cute-Name-Day.png`, `docs/downloads/9Pets-Cute-Name-Day.zip`, and docs cute data for Name Day.
- QA artifacts: `C:\tmp\9pets-cute-name-day-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Nautika Normal / 9Pets-Nautika
- Source audit: local normal Cubism folder `live2d/roles/v2a8_312001_ndk` exists with 29 motion files; local Spine path is `roles/v2a8_312001_ndk`.
- Normal source: `live2d/roles/v2a8_312001_ndk`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_baishou.motion3.json, running-left=b_baishou.motion3.json, waving=b_baishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=t_renzhen.motion3.json, review=t_renzhen.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Nautika`, `docs/assets/spritesheets/9Pets-Nautika.webp`, `docs/assets/detail-spritesheets/9Pets-Nautika.webp`, `docs/assets/previews/9Pets-Nautika.png`, `docs/downloads/9Pets-Nautika.zip`, and docs data for Nautika.
- QA artifacts: `C:\tmp\9pets-nautika-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Nautika Cute / 9Pets-Cute-Nautika
- Source audit: local official chibi/fight Spine source `roles/v2a8_312001_ndk/312001_ndk_fight.skel`.
- Spine source: `312001_ndk_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Nautika`, `docs/assets/spritesheets/9Pets-Cute-Nautika.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Nautika.webp`, `docs/assets/previews/9Pets-Cute-Nautika.png`, `docs/assets/source/9Pets-Cute-Nautika.png`, `docs/downloads/9Pets-Cute-Nautika.zip`, and docs cute data for Nautika.
- QA artifacts: `C:\tmp\9pets-cute-nautika-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Necrologist Normal / 9Pets-Necrologist
- Source audit: local normal Cubism folder `live2d/roles/303701_fugaoren` exists with 19 motion files; local Spine path is `roles/303701_fugaoren`.
- Normal source: `live2d/roles/303701_fugaoren`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_anfu.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_qidao.motion3.json, running=b_zhengli.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Necrologist`, `docs/assets/spritesheets/9Pets-Necrologist.webp`, `docs/assets/detail-spritesheets/9Pets-Necrologist.webp`, `docs/assets/previews/9Pets-Necrologist.png`, `docs/downloads/9Pets-Necrologist.zip`, and docs data for Necrologist.
- QA artifacts: `C:\tmp\9pets-necrologist-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Necrologist Cute / 9Pets-Cute-Necrologist
- Source audit: local official chibi/fight Spine source `roles/303701_fugaoren/303701_fugaoren_fight.skel`.
- Spine source: `303701_fugaoren_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Necrologist`, `docs/assets/spritesheets/9Pets-Cute-Necrologist.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Necrologist.webp`, `docs/assets/previews/9Pets-Cute-Necrologist.png`, `docs/assets/source/9Pets-Cute-Necrologist.png`, `docs/downloads/9Pets-Cute-Necrologist.zip`, and docs cute data for Necrologist.
- QA artifacts: `C:\tmp\9pets-cute-necrologist-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Nick Bottom Normal / 9Pets-Nick-Bottom
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/300501_nike/300501_nike_room.skel`; local Spine path is `roles/300501_nike`.
- Normal source: `roles/300501_nike/300501_nike_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=walk, failed=hit, waiting=sleep, running=walk, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Nick-Bottom`, `docs/assets/spritesheets/9Pets-Nick-Bottom.webp`, `docs/assets/detail-spritesheets/9Pets-Nick-Bottom.webp`, `docs/assets/previews/9Pets-Nick-Bottom.png`, `docs/downloads/9Pets-Nick-Bottom.zip`, and docs data for Nick Bottom.
- QA artifacts: `C:\tmp\9pets-nick-bottom-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Nick Bottom Cute / 9Pets-Cute-Nick-Bottom
- Source audit: local official chibi/fight Spine source `roles/300501_nike/300501_nike_fight.skel`.
- Spine source: `300501_nike_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Nick-Bottom`, `docs/assets/spritesheets/9Pets-Cute-Nick-Bottom.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Nick-Bottom.webp`, `docs/assets/previews/9Pets-Cute-Nick-Bottom.png`, `docs/assets/source/9Pets-Cute-Nick-Bottom.png`, `docs/downloads/9Pets-Cute-Nick-Bottom.zip`, and docs cute data for Nick Bottom.
- QA artifacts: `C:\tmp\9pets-cute-nick-bottom-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Noire Normal / 9Pets-Noire
- Source audit: local normal Cubism folder `live2d/roles/v2a5_311101_feilinshiduo` exists with 19 motion files; local Spine path is `roles/v2a5_311101_flsd`.
- Normal source: `live2d/roles/v2a5_311101_feilinshiduo`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_bietoufa.motion3.json, jumping=b_diantou.motion3.json, failed=b_bietoufa.motion3.json, waiting=b_diantou.motion3.json, running=t_renzhen.motion3.json, review=t_renzhen.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Noire`, `docs/assets/spritesheets/9Pets-Noire.webp`, `docs/assets/detail-spritesheets/9Pets-Noire.webp`, `docs/assets/previews/9Pets-Noire.png`, `docs/downloads/9Pets-Noire.zip`, and docs data for Noire.
- QA artifacts: `C:\tmp\9pets-noire-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Noire Cute / 9Pets-Cute-Noire
- Source audit: local official chibi/fight Spine source `roles/v2a5_311101_flsd/311101_flsd_fight.skel`.
- Spine source: `311101_flsd_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Noire`, `docs/assets/spritesheets/9Pets-Cute-Noire.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Noire.webp`, `docs/assets/previews/9Pets-Cute-Noire.png`, `docs/assets/source/9Pets-Cute-Noire.png`, `docs/downloads/9Pets-Cute-Noire.zip`, and docs cute data for Noire.
- QA artifacts: `C:\tmp\9pets-cute-noire-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Oliver Fog Normal / 9Pets-Oliver-Fog
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/301801_wuxingzhe/301801_wuxingzhe_room.skel`; local Spine path is `roles/301801_wuxingzhe`.
- Normal source: `roles/301801_wuxingzhe/301801_wuxingzhe_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Oliver-Fog`, `docs/assets/spritesheets/9Pets-Oliver-Fog.webp`, `docs/assets/detail-spritesheets/9Pets-Oliver-Fog.webp`, `docs/assets/previews/9Pets-Oliver-Fog.png`, `docs/downloads/9Pets-Oliver-Fog.zip`, and docs data for Oliver Fog.
- QA artifacts: `C:\tmp\9pets-oliver-fog-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Oliver Fog Cute / 9Pets-Cute-Oliver-Fog
- Source audit: local official chibi/fight Spine source `roles/301801_wuxingzhe/301801_wuxingzhe_fight.skel`.
- Spine source: `301801_wuxingzhe_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Oliver-Fog`, `docs/assets/spritesheets/9Pets-Cute-Oliver-Fog.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Oliver-Fog.webp`, `docs/assets/previews/9Pets-Cute-Oliver-Fog.png`, `docs/assets/source/9Pets-Cute-Oliver-Fog.png`, `docs/downloads/9Pets-Cute-Oliver-Fog.zip`, and docs cute data for Oliver Fog.
- QA artifacts: `C:\tmp\9pets-cute-oliver-fog-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - ONiON Normal / 9Pets-ONiON
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/305401_yangcongtou/305401_yangcongtou_room.skel`; local Spine path is `roles/305401_yangcongtou`.
- Normal source: `roles/305401_yangcongtou/305401_yangcongtou_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=walk, failed=hit, waiting=sleep, running=walk, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-ONiON`, `docs/assets/spritesheets/9Pets-ONiON.webp`, `docs/assets/detail-spritesheets/9Pets-ONiON.webp`, `docs/assets/previews/9Pets-ONiON.png`, `docs/downloads/9Pets-ONiON.zip`, and docs data for ONiON.
- QA artifacts: `C:\tmp\9pets-onion-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - ONiON Cute / 9Pets-Cute-ONiON
- Source audit: local official chibi/fight Spine source `roles/305401_yangcongtou/305401_yangcongtou_fight.skel`.
- Spine source: `305401_yangcongtou_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-ONiON`, `docs/assets/spritesheets/9Pets-Cute-ONiON.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-ONiON.webp`, `docs/assets/previews/9Pets-Cute-ONiON.png`, `docs/assets/source/9Pets-Cute-ONiON.png`, `docs/downloads/9Pets-Cute-ONiON.zip`, and docs cute data for ONiON.
- QA artifacts: `C:\tmp\9pets-cute-onion-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Paper Heron Normal / 9Pets-Paper-Heron
- Source audit: local normal Cubism folder `live2d/roles/v3a4_314101_lsj` exists with 34 motion files; local Spine path is `roles/v3a4_314101_lsj`.
- Normal source: `live2d/roles/v3a4_314101_lsj`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_tanshou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Paper-Heron`, `docs/assets/spritesheets/9Pets-Paper-Heron.webp`, `docs/assets/detail-spritesheets/9Pets-Paper-Heron.webp`, `docs/assets/previews/9Pets-Paper-Heron.png`, `docs/downloads/9Pets-Paper-Heron.zip`, and docs data for Paper Heron.
- QA artifacts: `C:\tmp\9pets-paper-heron-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Paper Heron Cute / 9Pets-Cute-Paper-Heron
- Source audit: local official chibi/fight Spine source `roles/v3a4_314101_lsj/314101_lsj_fight.skel`.
- Spine source: `314101_lsj_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Paper-Heron`, `docs/assets/spritesheets/9Pets-Cute-Paper-Heron.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Paper-Heron.webp`, `docs/assets/previews/9Pets-Cute-Paper-Heron.png`, `docs/assets/source/9Pets-Cute-Paper-Heron.png`, `docs/downloads/9Pets-Cute-Paper-Heron.zip`, and docs cute data for Paper Heron.
- QA artifacts: `C:\tmp\9pets-cute-paper-heron-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Pavia Normal / 9Pets-Pavia
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/301501_langqun/301501_langqun_room.skel`; local Spine path is `roles/301501_langqun`.
- Normal source: `roles/301501_langqun/301501_langqun_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Pavia`, `docs/assets/spritesheets/9Pets-Pavia.webp`, `docs/assets/detail-spritesheets/9Pets-Pavia.webp`, `docs/assets/previews/9Pets-Pavia.png`, `docs/downloads/9Pets-Pavia.zip`, and docs data for Pavia.
- QA artifacts: `C:\tmp\9pets-pavia-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Pavia Cute / 9Pets-Cute-Pavia
- Source audit: local official chibi/fight Spine source `roles/301501_langqun/301501_langqun_fight.skel`.
- Spine source: `301501_langqun_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Pavia`, `docs/assets/spritesheets/9Pets-Cute-Pavia.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Pavia.webp`, `docs/assets/previews/9Pets-Cute-Pavia.png`, `docs/assets/source/9Pets-Cute-Pavia.png`, `docs/downloads/9Pets-Cute-Pavia.zip`, and docs cute data for Pavia.
- QA artifacts: `C:\tmp\9pets-cute-pavia-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Pickles Normal / 9Pets-Pickles
- Source audit: local normal Cubism folder `live2d/roles/306301_pikelesi` exists with 54 motion files; local Spine path is `roles/306301_pikelesi`.
- Normal source: `live2d/roles/306301_pikelesi`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yangtou.motion3.json, running-left=b_yangtou.motion3.json, waving=b_bizi.motion3.json, jumping=b_yangtou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_waitou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Pickles`, `docs/assets/spritesheets/9Pets-Pickles.webp`, `docs/assets/detail-spritesheets/9Pets-Pickles.webp`, `docs/assets/previews/9Pets-Pickles.png`, `docs/downloads/9Pets-Pickles.zip`, and docs data for Pickles.
- QA artifacts: `C:\tmp\9pets-pickles-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Pickles Cute / 9Pets-Cute-Pickles
- Source audit: local official chibi/fight Spine source `roles/306301_pikelesi/306301_pikelesi_fight.skel`.
- Spine source: `306301_pikelesi_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Pickles`, `docs/assets/spritesheets/9Pets-Cute-Pickles.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Pickles.webp`, `docs/assets/previews/9Pets-Cute-Pickles.png`, `docs/assets/source/9Pets-Cute-Pickles.png`, `docs/downloads/9Pets-Cute-Pickles.zip`, and docs cute data for Pickles.
- QA artifacts: `C:\tmp\9pets-cute-pickles-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Pioneer Normal / 9Pets-Pioneer
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/v2a0_309601_xqz/309601_xqz_room.skel`; local Spine path is `roles/v2a0_309601_xqz`.
- Normal source: `roles/v2a0_309601_xqz/309601_xqz_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Pioneer`, `docs/assets/spritesheets/9Pets-Pioneer.webp`, `docs/assets/detail-spritesheets/9Pets-Pioneer.webp`, `docs/assets/previews/9Pets-Pioneer.png`, `docs/downloads/9Pets-Pioneer.zip`, and docs data for Pioneer.
- QA artifacts: `C:\tmp\9pets-pioneer-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Pioneer Cute / 9Pets-Cute-Pioneer
- Source audit: local official chibi/fight Spine source `roles/v2a0_309601_xqz/309601_xqz_fight.skel`.
- Spine source: `309601_xqz_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Pioneer`, `docs/assets/spritesheets/9Pets-Cute-Pioneer.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Pioneer.webp`, `docs/assets/previews/9Pets-Cute-Pioneer.png`, `docs/assets/source/9Pets-Cute-Pioneer.png`, `docs/downloads/9Pets-Cute-Pioneer.zip`, and docs cute data for Pioneer.
- QA artifacts: `C:\tmp\9pets-cute-pioneer-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Poltergeist Normal / 9Pets-Poltergeist
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/304601_chaonaogui/304601_chaonaogui_room.skel`; local Spine path is `roles/304601_chaonaogui`.
- Normal source: `roles/304601_chaonaogui/304601_chaonaogui_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Poltergeist`, `docs/assets/spritesheets/9Pets-Poltergeist.webp`, `docs/assets/detail-spritesheets/9Pets-Poltergeist.webp`, `docs/assets/previews/9Pets-Poltergeist.png`, `docs/downloads/9Pets-Poltergeist.zip`, and docs data for Poltergeist.
- QA artifacts: `C:\tmp\9pets-poltergeist-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Poltergeist Cute / 9Pets-Cute-Poltergeist
- Source audit: local official chibi/fight Spine source `roles/304601_chaonaogui/304601_chaonaogui_fight.skel`.
- Spine source: `304601_chaonaogui_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=posture, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Poltergeist`, `docs/assets/spritesheets/9Pets-Cute-Poltergeist.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Poltergeist.webp`, `docs/assets/previews/9Pets-Cute-Poltergeist.png`, `docs/assets/source/9Pets-Cute-Poltergeist.png`, `docs/downloads/9Pets-Cute-Poltergeist.zip`, and docs cute data for Poltergeist.
- QA artifacts: `C:\tmp\9pets-cute-poltergeist-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Rabies Normal / 9Pets-Rabies
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/304201_aichong/304201_aichong_room.skel`; local Spine path is `roles/304201_aichong`.
- Normal source: `roles/304201_aichong/304201_aichong_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Rabies`, `docs/assets/spritesheets/9Pets-Rabies.webp`, `docs/assets/detail-spritesheets/9Pets-Rabies.webp`, `docs/assets/previews/9Pets-Rabies.png`, `docs/downloads/9Pets-Rabies.zip`, and docs data for Rabies.
- QA artifacts: `C:\tmp\9pets-rabies-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Rabies Cute / 9Pets-Cute-Rabies
- Source audit: local official chibi/fight Spine source `roles/304201_aichong/304201_aichong_fight.skel`.
- Spine source: `304201_aichong_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Rabies`, `docs/assets/spritesheets/9Pets-Cute-Rabies.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Rabies.webp`, `docs/assets/previews/9Pets-Cute-Rabies.png`, `docs/assets/source/9Pets-Cute-Rabies.png`, `docs/downloads/9Pets-Cute-Rabies.zip`, and docs cute data for Rabies.
- QA artifacts: `C:\tmp\9pets-cute-rabies-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Ramona Normal / 9Pets-Ramona
- Source audit: local normal Cubism folder `live2d/roles/v3a5_314201_lmn` exists with 29 motion files; local Spine path is `roles/v3a5_314201_lmn`.
- Normal source: `live2d/roles/v3a5_314201_lmn`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_chayao1.motion3.json, jumping=b_diantou.motion3.json, failed=b_chayao1.motion3.json, waiting=t_yihuo.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Ramona`, `docs/assets/spritesheets/9Pets-Ramona.webp`, `docs/assets/detail-spritesheets/9Pets-Ramona.webp`, `docs/assets/previews/9Pets-Ramona.png`, `docs/downloads/9Pets-Ramona.zip`, and docs data for Ramona.
- QA artifacts: `C:\tmp\9pets-ramona-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Ramona Cute / 9Pets-Cute-Ramona
- Source audit: local official chibi/fight Spine source `roles/v3a5_314201_lmn/314201_lmn_fight.skel`.
- Spine source: `314201_lmn_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Ramona`, `docs/assets/spritesheets/9Pets-Cute-Ramona.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Ramona.webp`, `docs/assets/previews/9Pets-Cute-Ramona.png`, `docs/assets/source/9Pets-Cute-Ramona.png`, `docs/downloads/9Pets-Cute-Ramona.zip`, and docs cute data for Ramona.
- QA artifacts: `C:\tmp\9pets-cute-ramona-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Recoleta Normal / 9Pets-Recoleta
- Source audit: local normal Cubism folder `live2d/roles/v2a6_311401_xgj` exists with 23 motion files; local Spine path is `roles/v2a6_311401_xgj`.
- Normal source: `live2d/roles/v2a6_311401_xgj`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_shenshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Recoleta`, `docs/assets/spritesheets/9Pets-Recoleta.webp`, `docs/assets/detail-spritesheets/9Pets-Recoleta.webp`, `docs/assets/previews/9Pets-Recoleta.png`, `docs/downloads/9Pets-Recoleta.zip`, and docs data for Recoleta.
- QA artifacts: `C:\tmp\9pets-recoleta-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Recoleta Cute / 9Pets-Cute-Recoleta
- Source audit: local official chibi/fight Spine source `roles/v2a6_311401_xgj/311401_xgj_fight.skel`.
- Spine source: `311401_xgj_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Recoleta`, `docs/assets/spritesheets/9Pets-Cute-Recoleta.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Recoleta.webp`, `docs/assets/previews/9Pets-Cute-Recoleta.png`, `docs/assets/source/9Pets-Cute-Recoleta.png`, `docs/downloads/9Pets-Cute-Recoleta.zip`, and docs cute data for Recoleta.
- QA artifacts: `C:\tmp\9pets-cute-recoleta-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Reed Normal / 9Pets-Reed
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/v3a4_313801_lcj/313801_lcj_room.skel`; local Spine path is `roles/v3a4_313801_lcj`.
- Normal source: `roles/v3a4_313801_lcj/313801_lcj_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Reed`, `docs/assets/spritesheets/9Pets-Reed.webp`, `docs/assets/detail-spritesheets/9Pets-Reed.webp`, `docs/assets/previews/9Pets-Reed.png`, `docs/downloads/9Pets-Reed.zip`, and docs data for Reed.
- QA artifacts: `C:\tmp\9pets-reed-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Reed Cute / 9Pets-Cute-Reed
- Source audit: local official chibi/fight Spine source `roles/v3a4_313801_lcj/313801_lcj_fight.skel`.
- Spine source: `313801_lcj_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Reed`, `docs/assets/spritesheets/9Pets-Cute-Reed.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Reed.webp`, `docs/assets/previews/9Pets-Cute-Reed.png`, `docs/assets/source/9Pets-Cute-Reed.png`, `docs/downloads/9Pets-Cute-Reed.zip`, and docs cute data for Reed.
- QA artifacts: `C:\tmp\9pets-cute-reed-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Regulus Normal / 9Pets-Regulus
- Source audit: local normal Cubism folder `live2d/roles/v1a9_302504_xingti` exists with 31 motion files; local Spine path is `roles/v1a9_302504_xt`.
- Normal source: `live2d/roles/v1a9_302504_xingti`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_ruchang.motion3.json, running-left=b_ruchang.motion3.json, waving=b_shenshou.motion3.json, jumping=b_ruchang.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Regulus`, `docs/assets/spritesheets/9Pets-Regulus.webp`, `docs/assets/detail-spritesheets/9Pets-Regulus.webp`, `docs/assets/previews/9Pets-Regulus.png`, `docs/downloads/9Pets-Regulus.zip`, and docs data for Regulus.
- QA artifacts: `C:\tmp\9pets-regulus-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Regulus Cute / 9Pets-Cute-Regulus
- Source audit: local official chibi/fight Spine source ``.
- Spine source: ``.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Regulus`, `docs/assets/spritesheets/9Pets-Cute-Regulus.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Regulus.webp`, `docs/assets/previews/9Pets-Cute-Regulus.png`, `docs/assets/source/9Pets-Cute-Regulus.png`, `docs/downloads/9Pets-Cute-Regulus.zip`, and docs cute data for Regulus.
- QA artifacts: `C:\tmp\9pets-cute-regulus-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Rhiannon Normal / 9Pets-Rhiannon
- Source audit: local normal Cubism folder `live2d/roles/v3a7_314601_xran` exists with 33 motion files; local Spine path is `roles/v3a7_314601_xran`.
- Normal source: `live2d/roles/v3a7_314601_xran`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_chizhang.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=t_yihuo.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Rhiannon`, `docs/assets/spritesheets/9Pets-Rhiannon.webp`, `docs/assets/detail-spritesheets/9Pets-Rhiannon.webp`, `docs/assets/previews/9Pets-Rhiannon.png`, `docs/downloads/9Pets-Rhiannon.zip`, and docs data for Rhiannon.
- QA artifacts: `C:\tmp\9pets-rhiannon-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Rhiannon Cute / 9Pets-Cute-Rhiannon
- Source audit: local official chibi/fight Spine source `roles/v3a7_314601_xran/314601_xran_fight.skel`.
- Spine source: `314601_xran_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Rhiannon`, `docs/assets/spritesheets/9Pets-Cute-Rhiannon.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Rhiannon.webp`, `docs/assets/previews/9Pets-Cute-Rhiannon.png`, `docs/assets/source/9Pets-Cute-Rhiannon.png`, `docs/downloads/9Pets-Cute-Rhiannon.zip`, and docs cute data for Rhiannon.
- QA artifacts: `C:\tmp\9pets-cute-rhiannon-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Rubuska Normal / 9Pets-Rubuska
- Source audit: local normal Cubism folder `live2d/roles/v3a1_312501_ysm` exists with 33 motion files; local Spine path is `roles/v3a1_312501_ysm`.
- Normal source: `live2d/roles/v3a1_312501_ysm`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_taishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=t_renzhen.motion3.json, review=t_renzhen.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Rubuska`, `docs/assets/spritesheets/9Pets-Rubuska.webp`, `docs/assets/detail-spritesheets/9Pets-Rubuska.webp`, `docs/assets/previews/9Pets-Rubuska.png`, `docs/downloads/9Pets-Rubuska.zip`, and docs data for Rubuska.
- QA artifacts: `C:\tmp\9pets-rubuska-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Rubuska Cute / 9Pets-Cute-Rubuska
- Source audit: local official chibi/fight Spine source `roles/v3a1_312501_ysm/312501_ysm_fight.skel`.
- Spine source: `312501_ysm_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Rubuska`, `docs/assets/spritesheets/9Pets-Cute-Rubuska.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Rubuska.webp`, `docs/assets/previews/9Pets-Cute-Rubuska.png`, `docs/assets/source/9Pets-Cute-Rubuska.png`, `docs/downloads/9Pets-Cute-Rubuska.zip`, and docs cute data for Rubuska.
- QA artifacts: `C:\tmp\9pets-cute-rubuska-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Satsuki Normal / 9Pets-Satsuki
- Source audit: local normal Cubism folder `live2d/roles/303801_wuseyue` exists with 22 motion files; local Spine path is `roles/303801_wuseyue`.
- Normal source: `live2d/roles/303801_wuseyue`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_taishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=t_haoqi.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Satsuki`, `docs/assets/spritesheets/9Pets-Satsuki.webp`, `docs/assets/detail-spritesheets/9Pets-Satsuki.webp`, `docs/assets/previews/9Pets-Satsuki.png`, `docs/downloads/9Pets-Satsuki.zip`, and docs data for Satsuki.
- QA artifacts: `C:\tmp\9pets-satsuki-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Satsuki Cute / 9Pets-Cute-Satsuki
- Source audit: local official chibi/fight Spine source `roles/303801_wuseyue/303801_wuseyue_fight.skel`.
- Spine source: `303801_wuseyue_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Satsuki`, `docs/assets/spritesheets/9Pets-Cute-Satsuki.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Satsuki.webp`, `docs/assets/previews/9Pets-Cute-Satsuki.png`, `docs/assets/source/9Pets-Cute-Satsuki.png`, `docs/downloads/9Pets-Cute-Satsuki.zip`, and docs cute data for Satsuki.
- QA artifacts: `C:\tmp\9pets-cute-satsuki-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Semmelweis Normal / 9Pets-Semmelweis
- Source audit: local normal Cubism folder `live2d/roles/v1a9_308801_smews` exists with 23 motion files; local Spine path is `roles/v1a9_308801_smews`.
- Normal source: `live2d/roles/v1a9_308801_smews`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaoqing.motion3.json, running-left=b_yaoqing.motion3.json, waving=b_yaoqing.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Semmelweis`, `docs/assets/spritesheets/9Pets-Semmelweis.webp`, `docs/assets/detail-spritesheets/9Pets-Semmelweis.webp`, `docs/assets/previews/9Pets-Semmelweis.png`, `docs/downloads/9Pets-Semmelweis.zip`, and docs data for Semmelweis.
- QA artifacts: `C:\tmp\9pets-semmelweis-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Semmelweis Cute / 9Pets-Cute-Semmelweis
- Source audit: local official chibi/fight Spine source `roles/v1a9_308801_smews/308801_smews_fight.skel`.
- Spine source: `308801_smews_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Semmelweis`, `docs/assets/spritesheets/9Pets-Cute-Semmelweis.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Semmelweis.webp`, `docs/assets/previews/9Pets-Cute-Semmelweis.png`, `docs/assets/source/9Pets-Cute-Semmelweis.png`, `docs/downloads/9Pets-Cute-Semmelweis.zip`, and docs cute data for Semmelweis.
- QA artifacts: `C:\tmp\9pets-cute-semmelweis-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Sentinel Normal / 9Pets-Sentinel
- Source audit: local normal Cubism folder `live2d/roles/v3a0_312601_mlan` exists with 23 motion files; local Spine path is `roles/v3a0_312601_mlan`.
- Normal source: `live2d/roles/v3a0_312601_mlan`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_cidao.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Sentinel`, `docs/assets/spritesheets/9Pets-Sentinel.webp`, `docs/assets/detail-spritesheets/9Pets-Sentinel.webp`, `docs/assets/previews/9Pets-Sentinel.png`, `docs/downloads/9Pets-Sentinel.zip`, and docs data for Sentinel.
- QA artifacts: `C:\tmp\9pets-sentinel-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Sentinel Cute / 9Pets-Cute-Sentinel
- Source audit: local official chibi/fight Spine source `roles/v3a0_312601_mlan/312601_mlan_fight.skel`.
- Spine source: `312601_mlan_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Sentinel`, `docs/assets/spritesheets/9Pets-Cute-Sentinel.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Sentinel.webp`, `docs/assets/previews/9Pets-Cute-Sentinel.png`, `docs/assets/source/9Pets-Cute-Sentinel.png`, `docs/downloads/9Pets-Cute-Sentinel.zip`, and docs cute data for Sentinel.
- QA artifacts: `C:\tmp\9pets-cute-sentinel-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Shamane Normal / 9Pets-Shamane
- Source audit: local normal Cubism folder `live2d/roles/307201_zongmaoshali` exists with 19 motion files; local Spine path is `roles/v1a3_307201_zongmaoshali`.
- Normal source: `live2d/roles/307201_zongmaoshali`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_taishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_shengqi.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=t_yansu.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Shamane`, `docs/assets/spritesheets/9Pets-Shamane.webp`, `docs/assets/detail-spritesheets/9Pets-Shamane.webp`, `docs/assets/previews/9Pets-Shamane.png`, `docs/downloads/9Pets-Shamane.zip`, and docs data for Shamane.
- QA artifacts: `C:\tmp\9pets-shamane-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Shamane Cute / 9Pets-Cute-Shamane
- Source audit: local official chibi/fight Spine source `roles/v1a3_307201_zongmaoshali/307201_zongmaoshali_fight.skel`.
- Spine source: `307201_zongmaoshali_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Shamane`, `docs/assets/spritesheets/9Pets-Cute-Shamane.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Shamane.webp`, `docs/assets/previews/9Pets-Cute-Shamane.png`, `docs/assets/source/9Pets-Cute-Shamane.png`, `docs/downloads/9Pets-Cute-Shamane.zip`, and docs cute data for Shamane.
- QA artifacts: `C:\tmp\9pets-cute-shamane-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Silverwing Eagle Normal / 9Pets-Silverwing-Eagle
- Source audit: local normal Cubism folder `live2d/roles/v3a7_315401_spxcqe` exists with 19 motion files; local Spine path is `roles/v3a7_315401_yzxcqe`.
- Normal source: `live2d/roles/v3a7_315401_spxcqe`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_diantou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Silverwing-Eagle`, `docs/assets/spritesheets/9Pets-Silverwing-Eagle.webp`, `docs/assets/detail-spritesheets/9Pets-Silverwing-Eagle.webp`, `docs/assets/previews/9Pets-Silverwing-Eagle.png`, `docs/downloads/9Pets-Silverwing-Eagle.zip`, and docs data for Silverwing Eagle.
- QA artifacts: `C:\tmp\9pets-silverwing-eagle-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Silverwing Eagle Cute / 9Pets-Cute-Silverwing-Eagle
- Source audit: local official chibi/fight Spine source `roles/v3a7_315401_yzxcqe/315401_yzxcqe_fight.skel`.
- Spine source: `315401_yzxcqe_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Silverwing-Eagle`, `docs/assets/spritesheets/9Pets-Cute-Silverwing-Eagle.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Silverwing-Eagle.webp`, `docs/assets/previews/9Pets-Cute-Silverwing-Eagle.png`, `docs/assets/source/9Pets-Cute-Silverwing-Eagle.png`, `docs/downloads/9Pets-Cute-Silverwing-Eagle.zip`, and docs cute data for Silverwing Eagle.
- QA artifacts: `C:\tmp\9pets-cute-silverwing-eagle-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Sonetto Normal / 9Pets-Sonetto
- Source audit: local normal Cubism folder `live2d/roles/302301_shisihangshi` exists with 22 motion files; local Spine path is `roles/302301_shisihangshi`.
- Normal source: `live2d/roles/302301_shisihangshi`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yangtou.motion3.json, running-left=b_yangtou.motion3.json, waving=b_diantou.motion3.json, jumping=b_yangtou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_qidao.motion3.json, running=b_moxiaba.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Sonetto`, `docs/assets/spritesheets/9Pets-Sonetto.webp`, `docs/assets/detail-spritesheets/9Pets-Sonetto.webp`, `docs/assets/previews/9Pets-Sonetto.png`, `docs/downloads/9Pets-Sonetto.zip`, and docs data for Sonetto.
- QA artifacts: `C:\tmp\9pets-sonetto-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Sonetto Cute / 9Pets-Cute-Sonetto
- Source audit: local official chibi/fight Spine source `roles/302301_shisihangshi/302301_shisihangshi_fight.skel`.
- Spine source: `302301_shisihangshi_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Sonetto`, `docs/assets/spritesheets/9Pets-Cute-Sonetto.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Sonetto.webp`, `docs/assets/previews/9Pets-Cute-Sonetto.png`, `docs/assets/source/9Pets-Cute-Sonetto.png`, `docs/downloads/9Pets-Cute-Sonetto.zip`, and docs cute data for Sonetto.
- QA artifacts: `C:\tmp\9pets-cute-sonetto-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Sotheby Normal / 9Pets-Sotheby
- Source audit: local normal Cubism folder `live2d/roles/300902_sufubi` exists with 24 motion files; local Spine path is `roles/300902_sufubi`.
- Normal source: `live2d/roles/300902_sufubi`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_baoshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=t_haoqi.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Sotheby`, `docs/assets/spritesheets/9Pets-Sotheby.webp`, `docs/assets/detail-spritesheets/9Pets-Sotheby.webp`, `docs/assets/previews/9Pets-Sotheby.png`, `docs/downloads/9Pets-Sotheby.zip`, and docs data for Sotheby.
- QA artifacts: `C:\tmp\9pets-sotheby-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Sotheby Cute / 9Pets-Cute-Sotheby
- Source audit: local official chibi/fight Spine source ``.
- Spine source: ``.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Sotheby`, `docs/assets/spritesheets/9Pets-Cute-Sotheby.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Sotheby.webp`, `docs/assets/previews/9Pets-Cute-Sotheby.png`, `docs/assets/source/9Pets-Cute-Sotheby.png`, `docs/downloads/9Pets-Cute-Sotheby.zip`, and docs cute data for Sotheby.
- QA artifacts: `C:\tmp\9pets-cute-sotheby-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Spathodea Normal / 9Pets-Spathodea
- Source audit: local normal Cubism folder `live2d/roles/v1a5_307301_kerandian` exists with 23 motion files; local Spine path is `roles/v1a5_307301_kerandian`.
- Normal source: `live2d/roles/v1a5_307301_kerandian`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_cashi.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=t_yihuo.motion3.json, running=b_guancha.motion3.json, review=b_guancha.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Spathodea`, `docs/assets/spritesheets/9Pets-Spathodea.webp`, `docs/assets/detail-spritesheets/9Pets-Spathodea.webp`, `docs/assets/previews/9Pets-Spathodea.png`, `docs/downloads/9Pets-Spathodea.zip`, and docs data for Spathodea.
- QA artifacts: `C:\tmp\9pets-spathodea-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Spathodea Cute / 9Pets-Cute-Spathodea
- Source audit: local official chibi/fight Spine source `roles/v1a5_307301_kerandian/307301_kerandian_fight.skel`.
- Spine source: `307301_kerandian_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Spathodea`, `docs/assets/spritesheets/9Pets-Cute-Spathodea.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Spathodea.webp`, `docs/assets/previews/9Pets-Cute-Spathodea.png`, `docs/assets/source/9Pets-Cute-Spathodea.png`, `docs/downloads/9Pets-Cute-Spathodea.zip`, and docs cute data for Spathodea.
- QA artifacts: `C:\tmp\9pets-cute-spathodea-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Sputnik Normal / 9Pets-Sputnik
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/305501_siputenike/305501_siputenike_room.skel`; local Spine path is `roles/305501_siputenike`.
- Normal source: `roles/305501_siputenike/305501_siputenike_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Sputnik`, `docs/assets/spritesheets/9Pets-Sputnik.webp`, `docs/assets/detail-spritesheets/9Pets-Sputnik.webp`, `docs/assets/previews/9Pets-Sputnik.png`, `docs/downloads/9Pets-Sputnik.zip`, and docs data for Sputnik.
- QA artifacts: `C:\tmp\9pets-sputnik-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Sputnik Cute / 9Pets-Cute-Sputnik
- Source audit: local official chibi/fight Spine source `roles/305501_siputenike/305501_siputenike_fight.skel`.
- Spine source: `305501_siputenike_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Sputnik`, `docs/assets/spritesheets/9Pets-Cute-Sputnik.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Sputnik.webp`, `docs/assets/previews/9Pets-Cute-Sputnik.png`, `docs/assets/source/9Pets-Cute-Sputnik.png`, `docs/downloads/9Pets-Cute-Sputnik.zip`, and docs cute data for Sputnik.
- QA artifacts: `C:\tmp\9pets-cute-sputnik-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Sweetheart Normal / 9Pets-Sweetheart
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/301101_malilian/301101_malilian_room.skel`; local Spine path is `roles/301101_malilian`.
- Normal source: `roles/301101_malilian/301101_malilian_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Sweetheart`, `docs/assets/spritesheets/9Pets-Sweetheart.webp`, `docs/assets/detail-spritesheets/9Pets-Sweetheart.webp`, `docs/assets/previews/9Pets-Sweetheart.png`, `docs/downloads/9Pets-Sweetheart.zip`, and docs data for Sweetheart.
- QA artifacts: `C:\tmp\9pets-sweetheart-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Sweetheart Cute / 9Pets-Cute-Sweetheart
- Source audit: local official chibi/fight Spine source `roles/301101_malilian/301101_malilian_fight.skel`.
- Spine source: `301101_malilian_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Sweetheart`, `docs/assets/spritesheets/9Pets-Cute-Sweetheart.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Sweetheart.webp`, `docs/assets/previews/9Pets-Cute-Sweetheart.png`, `docs/assets/source/9Pets-Cute-Sweetheart.png`, `docs/downloads/9Pets-Cute-Sweetheart.zip`, and docs cute data for Sweetheart.
- QA artifacts: `C:\tmp\9pets-cute-sweetheart-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Tennant Normal / 9Pets-Tennant
- Source audit: local normal Cubism folder `live2d/roles/304301_tannante` exists with 17 motion files; local Spine path is `roles/304301_tannante`.
- Normal source: `live2d/roles/304301_tannante`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_shenshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Tennant`, `docs/assets/spritesheets/9Pets-Tennant.webp`, `docs/assets/detail-spritesheets/9Pets-Tennant.webp`, `docs/assets/previews/9Pets-Tennant.png`, `docs/downloads/9Pets-Tennant.zip`, and docs data for Tennant.
- QA artifacts: `C:\tmp\9pets-tennant-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Tennant Cute / 9Pets-Cute-Tennant
- Source audit: local official chibi/fight Spine source `roles/304301_tannante/304301_tannante_fight.skel`.
- Spine source: `304301_tannante_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=posture, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Tennant`, `docs/assets/spritesheets/9Pets-Cute-Tennant.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Tennant.webp`, `docs/assets/previews/9Pets-Cute-Tennant.png`, `docs/assets/source/9Pets-Cute-Tennant.png`, `docs/downloads/9Pets-Cute-Tennant.zip`, and docs cute data for Tennant.
- QA artifacts: `C:\tmp\9pets-cute-tennant-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - The Fool Normal / 9Pets-The-Fool
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/301201_nongchen/301201_nongchen_room.skel`; local Spine path is `roles/301201_nongchen`.
- Normal source: `roles/301201_nongchen/301201_nongchen_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-The-Fool`, `docs/assets/spritesheets/9Pets-The-Fool.webp`, `docs/assets/detail-spritesheets/9Pets-The-Fool.webp`, `docs/assets/previews/9Pets-The-Fool.png`, `docs/downloads/9Pets-The-Fool.zip`, and docs data for The Fool.
- QA artifacts: `C:\tmp\9pets-the-fool-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - The Fool Cute / 9Pets-Cute-The-Fool
- Source audit: local official chibi/fight Spine source `roles/301201_nongchen/301201_nongchen_fight.skel`.
- Spine source: `301201_nongchen_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-The-Fool`, `docs/assets/spritesheets/9Pets-Cute-The-Fool.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-The-Fool.webp`, `docs/assets/previews/9Pets-Cute-The-Fool.png`, `docs/assets/source/9Pets-Cute-The-Fool.png`, `docs/downloads/9Pets-Cute-The-Fool.zip`, and docs cute data for The Fool.
- QA artifacts: `C:\tmp\9pets-cute-the-fool-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Tooth Fairy Normal / 9Pets-Tooth-Fairy
- Source audit: local normal Cubism folder `live2d/roles/305301_yaxian` exists with 40 motion files; local Spine path is `roles/305301_yaxian`.
- Normal source: `live2d/roles/305301_yaxian`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_changge.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Tooth-Fairy`, `docs/assets/spritesheets/9Pets-Tooth-Fairy.webp`, `docs/assets/detail-spritesheets/9Pets-Tooth-Fairy.webp`, `docs/assets/previews/9Pets-Tooth-Fairy.png`, `docs/downloads/9Pets-Tooth-Fairy.zip`, and docs data for Tooth Fairy.
- QA artifacts: `C:\tmp\9pets-tooth-fairy-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Tooth Fairy Cute / 9Pets-Cute-Tooth-Fairy
- Source audit: local official chibi/fight Spine source `roles/305301_yaxian/305301_yaxian_fight.skel`.
- Spine source: `305301_yaxian_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Tooth-Fairy`, `docs/assets/spritesheets/9Pets-Cute-Tooth-Fairy.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Tooth-Fairy.webp`, `docs/assets/previews/9Pets-Cute-Tooth-Fairy.png`, `docs/assets/source/9Pets-Cute-Tooth-Fairy.png`, `docs/downloads/9Pets-Cute-Tooth-Fairy.zip`, and docs cute data for Tooth Fairy.
- QA artifacts: `C:\tmp\9pets-cute-tooth-fairy-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - TTT Normal / 9Pets-TTT
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/303301_ttt/303301_ttt_room.skel`; local Spine path is `roles/303301_ttt`.
- Normal source: `roles/303301_ttt/303301_ttt_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=idle, running-left=idle, waving=click, jumping=idle, failed=hit, waiting=sleep, running=idle, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-TTT`, `docs/assets/spritesheets/9Pets-TTT.webp`, `docs/assets/detail-spritesheets/9Pets-TTT.webp`, `docs/assets/previews/9Pets-TTT.png`, `docs/downloads/9Pets-TTT.zip`, and docs data for TTT.
- QA artifacts: `C:\tmp\9pets-ttt-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - TTT Cute / 9Pets-Cute-TTT
- Source audit: local official chibi/fight Spine source `roles/303301_ttt/303301_ttt_fight.skel`.
- Spine source: `303301_ttt_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-TTT`, `docs/assets/spritesheets/9Pets-Cute-TTT.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-TTT.webp`, `docs/assets/previews/9Pets-Cute-TTT.png`, `docs/assets/source/9Pets-Cute-TTT.png`, `docs/downloads/9Pets-Cute-TTT.zip`, and docs cute data for TTT.
- QA artifacts: `C:\tmp\9pets-cute-ttt-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Tuesday Normal / 9Pets-Tuesday
- Source audit: local normal Cubism folder `live2d/roles/v2a1_309801_lsp` exists with 20 motion files; local Spine path is `roles/v2a1_309801_lsp`.
- Normal source: `live2d/roles/v2a1_309801_lsp`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaoqing.motion3.json, running-left=b_yaoqing.motion3.json, waving=b_yaoqing.motion3.json, jumping=b_diantou.motion3.json, failed=b_daliang.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Tuesday`, `docs/assets/spritesheets/9Pets-Tuesday.webp`, `docs/assets/detail-spritesheets/9Pets-Tuesday.webp`, `docs/assets/previews/9Pets-Tuesday.png`, `docs/downloads/9Pets-Tuesday.zip`, and docs data for Tuesday.
- QA artifacts: `C:\tmp\9pets-tuesday-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Tuesday Cute / 9Pets-Cute-Tuesday
- Source audit: local official chibi/fight Spine source `roles/v2a1_309801_lsp/309801_lsp_fight.skel`.
- Spine source: `309801_lsp_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Tuesday`, `docs/assets/spritesheets/9Pets-Cute-Tuesday.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Tuesday.webp`, `docs/assets/previews/9Pets-Cute-Tuesday.png`, `docs/assets/source/9Pets-Cute-Tuesday.png`, `docs/downloads/9Pets-Cute-Tuesday.zip`, and docs cute data for Tuesday.
- QA artifacts: `C:\tmp\9pets-cute-tuesday-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Twins Sleep Normal / 9Pets-Twins-Sleep
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/304001_lisha&luyisi/304001_lisha&luyisi_room.skel`; local Spine path is `roles/304001_lisha&luyisi`.
- Normal source: `roles/304001_lisha&luyisi/304001_lisha&luyisi_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=walk, failed=hit, waiting=sleep, running=walk, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Twins-Sleep`, `docs/assets/spritesheets/9Pets-Twins-Sleep.webp`, `docs/assets/detail-spritesheets/9Pets-Twins-Sleep.webp`, `docs/assets/previews/9Pets-Twins-Sleep.png`, `docs/downloads/9Pets-Twins-Sleep.zip`, and docs data for Twins Sleep.
- QA artifacts: `C:\tmp\9pets-twins-sleep-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Twins Sleep Cute / 9Pets-Cute-Twins-Sleep
- Source audit: local official chibi/fight Spine source `roles/304001_lisha&luyisi/304001_lisha&luyisi_fight.skel`.
- Spine source: `304001_lisha&luyisi_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Twins-Sleep`, `docs/assets/spritesheets/9Pets-Cute-Twins-Sleep.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Twins-Sleep.webp`, `docs/assets/previews/9Pets-Cute-Twins-Sleep.png`, `docs/assets/source/9Pets-Cute-Twins-Sleep.png`, `docs/downloads/9Pets-Cute-Twins-Sleep.zip`, and docs cute data for Twins Sleep.
- QA artifacts: `C:\tmp\9pets-cute-twins-sleep-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Ulrich Normal / 9Pets-Ulrich
- Source audit: local normal Cubism folder `live2d/roles/v2a4_310701_welx` exists with 8 motion files; local Spine path is `roles/v2a8_310701_welx`.
- Normal source: `live2d/roles/v2a4_310701_welx`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_diantou.motion3.json, failed=b_baoxiong.motion3.json, waiting=b_tanshou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Ulrich`, `docs/assets/spritesheets/9Pets-Ulrich.webp`, `docs/assets/detail-spritesheets/9Pets-Ulrich.webp`, `docs/assets/previews/9Pets-Ulrich.png`, `docs/downloads/9Pets-Ulrich.zip`, and docs data for Ulrich.
- QA artifacts: `C:\tmp\9pets-ulrich-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Ulrich Cute / 9Pets-Cute-Ulrich
- Source audit: local official chibi/fight Spine source `roles/v2a8_310701_welx/310701_welx_fight.skel`.
- Spine source: `310701_welx_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Ulrich`, `docs/assets/spritesheets/9Pets-Cute-Ulrich.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Ulrich.webp`, `docs/assets/previews/9Pets-Cute-Ulrich.png`, `docs/assets/source/9Pets-Cute-Ulrich.png`, `docs/downloads/9Pets-Cute-Ulrich.zip`, and docs cute data for Ulrich.
- QA artifacts: `C:\tmp\9pets-cute-ulrich-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Ulu Normal / 9Pets-Ulu
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/v1a5_307601_hepingwulu/307601_hepingwulu_room.skel`; local Spine path is `roles/v1a5_307601_hepingwulu`.
- Normal source: `roles/v1a5_307601_hepingwulu/307601_hepingwulu_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=walk, failed=hit, waiting=sleep, running=walk, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Ulu`, `docs/assets/spritesheets/9Pets-Ulu.webp`, `docs/assets/detail-spritesheets/9Pets-Ulu.webp`, `docs/assets/previews/9Pets-Ulu.png`, `docs/downloads/9Pets-Ulu.zip`, and docs data for Ulu.
- QA artifacts: `C:\tmp\9pets-ulu-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Ulu Cute / 9Pets-Cute-Ulu
- Source audit: local official chibi/fight Spine source `roles/v1a5_307601_hepingwulu/307601_hepingwulu_fight.skel`.
- Spine source: `307601_hepingwulu_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Ulu`, `docs/assets/spritesheets/9Pets-Cute-Ulu.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Ulu.webp`, `docs/assets/previews/9Pets-Cute-Ulu.png`, `docs/assets/source/9Pets-Cute-Ulu.png`, `docs/downloads/9Pets-Cute-Ulu.zip`, and docs cute data for Ulu.
- QA artifacts: `C:\tmp\9pets-cute-ulu-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Vila Normal / 9Pets-Vila
- Source audit: local normal Cubism folder `live2d/roles/v1a8_308701_weila` exists with 20 motion files; local Spine path is `roles/v1a8_308701_weila`.
- Normal source: `live2d/roles/v1a8_308701_weila`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_taishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Vila`, `docs/assets/spritesheets/9Pets-Vila.webp`, `docs/assets/detail-spritesheets/9Pets-Vila.webp`, `docs/assets/previews/9Pets-Vila.png`, `docs/downloads/9Pets-Vila.zip`, and docs data for Vila.
- QA artifacts: `C:\tmp\9pets-vila-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Vila Cute / 9Pets-Cute-Vila
- Source audit: local official chibi/fight Spine source `roles/v1a8_308701_weila/308701_weila_fight.skel`.
- Spine source: `308701_weila_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Vila`, `docs/assets/spritesheets/9Pets-Cute-Vila.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Vila.webp`, `docs/assets/previews/9Pets-Cute-Vila.png`, `docs/assets/source/9Pets-Cute-Vila.png`, `docs/downloads/9Pets-Cute-Vila.zip`, and docs cute data for Vila.
- QA artifacts: `C:\tmp\9pets-cute-vila-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Voyager Normal / 9Pets-Voyager
- Source audit: local normal Cubism folder `live2d/roles/304801_yuanlv` exists with 67 motion files; local Spine path is `roles/304801_yuanlv`.
- Normal source: `live2d/roles/304801_yuanlv`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_beishou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=t_haoqi.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Voyager`, `docs/assets/spritesheets/9Pets-Voyager.webp`, `docs/assets/detail-spritesheets/9Pets-Voyager.webp`, `docs/assets/previews/9Pets-Voyager.png`, `docs/downloads/9Pets-Voyager.zip`, and docs data for Voyager.
- QA artifacts: `C:\tmp\9pets-voyager-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Voyager Cute / 9Pets-Cute-Voyager
- Source audit: local official chibi/fight Spine source `roles/304801_yuanlv/304801_yuanlv_fight.skel`.
- Spine source: `304801_yuanlv_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Voyager`, `docs/assets/spritesheets/9Pets-Cute-Voyager.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Voyager.webp`, `docs/assets/previews/9Pets-Cute-Voyager.png`, `docs/assets/source/9Pets-Cute-Voyager.png`, `docs/downloads/9Pets-Cute-Voyager.zip`, and docs cute data for Voyager.
- QA artifacts: `C:\tmp\9pets-cute-voyager-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - White Rum Normal / 9Pets-White-Rum
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/v2a2_310101_bailangmu/310101_bailangmu_room.skel`; local Spine path is `roles/v2a2_310101_bailangmu`.
- Normal source: `roles/v2a2_310101_bailangmu/310101_bailangmu_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=idle_birthday_up, failed=hit, waiting=sleep, running=idle_birthday_loop, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-White-Rum`, `docs/assets/spritesheets/9Pets-White-Rum.webp`, `docs/assets/detail-spritesheets/9Pets-White-Rum.webp`, `docs/assets/previews/9Pets-White-Rum.png`, `docs/downloads/9Pets-White-Rum.zip`, and docs data for White Rum.
- QA artifacts: `C:\tmp\9pets-white-rum-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - White Rum Cute / 9Pets-Cute-White-Rum
- Source audit: local official chibi/fight Spine source `roles/v2a2_310101_bailangmu/310101_bailangmu_fight.skel`.
- Spine source: `310101_bailangmu_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-White-Rum`, `docs/assets/spritesheets/9Pets-Cute-White-Rum.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-White-Rum.webp`, `docs/assets/previews/9Pets-Cute-White-Rum.png`, `docs/assets/source/9Pets-Cute-White-Rum.png`, `docs/downloads/9Pets-Cute-White-Rum.zip`, and docs cute data for White Rum.
- QA artifacts: `C:\tmp\9pets-cute-white-rum-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Willow Normal / 9Pets-Willow
- Source audit: local normal Cubism folder `live2d/roles/v2a3_310401_ddg` exists with 25 motion files; local Spine path is `roles/v2a3_310401_ddg`.
- Normal source: `live2d/roles/v2a3_310401_ddg`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_xingli.motion3.json, running-left=b_xingli.motion3.json, waving=b_baishou.motion3.json, jumping=b_xingli.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Willow`, `docs/assets/spritesheets/9Pets-Willow.webp`, `docs/assets/detail-spritesheets/9Pets-Willow.webp`, `docs/assets/previews/9Pets-Willow.png`, `docs/downloads/9Pets-Willow.zip`, and docs data for Willow.
- QA artifacts: `C:\tmp\9pets-willow-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Willow Cute / 9Pets-Cute-Willow
- Source audit: local official chibi/fight Spine source `roles/v2a3_310401_ddg/310401_ddg_fight.skel`.
- Spine source: `310401_ddg_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Willow`, `docs/assets/spritesheets/9Pets-Cute-Willow.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Willow.webp`, `docs/assets/previews/9Pets-Cute-Willow.png`, `docs/assets/source/9Pets-Cute-Willow.png`, `docs/downloads/9Pets-Cute-Willow.zip`, and docs cute data for Willow.
- QA artifacts: `C:\tmp\9pets-cute-willow-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Windsong Normal / 9Pets-Windsong
- Source audit: local normal Cubism folder `live2d/roles/v1a8_307701_beifangshaoge` exists with 20 motion files; local Spine path is `roles/v1a8_307701_beifangshaoge`.
- Normal source: `live2d/roles/v1a8_307701_beifangshaoge`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_chizi.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_diantou.motion3.json, running=b_diantou.motion3.json, review=t_yansu.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Windsong`, `docs/assets/spritesheets/9Pets-Windsong.webp`, `docs/assets/detail-spritesheets/9Pets-Windsong.webp`, `docs/assets/previews/9Pets-Windsong.png`, `docs/downloads/9Pets-Windsong.zip`, and docs data for Windsong.
- QA artifacts: `C:\tmp\9pets-windsong-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Windsong Cute / 9Pets-Cute-Windsong
- Source audit: local official chibi/fight Spine source `roles/v1a8_307701_beifangshaoge/307701_beifangshaoge_fight.skel`.
- Spine source: `307701_beifangshaoge_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=posture, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Windsong`, `docs/assets/spritesheets/9Pets-Cute-Windsong.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Windsong.webp`, `docs/assets/previews/9Pets-Cute-Windsong.png`, `docs/assets/source/9Pets-Cute-Windsong.png`, `docs/downloads/9Pets-Cute-Windsong.zip`, and docs cute data for Windsong.
- QA artifacts: `C:\tmp\9pets-cute-windsong-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Zima Normal / 9Pets-Zima
- Source audit: no cached normal Cubism source was available; selected normal-equivalent room Spine `roles/301301_dong/301301_dong_room.skel`; local Spine path is `roles/301301_dong`.
- Normal source: `roles/301301_dong/301301_dong_room.skel`.
- Motions selected by the renderer: idle=idle, running-right=walk, running-left=walk, waving=click, jumping=walk, failed=hit, waiting=sleep, running=walk, review=click.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Zima`, `docs/assets/spritesheets/9Pets-Zima.webp`, `docs/assets/detail-spritesheets/9Pets-Zima.webp`, `docs/assets/previews/9Pets-Zima.png`, `docs/downloads/9Pets-Zima.zip`, and docs data for Zima.
- QA artifacts: `C:\tmp\9pets-zima-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal room Spine pass.

### 2026-06-12 - Zima Cute / 9Pets-Cute-Zima
- Source audit: local official chibi/fight Spine source `roles/301301_dong/301301_dong_fight.skel`.
- Spine source: `301301_dong_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Zima`, `docs/assets/spritesheets/9Pets-Cute-Zima.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Zima.webp`, `docs/assets/previews/9Pets-Cute-Zima.png`, `docs/assets/source/9Pets-Cute-Zima.png`, `docs/downloads/9Pets-Cute-Zima.zip`, and docs cute data for Zima.
- QA artifacts: `C:\tmp\9pets-cute-zima-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - X Normal / 9Pets-X
- Source audit: local normal Cubism folder `live2d/roles/301001_x` exists with 21 motion files; local Spine path is `roles/301001_x`.
- Normal source: `live2d/roles/301001_x`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_diantou.motion3.json, failed=t_nanguo.motion3.json, waiting=b_tanshou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-X`, `docs/assets/spritesheets/9Pets-X.webp`, `docs/assets/detail-spritesheets/9Pets-X.webp`, `docs/assets/previews/9Pets-X.png`, `docs/downloads/9Pets-X.zip`, and docs data for X.
- QA artifacts: `C:\tmp\9pets-x-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - X Cute / 9Pets-Cute-X
- Source audit: local official chibi/fight Spine source `roles/301001_x/301001_x_fight.skel`.
- Spine source: `301001_x_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-X`, `docs/assets/spritesheets/9Pets-Cute-X.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-X.webp`, `docs/assets/previews/9Pets-Cute-X.png`, `docs/assets/source/9Pets-Cute-X.png`, `docs/downloads/9Pets-Cute-X.zip`, and docs cute data for X.
- QA artifacts: `C:\tmp\9pets-cute-x-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Yenisei Normal / 9Pets-Yenisei
- Source audit: local normal Cubism folder `live2d/roles/v1a6_308201_xiaoyenisai` exists with 21 motion files; local Spine path is `roles/v1a6_308201_xyns`.
- Normal source: `live2d/roles/v1a6_308201_xiaoyenisai`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yaotou.motion3.json, running-left=b_yaotou.motion3.json, waving=b_diantou.motion3.json, jumping=b_diantou.motion3.json, failed=b_diantou.motion3.json, waiting=b_diantou.motion3.json, running=b_sikao.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Yenisei`, `docs/assets/spritesheets/9Pets-Yenisei.webp`, `docs/assets/detail-spritesheets/9Pets-Yenisei.webp`, `docs/assets/previews/9Pets-Yenisei.png`, `docs/downloads/9Pets-Yenisei.zip`, and docs data for Yenisei.
- QA artifacts: `C:\tmp\9pets-yenisei-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Yenisei Cute / 9Pets-Cute-Yenisei
- Source audit: local official chibi/fight Spine source `roles/v1a6_308201_xyns/308201_xyns_fight.skel`.
- Spine source: `308201_xyns_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Yenisei`, `docs/assets/spritesheets/9Pets-Cute-Yenisei.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Yenisei.webp`, `docs/assets/previews/9Pets-Cute-Yenisei.png`, `docs/assets/source/9Pets-Cute-Yenisei.png`, `docs/downloads/9Pets-Cute-Yenisei.zip`, and docs cute data for Yenisei.
- QA artifacts: `C:\tmp\9pets-cute-yenisei-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - A Knight Normal / 9Pets-A-Knight
- Source audit: local normal Cubism folder `live2d/roles/v3a1_300731_wxk` exists with 16 motion files; local Spine path is `roles/v3a1_300731_wxk`.
- Normal source: `live2d/roles/v3a1_300731_wxk`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_xingli.motion3.json, running-left=b_xingli.motion3.json, waving=b_shenshou.motion3.json, jumping=b_jujian.motion3.json, failed=b_shengqi.motion3.json, waiting=b_tanshou.motion3.json, running=b_cashi.motion3.json, review=b_sikao.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-A-Knight`, `docs/assets/spritesheets/9Pets-A-Knight.webp`, `docs/assets/detail-spritesheets/9Pets-A-Knight.webp`, `docs/assets/previews/9Pets-A-Knight.png`, `docs/downloads/9Pets-A-Knight.zip`, and docs data for A Knight.
- QA artifacts: `C:\tmp\9pets-a-knight-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - A Knight Cute / 9Pets-Cute-A-Knight
- Source audit: local official chibi/fight Spine source ``.
- Spine source: ``.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=posture, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-A-Knight`, `docs/assets/spritesheets/9Pets-Cute-A-Knight.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-A-Knight.webp`, `docs/assets/previews/9Pets-Cute-A-Knight.png`, `docs/assets/source/9Pets-Cute-A-Knight.png`, `docs/downloads/9Pets-Cute-A-Knight.zip`, and docs cute data for A Knight.
- QA artifacts: `C:\tmp\9pets-cute-a-knight-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

### 2026-06-12 - Coppelia Normal / 9Pets-Coppelia
- Source audit: local normal Cubism folder `live2d/roles/v3a7_314401_fly` exists with 28 motion files; local Spine path is `roles/v3a7_314401_fly`.
- Normal source: `live2d/roles/v3a7_314401_fly`.
- Motions selected by the renderer: idle=b_idle.motion3.json, running-right=b_yincha.motion3.json, running-left=b_tanshou.motion3.json, waving=b_tanshou.motion3.json, jumping=b_yincha.motion3.json, failed=b_kuqi.motion3.json, waiting=b_kuqi1.motion3.json, running=b_sikao.motion3.json, review=b_diantou.motion3.json.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/9Pets-Coppelia`, `docs/assets/spritesheets/9Pets-Coppelia.webp`, `docs/assets/detail-spritesheets/9Pets-Coppelia.webp`, `docs/assets/previews/9Pets-Coppelia.png`, `docs/downloads/9Pets-Coppelia.zip`, and docs data for Coppelia.
- QA artifacts: `C:\tmp\9pets-coppelia-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal Live2D pass.

### 2026-06-12 - Coppelia Cute / 9Pets-Cute-Coppelia
- Source audit: local official chibi/fight Spine source `roles/v3a7_314401_fly/314401_fly_fight.skel`.
- Spine source: `314401_fly_fight.skel`.
- Motions selected by the renderer: idle=idle, running-right=posture, running-left=posture, waving=giddy, jumping=skill1, failed=hit, waiting=sleep, running=posture, review=posture.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/9Pets-Cute-Coppelia`, `docs/assets/spritesheets/9Pets-Cute-Coppelia.webp`, `docs/assets/detail-spritesheets/9Pets-Cute-Coppelia.webp`, `docs/assets/previews/9Pets-Cute-Coppelia.png`, `docs/assets/source/9Pets-Cute-Coppelia.png`, `docs/downloads/9Pets-Cute-Coppelia.zip`, and docs cute data for Coppelia.
- QA artifacts: `C:\tmp\9pets-cute-coppelia-final-contact.png`.
- Verification: `python tools\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.

