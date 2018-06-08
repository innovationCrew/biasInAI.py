# biasInAP.py
# Exploration of AI bias in Word Embedings

## Introduction

A word embedding that represent each word (or common phrase) w as a d-dimensional word vector. These vectors are trained on word co-occurance ni text corpora, and are used as a substitute for word meanings e.g. words with similar semantic meanings tend to have vectors that are close together. Word embeddings such as GloVe are used extesively for several NLP tasks suck as web searching, document ranking, sentiment analysis, [question retrieval] and even [parsing resumes]

Vector differences between words represent relationships between words, for example given an analogy puzzle, “man is to king as woman is to x” (denoted as man:king :: woman:x), simple arithmetic of the embedding vectors finds that x=queen is the best answer because:
<img src="https://latex.codecogs.com/svg.latex?\overrightarrow{man}-\overrightarrow{woman}=\overrightarrow{king}-\overrightarrow{queen}">

Similarly x=Japan is returned for Paris:France :: Tokyo:x. 

This project shows an interactive way of exploring these relationships

[parsing resumes]: https://lenabayeva.files.wordpress.com/2015/03/snn-textkernelposter-2015.pdf
[question retrieval]: https://arxiv.org/abs/1512.05726


## Build instructions

### Build the dockerfile

```bash
cd docker
docker build -t minicondabias .
```