<!-- BEGIN GENERATED CURRICULUM -->
# E08 — Boxes versus masks

[Exercise row in the spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit#gid=1325933506&range=A9:K9) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** Computer vision  
**Suggested effort:** 2–3 h  
**Suggested stack:** torchvision, PyTorch, Pillow; SAM optional

This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: 2026-10-21.

## Related papers

- **P021:** [Rapid Object Detection Using a Boosted Cascade of Simple Features](https://doi.org/10.1109/CVPR.2001.990517)
- **P036:** [Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/abs/1506.01497)
- **P038:** [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597)
- **P044:** [Mask R-CNN](https://openaccess.thecvf.com/content_iccv_2017/html/He_Mask_R-CNN_ICCV_2017_paper.html)
- **P069:** [Segment Anything](https://arxiv.org/abs/2304.02643)

## Work by hand

calculate box IoU and mask IoU for one annotated example; explain semantic versus instance segmentation.

## Implement and investigate

annotate five images; run pretrained torchvision Mask R-CNN (SAM optional); compare predicted boxes/masks to your annotations.

## Requested deliverables

annotations/; detect_segment.py; five overlay images; iou.csv; notes.md comparing U-Net, Faster R-CNN, Mask R-CNN, SAM.

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
