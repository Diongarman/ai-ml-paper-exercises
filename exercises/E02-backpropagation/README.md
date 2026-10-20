# E02 — Backprop by hand

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A3:K3) · [Repository guide](../../README.md)

**Stage:** Neural foundations  
**Suggested effort:** 2–3 h  
**Suggested stack:** NumPy, PyTorch, Matplotlib

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P010:** [Learning Representations by Back-Propagating Errors](https://doi.org/10.1038/323533a0)
- **P012:** [Approximation by Superpositions of a Sigmoidal Function](https://doi.org/10.1007/BF02551274)
- **P030:** [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)

## Work by hand

for XOR input (0,1)→1, use two hidden units, tanh activations, sigmoid output and binary cross-entropy to compute forward pass, gradients and one SGD update.

## Implement and investigate

train all four rows with manual NumPy backprop; repeat in PyTorch autograd and compare one gradient.

## Requested deliverables

notes.md or photographed workings; xor_numpy.py; xor_torch.py; loss_curve.png; four final predictions.

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
