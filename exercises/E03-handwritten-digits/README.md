# E03 — Recognize handwritten digits

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A4:K4) · [Repository guide](../../README.md)

**Stage:** Computer vision  
**Suggested effort:** 3–5 h  
**Suggested stack:** PyTorch, torchvision, scikit-learn, pandas

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P013:** [Backpropagation Applied to Handwritten Zip Code Recognition](https://doi.org/10.1162/neco.1989.1.4.541)
- **P014:** [Handwritten Digit Recognition with a Back-Propagation Network](https://papers.nips.cc/paper_files/paper/1989/hash/53c3bce66e43be4f209556518c2fcb54-Abstract.html)
- **P018:** [Gradient-Based Learning Applied to Document Recognition](https://proceedingsoftheieee.ieee.org/gradient-based-learning-applied-to-document-recognition/)

## Work by hand

calculate one 3×3 convolution output, output shapes, and CNN versus MLP parameter counts.

## Implement and investigate

load MNIST with torchvision; train MLP and small LeNet-style nn.Module with DataLoader; evaluate held-out digits.

## Requested deliverables

digit_models.py; results.csv; two confusion matrices; 12 error images; notes.md on weight sharing and errors.

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
