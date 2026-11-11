# Palette and Semantic Roles

**Rose–Plum–Gold is the default visual signature of this personal skill.** Use it unless the project explicitly needs another family or a particular comparison requires a supporting/contrasting hue. The swatches and role assignments below are adjustable references: preserve their visual logic, test the actual marks, and change a member when size, medium, background, contrast, or colour-vision checks require it.

## Default direction

Build a bright, restrained rose-led family on a white ground, balanced by plum structure/reference marks and a warm gold stimulus/input accent. Aim for a figure that feels composed and comfortable: one dominant accent, quiet structural neutrals, deliberate whitespace, and enough contrast to survive final-size reading. The palette is a signature, not a license to colour every object; neutral space and uncoloured structure are part of the system.

## Reference range and variants

The current ICBR manuscript figures and RoboSoft submission figures use `light` by default. The shared `figure_style.py` also defines `mid` and `deep`. These are tonal variants of the same visual family, not separate identities or limits on supporting colours. Choose one coherent variant for a figure set and inspect the actual co-occurring marks after a change.

| Role | Light (default) | Mid | Deep | Guidance |
|---|---|---|---|---|
| Primary result / endpoints | rose `#E27A9E`; stroke `#C2507C` | rose `#CA799A` | rose `#B73E70`; stroke `#B4577F` | Main observed result marks |
| Secondary/readout rose | `#F2B1C7`; edge `#D0698D` | `#E3B6CA`; edge `#BE7C9C` | `#D99AB3`; edge `#B4577F` | Pale fill always gets darker edge or non-colour cue |
| Pale rose accent | `#F4BFD0` | `#F0D2DE` | `#EBC3D2` | Broad fills only; not text or thin strokes |
| Stimulus / specific input | gold `#EDAF26`; line `#DB9A1D` | gold `#D4A239`; line `#B8862A` | gold `#D4A239`; line `#B8862A` | Project anchor: gold/yellow means stimulus/input |
| Structural/internal | plum `#6E5677` | plum `#5A4A66` | plum `#463B50` | Model structure and internal combinations |
| Forecast / prior-averaged | mulberry `#A8668F`; dark `#8A4E75` | `#9C537C`; dark `#7B3E61` | `#87385F`; dark `#6E2C4C` | Remains distinct from stimulus gold |
| Ordinary / reference fill | grey `#B9AEB7`; edge `#8A818A` | grey `#D0CBCF`; edge `#8F878F` | grey `#C9C5C8`; edge `#8F878F` | De-emphasized, not invisible |
| Light reference fill | `#DAD4D8`; edge `#A9A1A9` | `#DDD8DC`; edge `#A9A1A9` | `#DAD4D8`; edge `#A9A1A9` | Needs edge/shape redundancy |
| Signed negative role | `#4E4350` | `#413A43` | `#413A43` | Only within a labelled signed diverging scale |
| Text / axes | ink `#2E2531`; label `#49424B`; tick `#6B626D`; muted `#7D7280` | same shared neutrals | same shared neutrals | Keep text neutral and legible |

A local warm orange such as `#E8A13C` appeared in a specific three-response figure; it is not part of this default role range.

## Colour logic

- Keep a colour's meaning stable across related panels. Rose–Plum–Gold is the base grammar: rose carries the primary result accent, plum carries structure and measured contrast, and gold is reserved for stimulus/input when that role exists. Gold is not a general-purpose default or decorative highlight; use it elsewhere only as a rare, intentional accent with a clear meaning.
- Use colour sparingly. Let whitespace, neutral ink, line weight, marker shape, fill state, and direct labels do part of the work. Do not colour every object.
- Use a dark companion for pale fills. Pair warm accents with quiet cool or neutral structure so the page does not become visually loud.
- For ordered magnitude, use a sequential scale with a perceptually meaningful lightness progression. For signed values with a meaningful centre, use a diverging scale with a clear neutral midpoint. For unordered categories, use a small qualitative set; keep category colours balanced rather than implying rank.
- Keep treatment or method identity separate from evidence priority. Equal-status groups can use balanced extensions of the base family or restrained monochrome; make the primary estimate prominent through composition, not an arbitrary colour hierarchy.
- Use marker shape, fill state, line style, direct labels, or facets as redundant channels. Do not rely on hue alone.
- Keep neutral references visible enough to compare; neutral does not mean invisible.

## Palette reasoning

Use these practical checks when choosing or extending the default family:

1. **Role:** what does the colour mean here, and does that meaning recur elsewhere?
2. **Lightness:** can the hierarchy still be read in grayscale and after downscaling?
3. **Harmony:** does the supporting hue balance the rose, plum, and gold without competing with the primary answer? Prefer a restrained analogous, split-complementary, or neutral relationship over a decorative rainbow.
4. **Contrast:** do adjacent marks separate on the intended background at their actual size?
5. **Accessibility:** do shape, fill, line, and direct labels preserve the distinction under common colour-vision simulations and print?
6. **Medium:** will the selection survive white paper, projection, dark background, or the target export?

These are design questions, not universal numerical thresholds.

## Choosing and checking a palette

Keep Rose–Plum–Gold as the starting family. Add a hue only when it represents a distinct role or resolves a real comparison need; do not add colour only to make a panel lively. For each panel, check contrast against the intended background at final marker/stroke size, separation under colour-vision simulations and grayscale where relevant, pale-fill visibility after printing/downscaling, and the assigned semantic meaning across the figure set. The swatch metric is only a prompt to inspect actual marks, not a pass/fail certificate.

The current suite found soft rose versus neutral grey weak under some colour-vision simulations (deutan ΔE76 about 2.7). The documented solution is a deeper edge plus shape/fill redundancy, not a claim that the fills alone are universally distinguishable. Use `../scripts/check_palette.py` to inspect new candidates; `../scripts/palette_check.py` preserves the historical v4 candidate comparison. See the source repository’s `outputs/pastel_figure_suite/palette_checks.json` for recorded current-suite values.

## When the user requests another hue family

Respect the request. Preserve the same design logic with a different set of role colours: result accent, structural/reference neutrals, stimulus/input accent if semantically applicable, darker stroke companions, and non-colour encoding. Re-run the checks; do not keep a token rose accent against the user's explicit direction.
