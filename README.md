# Figure Craft

A personal visual craft system for scientific figures: composed, calm, quietly distinctive, and careful with meaning. Rose–Plum–Gold is the recognizable default signature, while the figure's question, evidence, medium, and audience decide the final form.

Figure Craft is organized as a light entrypoint, progressive references, editable templates, project assets, and focused checks. Its interaction model takes a cue from [p-to-q/via](https://github.com/p-to-q/via): define the job clearly at the start, keep the prompt light, let judgment choose the path, and load detail progressively. Figure Craft has a different output and does not require route maps.

> The original documentation and code are released under [Apache-2.0](LICENSE). Bundled research figures, renderers, and fonts may have separate source-specific conditions; see [NOTICE](NOTICE) before redistributing those assets.

## Architecture

Figure Craft has one light entrypoint and several progressively loaded layers:

- **Entrypoint:** [SKILL.md](SKILL.md) defines when the skill applies, its visual default, the operating shape, and the non-negotiable scientific boundaries.
- **References:** `references/` holds the detailed design language, composition patterns, palette logic, spacing evidence, QA limits, and the optional manifest. Load the smallest relevant subset.
- **Templates:** `templates/` contains editable examples and visual references. They are evidence about reusable decisions, not routes the model must follow.
- **Scripts:** `scripts/` provides deterministic rendering and diagnostics where the project uses Matplotlib. A script result is evidence about that check only.
- **Assets:** `assets/` contains fonts and other reusable project material whose licensing and glyph coverage still need verification.

The model decides what the figure means and which design direction is honest. The references make that decision more consistent; the scripts test selected properties; the final visual and scientific review remain separate.

## Package map

- `SKILL.md`: the compact always-on figure-making prompt, visual defaults, working attitude, and boundaries.
- `references/template-map.md`: how to choose and adapt the real RobotSoft/ICBR figure templates.
- `references/design-system.md`: Rose–Plum–Gold semantic roles, light/mid/deep variants, line conventions, and figure-set consistency.
- `references/composition-and-type.md`: composition choices including multivariable integration, shared alignment tracks, type roles, spacing, and text/line clearance.
- `references/qa-and-provenance.md`: source units, iterative refinement, automated checks, visual review, and paper-level consistency.
- `references/acceptance-scorecard.md`: task-scaled review aid for iterative refinement, not a numeric gate or stopping condition.
- `references/forward-tests.md`: lightweight semantic regression cases for routing, ambiguity handling, and adjustable defaults.
- `references/research-guides-and-open-source.md`: sourced practical tips, open-source project review, and guidance on what is venue-specific versus general.
- `references/figure-manifest-template.yaml`: optional project-level record for coordinated sets and handoffs.
- `references/palette-and-roles.md`: Rose–Plum–Gold role logic, colour harmony and accessibility checks, and light/mid/deep swatches.
- `references/layout-and-qa.md`: lower-level implementation details from the current renderers.
- `references/spacing-and-verification.md`: adjustable measured defaults and the repeated verification loop.
- `templates/robotsoft/`: formal RobotSoft paper figures, PNG/PDF references, and `render_compact_figures.py` source pattern.
- `templates/icbr/`: formal ICBR/research-craft figures, supplementary figures, graphical abstract, and renderer source patterns.
- `templates/template_multipanel.*`: a data-independent three-panel alignment smoke test.
- `assets/fonts/`: the project BentonSans regular/italic/bold and JuliaMono files used by the current figures.
- `scripts/figure_style.py`: portable millimetre canvas, palette roles, typography, glyph/bounds/collision checks, and saving helpers.
- `scripts/template_multipanel.py`: reproducible general multi-panel template test.
- `scripts/check_palette.py`: candidate colour, contrast, and colour-vision diagnostic.
- `scripts/palette_check.py`: historical ICBR v4 candidate diagnostic preserved for provenance.

## Use the templates

The formal images are optional visual references, not universal answers. When adapting one substantially, inspect its renderer and available source contract; replace data, labels, intervals, axes, and claims from the new evidence. Use graphical-abstract assets to study hierarchy and icon language, not to inherit unsupported scientific relationships. The smoke-test output defaults to `templates/template_multipanel.pdf` and `.png`, so it refreshes the bundled preview when run.

The bundled fonts allow the portable style smoke test to run without the research repository. The larger RobotSoft/ICBR renderers still expect their original analysis data paths and should be treated as source patterns unless those data are deliberately supplied in the new project.

## Minimal smoke test

With the project environment containing NumPy and Matplotlib (for example, install them into an isolated project environment with `python -m pip install numpy matplotlib`):

```sh
ROSE_FIGURE_FONT_DIRS="$PWD/assets/fonts" python scripts/template_multipanel.py templates/template_multipanel
python scripts/check_palette.py '#E27A9E' '#F2B1C7' '#6E5677' '#EDAF26'
```

The smoke test uses the bundled font directory, shared panel/title geometry, interval rows, a stimulus marker, and rendered-text checks. It is not a scientific result and does not replace final-size visual review.

## Provenance and contribution

The figure templates and style implementation originate in the author's research workflow and are included as visual references and source patterns. The README and reference design rules are the local package. External repository information is used as organizational inspiration only. See [CONTRIBUTING.md](CONTRIBUTING.md) for changes and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations.
