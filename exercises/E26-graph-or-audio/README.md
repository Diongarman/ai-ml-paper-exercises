# E26 — Graph or audio branch

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A27:K27) · [Repository guide](../../README.md)

**Stage:** Other modalities  
**Suggested effort:** 2–4 h  
**Suggested stack:** PyTorch Geometric (graph) or PyTorch (audio)

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P040:** [Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/abs/1609.02907)
- **P041:** [WaveNet: A Generative Model for Raw Audio](https://arxiv.org/abs/1609.03499)

## Work by hand

choose one branch: calculate one normalized neighbor aggregation (graph) or a dilated causal receptive field (audio).

## Implement and investigate

graph—GCNConv on Karate Club; audio—small causal Conv1d predictor. State which branch you chose.

## Requested deliverables

notes.md; graph_gcn.py + node_plot.png OR audio_causal.py + waveform_plot.png; short results.csv.

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
