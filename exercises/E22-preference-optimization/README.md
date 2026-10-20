# E22 — Preference pairs and DPO

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A23:K23) · [Repository guide](../../README.md)

**Stage:** Alignment  
**Suggested effort:** 2–3 h  
**Suggested stack:** PyTorch, pandas, Matplotlib

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P066:** [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155)
- **P067:** [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)

## Work by hand

label five preference pairs; calculate one DPO log-sigmoid loss term from supplied policy/reference log-probabilities.

## Implement and investigate

implement that loss in PyTorch tensors and vary the preference strength β; do not fine-tune a large LLM here.

## Requested deliverables

preferences.csv; notes.md (worked loss); dpo_loss.py; beta_curve.png; reward-model versus DPO diagram.

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
