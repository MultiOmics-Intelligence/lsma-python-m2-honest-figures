<a href="https://lsma.co.uk/courses"><img src="https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/lsma-walk-courses.svg" alt="LSMA, London School of Multiomics and AI: learn by doing, on real data" width="100%"></a>

# Module 2 project: Remake a figure

LSMA · Introduction to Python · Module 2 project

<p>
<img src="https://img.shields.io/badge/LSMA-free%20course-D9481F?style=flat-square" alt="LSMA free course">
<img src="https://img.shields.io/badge/course-Introduction%20to%20Python-0F1B33?style=flat-square" alt="Course">
<img src="https://img.shields.io/badge/language-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Language">
<img src="https://img.shields.io/badge/checks-automatic-2F7D5B?style=flat-square&logo=githubactions&logoColor=white" alt="Automatic checks">
</p>

## Research question

A colleague's draft figure has three panels. Can you rebuild the same three panels so that each one answers its question honestly?

**The draft.** Panel 1: 3D bars of mean tooth length for the six groups, rainbow colours, y-axis starting at 5, ± SE bars, no units. Panel 2: a volcano plot in red and green, with all 159 significant genes labelled. Panel 3: a heatmap of raw expression values in the rainbow palette. Saved as a 72 dpi JPEG screenshot.

## What you will build

| Files in (`data/`) | Files out (`results/`) |
|---|---|
| `toothgrowth.csv`, 60 guinea pigs, tooth length by vitamin C dose and source | `problems.md`, every problem in the draft and the lesson that fixes it |
| `de_results_example.csv`, a differential expression table of 3,000 genes | `panel_a_summary.csv`, n, mean and 95% CI for the six groups |
| `expression_example.csv`, 30 genes in 4 control and 4 treated samples | `volcano_counts.csv` and `labelled_genes.txt`, for panel B |
| | `heatmap_sample_order.txt`, the clustered sample order in panel C |
| | `figure.pdf` and `figure.png` (600 dpi), the finished three-panel figure |
| | `legend.md`, the figure legend, alt text and greyscale check |

Your code lives in one script, `scripts/remake_figure.py`, from loading the files to saving the final PDF.

## Before you start

1. Get your own copy. Use the GitHub Classroom invitation link in the project lesson on [lsma.co.uk](https://lsma.co.uk), or press **Use this template** on this page.
2. Clone your copy to your computer, or open it in GitHub Codespaces.
3. Install the packages once: `pip install pandas matplotlib seaborn scipy` (and `adjustText` if you want it).
4. Work in `scripts/`. Run everything from the top folder of your copy: `python scripts/remake_figure.py`.
5. Write every output to `results/`, with the exact file names above.

You can run the checks yourself at any time: `python tests/check_results.py`.

## Tasks

### 1. List the problems

Lesson to revisit: lessons 1–5.

In `results/problems.md`, write down every problem in the draft, one numbered line each, and the lesson that fixes it. Group them by panel.

**Checkpoint:** at least eight problems, including 3D, rainbow, truncated axis, SE bars without points, red–green, over-labelling, unscaled heatmap and the file format.

### 2. Panel A: the experiment

Lesson to revisit: lessons 1–3.

Tooth length by dose and source, every animal shown, with means and 95% confidence intervals, in Okabe–Ito colours. Save the numbers you drew as `results/panel_a_summary.csv` with the columns `supp`, `dose`, `n`, `mean`, `ci_low` and `ci_high`.

**Checkpoint:** six groups of 10 points; at 2 mg the two sources overlap almost completely.

### 3. Panel B: the volcano

Lesson to revisit: lessons 4 and 7.

Volcano plot of `de_results_example.csv` in blue and orange, with threshold lines, labelling only the five genes with the smallest adjusted p-values. Save the status counts as `results/volcano_counts.csv` (columns `status`, `count`) and the five labelled genes, one per line, as `results/labelled_genes.txt`.

**Checkpoint:** 76 up and 83 down; five labels that do not overlap.

### 4. Panel C: the heatmap

Lesson to revisit: lessons 4 and 7.

Clustered heatmap of `expression_example.csv`, z-scored by gene, diverging palette centred on zero, with a group colour bar. Write the clustered sample order, one name per line, to `results/heatmap_sample_order.txt`.

**Checkpoint:** samples split into control and treated; two blocks of six genes change in opposite directions.

### 5. Assemble and export

Lesson to revisit: lessons 6 and 8.

Combine the panels with letters A–C at 180 mm wide; save as `results/figure.pdf` and as `results/figure.png` at 600 dpi.

**Checkpoint:** the PNG is about 4,250 pixels wide (a little less from Python with `bbox_inches="tight"`, which trims the margins), and all text is still readable when the figure is printed at 180 mm.

### 6. Legend and alt text

Lesson to revisit: lesson 8.

Write the figure legend and two sentences of alt text in `results/legend.md`, under the headings **Figure legend**, **Alt text** and **Greyscale check**. Check the figure in greyscale and say what you saw.

**Checkpoint:** the legend explains every point, line, colour and error bar; the figure still reads in greyscale.

The automatic checks test your numbers and files, not how the figure looks. Judge the look yourself, at printed size.

## Hand in

Commit and push `scripts/` and `results/`. The **Checks** tab (GitHub Actions) then runs. A green tick means every checkpoint passed. You can push as often as you like.

## If a check fails

Open the failed run in the Actions tab and read the log. Each line starts with PASS or FAIL and names the task, for example `FAIL  Task 3 · Panel B: the volcano: ...`. The message tells you what to look at, not the answer. Fix that task, run your script again and push.

## Getting help

- The project lesson on lsma.co.uk, and the earlier lessons named in each task.
- Helix, the course tutor.
- Email info@lsma.co.uk.

Never post personal data in public, in an issue, a commit or a file.

**Follow LSMA**

<p>
  <a href="https://lsma.co.uk"><img src="https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/btn-lsma-website.svg" alt="LSMA: lsma.co.uk" height="54"></a>
  <a href="https://www.linkedin.com/showcase/113252126/"><img src="https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/btn-lsma-linkedin.svg" alt="LSMA on LinkedIn" height="54"></a>
  <a href="https://www.instagram.com/lsma.uk/"><img src="https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/btn-lsma-instagram.svg" alt="LSMA on Instagram: @lsma.uk" height="54"></a>
  <a href="mailto:info@lsma.co.uk"><img src="https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/btn-lsma-email.svg" alt="Email: info@lsma.co.uk" height="54"></a>
</p>

Good luck, and enjoy the project.

**Dr. Anas Alzaeem**<br>
Academic Director, LSMA

[![Dr. Anas Alzaeem, Academic Director, LSMA](https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/signature/LSMA_Banner_Anas_Alzaeem.png)](https://lsma.co.uk)

© 2026 MultiOmics Intelligence Ltd. LSMA is the education arm of MultiOmics Intelligence. Code licensed under MIT.
