# Data

| File | What it is | Source and licence |
|---|---|---|
| `toothgrowth.csv` | 60 guinea pigs, 10 per group: odontoblast (tooth-forming cell) length `len`, supplement `supp` (OJ = orange juice, VC = ascorbic acid) and `dose` in mg a day (0.5, 1 or 2). | Crampton, E. W. (1947), "The growth of the odontoblasts of the incisor tooth as a criterion of the vitamin C intake of the guinea pig", Journal of Nutrition 33(5), 491–504. Exported unchanged from R's built-in `ToothGrowth` dataset (R datasets package, GPL-2 or GPL-3). Published experimental measurements on animals; no human data. |
| `expression_example.csv` | 30 genes (G01–G30) in 8 samples: `ctrl_1`–`ctrl_4` and `treat_1`–`treat_4`. Six genes rise with treatment and six fall; the rest are noise. | Synthetic, made for teaching. |
| `de_results_example.csv` | A differential expression results table for 3,000 genes: `baseMean`, `log2FoldChange`, `lfcSE`, `pvalue` and `padj` (Benjamini–Hochberg). | Synthetic, made for teaching. |

The expression and results tables are synthetic, made for teaching: they are not from any real experiment. They are released with the code under the MIT licence.
