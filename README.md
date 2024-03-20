### Clone the repo
```
git clone https://github.com/mudittt/text-summarizer.git
```


### Setup a conda environment
```
conda create --name torch python=3.8
conda activate torch
```

- if you're using a macbook with an apple chip,
then install the nightly version of pytorch to use pytorch with gpu support on your mac.

- install all other remaining package from requirements.txt

```
conda install pytorch-nightly::pytorch torchvision torchaudio -c pytorch-nightly
```

```
conda install transformers accelerate sentencepiece
```

```
conda install sacrebleu rouge-score py7zr pandas boto3 mypy-boto3-s3 nltk matplotlib notebook uvicorn fastapi python-box 
```
```
conda install protobuf
```

### Workflows
```

- Update config.yaml
- Update params.yaml
- Update entity
- Update the configuration manager in src config
- update the conponents
- update the pipeline
- update the main.py
- update the app.py

```



