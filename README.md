# biasInAI.py
# Exploration of AI bias in Word Embedings

## Introduction

A word embedding that represent each word (or common phrase) w as a d-dimensional word vector. These vectors are trained on word co-occurance ni text corpora, and are used as a substitute for word meanings e.g. words with similar semantic meanings tend to have vectors that are close together. Word embeddings such as GloVe are used extesively for several NLP tasks suck as web searching, document ranking, sentiment analysis, [question retrieval] and even [parsing resumes]

Vector differences between words represent relationships between words, for example given an analogy puzzle, “man is to king as woman is to x” (denoted as man:king :: woman:x), simple arithmetic of the embedding vectors finds that x=queen is the best answer because:
<img src="https://latex.codecogs.com/svg.latex?\overrightarrow{man}-\overrightarrow{woman}=\overrightarrow{king}-\overrightarrow{queen}">

Similarly x=Japan is returned for Paris:France :: Tokyo:x. 

This project shows an interactive way of exploring these relationships

[parsing resumes]: https://lenabayeva.files.wordpress.com/2015/03/snn-textkernelposter-2015.pdf
[question retrieval]: https://arxiv.org/abs/1512.05726


## Requirements for minoconda for Linux)

Install Miniconda (or any other python 3 interface)

```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

conda config --add channels conda-forge
conda install --yes --file requirements.txt 

### Alternativly instructions for default Python3
# sudo apt install python3
# pip3 install requirements.txt 

```

## Instructions (With Docker)



### Build doker container (one time)
```bash
cd docker
docker build -t minicondaapp .
```

### Running the application

```bash
# running the docker container
docker run --rm -ti -v $PWD:/project -p 5000:5000 minicondaapp

# 
export FLASK_DEBUG=1
# FOR MAC ONLY --> export LANG=en_US.UTF-8 & export LC_ALL=en_US.UTF-8
FLASK_APP=webAPI flask run --host=0.0.0.0
```


## Running uwsgi

```bash
### MAnnually
# uwsgi --http :80 --wsgi-file web.py  --callable app --processes 2 --threads 2
# This will spawn 4 processes (each with 2 threads) each.
# see https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html

# Running on port 80
sudo /home/ubuntu/miniconda3/bin/uwsgi --ini uwsgi.ini # --fallback-config uwsgi_safe.ini 

## On port 8080
uwsgi --ini uwsgi_safe.ini 



## TODO:
use ngnix : for isolation and load balancing
optimizie number of threads & processes for optimal performance.

