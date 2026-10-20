# E20 — Images and text in one space

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A21:K21) · [Repository guide](../../README.md)

**Stage:** Multimodal  
**Suggested effort:** 2–3 h  
**Suggested stack:** Hugging Face Transformers, PyTorch, Pillow

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P059:** [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- **P053:** [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)

## Work by hand

compute cosine similarity for one image/text vector pair and explain zero-shot ranking.

## Implement and investigate

run pretrained CLIP on a small labeled image folder and candidate captions; store score matrix and inspect two mistakes.

## Requested deliverables

clip_retrieval.py; similarity.csv; ranked_examples.png; notes.md with failure analysis.

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
