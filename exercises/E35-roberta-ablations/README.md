<!-- BEGIN GENERATED CURRICULUM -->
# E35 — BERT and RoBERTa training ablations

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A36:K36) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Language  
**Suggested effort:** 3–5 h  
**Suggested stack:** PyTorch, pandas, Matplotlib; tokenizer optional

**Prerequisites:** [E16](../../exercises/E16-attention-matrix/), [E17](../../exercises/E17-pretraining-objectives/)

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P048:** [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
- **P085:** [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692)

## Work by hand

construct fixed and dynamically resampled masked-token examples; design a one-factor-at-a-time ablation table, including how to hold training tokens, updates and evaluation masks constant.

## Implement and investigate

extend the tiny masked LM from E17; compare fixed versus dynamic masks using the same architecture, corpus, optimizer, token budget and held-out evaluation. Use the same held-out mask set and several seeds; keep other recipe changes separate. Record the no-next-sentence-prediction choice. Label results as RoBERTa-inspired toy ablations, not a reproduction.

## Requested deliverables

notes.md; mask_examples.py; train_ablation.py; ablation_config.json; metrics.csv; heldout_loss.png.

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
