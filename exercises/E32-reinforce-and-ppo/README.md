<!-- BEGIN GENERATED CURRICULUM -->
# E32 — From REINFORCE to PPO

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A33:K33) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Reinforcement learning  
**Suggested effort:** 3–5 h  
**Suggested stack:** PyTorch, NumPy, Matplotlib

**Prerequisites:** [E11](../../exercises/E11-gridworld/)

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P076:** [Simple statistical gradient-following algorithms for connectionist reinforcement learning](https://link.springer.com/article/10.1007/BF00992696)
- **P082:** [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
- **P066:** [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155)

## Work by hand

calculate a REINFORCE update for a categorical policy with an action-independent baseline; evaluate the PPO clipped surrogate for positive and negative advantages and several probability ratios.

## Implement and investigate

train REINFORCE on a tiny bandit, then implement and test PPO clipped loss on a fixed batch of actions, advantages and detached old log-probabilities. Plot clipping behavior and record sample/seed variability. A full on-policy PPO environment run is optional; this toy exercise does not reproduce RLHF.

## Requested deliverables

notes.md; reinforce_bandit.py; ppo_loss.py; bandit_rewards.csv; ppo_clipping.png; tests for both advantage signs.

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
