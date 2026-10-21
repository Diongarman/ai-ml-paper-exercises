# AI and ML paper reading roadmap

**85 papers · 35 exercises · 8 tracks · 42 broad steps.** Curriculum version: 2026-10-21.

[Live spreadsheet](https://docs.google.com/spreadsheets/d/1_eHEWFzFJ7ncNSaKj2OCUYB6H8rWtdbSnBG4BsRaE2I/edit) · [Exercise workspaces](README.md#exercise-index) · [Shared curriculum data](roadmap.json)

The broad sequence groups learning dependencies and topics, rather than sorting every paper by publication date. IDs stay fixed; follow the displayed order. Read all papers and prerequisites linked to an exercise before attempting it. Attention Is All You Need introduces the Transformer architecture used by BERT; ELMo uses bidirectional LSTMs.

The Papers tab retains stable ID order, so P076–P085 are appended there. The broad sequence and deeper paths below show their learning order. Years use the cited publication year for proceedings/journals, or first preprint year for arXiv papers.

## Broad sequence

| Step | Paper | Year | Exercises |
| --- | --- | --- | --- |
| 1 | **P001** [A Logical Calculus of the Ideas Immanent in Nervous Activity](https://doi.org/10.1007/BF02478259) | 1943 | [E01](exercises/E01-perceptron/) |
| 2 | **P003** [The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain](https://doi.org/10.1037/h0042519) | 1958 | [E01](exercises/E01-perceptron/) |
| 3 | **P010** [Learning Representations by Back-Propagating Errors](https://doi.org/10.1038/323533a0) | 1986 | [E02](exercises/E02-backpropagation/), [E30](exercises/E30-dropout/) |
| 4 | **P013** [Backpropagation Applied to Handwritten Zip Code Recognition](https://doi.org/10.1162/neco.1989.1.4.541) | 1989 | [E03](exercises/E03-handwritten-digits/) |
| 5 | **P014** [Handwritten Digit Recognition with a Back-Propagation Network](https://papers.nips.cc/paper_files/paper/1989/hash/53c3bce66e43be4f209556518c2fcb54-Abstract.html) | 1989 | [E03](exercises/E03-handwritten-digits/) |
| 6 | **P018** [Gradient-Based Learning Applied to Document Recognition](https://proceedingsoftheieee.ieee.org/gradient-based-learning-applied-to-document-recognition/) | 1998 | [E03](exercises/E03-handwritten-digits/), [E07](exercises/E07-cnn-shapes/) |
| 7 | **P009** [Induction of Decision Trees](https://doi.org/10.1007/BF00116251) | 1986 | [E04](exercises/E04-tabular-models/) |
| 8 | **P015** [Q-Learning](https://doi.org/10.1007/BF00992698) | 1992 | [E11](exercises/E11-gridworld/) |
| 9 | **P017** [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | [E15](exercises/E15-seq2seq-attention/), [E33](exercises/E33-contextual-embeddings/), [E34](exercises/E34-ulmfit-transfer/) |
| 10 | **P026** [ImageNet: A Large-Scale Hierarchical Image Database](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf) | 2009 | [E06](exercises/E06-image-benchmark/) |
| 11 | **P027** [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) | 2012 | [E07](exercises/E07-cnn-shapes/) |
| 12 | **P078** [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://jmlr.org/papers/v15/srivastava14a.html) | 2014 | [E30](exercises/E30-dropout/) |
| 13 | **P029** [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) | 2013 | [E14](exercises/E14-word-vectors/), [E29](exercises/E29-negative-sampling-and-glove/), [E33](exercises/E33-contextual-embeddings/) |
| 14 | **P077** [Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/abs/1310.4546) | 2013 | [E29](exercises/E29-negative-sampling-and-glove/) |
| 15 | **P079** [GloVe: Global Vectors for Word Representation](https://aclanthology.org/D14-1162/) | 2014 | [E29](exercises/E29-negative-sampling-and-glove/) |
| 16 | **P033** [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) | 2014 | [E15](exercises/E15-seq2seq-attention/) |
| 17 | **P032** [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) | 2014 | [E15](exercises/E15-seq2seq-attention/) |
| 18 | **P031** [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661) | 2014 | [E18](exercises/E18-generative-models/) |
| 19 | **P037** [Human-Level Control Through Deep Reinforcement Learning](https://www.nature.com/articles/nature14236) | 2015 | [E11](exercises/E11-gridworld/) |
| 20 | **P080** [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167) | 2015 | [E31](exercises/E31-batch-and-layer-normalization/) |
| 21 | **P035** [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) | 2015 | [E07](exercises/E07-cnn-shapes/), [E31](exercises/E31-batch-and-layer-normalization/) |
| 22 | **P046** [Mastering the Game of Go Without Human Knowledge](https://doi.org/10.1038/nature24270) | 2017 | [E12](exercises/E12-alphazero-self-play/) |
| 23 | **P045** [Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](https://arxiv.org/abs/1712.01815) | 2017 | [E12](exercises/E12-alphazero-self-play/), [E13](exercises/E13-learned-dynamics/) |
| 24 | **P081** [Layer Normalization](https://arxiv.org/abs/1607.06450) | 2016 | [E31](exercises/E31-batch-and-layer-normalization/) |
| 25 | **P043** [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 2017 | [E16](exercises/E16-attention-matrix/), [E31](exercises/E31-batch-and-layer-normalization/) |
| 26 | **P083** [Deep Contextualized Word Representations](https://aclanthology.org/N18-1202/) | 2018 | [E33](exercises/E33-contextual-embeddings/) |
| 27 | **P084** [Universal Language Model Fine-tuning for Text Classification](https://aclanthology.org/P18-1031/) | 2018 | [E34](exercises/E34-ulmfit-transfer/) |
| 28 | **P049** [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | 2018 | [E16](exercises/E16-attention-matrix/), [E17](exercises/E17-pretraining-objectives/) |
| 29 | **P048** [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | 2018 | [E16](exercises/E16-attention-matrix/), [E17](exercises/E17-pretraining-objectives/), [E33](exercises/E33-contextual-embeddings/), [E35](exercises/E35-roberta-ablations/) |
| 30 | **P085** [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692) | 2019 | [E35](exercises/E35-roberta-ablations/) |
| 31 | **P057** [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) | 2020 | [E21](exercises/E21-scaling-laws/) |
| 32 | **P055** [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | 2020 | [E21](exercises/E21-scaling-laws/) |
| 33 | **P053** [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) | 2020 | [E19](exercises/E19-self-supervised-vision/), [E20](exercises/E20-image-text-alignment/) |
| 34 | **P059** [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | 2021 | [E20](exercises/E20-image-text-alignment/) |
| 35 | **P058** [Highly Accurate Protein Structure Prediction with AlphaFold](https://www.nature.com/articles/s41586-021-03819-2) | 2021 | [E27](exercises/E27-protein-structures/) |
| 36 | **P065** [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | 2022 | [E21](exercises/E21-scaling-laws/) |
| 37 | **P076** [Simple statistical gradient-following algorithms for connectionist reinforcement learning](https://link.springer.com/article/10.1007/BF00992696) | 1992 | [E32](exercises/E32-reinforce-and-ppo/) |
| 38 | **P082** [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) | 2017 | [E32](exercises/E32-reinforce-and-ppo/) |
| 39 | **P066** [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) | 2022 | [E22](exercises/E22-preference-optimization/), [E32](exercises/E32-reinforce-and-ppo/) |
| 40 | **P067** [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) | 2023 | [E22](exercises/E22-preference-optimization/) |
| 41 | **P069** [Segment Anything](https://arxiv.org/abs/2304.02643) | 2023 | [E08](exercises/E08-boxes-and-masks/) |
| 42 | **P073** [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) | 2025 | [E23](exercises/E23-reasoning-verifiers/) |

## Placement guide

| Papers | Placement | Reason |
| --- | --- | --- |
| P029, P077, P079 | After AlexNet; before sequence-to-sequence models. | Read the original Word2Vec paper, its negative-sampling follow-up, then GloVe before contextual embeddings. |
| P078 | After AlexNet; revisit after backpropagation. | Establish dropout as a practical neural-network regularization technique. |
| P080 | Before ResNet. | Understand batch normalization before modern CNN training recipes. |
| P081 | Immediately before Attention Is All You Need. | Layer normalization is a component of the original Transformer. |
| P083, P084 | After recurrence/attention foundations; before GPT and BERT. | ELMo and ULMFiT show contextual features and recurrent-model transfer; ELMo does not require Transformer architecture. |
| P085 | Immediately after BERT. | Use RoBERTa to examine which gains come from the pretraining recipe. |
| P076, P082 | Before InstructGPT in the broad path; after Q-learning foundations in the RL path. | Read REINFORCE before PPO, then connect policy optimization to RLHF. |

## Deeper paths

### Neural foundations

Move from neurons and gradients to optimization, regularization and normalization.

**Paper order:** P001 → P003 → P010 → P012 → P030 → P078 → P080 → P081

**Exercises:** [E01](exercises/E01-perceptron/), [E02](exercises/E02-backpropagation/), [E30](exercises/E30-dropout/), [E31](exercises/E31-batch-and-layer-normalization/)

### Classical ML & search

Use baselines, search, and probabilistic reasoning.

**Paper order:** P002 → P005 → P006 → P009 → P016 → P020 → P019 → P042

**Exercises:** [E04](exercises/E04-tabular-models/), [E05](exercises/E05-expectation-maximization/), [E09](exercises/E09-astar-search/), [E10](exercises/E10-belief-networks/)

### Computer vision

Follow handwriting, image benchmarks, CNN training, residual networks and masks.

**Paper order:** P007 → P013 → P014 → P018 → P026 → P027 → P078 → P080 → P034 → P035 → P053 → P069

**Exercises:** [E03](exercises/E03-handwritten-digits/), [E06](exercises/E06-image-benchmark/), [E07](exercises/E07-cnn-shapes/), [E30](exercises/E30-dropout/), [E31](exercises/E31-batch-and-layer-normalization/), [E08](exercises/E08-boxes-and-masks/), [E19](exercises/E19-self-supervised-vision/)

### Reinforcement learning

Connect value learning, policy gradients, planning and PPO to RLHF.

**Paper order:** P011 → P015 → P076 → P037 → P039 → P046 → P045 → P051 → P082 → P066

**Exercises:** [E11](exercises/E11-gridworld/), [E32](exercises/E32-reinforce-and-ppo/), [E12](exercises/E12-alphazero-self-play/), [E13](exercises/E13-learned-dynamics/), [E22](exercises/E22-preference-optimization/)

### Sequence & attention

Study recurrence, alignment, layer normalization, attention and contextual representations.

**Paper order:** P017 → P033 → P032 → P081 → P043 → P083

**Exercises:** [E15](exercises/E15-seq2seq-attention/), [E31](exercises/E31-batch-and-layer-normalization/), [E16](exercises/E16-attention-matrix/), [E33](exercises/E33-contextual-embeddings/)

### Language models & alignment

Compare static and contextual vectors, recurrent and Transformer transfer, scaling and alignment; read prerequisites before linked exercises.

**Paper order:** P022 → P029 → P077 → P079 → P017 → P083 → P084 → P081 → P043 → P049 → P048 → P085 → P057 → P055 → P065 → P076 → P082 → P066 → P067 → P073

**Exercises:** [E14](exercises/E14-word-vectors/), [E29](exercises/E29-negative-sampling-and-glove/), [E15](exercises/E15-seq2seq-attention/), [E31](exercises/E31-batch-and-layer-normalization/), [E16](exercises/E16-attention-matrix/), [E17](exercises/E17-pretraining-objectives/), [E33](exercises/E33-contextual-embeddings/), [E34](exercises/E34-ulmfit-transfer/), [E35](exercises/E35-roberta-ablations/), [E21](exercises/E21-scaling-laws/), [E32](exercises/E32-reinforce-and-ppo/), [E22](exercises/E22-preference-optimization/), [E23](exercises/E23-reasoning-verifiers/), [E24](exercises/E24-retrieval/), [E25](exercises/E25-low-rank-adaptation/), [E28](exercises/E28-abstention/)

### Generative & multimodal

Compare generation procedures and image–text alignment.

**Paper order:** P028 → P031 → P054 → P063 → P059 → P072

**Exercises:** [E18](exercises/E18-generative-models/), [E20](exercises/E20-image-text-alignment/)

### Graphs, audio & science

Explore non-text structures and scientific prediction.

**Paper order:** P040 → P041 → P058 → P070

**Exercises:** [E26](exercises/E26-graph-or-audio/), [E27](exercises/E27-protein-structures/)

## Complete paper catalogue

Full authors, topics and learning rationale are also in roadmap.json and the spreadsheet. Personal reading dates, notes and status stay in the spreadsheet.

| ID | Year | Paper | Track | Tier | Exercises |
| --- | --- | --- | --- | --- | --- |
| P001 | 1943 | [A Logical Calculus of the Ideas Immanent in Nervous Activity](https://doi.org/10.1007/BF02478259) | Neural foundations | Core | [E01](exercises/E01-perceptron/) |
| P002 | 1950 | [Computing Machinery and Intelligence](https://doi.org/10.1093/mind/LIX.236.433) | Classical ML & search | Explore | — |
| P003 | 1958 | [The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain](https://doi.org/10.1037/h0042519) | Neural foundations | Core | [E01](exercises/E01-perceptron/) |
| P004 | 1959 | [Some Studies in Machine Learning Using the Game of Checkers](https://doi.org/10.1147/rd.33.0210) | Classical ML & search | Explore | [E09](exercises/E09-astar-search/) |
| P005 | 1968 | [A Formal Basis for the Heuristic Determination of Minimum Cost Paths](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf) | Classical ML & search | Core | [E09](exercises/E09-astar-search/) |
| P006 | 1977 | [Maximum Likelihood from Incomplete Data via the EM Algorithm](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x) | Classical ML & search | Core | [E05](exercises/E05-expectation-maximization/) |
| P007 | 1980 | [Neocognitron: A Self-Organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position](https://doi.org/10.1007/BF00344251) | Computer vision | Explore | — |
| P008 | 1986 | [Fusion, Propagation, and Structuring in Belief Networks](https://www.sciencedirect.com/science/article/pii/000437028690072X) | Classical ML & search | Explore | [E10](exercises/E10-belief-networks/) |
| P009 | 1986 | [Induction of Decision Trees](https://doi.org/10.1007/BF00116251) | Classical ML & search | Core | [E04](exercises/E04-tabular-models/) |
| P010 | 1986 | [Learning Representations by Back-Propagating Errors](https://doi.org/10.1038/323533a0) | Neural foundations | Core | [E02](exercises/E02-backpropagation/), [E30](exercises/E30-dropout/) |
| P011 | 1988 | [Learning to Predict by the Methods of Temporal Differences](https://doi.org/10.1007/BF00115009) | Reinforcement learning | Core | [E11](exercises/E11-gridworld/) |
| P012 | 1989 | [Approximation by Superpositions of a Sigmoidal Function](https://doi.org/10.1007/BF02551274) | Neural foundations | Explore | [E02](exercises/E02-backpropagation/) |
| P013 | 1989 | [Backpropagation Applied to Handwritten Zip Code Recognition](https://doi.org/10.1162/neco.1989.1.4.541) | Computer vision | Core | [E03](exercises/E03-handwritten-digits/) |
| P014 | 1989 | [Handwritten Digit Recognition with a Back-Propagation Network](https://papers.nips.cc/paper_files/paper/1989/hash/53c3bce66e43be4f209556518c2fcb54-Abstract.html) | Computer vision | Core | [E03](exercises/E03-handwritten-digits/) |
| P015 | 1992 | [Q-Learning](https://doi.org/10.1007/BF00992698) | Reinforcement learning | Core | [E11](exercises/E11-gridworld/) |
| P016 | 1995 | [Support-Vector Networks](https://doi.org/10.1007/BF00994018) | Classical ML & search | Core | [E04](exercises/E04-tabular-models/) |
| P017 | 1997 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | Sequence & attention | Core | [E15](exercises/E15-seq2seq-attention/), [E33](exercises/E33-contextual-embeddings/), [E34](exercises/E34-ulmfit-transfer/) |
| P018 | 1998 | [Gradient-Based Learning Applied to Document Recognition](https://proceedingsoftheieee.ieee.org/gradient-based-learning-applied-to-document-recognition/) | Computer vision | Core | [E03](exercises/E03-handwritten-digits/), [E07](exercises/E07-cnn-shapes/) |
| P019 | 2001 | [Greedy Function Approximation: A Gradient Boosting Machine](https://doi.org/10.1214/aos/1013203451) | Classical ML & search | Explore | [E04](exercises/E04-tabular-models/) |
| P020 | 2001 | [Random Forests](https://doi.org/10.1023/A:1010933404324) | Classical ML & search | Core | [E04](exercises/E04-tabular-models/) |
| P021 | 2001 | [Rapid Object Detection Using a Boosted Cascade of Simple Features](https://doi.org/10.1109/CVPR.2001.990517) | Computer vision | Explore | [E08](exercises/E08-boxes-and-masks/) |
| P022 | 2003 | [A Neural Probabilistic Language Model](https://jmlr.csail.mit.edu/papers/v3/bengio03a.html) | Language models & alignment | Core | [E14](exercises/E14-word-vectors/) |
| P023 | 2003 | [Latent Dirichlet Allocation](https://www.jmlr.org/papers/v3/blei03a.html) | Classical ML & search | Explore | — |
| P024 | 2004 | [Distinctive Image Features from Scale-Invariant Keypoints](https://doi.org/10.1023/B:VISI.0000029664.99615.94) | Computer vision | Explore | — |
| P025 | 2006 | [A Fast Learning Algorithm for Deep Belief Nets](https://doi.org/10.1162/neco.2006.18.7.1527) | Neural foundations | Explore | — |
| P026 | 2009 | [ImageNet: A Large-Scale Hierarchical Image Database](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf) | Computer vision | Core | [E06](exercises/E06-image-benchmark/) |
| P027 | 2012 | [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) | Computer vision | Core | [E07](exercises/E07-cnn-shapes/) |
| P028 | 2013 | [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114) | Generative & multimodal | Core | [E18](exercises/E18-generative-models/) |
| P029 | 2013 | [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) | Language models & alignment | Core | [E14](exercises/E14-word-vectors/), [E29](exercises/E29-negative-sampling-and-glove/), [E33](exercises/E33-contextual-embeddings/) |
| P030 | 2014 | [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) | Neural foundations | Explore | [E02](exercises/E02-backpropagation/) |
| P031 | 2014 | [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661) | Generative & multimodal | Core | [E18](exercises/E18-generative-models/) |
| P032 | 2014 | [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) | Sequence & attention | Core | [E15](exercises/E15-seq2seq-attention/) |
| P033 | 2014 | [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) | Sequence & attention | Core | [E15](exercises/E15-seq2seq-attention/) |
| P034 | 2014 | [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556) | Computer vision | Explore | [E07](exercises/E07-cnn-shapes/) |
| P035 | 2015 | [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) | Computer vision | Core | [E07](exercises/E07-cnn-shapes/), [E31](exercises/E31-batch-and-layer-normalization/) |
| P036 | 2015 | [Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/abs/1506.01497) | Computer vision | Explore | [E08](exercises/E08-boxes-and-masks/) |
| P037 | 2015 | [Human-Level Control Through Deep Reinforcement Learning](https://www.nature.com/articles/nature14236) | Reinforcement learning | Core | [E11](exercises/E11-gridworld/) |
| P038 | 2015 | [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597) | Computer vision | Core | [E08](exercises/E08-boxes-and-masks/) |
| P039 | 2016 | [Mastering the Game of Go with Deep Neural Networks and Tree Search](https://doi.org/10.1038/nature16961) | Reinforcement learning | Core | [E12](exercises/E12-alphazero-self-play/) |
| P040 | 2016 | [Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/abs/1609.02907) | Graphs, audio & science | Explore | [E26](exercises/E26-graph-or-audio/) |
| P041 | 2016 | [WaveNet: A Generative Model for Raw Audio](https://arxiv.org/abs/1609.03499) | Graphs, audio & science | Explore | [E26](exercises/E26-graph-or-audio/) |
| P042 | 2016 | [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754) | Classical ML & search | Explore | [E04](exercises/E04-tabular-models/) |
| P043 | 2017 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | Sequence & attention | Core | [E16](exercises/E16-attention-matrix/), [E31](exercises/E31-batch-and-layer-normalization/) |
| P044 | 2017 | [Mask R-CNN](https://openaccess.thecvf.com/content_iccv_2017/html/He_Mask_R-CNN_ICCV_2017_paper.html) | Computer vision | Explore | [E08](exercises/E08-boxes-and-masks/) |
| P045 | 2017 | [Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](https://arxiv.org/abs/1712.01815) | Reinforcement learning | Core | [E12](exercises/E12-alphazero-self-play/), [E13](exercises/E13-learned-dynamics/) |
| P046 | 2017 | [Mastering the Game of Go Without Human Knowledge](https://doi.org/10.1038/nature24270) | Reinforcement learning | Core | [E12](exercises/E12-alphazero-self-play/) |
| P047 | 2017 | [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538) | Language models & alignment | Explore | — |
| P048 | 2018 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | Language models & alignment | Core | [E16](exercises/E16-attention-matrix/), [E17](exercises/E17-pretraining-objectives/), [E33](exercises/E33-contextual-embeddings/), [E35](exercises/E35-roberta-ablations/) |
| P049 | 2018 | [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | Language models & alignment | Core | [E16](exercises/E16-attention-matrix/), [E17](exercises/E17-pretraining-objectives/) |
| P050 | 2019 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683) | Language models & alignment | Explore | [E17](exercises/E17-pretraining-objectives/) |
| P051 | 2019 | [Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model](https://arxiv.org/abs/1911.08265) | Reinforcement learning | Explore | [E13](exercises/E13-learned-dynamics/) |
| P052 | 2020 | [A Simple Framework for Contrastive Learning of Visual Representations](https://proceedings.mlr.press/v119/chen20j.html) | Computer vision | Explore | [E19](exercises/E19-self-supervised-vision/) |
| P053 | 2020 | [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) | Computer vision | Core | [E19](exercises/E19-self-supervised-vision/), [E20](exercises/E20-image-text-alignment/) |
| P054 | 2020 | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | Generative & multimodal | Core | [E18](exercises/E18-generative-models/) |
| P055 | 2020 | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | Language models & alignment | Core | [E21](exercises/E21-scaling-laws/) |
| P056 | 2020 | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | Language models & alignment | Explore | [E24](exercises/E24-retrieval/) |
| P057 | 2020 | [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) | Language models & alignment | Core | [E21](exercises/E21-scaling-laws/) |
| P058 | 2021 | [Highly Accurate Protein Structure Prediction with AlphaFold](https://www.nature.com/articles/s41586-021-03819-2) | Graphs, audio & science | Core | [E27](exercises/E27-protein-structures/) |
| P059 | 2021 | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | Generative & multimodal | Core | [E20](exercises/E20-image-text-alignment/) |
| P060 | 2021 | [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | Language models & alignment | Explore | [E25](exercises/E25-low-rank-adaptation/) |
| P061 | 2021 | [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377) | Computer vision | Explore | [E19](exercises/E19-self-supervised-vision/) |
| P062 | 2022 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) | Language models & alignment | Explore | [E23](exercises/E23-reasoning-verifiers/) |
| P063 | 2022 | [High-Resolution Image Synthesis with Latent Diffusion Models](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) | Generative & multimodal | Explore | [E18](exercises/E18-generative-models/) |
| P064 | 2022 | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | Language models & alignment | Explore | [E23](exercises/E23-reasoning-verifiers/), [E24](exercises/E24-retrieval/) |
| P065 | 2022 | [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | Language models & alignment | Core | [E21](exercises/E21-scaling-laws/) |
| P066 | 2022 | [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) | Language models & alignment | Core | [E22](exercises/E22-preference-optimization/), [E32](exercises/E32-reinforce-and-ppo/) |
| P067 | 2023 | [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) | Language models & alignment | Core | [E22](exercises/E22-preference-optimization/) |
| P068 | 2023 | [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) | Language models & alignment | Explore | — |
| P069 | 2023 | [Segment Anything](https://arxiv.org/abs/2304.02643) | Computer vision | Recent | [E08](exercises/E08-boxes-and-masks/) |
| P070 | 2024 | [Accurate Structure Prediction of Biomolecular Interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w) | Graphs, audio & science | Recent | [E27](exercises/E27-protein-structures/) |
| P071 | 2024 | [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) | Language models & alignment | Recent | — |
| P072 | 2024 | [Emu3: Next-Token Prediction is All You Need](https://arxiv.org/abs/2409.18869) | Generative & multimodal | Recent | — |
| P073 | 2025 | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) | Language models & alignment | Recent | [E23](exercises/E23-reasoning-verifiers/) |
| P074 | 2025 | [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) | Language models & alignment | Recent | — |
| P075 | 2026 | [Evaluating Large Language Models for Accuracy Incentivizes Hallucinations](https://www.nature.com/articles/s41586-026-10549-w) | Language models & alignment | Recent | [E23](exercises/E23-reasoning-verifiers/), [E28](exercises/E28-abstention/) |
| P076 | 1992 | [Simple statistical gradient-following algorithms for connectionist reinforcement learning](https://link.springer.com/article/10.1007/BF00992696) | Reinforcement learning | Core | [E32](exercises/E32-reinforce-and-ppo/) |
| P077 | 2013 | [Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/abs/1310.4546) | Language models & alignment | Core | [E29](exercises/E29-negative-sampling-and-glove/) |
| P078 | 2014 | [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://jmlr.org/papers/v15/srivastava14a.html) | Neural foundations | Core | [E30](exercises/E30-dropout/) |
| P079 | 2014 | [GloVe: Global Vectors for Word Representation](https://aclanthology.org/D14-1162/) | Language models & alignment | Explore | [E29](exercises/E29-negative-sampling-and-glove/) |
| P080 | 2015 | [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167) | Neural foundations | Core | [E31](exercises/E31-batch-and-layer-normalization/) |
| P081 | 2016 | [Layer Normalization](https://arxiv.org/abs/1607.06450) | Neural foundations | Core | [E31](exercises/E31-batch-and-layer-normalization/) |
| P082 | 2017 | [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) | Reinforcement learning | Core | [E32](exercises/E32-reinforce-and-ppo/) |
| P083 | 2018 | [Deep Contextualized Word Representations](https://aclanthology.org/N18-1202/) | Language models & alignment | Core | [E33](exercises/E33-contextual-embeddings/) |
| P084 | 2018 | [Universal Language Model Fine-tuning for Text Classification](https://aclanthology.org/P18-1031/) | Language models & alignment | Explore | [E34](exercises/E34-ulmfit-transfer/) |
| P085 | 2019 | [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692) | Language models & alignment | Explore | [E35](exercises/E35-roberta-ablations/) |

## Keeping the two copies aligned

roadmap.json contains the shared curriculum: paper metadata, exercise briefs, relationships, broad order and deeper paths. It excludes personal status, reading dates and notes. The spreadsheet holds that progress; exercise notes.md files and execution/results sections hold your own work.

For a curriculum change, edit roadmap.json, run `python scripts/sync_roadmap.py --write`, then `python scripts/sync_roadmap.py --check`. Apply the same fields to the existing spreadsheet by stable ID, preserving tracking columns, and compare the spreadsheet readback with the manifest. Include reading paths, inverse paper/exercise mappings and Work links in that comparison.

The script validates and regenerates repository content. It does not connect to Google Sheets or automatically synchronize future edits. Personal exercise notes and the execution/results sections are preserved by generation.
