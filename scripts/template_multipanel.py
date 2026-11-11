#!/usr/bin/env python3
"""Render a small, data-independent Rose Figure multi-panel template.

This is a layout/style smoke test, not a scientific example. It verifies that the
portable style, bundled fonts, shared panel/title tracks, common numeric anchors,
and rendered-text checks work without a project's analysis data.
"""
from pathlib import Path
import sys

import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import figure_style as fs


def main(output=None):
    fs.setup()
    canvas = fs.Canvas(88)
    for x, letter, title in [(4, 'a', 'Paired observations'), (64, 'b', 'Effect and interval'), (124, 'c', 'Structure and stimulus')]:
        canvas.header(x, 84, letter, title)

    # Shared x track and y track make the template transferable across three panels.
    ax = canvas.ax(11, 25, 42, 49)
    x = np.arange(1, 7)
    y = np.array([0.82, 0.91, 0.77, 1.03, 0.96, 1.08])
    ax.plot(x, y, color=fs.MUTED, lw=.7, zorder=1)
    ax.scatter(x, y, s=20, c=fs.ROSE, edgecolors=fs.ROSE_LINE, linewidths=.55, zorder=2)
    ax.axhline(1, color=fs.MUTED, lw=.55, ls=(0, (2, 2)))
    ax.set(xlim=(.5, 6.5), ylim=(.65, 1.18), xlabel='Matched unit', ylabel='Observed result')
    ax.xaxis.labelpad = 2
    ax.yaxis.labelpad = 2
    fs.clean(ax)

    ax = canvas.ax(69, 25, 43, 49)
    effects = np.array([-.42, -.18, .08, .21])
    lo = effects - np.array([.13, .11, .16, .12])
    hi = effects + np.array([.14, .12, .15, .13])
    for i, (est, low, high) in enumerate(zip(effects, lo, hi)):
        fs.interval(ax, i, est, low, high, fs.ROSE if i < 2 else fs.PLUM, filled=i == 0)
    ax.axvline(0, color=fs.MUTED, lw=.55, ls=(0, (2, 2)))
    ax.set(xlim=(-.7, .6), ylim=(3.5, -.7), xlabel='Difference', yticks=range(4), yticklabels=['A', 'B', 'C', 'D'])
    fs.clean(ax)

    ax = canvas.ax(130, 25, 41, 49)
    xx = np.linspace(0, 1, 10)
    ax.plot(xx, .2 + .6 * xx, color=fs.PLUM, lw=1.0, label='structure')
    ax.scatter([.08], [.25], s=32, facecolor=fs.GOLD, edgecolor=fs.GOLD_DARK, linewidth=.7, zorder=3, label='stimulus')
    ax.scatter([.9], [.74], s=32, facecolor=fs.ROSE, edgecolor=fs.ROSE_LINE, linewidth=.7, zorder=3, label='readout')
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel='Normalised position', ylabel='Role')
    fs.clean(ax)
    ax.legend(loc='lower right', fontsize=5.5, handlelength=1.2, borderaxespad=.2)

    output = Path(output or (HERE.parent / 'templates' / 'template_multipanel.png'))
    output.parent.mkdir(parents=True, exist_ok=True)
    fs.check_text(canvas.fig, canvas.manual)
    canvas.fig.savefig(output.with_suffix('.pdf'), metadata={'CreationDate': None, 'ModDate': None})
    canvas.fig.savefig(output.with_suffix('.png'), dpi=300)
    plt.close(canvas.fig)
    print(f'wrote {output.with_suffix(".pdf")} and {output.with_suffix(".png")}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
