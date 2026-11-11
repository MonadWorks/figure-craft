# Spacing and Verification

**Everything in this reference is adjustable.** The values are measured starting points from the bundled paper renderers, not universal laws or venue requirements. Use them when they fit; change them when canvas, medium, density, font, or scientific semantics call for it. If the final canvas is not yet known, use a provisional project size and mark it adjustable. Record meaningful deviations and re-verify at the actual final size.

## Geometry and spacing

| Element | Project starting point | Use |
|---|---:|---|
| Main figure width | 180 mm | Existing paper figure family; redraw at delivery size |
| Graphical abstract width | 190 mm | Existing graphic-abstract system; venue may differ |
| Panel-letter to title start | 5 mm | Consistent title anchor in current Canvas helper |
| Axis label to axis | 2–3 mm | Current `labelpad` values, converted at final size |
| Tick label pad | 2 pt | Current Matplotlib default |
| Text-to-mark clearance | begin around 0.8 mm where space permits | Human layout starting point; code does not certify text-to-mark collisions |
| Registered text-box overlap tolerance | 0.8 px on the rendered canvas | Current `check_text()` ignores intersections smaller than this in both dimensions |
| Adjacent x-tick clearance | 0.8 mm minimum | Current helper reports closer visible tick-label pairs |
| Two formula/equation groups | about 1.2 mm ink-to-ink | Graphical-abstract-specific measured value |
| Section heading to formula | about 4.2 mm ink-to-ink | Graphical-abstract-specific measured value |
| Repeated body-line pitch | about 3.2 mm | Compact graphical-abstract body text |
| Paragraph pitch | about 4.5 mm | Compact graphical-abstract text blocks |

The millimetre values above are physical gaps between ink bounds where stated, not text anchor coordinates. For other scripts, fonts, or type sizes, measure the rendered bounds and re-tune. Equal numeric anchor positions do not guarantee equal visual gaps when text widths differ.

## Line and marker hierarchy

| Element | Project starting point |
|---|---:|
| axes/spines | 0.6 pt |
| grid/light rule | 0.4–0.6 pt |
| reference/zero/identity line | 0.55–0.8 pt, muted and usually dashed |
| paired connector | 0.35–0.6 pt, pale, behind data marks |
| ordinary data stroke/edge | 0.35–0.8 pt |
| primary interval | 1.1–1.6 pt |
| adjusted/secondary interval | about 0.55 pt, paler |
| marker outline | 0.5–0.9 pt |

Keep visible line roles distinct after reduction. A data line should not look like a gridline; a reference line should not compete with the estimate. Put connectors behind markers and intervals. Break or route lines around labels rather than allowing them to cross text. Use a background patch only as a small functional mask; if it needs broad padding, redesign the route.

## Type ladder

Use final physical size, not monitor zoom, as the reference. Current 180 mm figures use roughly:

- 8 pt bold panel letters;
- 7–8 pt panel titles;
- 7 pt axis labels;
- 6.2–6.8 pt categories;
- 6–6.5 pt ticks;
- 5.8–6.2 pt notes and numeric intervals.

Use BentonSans for labels and JuliaMono for aligned statistical numbers in this project kit. Use weight before adding colour for hierarchy. If a caption can carry the detail, do not shrink text below the practical floor to keep it inside the panel. Check every glyph, minus sign, Greek letter, superscript, and unit in the actual font.

## Alignment rules extracted from scripts

- Use one global page coordinate system (millimetres in the current helper), not independent hand nudges in each axes.
- Reuse panel-letter x tracks and title baselines across rows/columns. Current panel titles begin 5 mm after their letter.
- Align repeated row labels, estimates, intervals, and values to common anchors. Use the same data-to-page transform for labels tied to plotted positions.
- Align left/right figures by the actual text baselines or text-box edges for matching rows; do not assume equal axes rectangles create equal label alignment.
- Reserve gutters for long labels so they do not shift the plotting area or numeric columns.
- Check optical centring from rendered ink bounds, especially for formulas, mixed fonts, and icons; geometric centre alone can look off.

## Verification loop

**Pass 1 — contract:** compare every data artist to the declared source, independent unit, transformation, interval, denominator, axis range, and caption. Confirm no observation or tail disappeared.

**Pass 2 — geometry:** draw at final size; check all visible text bounds, missing glyphs, font floor, tick collisions, registered label collisions, panel anchors, shared baselines, number columns, and intended clearances. Export an alignment proof separately when helpful.

**Pass 3 — appearance:** inspect the PDF/PNG at intended physical size and downscaled. Look for text crossed by lines, data hidden by legends, interval caps colliding with labels, weak pale-colour pairs, uneven whitespace, and misleading visual weight.

**Pass 4 — paper:** compare main figures, supplement, and graphical abstract together. Check stable role meanings, font, palette kit, line hierarchy, method order, reference lines, and intentional scale exceptions. Revise the system, not just one image, when drift is systematic.

Run checks again after every geometry or style change. A clean text-box audit does not detect every text-to-data collision; visual review remains necessary. If images cannot be inspected in the current environment, state that explicitly.

## Checks already implemented

`figure_style.py` implements text out-of-canvas, font-size, empty-glyph, registered text/axis/tick overlap, and crowded x-tick checks. The figure renderers also capture panel anchors, layout receipts, and graphical-abstract ink spacing. These are useful mechanisms; they do not provide a universal visual-quality score. Use the [acceptance scorecard](acceptance-scorecard.md) to combine pass/fail gates with human judgement.
