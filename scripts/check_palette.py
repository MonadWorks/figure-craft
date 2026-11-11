#!/usr/bin/env python3
"""Print descriptive contrast and colour-vision diagnostics for supplied hex colours.

Usage:
  python check_palette.py '#E27A9E' '#F2B1C7' '#6E5677' --background '#FFFFFF'

Requires NumPy. Metrics are diagnostics, not universal pass/fail thresholds.
"""
import argparse
import numpy as np

MACHADO = {
    "protan": [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
    "deutan": [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
    "tritan": [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]],
}
WHITE = np.array([1.0, 1.0, 1.0])


def rgb(value):
    value = value.lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError("hex colours must use #RRGGBB")
    try:
        return np.array([int(value[i:i + 2], 16) for i in (0, 2, 4)]) / 255
    except ValueError as exc:
        raise argparse.ArgumentTypeError("invalid hexadecimal colour") from exc


def linear(c):
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def srgb(c):
    c = np.clip(c, 0, 1)
    return np.where(c <= 0.0031308, 12.92 * c, 1.055 * c ** (1 / 2.4) - 0.055)


def luminance(c):
    return float(linear(c) @ [0.2126, 0.7152, 0.0722])


def contrast(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def lab(c):
    xyz = np.array([[0.4124564, 0.3575761, 0.1804375],
                    [0.2126729, 0.7151522, 0.0721750],
                    [0.0193339, 0.1191920, 0.9503041]]) @ linear(c)
    xyz /= [0.95047, 1.0, 1.08883]
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.array([116 * f[1] - 16, 500 * (f[0] - f[1]), 200 * (f[1] - f[2])])


def simulate(c, kind):
    return srgb(np.asarray(MACHADO[kind]) @ linear(c))


def delta_e(a, b):
    return float(np.linalg.norm(lab(a) - lab(b)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("colours", nargs="+", help="one or more #RRGGBB colours")
    parser.add_argument("--background", default="#FFFFFF", help="background hex, default white")
    args = parser.parse_args()
    colours = [(value.upper(), rgb(value)) for value in args.colours]
    background = rgb(args.background)
    print("COLOUR       CONTRAST/BG  PAIRWISE dE76: normal / protan / deutan / tritan")
    for name, colour in colours:
        print(f"{name:12s} {contrast(colour, background):8.2f}:1")
    for i, (name_a, a) in enumerate(colours):
        for name_b, b in colours[i + 1:]:
            values = [delta_e(a, b)] + [delta_e(simulate(a, k), simulate(b, k)) for k in MACHADO]
            print(f"{name_a} vs {name_b}: " + " / ".join(f"{v:.1f}" for v in values))
    print("Descriptive diagnostics only; inspect the actual marks at final size and use redundant encodings.")


if __name__ == "__main__":
    main()
