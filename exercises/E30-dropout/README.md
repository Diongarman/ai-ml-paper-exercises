<!-- BEGIN GENERATED CURRICULUM -->
# E30 — Dropout and overfitting

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A31:K31) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Neural foundations  
**Suggested effort:** 2–4 h  
**Suggested stack:** NumPy, PyTorch, scikit-learn, Matplotlib

**Prerequisites:** [E02](../../exercises/E02-backpropagation/)

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P010:** [Learning Representations by Back-Propagating Errors](https://doi.org/10.1038/323533a0)
- **P078:** [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://jmlr.org/papers/v15/srivastava14a.html)

## Work by hand

apply an inverted-dropout mask to a small activation vector and show why dividing retained activations by the keep probability preserves the expectation; state train/eval behavior.

## Implement and investigate

implement inverted dropout and compare it with PyTorch on fixed masks. Train a small MLP with and without dropout on the same fixed train/validation split, keeping model and budget constant; report multiple seeds and a case where dropout may not help.

## Requested deliverables

notes.md; dropout.py; train_mlp.py; metrics.csv; train_validation_curves.png; seed and split settings.

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
