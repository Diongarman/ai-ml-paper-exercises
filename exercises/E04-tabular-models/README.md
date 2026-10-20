# E04 — Tabular model comparison

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A5:K5) · [Repository guide](../../README.md)

**Stage:** Classical ML  
**Suggested effort:** 3–4 h  
**Suggested stack:** pandas, scikit-learn, XGBoost (optional)

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P009:** [Induction of Decision Trees](https://doi.org/10.1007/BF00116251)
- **P016:** [Support-Vector Networks](https://doi.org/10.1007/BF00994018)
- **P020:** [Random Forests](https://doi.org/10.1023/A:1010933404324)
- **P019:** [Greedy Function Approximation: A Gradient Boosting Machine](https://doi.org/10.1214/aos/1013203451)
- **P042:** [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754)

## Work by hand

calculate one decision-tree split's impurity reduction and sketch a 2D SVM margin.

## Implement and investigate

use one fixed train/test split and scikit-learn Pipelines for tree, SVM, forest, boosting; add XGBoost if installed; tune on training data only.

## Requested deliverables

tabular_benchmark.py; metrics.csv; comparison plot; notes.md explaining leakage control and two error cases.

Use [notes.md](notes.md) for explanations and worked mathematics. Save small results in results/ and plots in figures/, or keep the brief's filenames beside your script. Link to handwritten workings if you prefer writing them elsewhere.

## How to run

Add the exact commands after you create an implementation. No runnable implementation has been added yet.

- Python version:
- Dependencies and installed versions:
- Dataset/source and split, if relevant:
- Random seed:
- Command or notebook execution steps:

## Results and limitations

Record the observed outputs, comparison with your hand calculation or baseline, and the limits of what the experiment demonstrates. Link to the saved figures/results.
