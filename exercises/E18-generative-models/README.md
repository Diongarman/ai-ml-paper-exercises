# E18 — Three ways to make points

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A19:K19) · [Repository guide](../../README.md)

**Stage:** Generative models  
**Suggested effort:** 4–6 h  
**Suggested stack:** PyTorch, scikit-learn, Matplotlib

This is an unsolved starter workspace. The brief below was copied from the roadmap on 20 October 2026; use the linked spreadsheet for any later revisions and progress status.

## Related papers

- **P028:** [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114)
- **P031:** [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661)
- **P054:** [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)
- **P063:** [High-Resolution Image Synthesis with Latent Diffusion Models](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html)

## Work by hand

write the VAE reconstruction/KL terms, GAN min–max roles, and one diffusion denoising step.

## Implement and investigate

use small PyTorch MLPs on a 2D two-moons mixture; train VAE, GAN, and diffusion toy models with identical data and seeds.

## Requested deliverables

generative_notes.md; three training scripts/notebook sections; samples.png; training_curves.png; comparison table.

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
