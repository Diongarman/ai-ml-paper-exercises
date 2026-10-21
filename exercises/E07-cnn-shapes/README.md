<!-- BEGIN GENERATED CURRICULUM -->
# E07 — Trace a CNN

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A8:K8) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Computer vision  
**Suggested effort:** 2–3 h  
**Suggested stack:** PyTorch, torchvision, Matplotlib

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P018:** [Gradient-Based Learning Applied to Document Recognition](https://proceedingsoftheieee.ieee.org/gradient-based-learning-applied-to-document-recognition/)
- **P027:** [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html)
- **P034:** [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556)
- **P035:** [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)

## Work by hand

trace tensor shapes and receptive fields for a small CNN; calculate one residual block's skip addition.

## Implement and investigate

implement a compact LeNet-style model in PyTorch and use hooks or a forward pass to check shapes; compare paper architectures in notes.

## Requested deliverables

architecture_notes.md; cnn_shapes.py; layer_shapes.csv; one feature-map figure.

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
