<!-- BEGIN GENERATED CURRICULUM -->
# E29 — Negative sampling versus co-occurrence

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A30:K30) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Language  
**Suggested effort:** 3–5 h  
**Suggested stack:** NumPy or PyTorch, pandas, Matplotlib

**Prerequisites:** [E14](../../exercises/E14-word-vectors/)

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P029:** [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- **P077:** [Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/abs/1310.4546)
- **P079:** [GloVe: Global Vectors for Word Representation](https://aclanthology.org/D14-1162/)

## Work by hand

calculate one positive/negative skip-gram loss and one weighted GloVe residual from a tiny co-occurrence table; distinguish the two objectives.

## Implement and investigate

build a small corpus and co-occurrence counts; train tiny skip-gram with negative sampling and GloVe objectives using NumPy or PyTorch. Inspect nearest neighbors within each model and record vocabulary, window, seeds and data limits; do not compare coordinates across independently trained spaces.

## Requested deliverables

notes.md; corpus.txt; word_objectives.py; neighbors.csv; loss_curves.png; model/data settings.

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
