# Research Guides and Open-Source Ideas

Use this as a source-backed idea bank, not a universal checklist. Its baseline is careful, restrained, and reader-centered: use it by default without importing a particular journal's visual house style. Near submission, check the target journal's current artwork instructions and make only the technical adjustments needed. Apply design advice according to the evidence, audience, and medium.

## Small practices worth keeping

### Before drawing

- **Write the reader's question in one sentence.** Decide what someone should notice first; let that determine the reading order and visual hierarchy.
- **Choose the representation for the comparison, not for familiarity.** A bar chart is not a default for distributions; use points, intervals, paired connections, or small multiples when those expose the evidence more directly.
- **Set the intended final dimensions early.** Check type, marks, gaps, line weights, and image resolution at that size, not just while zoomed in on a large canvas. Avoid enlarging a low-resolution image after the fact.
- **Separate the plotted evidence from explanation.** Put concise labels and essential keys near the marks; use the caption for methods and details that do not belong inside the graphic.

### While composing

- **Give each panel a job.** Order panels so the reader can follow the argument; let panels with more evidence have the space they need rather than forcing a rigid grid.
- **Group by proximity and alignment.** Shared baselines, repeated label tracks, and consistent gaps make related items feel related. Keep enough breathing room that groups do not blur together.
- **Spend emphasis selectively.** Size, darkness, saturation, and line weight all attract attention. Use one or two levels of emphasis; do not make every mark compete for the first look.
- **Remove elements that do not help interpretation.** Decorative icons, shadows, redundant legends, and unnecessary gridlines usually cost attention. Keep a grid or reference line when it helps estimate or compare values.
- **Make image panels self-explanatory.** State what is shown and add scale bars, magnification, inset boundaries, and clear color/annotation keys where relevant. Ensure an inset is visibly connected to its source region.
- **Use redundant encodings for important distinctions.** Pair hue with shape, line style, fill state, direct labels, or position when readers must identify categories or traces.

### When several variables belong together

Do not stop at two variables because a familiar chart form has two axes. A third dimension can make a figure more informative when it has a real relationship to the question and a clear visual channel: position for the primary comparison, then possibly shape, line style, size, fill, a spatial/mechanistic scaffold, or a compact facet for another factor. Keep the mapping stable, label it directly, and make the primary relationship visible before the reader decodes secondary channels.

Try an integrated composition when the variables are related parts of one explanation: for example, project measurements onto a meaningful spatial or mechanistic layout, or coordinate aligned panels so the shared entities and changing conditions can be compared. Use an established domain structure only when it is real and useful; do not turn an illustrative schematic into evidence.

Compare the integrated view with small multiples or separate panels. Prefer the integrated view when it reveals a relationship that separation would hide and the marks remain distinguishable. Prefer separation when overplotting, too many simultaneous encodings, or unequal scales obscure the result. For small multiples, keep ordering and comparable scales consistent when the comparison depends on them; if scales differ to reveal local patterns, make the difference explicit and preserve absolute context.

A useful test: can a reader explain the primary relationship and the extra variable without repeatedly hunting through a complex legend? If not, reduce channels, label directly, or split the view. More information is not automatically more insight; integration should uncover structure, not merely increase density.


- **Inspect the figure at actual output size and in its expected context.** For print, consider a grayscale/print check; for projection or small screens, check contrast and type at the likely viewing size.
- **Read it once without the caption, then verify it with the caption.** The main comparison should be apparent; the caption should clarify the design and scientific details rather than rescue an ambiguous encoding.
- **Check that the final export preserves the source.** Confirm vector/text editability where requested, embedded fonts where required, and that raster images were acquired at adequate resolution rather than artificially upscaled.
- **For multi-panel images, check shared scales, panel order, scale bars, boundaries, and labels together.** Local correctness does not guarantee that the assembled figure reads coherently.

## What not to turn into universal rules

- Journal-specific sizes, font families, point-size ranges, panel limits, formats, and raster-resolution thresholds are submission constraints, not universal design laws. Check the target venue's current instructions near submission; do not impose a house style on exploratory design.
- TIFF is useful for raster photographs, microscopy, and venues that request it, but it is not a reason to flatten vector plots. For this skill, a raster export of 3000 dpi or above is a reasonable default; still check effective pixel dimensions at final size and follow the target medium when it specifies another value. Prefer editable vector PDF/SVG for plots and text when accepted.
- A top-left start and left-to-right reading order are useful conventions for many audiences, not a rule for every language, circular process, spatial map, or deliberately centered composition.
- Removing every gridline, minimizing every white space, or banning all coloured text is too absolute. Keep or remove an element according to whether it supports reading at final size.
- Accessibility is not guaranteed by choosing a palette marketed as “colourblind safe.” Test the actual co-occurring marks and preserve distinctions with non-colour channels.
- A familiar plot type, journal preset, or “publication-ready” theme does not verify the statistical object, data integrity, or interpretation.

## Open-source projects reviewed

These projects are useful references for different parts of the workflow. They are not templates to copy wholesale.

| Project | Useful idea to adopt | Do not inherit automatically |
|---|---|---|
| [SciencePlots](https://github.com/garrettj403/SciencePlots) | Small composable style sheets and a gallery make style choices easy to discover; its journal-specific styles illustrate how venue overrides can be layered over a base. | Its “science” appearance, font assumptions, or combinations are not universal; a style preset cannot choose an honest plot or validate a figure. |
| [tueplots](https://github.com/pnkraemer/tueplots) | Keep reusable settings explicit and composable; support scoped settings rather than silently changing global plotting state. Make size/type consistency repeatable across a figure set. | Do not replace a considered visual identity with unopinionated settings alone; journal presets are starting points and should be checked against current venue guidance. |
| [Matplotlib colormap guidance](https://matplotlib.org/stable/users/explain/colors/colormaps.html) and [Matplotlib styles](https://github.com/matplotlib/matplotlib/tree/main/lib/matplotlib/mpl-data/stylelib) | Choose sequential maps for ordered magnitude, diverging maps for meaningful center values, cyclic maps for wrapping quantities, and qualitative palettes for unordered categories. Prefer perceptually coherent lightness progression for quantitative maps. | Do not use rainbow/jet-like maps by habit or use a categorical palette as a continuous scale. Do not let hue imply order or scientific meaning it does not carry. |
| [SciencePlots gallery](https://github.com/garrettj403/SciencePlots) and [tueplots examples](https://github.com/pnkraemer/tueplots) | Show a range of concrete examples so users can compare outcomes rather than memorizing abstract settings. | Do not treat repository popularity, stars, screenshots, or a “publication-ready” label as evidence of correctness or accessibility. Review license, maintenance, and dependencies before adopting code. |

Figure Craft's default visual identity remains Rose–Plum–Gold. These sources guide the decision process and technical checks; they do not override that identity unless the project, scientific semantics, venue, or user explicitly requires another solution.

## Sources

- Nature Research Figure Guide, [Preparing figures: specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/) and [Building and exporting figure panels](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/). Venue-specific production guidance; its main figures prefer editable vector files, while Extended Data has separate image-format and resolution rules.
- [PLOS figure guidelines](https://journals.plos.org/plosone/s/figures). Venue-specific technical requirements and image-integrity guidance; check the detailed file requirements for the target journal and content type.
- Rougier, Droettboom & Bourne, [Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833), *PLOS Computational Biology* (2014). General design principles including audience, captions, and effective use of visual encodings.
- Jambor et al., [Creating clear and informative image-based figures for scientific publications](https://doi.org/10.1371/journal.pbio.3001161), *PLOS Biology* (2021). Evidence and recommendations for image-based figures, including scale bars, insets, annotations, and accessibility.
- Matplotlib, [Choosing Colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html). Perceptual rationale and functional colormap categories.
- Open-source repositories: [SciencePlots](https://github.com/garrettj403/SciencePlots), [tueplots](https://github.com/pnkraemer/tueplots), and [Matplotlib](https://github.com/matplotlib/matplotlib).
