<!-- BEGIN GENERATED CURRICULUM -->
# E19 — Learn without labels

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A20:K20) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Computer vision  
**Suggested effort:** 3–5 h  
**Suggested stack:** PyTorch, torchvision, scikit-learn

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P052:** [A Simple Framework for Contrastive Learning of Visual Representations](https://proceedings.mlr.press/v119/chen20j.html)
- **P061:** [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377)
- **P053:** [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)

## Work by hand

calculate a small contrastive loss with one positive and two negatives; sketch patch masking.

## Implement and investigate

train a compact image encoder with two augmentations per image; freeze it and fit a linear probe. Compare to a random encoder; discuss MAE separately.

## Requested deliverables

self_supervised_notes.md; augmentations.png; encoder.py; probe_results.csv; neighbor_grid.png.

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
