<!-- BEGIN GENERATED CURRICULUM -->
# E33 — Word2Vec, ELMo and BERT in context

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A34:K34) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Language  
**Suggested effort:** 3–5 h  
**Suggested stack:** Python, NumPy, Matplotlib; Transformers for BERT; original ELMo/Word2Vec tools or documented cached vectors in separate environments

**Prerequisites:** [E14](../../exercises/E14-word-vectors/), [E15](../../exercises/E15-seq2seq-attention/), [E16](../../exercises/E16-attention-matrix/), [E17](../../exercises/E17-pretraining-objectives/)

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P029:** [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- **P017:** [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735)
- **P083:** [Deep Contextualized Word Representations](https://aclanthology.org/N18-1202/)
- **P048:** [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)

## Work by hand

choose sentences using bank in financial and river contexts; explain why a static lookup is unchanged and calculate a learned softmax-weighted mixture of three toy ELMo layers, including the scale parameter.

## Implement and investigate

extract genuine pretrained Word2Vec, ELMo and BERT token vectors for the same marked word in at least four sentences (or use a documented cached export of those vectors). Compute cosine similarities separately within each model; record exact model/checkpoint, source, layer/mix, token alignment and subword pooling. Plot within-model same-sense versus different-sense comparisons. Never compare raw vectors across models. An optional small bidirectional LSTM is an ELMo-inspired demonstration, not a substitute for the three-model comparison or a full ELMo reproduction.

## Requested deliverables

notes.md; sentences.jsonl; compare_context.py; vectors.npz or reproducible extraction instructions; provenance.json; within_model_similarities.csv; context_comparison.png.

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
