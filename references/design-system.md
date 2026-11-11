# Design System: Home, Away, Third

**Rose–Plum–Gold is the default visual system of this skill.** It is a recognizable foundation, not a demand to colour every mark. Use its light, mid, and deep variants as the first candidates; add a supporting hue or change the family only when the science, medium, contrast, or explicit project direction requires it. Preserve the semantic logic and re-verify. The paper should read as one figure family, not a sequence of unrelated images.

## Rose–Plum–Gold variants

The bundled `light`, `mid`, and `deep` variants provide tested starting points for this family:

- **Light:** bright white-ground default. Rose results, pale rose secondary fills, plum structure, gold stimulus, neutral text.
- **Deep:** stronger strokes and darker rose/plum values for small panels, dense supplements, print, or weak white-background contrast.
- **Mid:** a balanced compromise for graphical abstracts, mixed schematic/data pages, or figures that need more presence without the density of deep.

Choose the variant that preserves comfortable contrast at actual size; the names describe palette depth, not a required publication tier.

For a coordinated figure set, choose a coherent kit for the marks being compared. A paper may use another kit for a distinct medium or role; document the reason when consistency matters. Do not mix variants inside one comparison merely for decoration.

## Example semantic roles

| Role | Default treatment | Backup encoding |
|---|---|---|
| observed result / primary outcome | rose fill or rose line | filled marker, stronger stroke, direct label |
| secondary readout | soft rose / pale rose | outline, lighter weight, separate shape |
| structure / model / internal | plum-grey | line style, network edge, square/diamond |
| reference / baseline / control | neutral grey | open marker, dashed line, lower emphasis |
| stimulus / applied input, when present | gold/yellow in this project system | gold ring, arrowhead, stimulus band, label |
| negative/signed direction | deep plum-grey or a tested opposing role | zero line, sign label, diverging scale |

Use only roles that exist in the project; the role map is not a requirement to assign every concept a colour. Add supporting hues when a comparison genuinely needs them, and do not reuse one visual channel for conflicting meanings.

Keep experimental identity separate from evidence priority. If two arms or methods have equal status, do not make one look like the “result” and the other like a “reference” merely to follow the palette table. Use equally weighted, clearly labelled colours—preferably harmonious with Rose–Plum–Gold—or line/marker differences. Emphasize the prespecified primary estimate through layout and annotation instead.

## Colour and line principles

- Use a dark companion for every pale fill that must survive small size or printing.
- Keep text and axes neutral; coloured text is reserved for short direct labels or a deliberate semantic callout.
- Use the lightest fills for area, broad bands, or large markers, never for fine text or hairline structure.
- Use one reference/zero/identity line treatment throughout the paper: usually muted grey, thin, and dashed only when it is a reference rather than data.
- Let line width express hierarchy: data/primary interval > structural connection > reference/grid. Keep line caps and joins consistent.
- Use transparency sparingly. Opacity can hide tails, make overlaps ambiguous, and weaken colour-vision separation.
- Test colours in the marks that actually co-occur. A swatch chart alone cannot show whether a rose point and grey point remain distinct at final size.

## Palette QA decisions

Run the bundled palette diagnostic for candidate roles, then inspect white-background contrast, grayscale, protan/deutan/tritan simulations, and the printed/downscaled result. Treat metrics as evidence about a pair, not as universal certification. If a pair is weak, add a stroke, shape, line style, direct label, or facet before adding more colours.

## Figure-set consistency

For a coordinated set or reproducible handoff, a project manifest can record role names, palette, fonts, canvas, line weights, panel treatment, and source/renderer versions. A single exploratory figure does not need a manifest. Keep meaningful conventions stable across related figures, and explain exceptions when they could confuse comparison.
