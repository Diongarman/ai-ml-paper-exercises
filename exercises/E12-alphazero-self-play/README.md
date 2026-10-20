# E12 — Mini AlphaZero self-play

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A13:K13) · [Repository guide](../../README.md)

**Stage:** Reinforcement learning  
**Suggested effort:** 4–6 h  
**Suggested stack:** Python, NumPy; PyTorch optional

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P039:** [Mastering the Game of Go with Deep Neural Networks and Tree Search](https://doi.org/10.1038/nature16961)
- **P046:** [Mastering the Game of Go Without Human Knowledge](https://doi.org/10.1038/nature24270)
- **P045:** [Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](https://arxiv.org/abs/1712.01815)

## Work by hand

draw a tic-tac-toe search tree, calculate PUCT/UCB terms for one node, and normalize visit counts.

## Implement and investigate

implement rules, MCTS and self-play; use a tabular value/policy estimate first. Optional: replace it with a tiny PyTorch network.

## Requested deliverables

notes.md (one search); tictactoe_mcts.py; visit_targets.csv; win_draw_curves.png; optional network.py.

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
