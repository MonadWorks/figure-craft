# QA and Provenance

**Tune the checks to the project and intended use.** Start from the skill's careful, restrained visual baseline; do not borrow a journal's house style by default. When a target journal is known and submission is approaching, check its current technical requirements and make only the necessary adjustments.

## What to keep together

For a deliverable figure, keep a reproducible unit sized to the task:

- figure contract or object/evidence note and caption when applicable;
- source table/arrays and selection keys, or the declared evidence/source for a schematic;
- renderer, notebook, or editable construction source;
- requested output formats: prefer editable vector PDF/SVG for plots, lines, and text when supported; use raster images at adequate effective resolution for photographs and pixel-based data;
- palette/type/layout manifest when a shared system is being used;
- source hashes and QA receipt when reproducibility or handoff matters;
- historical render when a redesign replaces an earlier version.

For exploratory work, a compact note and editable draft may be enough. Do not keep only a PNG for a deliverable, and do not silently regenerate a new random example to make a figure look better.

## Automated checks

Use the portable `scripts/figure_style.py` where Matplotlib is appropriate. It supports the bundled fonts, role palette, millimetre `Canvas`, data-to-page coordinate mapping, `check_text()`, and PDF/PNG saving. `scripts/template_multipanel.py` is a data-independent smoke test for three-panel geometry. Use `scripts/check_palette.py` for candidate colours.

At minimum, run:

- actual rendered text bounds against the canvas;
- font-size floor and glyph coverage;
- registered label/axis/tick collisions;
- crowded tick checks;
- panel/title/row/numeric anchor consistency;
- PDF MediaBox and PNG dimensions against the intended physical size;
- effective raster resolution at final placed size, and file format/colour mode required by the target use; prepare raster exports at 3000 dpi or above by default for this skill, unless the target medium or venue specifies another value; prefer vector for plots and text when possible;
- consider TIFF for raster photographs, microscopy, or a venue that requests it; keep PNG for transparent previews and lossless web/review use, and do not convert vector plots to TIFF without a real need;
- font embedding and editable vector output where required;
- source-data and renderer hashes;
- scale bars, inset boundaries, magnification, and annotation keys for image-based panels where relevant;
- all-value/tail retention and axis-limit checks appropriate to the scientific contract.

## Visual review

Automated checks cannot see every meaningful collision. Review the final-size render for:

- line or arrow crossing text;
- markers hidden by text, legends, or interval caps;
- weak distinction between pale rose and grey;
- hierarchy that makes a secondary panel look primary;
- uneven whitespace or an unbalanced left/right pair;
- clipped glyphs, math, minus signs, and units;
- visual exaggeration from axis limits, aspect ratio, or line weight;
- graphical-abstract icons that imply an unsupported mechanism.

When image viewing is unavailable, report that limitation instead of claiming visual approval.

## Scope of a passing check

A passing collision check proves only that the checked text boxes did not overlap. A palette metric describes a colour pair. A font embedding check proves technical embedding. None of these proves the analysis, scientific interpretation, visual taste, accessibility for every reader, or venue acceptance.

## Iterative refinement

Treat review as a loop, not a gate. A rendered draft creates new questions that a checklist cannot anticipate. After each pass, name the most consequential remaining issue and choose a change or test that addresses it; then render and review again. Move between scientific fidelity, first-glance comprehension, detail legibility, visual balance, final-size fit, accessibility, and caption/panel context as relevant. When the figure is unfamiliar, high-stakes, or intended for a broad audience, ask someone not immersed in the data to describe what they see. Their confusion is evidence for refinement, not a reason to add indiscriminate labels. Stop when the important readings are stable and remaining tradeoffs are intentional; benchmark success alone is not a stopping rule.

## Paper-level consistency pass

Before final delivery, compare all main and supplementary figures as a contact sheet or equivalent page sequence. Check that:

- the same role has the same meaning and method order;
- the palette kit, type family, panel letters, reference lines, and marker vocabulary are stable;
- the scale policy is intentional and captions explain exceptions;
- the graphical abstract uses the same semantic roles without pretending to be a statistical panel;
- local deviations have a recorded reason;
- source data, caption, and rendered figure agree.
