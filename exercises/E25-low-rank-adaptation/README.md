<!-- BEGIN GENERATED CURRICULUM -->
# E25 — Low-rank update

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A26:K26) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Adaptation  
**Suggested effort:** 2–3 h  
**Suggested stack:** PyTorch, pandas, Matplotlib

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P060:** [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

## Work by hand

for W∈R^(d×k), derive full d·k parameters versus rank-r update r(d+k).

## Implement and investigate

freeze a PyTorch nn.Linear weight, train two low-rank factors, then compare with full fine-tuning on a small classification task.

## Requested deliverables

lora_notes.md; lora_layer.py; parameter_counts.csv; adaptation_curves.png.

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
