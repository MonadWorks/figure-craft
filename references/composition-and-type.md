# Composition and Type

**All compositions and type values here are adjustable references.** Use only what helps the reader; change the grid, proportions, sizes, and spacing when needed, then verify at final size. These are decision aids, not a mandatory grid. Choose the arrangement that makes the scientific comparison easiest to read.

## Composition choices

- **One dominant panel + supporting panels:** use when one result answers the paper's main question and the others establish mechanism, robustness, or limitations. Give the dominant panel the most width and the clearest title track.
- **Paired panels:** use when two conditions share an independent unit or coordinate system. Share axes when the quantities are genuinely comparable; separate them when the statistical objects differ.
- **Row of mechanisms:** use when several components answer the same subquestion. Repeat the geometry, label tracks, and scale policy; change only the factor or evidence.
- **Schematic → data → conclusion:** use for a process or graphical abstract. The schematic explains the object and route; data panels carry measured/simulated evidence; the final statement must be tied to a real estimate, not decorative optimism.
- **Distribution + summary:** use a strip/ECDF/paired plot for individual units and a separate interval/forest object for the population summary when their scales or meanings differ.
- **Small multiples:** use for repeated settings or cohorts. Keep the same axis policy and encode the changing factor once in a title, facet label, or direct legend.
- **Integrated multivariable view:** when a third or further variable is part of the same scientific relationship, consider adding a second visual channel, a meaningful spatial/mechanistic scaffold, or aligned contextual panels. Make the primary comparison immediate; split into small multiples when added channels create ambiguity or clutter.
- **Context plus measurement:** place a true domain structure (for example, a physical layout, pathway, or process) beside or beneath quantitative encoding only when that structure is evidence-grounded and helps explain the result. Distinguish explanatory schematic marks from measured data.

Do not force symmetry. An asymmetrical layout is valid when evidence weight is asymmetrical. Do not shrink a primary panel merely to make every panel the same size. Do not reject an integrated composition merely because it is unconventional; test whether it exposes a real relationship more clearly than a conventional split view.

## Alignment tracks

Set these before writing labels:

- left edge for panel letters;
- title start and shared title baseline;
- plot-area left/right edges;
- category-label column;
- estimate and interval numeric columns;
- repeated row baselines;
- common reference/zero-line positions;
- caption or annotation clearance below the panel.

For left/right figures with corresponding rows, align the text boxes or baselines that carry the same sequence number, not just their axes. A label in the right panel may need a reserved gutter so its longer wording does not push the plot or break the left/right rhythm.

Keep a deliberate gap between text and line/mark. Never let a line run through a label merely because a bounding-box check treats the label as separate. Prefer moving the line, adding a short break, or reserving a label gutter.

## Type roles

The bundled project font set is BentonSans regular/italic/bold plus JuliaMono for compact numeric annotations. Use local fonts only after verifying their licence and glyph coverage.

| Role | Starting size at final physical size | Style |
|---|---:|---|
| panel letter | 8 pt | bold, short, dark ink |
| panel title | 7–8 pt | bold or semibold; sentence case |
| axis label | 7 pt | regular; use complete units and direction |
| category label | 6.2–6.8 pt | regular; wrap only when the row track allows it |
| tick label | 6–6.5 pt | regular; avoid unnecessary decimals |
| annotation/note | 5.8–6.2 pt | muted; only if it earns its space |
| numeric interval column | 5.8–6.2 pt | JuliaMono or another tabular/monospace face |
| graphical-abstract headline | size follows canvas and word count | bold; keep short enough to preserve whitespace |

These are starting ranges, not a permission to make all text tiny. If a label needs less than the practical floor, shorten the label, increase the panel, or move detail into the caption.

Use font weight to express hierarchy, not colour alone. Do not make every title bold, every label coloured, or every number monospace. Keep mathematical notation and units consistent across the paper.

## Text background and line clearance

A text background is a functional mask, not decoration. Use a paper-coloured patch only when it prevents a line or mark from crossing a short label; keep its padding small, its edges quiet, and its colour consistent with the figure ground. If a label needs a large opaque box to be legible, the composition is probably too crowded.

Before delivery, inspect:

- long title versus subtitle gap;
- left and right title starts;
- same sequence numbers on the same row;
- label-to-line and label-to-marker clearance;
- tick labels versus neighbouring ticks;
- numeric column width for the longest interval;
- legends versus data marks;
- caption/annotation versus panel border;
- text and lines after downscaling and PDF rasterisation.
