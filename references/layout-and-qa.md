# Layout and Figure QA

## Alignment system

Use an explicit page coordinate system at the intended physical size. The reference Matplotlib helper uses millimetres and a full-page canvas so panel geometry, annotations, and plots can share stable anchors.

Define alignment tracks instead of nudging labels independently:

- **Panel-letter track:** align corresponding panel letters to a shared left anchor per column.
- **Title track:** align title starts at a fixed offset from panel letters; use a shared baseline for panels in the same row.
- **Plot-area track:** reserve gutters for long category labels so they do not move the data axes.
- **Row track:** map category labels, estimates, intervals, and numeric columns through the same data-to-page coordinate transform.
- **Cross-row/column track:** align common plot edges and numeric columns across stacked or side-by-side panels.

For repeated panel identifiers or numbered rows, align their visible text boxes or baselines to shared coordinates, not their nominal axes-relative positions. Keep the intended gap between identifier, title, mark, and label explicit.

## Collision and bounds checks

Use a rendered-text pass after `canvas.draw()` so checks use actual font metrics. The bundled `figure_style.py` includes checks for:

- visible text outside the page;
- fonts below a configurable size floor;
- missing/empty glyphs;
- overlap among registered manual labels, axis labels, and visible tick labels;
- crowded x tick labels.

The pastel figure renderers also record panel anchors and emit separate alignment-proof images. Use those proof images for geometry review, never as manuscript figures.

Important limitation: bounding-box checks only cover the artists that are registered and the collision classes implemented. They do not guarantee that labels avoid every data mark, that no lines obscure important observations, or that the layout is aesthetically sound. Visually inspect the final-size output when possible.

## Scientific and visual preflight

Before delivery, check the following where applicable:

- panel question and caption agree;
- each plotted number traces to the declared source data and transformation;
- independent units and nested repeats are stated correctly;
- all observations and influential tails remain present unless the analysis contract says otherwise;
- paired data remain visibly paired;
- zero/identity/reference lines are visible and correctly labelled;
- intervals use the declared confidence level and independent unit;
- comparisons that should be comparable share axes/scales;
- no axis limit or aspect ratio creates a misleading comparison;
- colours are stable in meaning and backed by shape/fill/line redundancy;
- canvas size is the actual target size, with no accidental tight crop or silent rescaling;
- vector PDF/SVG and a high-resolution preview are exported, with source data and provenance retained;
- font embedding, glyph coverage, text bounds, clipping, and overlap checks pass;
- a human reviews the final-size render when visual quality matters.

A technical pass is evidence about the checked property only. It does not certify scientific validity, journal compliance, or aesthetic superiority.

## Reference implementation

`../scripts/figure_style.py` is copied from the current endpoint-revision renderer. It provides the current project palette, role mapping, millimetre `Canvas`, interval/axis helpers, and text checks. It depends on Matplotlib and NumPy and may expect project fonts in adjacent directories. Treat it as a source template: adapt font paths and role semantics for a new project, and verify its dependencies before running. Do not copy its study-specific assumptions into unrelated plots.

`../scripts/check_palette.py` accepts candidate hex colours and a background, then prints contrast and pairwise CIE76 differences under Machado protan/deutan/tritan simulations. `../scripts/palette_check.py` is the historical ICBR v4 candidate check. Both need NumPy; their ΔE and contrast outputs are descriptive diagnostics, not universal pass/fail thresholds.
