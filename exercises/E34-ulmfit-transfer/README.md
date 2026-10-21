<!-- BEGIN GENERATED CURRICULUM -->
# E34 — Recurrent language-model transfer

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A35:K35) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Adaptation  
**Suggested effort:** 4–6 h  
**Suggested stack:** PyTorch, pandas, Matplotlib

**Prerequisites:** [E15](../../exercises/E15-seq2seq-attention/), [E17](../../exercises/E17-pretraining-objectives/)

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P017:** [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735)
- **P084:** [Universal Language Model Fine-tuning for Text Classification](https://aclanthology.org/P18-1031/)

## Work by hand

sketch language-model pretraining, target-domain adaptation and classifier fine-tuning; assign discriminative learning rates and a gradual-unfreezing schedule for a small recurrent classifier.

## Implement and investigate

pretrain a tiny LSTM next-token model on a small corpus, adapt it to unlabeled training-domain text, then compare a frozen encoder, gradual unfreezing and a classifier trained from scratch on fixed labeled splits. Keep validation/test text out of language-model fitting and report multiple seeds, data sizes and learning rates. Label this ULMFiT-inspired; it does not reproduce the full AWD-LSTM recipe.

## Requested deliverables

notes.md; train_language_model.py; finetune_classifier.py; splits.json; transfer_metrics.csv; learning_curves.png.

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
