# Forward Tests

These are semantic regression cases for the skill, not figure-quality benchmarks. Run them as tabletop prompts after changing the entrypoint or routing references. A result passes when the response follows the expected constraints without inventing data or forcing a bundled style.

## Case A: existing figure, optional reference

**Prompt:** “Redesign the supplied paired-method figure for a paper. Keep the scientific conclusion and make it easier to read. The source table and caption are available.”

**Expected behaviour:**

- Treat the existing figure and source contract as inputs, not as permission to copy its claims blindly.
- Inspect the source table and caption; resolve the independent unit, estimand, pairing, interval convention, axis policy, and target size before changing the evidence encoding.
- Diagnose the old composition: identify what readers need, what currently obstructs them, and which parts remain useful. Redesign substantially if it improves clarity, hierarchy, spacing, or scientific legibility; do not preserve weak layout merely because it exists.
- Consider a paired-distribution plus aggregate-estimate composition, a direct paired view, or a fresh structure as the evidence warrants.
- Preserve all observations, tails, denominators, method order, and uncertainty unless a declared scientific change is requested.
- Load template-map and relevant layout/QA references only as needed; load the full provenance/manifest path only for a deliverable or handoff.
- Never claim that a bundled image, collision check, palette metric, or renderer pass validates the scientific conclusion.

**Failure signals:** automatically selecting the bundled figure as the template; inferring data or axes from the image; treating one layout or 180 mm canvas as mandatory; preserving an unsatisfactory composition without diagnosis; requiring a full paper manifest for an exploratory redesign.

## Case B: new figure, ambiguous design

**Prompt:** “Make a main figure for a 2x2 randomized clinical trial with two arms, repeated measurements, and a 12-week endpoint.”

**Expected behaviour:**

- Notice that “2x2” may mean a factorial design with four randomized cells, while “two arms” may mean a two-arm longitudinal design. Ask which design is intended before choosing a composition.
- Ask for the outcome and units, actual visits, direction, randomized and analysis units, baseline handling, analysis population, missing-data rule, model/adjustment, estimand, interval source, arm labels, and target physical size as relevant.
- Keep the main figure's claim and panel roles distinct; move supporting evidence elsewhere when including it would crowd or dilute the primary argument. Preserve all observations and document any analysis-defined exclusions or transformations.
- If it is a two-arm longitudinal trial, consider a time-course panel plus a separate primary endpoint contrast, but label trajectory summaries as descriptive or inferential and do not invent visits or values.
- If it is factorial, represent the four cells and prespecified main/interaction contrasts; do not collapse the design into two arms.
- Keep treatment identity separate from evidence priority. Equal-status arms may use balanced hues drawn from or harmonized with the Rose–Plum–Gold family, plus line/marker redundancy; retain the default family without falsely assigning one arm the primary-result role.
- Use a provisional canvas only when necessary, state the assumption, and revisit it at the actual venue size.

**Failure signals:** silently collapsing factorial structure; fabricating model-based trajectories; treating a treatment arm as a neutral “reference” without scientific justification; applying a full publication QA checklist before the design ambiguity is resolved.

## Case C: integrated variables and fresh verification

**Prompt:** “Build a figure showing spatially resolved measurements across treatment and cell type. I want it to feel integrated, not like three unrelated charts.”

**Expected behaviour:**

- Identify the reader's primary question and which variables are the evidence, context, and comparison factors before choosing an encoding.
- Explore a meaningful spatial or mechanistic scaffold with complementary channels, and compare it against aligned panels or small multiples; do not force integration if it hides overlap or scale differences.
- Label mappings directly, preserve the source measurements and uncertainty, and keep explanatory schematic elements visibly distinct from measured data.
- Render and review the draft from multiple relevant angles. Name the most consequential remaining issue, refine it, and repeat as needed; do not stop solely because an automated benchmark or fixed checklist passes.
- If journal submission constraints are not yet known, use the skill's coherent defaults. Check target-journal technical artwork rules near submission rather than adopting its house appearance upfront.

**Failure signals:** forcing every variable into colour/shape/size; inventing a spatial or causal relationship; using one dense legend for many layers; treating a journal preset as the default visual identity; stopping after a single render without checking how the figure reads.

## Interpretation

A passing forward test does not prove that a future figure is scientifically correct. It checks that the skill asks the right questions, branches when the branch changes the evidence, keeps bundled values adjustable, and scales verification to the requested deliverable.
