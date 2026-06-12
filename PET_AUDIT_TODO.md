# 9Pets Normal/Cute Audit TODO

Created: 2026-06-13 Asia/Shanghai

This replaces the old rebuild worklog. Treat every row as unaudited until normal
and cute have both been checked again. A character is done only after all row
columns are checked and the per-character commit exists.

## Audit Contract

- Normal must use the default skin. If a non-default skin is useful, package it
  separately as `9Pets-Character-Skin-Name`.
- Cute must stay in a `9Pets-Cute-Character` package and must not appear on the
  normal catalog page.
- Non-default cute skins must use `9Pets-Cute-Character-Skin-Name`.
- Reusable character source assets belong under
  `assets/source-cache/Reverse-1999-CN-Asset/`, not `C:\tmp`.
- Every audited character needs normal source QA, cute source QA, default skin
  verification, package naming verification, visual QA, `tools/verify_build.py`,
  and one git commit.

## Current P0 Findings

| Character | Issue | Required action |
| --- | --- | --- |
| Kiperina | Normal preview is nearly black and shows as a tiny package. | Re-render or fall back to a visible default-source package; verify package size display after rebuild. |
| Lorelei | Normal preview is nearly black and shows as a tiny package. | Re-render or fall back to a visible default-source package; verify package size display after rebuild. |
| Sotheby | Normal currently resolved to non-default skin `World on the Other Side` / asset `300902`. | Restore default skin as `9Pets-Sotheby`; move non-default skin to `9Pets-Sotheby-World-on-the-Other-Side` if kept. |
| Bette | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Bkornblume | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Bunny Bunny | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Centurion | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Charlie | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Cristallo | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Eagle | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Enigma | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Erick | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| John Titor | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| La Source | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Leilani | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Matilda | Screenshot review needed for default-skin visibility. | Confirm normal is default skin and visually readable. |
| Mesmer Jr. | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Ms. Moissan | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Nick Bottom | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Oliver Fog | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Pavia | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Pioneer | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Poltergeist | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Reed | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| The Fool | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Twins Sleep | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Ulu | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |
| Zima | Screenshot review needed for normal/cute separation. | Confirm normal source is not the cute/fight track; rebuild if the normal card uses cute-like output. |

## Per-Character Queue

Columns: Normal = normal source/package rebuilt or accepted; Cute = cute
source/package rebuilt or accepted; Default skin = normal uses default skin;
Naming = package names follow the skin/variant rule; Visual QA = page card,
detail page, contact sheet, and download checked; Commit = one git commit exists
for that character.

| Done | Character | Normal package | Cute package | Normal | Cute | Default skin | Naming | Visual QA | Commit | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ ] | 37 | `9Pets-37` | `9Pets-Cute-37` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | 6 | `9Pets-6` | `9Pets-Cute-6` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | A Knight | `9Pets-A-Knight` | `9Pets-Cute-A-Knight` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Aleph | `9Pets-Aleph` | `9Pets-Cute-Aleph` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Alexios | `9Pets-Alexios` | `9Pets-Cute-Alexios` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | aliEn T | `9Pets-aliEn-T` | `9Pets-Cute-aliEn-T` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | An-an Lee | `9Pets-An-an-Lee` | `9Pets-Cute-An-an-Lee` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Anjo Nala | `9Pets-Anjo-Nala` | `9Pets-Cute-Anjo-Nala` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | APPLe | `9Pets-APPLe` | `9Pets-Cute-APPLe` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Argus | `9Pets-Argus` | `9Pets-Cute-Argus` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Avgust | `9Pets-Avgust` | `9Pets-Cute-Avgust` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Baby Blue | `9Pets-Baby-Blue` | `9Pets-Cute-Baby-Blue` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | Hidden normal must be re-decided. |
| [ ] | Balloon Party | `9Pets-Balloon-Party` | `9Pets-Cute-Balloon-Party` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | Hidden normal must be re-decided. |
| [ ] | Barbara | `9Pets-Barbara` | `9Pets-Cute-Barbara` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Barcarola | `9Pets-Barcarola` | `9Pets-Cute-Barcarola` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Beryl | `9Pets-Beryl` | `9Pets-Cute-Beryl` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Bette | `9Pets-Bette` | `9Pets-Cute-Bette` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Bkornblume | `9Pets-Bkornblume` | `9Pets-Cute-Bkornblume` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Blonney | `9Pets-Blonney` | `9Pets-Cute-Blonney` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Brimley | `9Pets-Brimley` | `9Pets-Cute-Brimley` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Brume | `9Pets-Brume` | `9Pets-Cute-Brume` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Buddy Fairchild | `9Pets-Buddy-Fairchild` | `9Pets-Cute-Buddy-Fairchild` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Bunny Bunny | `9Pets-Bunny-Bunny` | `9Pets-Cute-Bunny-Bunny` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Centurion | `9Pets-Centurion` | `9Pets-Cute-Centurion` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Charlie | `9Pets-Charlie` | `9Pets-Cute-Charlie` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Charon | `9Pets-Charon` | `9Pets-Cute-Charon` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Cheng Heguang | `9Pets-Cheng-Heguang` | `9Pets-Cute-Cheng-Heguang` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Click | `9Pets-Click` | `9Pets-Cute-Click` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Coppelia | `9Pets-Coppelia` | `9Pets-Cute-Coppelia` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Corvus | `9Pets-Corvus` | `9Pets-Cute-Corvus` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Cristallo | `9Pets-Cristallo` | `9Pets-Cute-Cristallo` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Darley Clatter | `9Pets-Darley-Clatter` | `9Pets-Cute-Darley-Clatter` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Desert Flannel | `9Pets-Desert-Flannel` | `9Pets-Cute-Desert-Flannel` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Diggers | `9Pets-Diggers` | `9Pets-Cute-Diggers` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Dikke | `9Pets-Dikke` | `9Pets-Cute-Dikke` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Door | `9Pets-Door` | `9Pets-Cute-Door` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Druvis III | `9Pets-Druvis-III` | `9Pets-Cute-Druvis-III` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Eagle | `9Pets-Eagle` | `9Pets-Cute-Eagle` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Enigma | `9Pets-Enigma` | `9Pets-Cute-Enigma` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Erick | `9Pets-Erick` | `9Pets-Cute-Erick` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Eternity | `9Pets-Eternity` | `9Pets-Cute-Eternity` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Ezio Auditore | `9Pets-Ezio-Auditore` | `9Pets-Cute-Ezio-Auditore` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Ezra Theodore | `9Pets-Ezra-Theodore` | `9Pets-Cute-Ezra-Theodore` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Fatutu | `9Pets-Fatutu` | `9Pets-Cute-Fatutu` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Flutterpage | `9Pets-Flutterpage` | `9Pets-Cute-Flutterpage` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Getian | `9Pets-Getian` | `9Pets-Cute-Getian` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Hissabeth | `9Pets-Hissabeth` | `9Pets-Cute-Hissabeth` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Horropedia | `9Pets-Horropedia` | `9Pets-Cute-Horropedia` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Igor | `9Pets-Igor` | `9Pets-Cute-Igor` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Isolde | `9Pets-Isolde` | `9Pets-Cute-Isolde` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | J | `9Pets-J` | `9Pets-Cute-J` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Jessica | `9Pets-Jessica` | `9Pets-Cute-Jessica` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Jiu Niangzi | `9Pets-Jiu-Niangzi` | `9Pets-Cute-Jiu-Niangzi` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | John Titor | `9Pets-John-Titor` | `9Pets-Cute-John-Titor` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Kaalaa Baunaa | `9Pets-Kaalaa-Baunaa` | `9Pets-Cute-Kaalaa-Baunaa` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Kakania | `9Pets-Kakania` | `9Pets-Cute-Kakania` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Kanjira | `9Pets-Kanjira` | `9Pets-Cute-Kanjira` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Kassandra | `9Pets-Kassandra` | `9Pets-Cute-Kassandra` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Kiperina | `9Pets-Kiperina` | `9Pets-Cute-Kiperina` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 black/dark normal preview. |
| [ ] | La Source | `9Pets-La-Source` | `9Pets-Cute-La-Source` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Leilani | `9Pets-Leilani` | `9Pets-Cute-Leilani` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Liang Yue | `9Pets-Liang-Yue` | `9Pets-Cute-Liang-Yue` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Lilya | `9Pets-Lilya` | `9Pets-Cute-Lilya` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Loggerhead | `9Pets-Loggerhead` | `9Pets-Cute-Loggerhead` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Lopera | `9Pets-Lopera` | `9Pets-Cute-Lopera` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Lorelei | `9Pets-Lorelei` | `9Pets-Cute-Lorelei` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 black/dark normal preview. |
| [ ] | Lorentz Butterfly | `9Pets-Lorentz-Butterfly` | `9Pets-Cute-Lorentz-Butterfly` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Lucy | `9Pets-Lucy` | `9Pets-Cute-Lucy` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Marcus | `9Pets-Marcus` | `9Pets-Cute-Marcus` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Marsha | `9Pets-Marsha` | `9Pets-Cute-Marsha` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Matilda | `9Pets-Matilda` | `9Pets-Cute-Matilda` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot default-skin visibility. |
| [ ] | Medicine Pocket | `9Pets-Medicine-Pocket` | `9Pets-Cute-Medicine-Pocket` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Melania | `9Pets-Melania` | `9Pets-Cute-Melania` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Mercuria | `9Pets-Mercuria` | `9Pets-Cute-Mercuria` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Mesmer Jr. | `9Pets-Mesmer-Jr` | `9Pets-Cute-Mesmer-Jr` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Moldir | `9Pets-Moldir` | `9Pets-Cute-Moldir` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Mondlicht | `9Pets-Mondlicht` | `9Pets-Cute-Mondlicht` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Mr. Duncan | `9Pets-Mr-Duncan` | `9Pets-Cute-Mr-Duncan` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Ms. Moissan | `9Pets-Ms-Moissan` | `9Pets-Cute-Ms-Moissan` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Ms. NewBabel | `9Pets-Ms-NewBabel` | `9Pets-Cute-Ms-NewBabel` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Ms. Radio | `9Pets-Ms-Radio` | `9Pets-Cute-Ms-Radio` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Ms. Stranger | `9Pets-Ms-Stranger` | `9Pets-Cute-Ms-Stranger` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Name Day | `9Pets-Name-Day` | `9Pets-Cute-Name-Day` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Nautika | `9Pets-Nautika` | `9Pets-Cute-Nautika` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Necrologist | `9Pets-Necrologist` | `9Pets-Cute-Necrologist` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Nick Bottom | `9Pets-Nick-Bottom` | `9Pets-Cute-Nick-Bottom` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Noire | `9Pets-Noire` | `9Pets-Cute-Noire` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Oliver Fog | `9Pets-Oliver-Fog` | `9Pets-Cute-Oliver-Fog` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | ONiON | `9Pets-ONiON` | `9Pets-Cute-ONiON` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Paper Heron | `9Pets-Paper-Heron` | `9Pets-Cute-Paper-Heron` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Pavia | `9Pets-Pavia` | `9Pets-Cute-Pavia` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Pickles | `9Pets-Pickles` | `9Pets-Cute-Pickles` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Pioneer | `9Pets-Pioneer` | `9Pets-Cute-Pioneer` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Poltergeist | `9Pets-Poltergeist` | `9Pets-Cute-Poltergeist` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Rabies | `9Pets-Rabies` | `9Pets-Cute-Rabies` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Ramona | `9Pets-Ramona` | `9Pets-Cute-Ramona` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Recoleta | `9Pets-Recoleta` | `9Pets-Cute-Recoleta` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Reed | `9Pets-Reed` | `9Pets-Cute-Reed` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Regulus | `9Pets-Regulus` | `9Pets-Cute-Regulus` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Rhiannon | `9Pets-Rhiannon` | `9Pets-Cute-Rhiannon` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Rubuska | `9Pets-Rubuska` | `9Pets-Cute-Rubuska` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Satsuki | `9Pets-Satsuki` | `9Pets-Cute-Satsuki` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Semmelweis | `9Pets-Semmelweis` | `9Pets-Cute-Semmelweis` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Sentinel | `9Pets-Sentinel` | `9Pets-Cute-Sentinel` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Shamane | `9Pets-Shamane` | `9Pets-Cute-Shamane` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Silverwing Eagle | `9Pets-Silverwing-Eagle` | `9Pets-Cute-Silverwing-Eagle` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Sonetto | `9Pets-Sonetto` | `9Pets-Cute-Sonetto` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Sotheby | `9Pets-Sotheby` | `9Pets-Cute-Sotheby` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 normal currently non-default asset 300902. |
| [ ] | Spathodea | `9Pets-Spathodea` | `9Pets-Cute-Spathodea` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Sputnik | `9Pets-Sputnik` | `9Pets-Cute-Sputnik` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Sweetheart | `9Pets-Sweetheart` | `9Pets-Cute-Sweetheart` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Tennant | `9Pets-Tennant` | `9Pets-Cute-Tennant` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | The Fool | `9Pets-The-Fool` | `9Pets-Cute-The-Fool` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Tooth Fairy | `9Pets-Tooth-Fairy` | `9Pets-Cute-Tooth-Fairy` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | TTT | `9Pets-TTT` | `9Pets-Cute-TTT` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Tuesday | `9Pets-Tuesday` | `9Pets-Cute-Tuesday` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Twins Sleep | `9Pets-Twins-Sleep` | `9Pets-Cute-Twins-Sleep` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Ulrich | `9Pets-Ulrich` | `9Pets-Cute-Ulrich` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Ulu | `9Pets-Ulu` | `9Pets-Cute-Ulu` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | Vila | `9Pets-Vila` | `9Pets-Cute-Vila` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Voyager | `9Pets-Voyager` | `9Pets-Cute-Voyager` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | White Rum | `9Pets-White-Rum` | `9Pets-Cute-White-Rum` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Willow | `9Pets-Willow` | `9Pets-Cute-Willow` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Windsong | `9Pets-Windsong` | `9Pets-Cute-Windsong` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Zima | `9Pets-Zima` | `9Pets-Cute-Zima` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | P0 screenshot normal/cute separation. |
| [ ] | X | `9Pets-X` | `9Pets-Cute-X` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
| [ ] | Yenisei | `9Pets-Yenisei` | `9Pets-Cute-Yenisei` | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |  |
