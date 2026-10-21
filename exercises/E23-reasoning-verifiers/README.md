<!-- BEGIN GENERATED CURRICULUM -->
# E23 — Verifier-backed reasoning

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A24:K24) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Modern reasoning  
**Suggested effort:** 2–4 h  
**Suggested stack:** Python, pandas; local LLM optional

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P062:** [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
- **P064:** [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- **P073:** [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- **P075:** [Evaluating Large Language Models for Accuracy Incentivizes Hallucinations](https://www.nature.com/articles/s41586-026-10549-w)

## Work by hand

define an exact arithmetic verifier and grade two candidate reasoning traces; note what answer-only grading misses.

## Implement and investigate

generate 20 small tasks, run supplied or local-model responses through a Python verifier, compare prompt formats and record failure types.

## Requested deliverables

tasks.jsonl; verifier.py; eval_results.csv; notes.md with examples and limits of this toy study.

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
