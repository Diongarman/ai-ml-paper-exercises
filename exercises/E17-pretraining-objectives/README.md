<!-- BEGIN GENERATED CURRICULUM -->
# E17 — Compare pretraining objectives

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A18:K18) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Language  
**Suggested effort:** 2–4 h  
**Suggested stack:** PyTorch, Python; Hugging Face tokenizers optional

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P049:** [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
- **P048:** [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
- **P050:** [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)

## Work by hand

turn one short sentence into next-token, masked-token, and text-to-text training examples; list visible context for each.

## Implement and investigate

write dataset builders; train tiny PyTorch next-token and masked-token baselines on the same toy corpus (T5 objective as examples only).

## Requested deliverables

objectives.md; make_examples.py; examples.jsonl; train_small.py; loss_curves.png.

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
