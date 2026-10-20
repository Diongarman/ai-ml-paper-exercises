# E13 — Plan with learned dynamics

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A14:K14) · [Repository guide](../../README.md)

**Stage:** Reinforcement learning  
**Suggested effort:** 3–5 h  
**Suggested stack:** NumPy, PyTorch, Matplotlib

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P051:** [Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model](https://arxiv.org/abs/1911.08265)
- **P045:** [Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](https://arxiv.org/abs/1712.01815)

## Work by hand

compare one true grid transition with a model-predicted transition and sketch planning in latent state.

## Implement and investigate

collect trajectories, fit a tiny transition predictor, plan using it, and compare resulting paths with known-rule planning.

## Requested deliverables

notes.md (MuZero diagram and model errors); dynamics.py; transitions.csv; planning_comparison.png.

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
