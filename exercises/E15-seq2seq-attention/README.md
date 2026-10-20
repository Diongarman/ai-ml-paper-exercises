# E15 — Translation and alignment

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A16:K16) · [Repository guide](../../README.md)

**Stage:** Sequence models  
**Suggested effort:** 2–3 h  
**Suggested stack:** PyTorch, NumPy, Matplotlib

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P017:** [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735)
- **P033:** [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215)
- **P032:** [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)

## Work by hand

write encoder/decoder tensor shapes and calculate one attention-weighted context vector.

## Implement and investigate

make a tiny sequence copy or word-translation task with nn.LSTM encoder/decoder and additive attention; save a token alignment heatmap.

## Requested deliverables

seq2seq_attention.py; notes.md (worked context); alignment.png; five input/output examples.

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
