# E16 — Attention matrix by hand

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A17:K17) · [Repository guide](../../README.md)

**Stage:** Transformers  
**Suggested effort:** 2–3 h  
**Suggested stack:** NumPy, PyTorch

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P043:** [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- **P049:** [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
- **P048:** [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)

## Work by hand

compute all 3×3 QKᵀ/√d scores, softmax weights, weighted values, and a causal mask for three tokens.

## Implement and investigate

reproduce with NumPy, then check against PyTorch scaled_dot_product_attention; compare masked/unmasked outputs.

## Requested deliverables

notes.md (full matrix); attention_check.py; weights.csv; masked_vs_unmasked.png.

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
