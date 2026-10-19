"""Render the three line/plane configurations for study question LA-011."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon
import numpy as np


def project(x, y, z):
    return np.array([x + 0.45 * y, 0.55 * y + z])


plt.rcParams.update({"font.family": "Malgun Gothic", "axes.unicode_minus": False})
fig, axes = plt.subplots(1, 3, figsize=(12, 4.3), dpi=160)
fig.patch.set_facecolor("white")
blue, red = "#277FA1", "#CB443B"
fig.suptitle("파란 면: 평면 P     빨간 선: 직선 ℓ", fontsize=17, y=0.97)

corners = np.array([
    project(-1.1, -0.8, 0), project(1.1, -0.8, 0),
    project(1.1, 0.8, 0), project(-1.1, 0.8, 0),
])

for number, ax in enumerate(axes, start=1):
    ax.set_aspect("equal")
    ax.set_xlim(-1.85, 1.85)
    ax.set_ylim(-1.18, 1.46)
    ax.axis("off")
    ax.set_title(f"({number})", fontsize=21, fontweight="bold", pad=7)
    ax.add_patch(Polygon(corners, facecolor="#E2F1F7", edgecolor=blue,
                         linewidth=1.6, zorder=1))
    for y in [-0.4, 0, 0.4]:
        points = np.array([project(-1.1, y, 0), project(1.1, y, 0)])
        ax.plot(*points.T, color="#B7D7E3", linewidth=0.7, zorder=2)
    for x in [-0.55, 0, 0.55]:
        points = np.array([project(x, -0.8, 0), project(x, 0.8, 0)])
        ax.plot(*points.T, color="#B7D7E3", linewidth=0.7, zorder=2)
    ax.text(-1.36, -0.61, "$P$", color=blue, fontsize=18)


def double_arrow(ax, start, end, **kwargs):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="<->", mutation_scale=17,
                                linewidth=2.5, color=red, zorder=5, **kwargs))


# P is z=0. The displayed quadrilateral is a finite patch of the plane.
# Panel 1: (t, 0, 0).
double_arrow(axes[0], project(-1.64, 0, 0), project(1.64, 0, 0))
axes[0].text(1.48, 0.12, "$\ell$", color=red, fontsize=19)

# Panel 2: (t, 0, 0.95). A perpendicular guide indicates spatial separation.
double_arrow(axes[1], project(-1.64, 0, 0.95), project(1.64, 0, 0.95))
axes[1].text(1.48, 1.07, "$\ell$", color=red, fontsize=19)
foot, top = project(0.35, 0, 0), project(0.35, 0, 0.95)
axes[1].plot([foot[0], top[0]], [foot[1], top[1]], color="#7F8C91",
             linestyle=(0, (2, 3)), linewidth=1.2, zorder=3)
axes[1].plot([foot[0], foot[0] + 0.12, foot[0] + 0.12],
             [foot[1] + 0.12, foot[1] + 0.12, foot[1]],
             color="#7F8C91", linewidth=1, zorder=3)

# Panel 3: (0.4t, 0, t). Dashed line denotes the part below the plane.
origin, low, high = project(0, 0, 0), project(-0.4, 0, -1), project(0.5, 0, 1.25)
axes[2].add_patch(FancyArrowPatch(origin, low, arrowstyle="->", mutation_scale=17,
                                 linewidth=2.4, linestyle=(0, (4, 3)),
                                 color=red, zorder=4))
axes[2].add_patch(FancyArrowPatch(origin, high, arrowstyle="->", mutation_scale=17,
                                 linewidth=2.5, color=red, zorder=5))
axes[2].scatter([0], [0], s=28, color=red, zorder=6)
axes[2].text(high[0] + 0.13, high[1] - 0.12, "$\ell$", color=red, fontsize=19)

fig.text(0.5, 0.06, "색칠한 영역은 평면의 일부이며, 평면과 직선은 끝없이 이어집니다.",
         ha="center", fontsize=12, color="#4D5E67")
fig.subplots_adjust(left=0.025, right=0.975, top=0.79, bottom=0.15, wspace=0.10)

output = Path(__file__).with_name("LA-011.png")
fig.savefig(output, dpi=160, facecolor="white")
plt.close(fig)
print(f"Saved {output.name}.")
