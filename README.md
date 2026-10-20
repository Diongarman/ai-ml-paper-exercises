# AI and ML papers — exercises

Implementations, worked mathematics, and small experiments that accompany the [reading roadmap and exercises spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit).

## Use the spreadsheet and repository together

- **Spreadsheet:** reading order, paper links, tracks, priorities, reading dates, exercise status, and short reminders.
- **Repository:** detailed explanations, hand calculations, code or notebooks, figures, and small result files.
- Open the **Work link** in the spreadsheet's Exercises tab to reach the matching folder. Keep progress status in the spreadsheet.

The folders below are starter workspaces. The exercises have not been solved. Each README contains the initial brief from the spreadsheet, captured on 20 October 2026, and links to its source row and related papers. The live spreadsheet remains the source for planning and any revised briefs; these files do not sync automatically.

## Start with E01

1. Open [E01: Logic gates and XOR](exercises/E01-perceptron/README.md).
2. Work through the hand calculation and sketch, then implement the perceptron yourself.
3. Record your explanation in the folder's notes.md, or link to handwritten notes in Drive.
4. Save the small outputs requested in the brief and document the commands that produced them.
5. Commit your work and update the exercise status in the spreadsheet.

## Local setup

Clone this repository with GitHub Desktop or the clone URL shown by GitHub's **Code** menu. Open the cloned folder in your editor.

For the first exercise, create a Python virtual environment and install the small starter dependency set:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The activation command above is for macOS/Linux. Python 3.11 or later is a reasonable starting point; check package requirements when adding later stacks.

requirements.txt contains only NumPy and Matplotlib for E01. Add and record additional dependencies when you reach an exercise that needs them. Once an exercise runs, record the Python/package versions, random seed, dataset source/split, and exact commands in its README. You can keep an exercise-specific requirements.txt where versions or optional stacks differ.

## Folder conventions

Each exercise begins with README.md (brief and execution record) and notes.md (working space). Add implementations and outputs as you work; there are no placeholder solutions or claimed results.

- Put source files or notebooks beside the README, using the filenames requested by the brief where practical.
- Save small CSV/JSON outputs in results/ and figures in figures/; these are tracked by Git.
- Keep downloaded datasets in data/ and model weights in checkpoints/; both are ignored. Document how to obtain them.
- Keep handwritten derivations in your preferred app or Drive and link to them from notes.md.
- Label toy demonstrations and simplified implementations clearly, especially when they do not reproduce the original paper's scale or claims.

## Exercise index

| Exercise | Focus | Stage | Suggested effort |
| --- | --- | --- | --- |
| [E01](exercises/E01-perceptron/) | Logic gates and XOR | Neural foundations | 1–2 h |
| [E02](exercises/E02-backpropagation/) | Backprop by hand | Neural foundations | 2–3 h |
| [E03](exercises/E03-handwritten-digits/) | Recognize handwritten digits | Computer vision | 3–5 h |
| [E04](exercises/E04-tabular-models/) | Tabular model comparison | Classical ML | 3–4 h |
| [E05](exercises/E05-expectation-maximization/) | EM with hidden labels | Classical ML | 2–3 h |
| [E06](exercises/E06-image-benchmark/) | Inspect the image benchmark | Computer vision | 1–2 h |
| [E07](exercises/E07-cnn-shapes/) | Trace a CNN | Computer vision | 2–3 h |
| [E08](exercises/E08-boxes-and-masks/) | Boxes versus masks | Computer vision | 2–3 h |
| [E09](exercises/E09-astar-search/) | A* search | Search & probability | 2–3 h |
| [E10](exercises/E10-belief-networks/) | Belief-network inference | Search & probability | 1–2 h |
| [E11](exercises/E11-gridworld/) | Learn a gridworld policy | Reinforcement learning | 3–5 h |
| [E12](exercises/E12-alphazero-self-play/) | Mini AlphaZero self-play | Reinforcement learning | 4–6 h |
| [E13](exercises/E13-learned-dynamics/) | Plan with learned dynamics | Reinforcement learning | 3–5 h |
| [E14](exercises/E14-word-vectors/) | Inspect word vectors | Language | 2–3 h |
| [E15](exercises/E15-seq2seq-attention/) | Translation and alignment | Sequence models | 2–3 h |
| [E16](exercises/E16-attention-matrix/) | Attention matrix by hand | Transformers | 2–3 h |
| [E17](exercises/E17-pretraining-objectives/) | Compare pretraining objectives | Language | 2–4 h |
| [E18](exercises/E18-generative-models/) | Three ways to make points | Generative models | 4–6 h |
| [E19](exercises/E19-self-supervised-vision/) | Learn without labels | Computer vision | 3–5 h |
| [E20](exercises/E20-image-text-alignment/) | Images and text in one space | Multimodal | 2–3 h |
| [E21](exercises/E21-scaling-laws/) | Compute budget trade-off | Scaling | 2–3 h |
| [E22](exercises/E22-preference-optimization/) | Preference pairs and DPO | Alignment | 2–3 h |
| [E23](exercises/E23-reasoning-verifiers/) | Verifier-backed reasoning | Modern reasoning | 2–4 h |
| [E24](exercises/E24-retrieval/) | Retrieve before answering | Language | 2–3 h |
| [E25](exercises/E25-low-rank-adaptation/) | Low-rank update | Adaptation | 2–3 h |
| [E26](exercises/E26-graph-or-audio/) | Graph or audio branch | Other modalities | 2–4 h |
| [E27](exercises/E27-protein-structures/) | Read protein-model outputs | Scientific AI | 1–2 h |
| [E28](exercises/E28-abstention/) | When to abstain | AI evaluation | 1–2 h |

## Finishing an exercise

Use the deliverables in its README as the checklist. Include an explanation in your own words, the requested worked calculation, code that runs from documented commands, small saved results/figures, and at least one observation about errors or limitations. Record the seed and environment so you can reproduce the work later. Mark the status in the spreadsheet when you are satisfied with the evidence.
