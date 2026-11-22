"""Module 2 project: remake a figure.

Run from the top folder of your copy:   python scripts/remake_figure.py
Build the whole figure in this one script, from loading the files to saving
the final PDF and PNG. If anything changes, rerun it from the top.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

# Shared choices, set once (colour dictionaries, font size, width in mm).
MM = 1 / 25.4
okabe = {"Orange juice": "#E69F00", "Ascorbic acid": "#56B4E9"}
# TODO: add a colour dictionary for Up / Down / Not significant (blue and orange)
# TODO: set a default font size, e.g. plt.rcParams["font.size"] = 7

# ---------------------------------------------------------------------------
# Task 1 · List the problems (lessons 1-5)
# ---------------------------------------------------------------------------
# TODO: write results/problems.md: every problem in the draft, one numbered
#       line each, with the lesson that fixes it. Group them by panel.

# ---------------------------------------------------------------------------
# Figure layout (you will finish it in Task 5)
# ---------------------------------------------------------------------------
# TODO: make one figure 180 mm wide with three panels (axA, axB, axC).
#       Consider giving the heatmap more room than the other two.

# ---------------------------------------------------------------------------
# Task 2 · Panel A: the experiment (lessons 1-3)
# ---------------------------------------------------------------------------
tg = pd.read_csv(DATA / "toothgrowth.csv")
# TODO: every animal as a point, by dose and source, in Okabe-Ito colours.
# TODO: compute n, mean and 95% confidence interval for each of the six groups,
#       draw them on top of the points, and save results/panel_a_summary.csv
#       with columns supp, dose, n, mean, ci_low, ci_high.

# ---------------------------------------------------------------------------
# Task 3 · Panel B: the volcano (lessons 4 and 7)
# ---------------------------------------------------------------------------
de = pd.read_csv(DATA / "de_results_example.csv")
# TODO: status column (Up / Down / Not significant), blue and orange points,
#       threshold lines at log2 fold change -1 and 1 and at padj 0.05.
# TODO: save the status counts as results/volcano_counts.csv (columns status, count).
# TODO: label only the five genes with the smallest padj, and write their
#       names, one per line, to results/labelled_genes.txt.

# ---------------------------------------------------------------------------
# Task 4 · Panel C: the heatmap (lessons 4 and 7)
# ---------------------------------------------------------------------------
expr = pd.read_csv(DATA / "expression_example.csv", index_col="gene")
# TODO: z-score each gene; get the clustered order from sns.clustermap,
#       close that figure, and draw the reordered table into axC with
#       sns.heatmap (diverging palette centred on 0) and a group colour bar.
# TODO: write the clustered sample order, one name per line, to
#       results/heatmap_sample_order.txt.

# ---------------------------------------------------------------------------
# Task 5 · Assemble and export (lessons 6 and 8)
# ---------------------------------------------------------------------------
# TODO: panel letters A-C with transform=ax.transAxes.
# TODO: save results/figure.pdf and results/figure.png (dpi=600).

# ---------------------------------------------------------------------------
# Task 6 · Legend and alt text (lesson 8)
# ---------------------------------------------------------------------------
# TODO: write results/legend.md with the headings "Figure legend", "Alt text"
#       and "Greyscale check".
