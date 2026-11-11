[English](README.md) | [简体中文](README.zh-CN.md)

# Six-page RoboSoft manuscript

Read [main.pdf](main.pdf): **Predictive Risk and Recording Decisions in Partially Observed Neural Networks for Soft Actuation**. This is the current anonymous author-review version. Its seven pages contain the complete main argument, figures, tables and references. Essential evidence is in the paper.

The paper follows the original neural study through endpoint allocation, response ambiguity and finite-response factors, recurrent information and fifth-site selection, and structural robustness. A fresh Cosserat-arm study tests downstream motion prediction. The original uncertain criterion comparisons and fifth-site response results remain explicit. [The original neural manuscript](../../01_READ_CURRENT/paper_current.pdf), its full methods, and its supplementary analyses remain available as research records.

The official `ieeeconf.cls` uses US Letter, 10 pt and two columns. Figures retain the original BentonSans/JuliaMono typography and light pink, gold, and purple-grey palette. Panels are recomposed from frozen network-level data; the structural-robustness figure is copied exactly. The fifth-site strip includes all 80 networks, with axis limits covering every observation. Captions and comparison status are maintained in `figure1.tex` through `figure5.tex`.

## Build and inspect

With Python 3, a LaTeX installation providing `pdflatex`, `bibtex` `ieeetr.bst` and `flushend`, and Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`), run in this directory:

```sh
python3 build.py --render
```

This writes `main.pdf`, checks the page count (6--8 allowed), Letter dimensions, empty author metadata, citations, source hashes, and overflow, and renders previews to ignored `tmp/pdfs/`. `build_validation.json` identifies the checked PDF. Edit `main.tex`, figure captions, and `references.bib`; rebuild and inspect all pages after edits.

To regenerate figures, use the numerical Python environment in the [experiment instructions](../机器人实验/README.md), with Matplotlib and fontTools available:

```sh
python build.py --figures --render
```

`render_compact_figures.py` reads the retained neural summaries and imports the original `figure_style.py`; `plot_arm.py` reads the saved mechanical errors and the first prespecified trajectory. Source hashes and figure checks are in `figures/compact_source_data.json` and `figures/arm_source_data.json`. Keep the repository directory structure. Rendering changes presentation only; simulations and statistical intervals remain frozen. After running the historical mechanical analysis script, run this figure build to restore the current style.

[soft_arm_demo.mp4](soft_arm_demo.mp4) is the 44.5-second, 1080p simulation video (20 fps, approximately 1.27 MB). It introduces the recording policies, shows the Fig. 5 validation example with synchronized centerlines, projected tip paths and errors, and ends with the 40-network results. The motion plays at 0.05× physical speed from saved states; enlarged transverse axes are labeled. The video retains the manuscript palette and is anonymous.

[![Simulation video preview](soft_arm_demo.png)](soft_arm_demo.mp4)

Using the numerical Python environment and `ffmpeg`/`ffprobe`, run `python ../机器人实验/make_video.py` to regenerate the video and preview. Add `--preview-only` to inspect frames in ignored `tmp/video/previews/`, or `--output-dir /path/to/export` for a separate export. [video_validation.json](video_validation.json) records source hashes, statistics, encoding checks, and visual-review status. Authorship and final submission arrangements remain with the authors.
