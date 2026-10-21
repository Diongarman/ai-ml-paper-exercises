<!-- BEGIN GENERATED CURRICULUM -->
# E31 — Batch versus layer normalization

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A32:K32) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Neural foundations  
**Suggested effort:** 2–4 h  
**Suggested stack:** NumPy, PyTorch, pandas

**Prerequisites:** [E02](../../exercises/E02-backpropagation/)

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P080:** [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167)
- **P081:** [Layer Normalization](https://arxiv.org/abs/1607.06450)
- **P035:** [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
- **P043:** [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

## Work by hand

for a small batch-by-feature matrix, mark the axes and calculate BatchNorm and LayerNorm means, variances and affine outputs; use biased variance for the normalization calculation.

## Implement and investigate

implement both normalizations in NumPy and compare with PyTorch BatchNorm1d and LayerNorm. Show BatchNorm train/eval and running-statistic behavior, including its running-variance convention; vary the other examples in a batch and test which outputs change. Keep epsilon, affine parameters and axes explicit.

## Requested deliverables

notes.md; normalization.py; normalization_checks.csv; batch_composition.csv; train_eval_comparison.md.

Use [notes.md](notes.md) for explanations and worked mathematics. Save small results in results/ and plots in figures/, or keep the brief's filenames beside your script. Link to handwritten workings if you prefer writing them elsewhere.
<!-- END GENERATED CURRICULUM -->

## How to run

Add the exact commands after you create an implementation. No runnable implementation has been added yet.

- Python version:
- Dependencies and installed versions:
- Dataset/source and split, if relevant:
- Random seed:
- Command or notebook execution steps:

## Results and limitations

Record the observed outputs, comparison with your hand calculation or baseline, and the limits of what the experiment demonstrates. Link to the saved figures/results.
