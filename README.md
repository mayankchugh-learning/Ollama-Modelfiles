# Ollama-Modelfiles

```bash
git clone https://github.com/mayankchugh-learning/Ollama-Modelfiles.git
```

```bash
ollama list
```
# mistral

```bash
ollama show --help
```
```bash
ollama show mistral --parameters
```
```bash
ollama show mistral --license
```
```bash
ollama show mistral --system
```

```bash
ollama show mistral --modelfile
```

```bash
ollama create <NewModelfilename> -f ./Modelfile
```
```bash
ollama create BorisJohnsonModel -f ./mistralTweakModelfile
ollama create MasterYodaModel -f ./MasterYodaModelfile
ollama create EminemModel -f ./EminemModelfile
```
```bash
ollama list
```

```bash
ollama show <NewModelfilename> --modelfile
```

```bash
ollama run <NewModelfilename>
```
# Master Yoda
## SYSTEM "You are an asistant who speaks like Master Yoda, A fictional character from the Star Wars franchise"
```bash
ollama create MasterYodaMistral -f ./MasterYodaModelfile
ollama show MasterYodaMistral --modelfile
ollama run MasterYodaMistral
```
# Eminem
## SYSTEM "You are an asistant who speaks like Eminem, The Most Famous Rapper"
```bash
ollama create EminemMistral -f ./EminemModelfile
ollama show EminemMistral --modelfile
ollama run EminemMistral
```

# As your wish
```bash
ollama rm MasterYodaMistral
ollama rm EminemMistral
```

![alt text](image.png)

```bash
https://github.com/ollama/ollama/tree/main/examples/modelfile-mario
https://github.com/ollama/ollama/blob/main/docs/modelfile.md
```
--------------------------------------------------------------------------------------
# How to run HuggingFace Model on locally using Ollama 
## Step 1: Download and Install Ollama

First, download and install Ollama from the following GitHub repository:

[Ollama GitHub Repository](https://github.com/mayankchugh-learning/OllamaRAGApp.git)

## Step 2: Create and activate Conda envirnoment

```bash
conda create -p ollamaHuggingFaceEnv python=3 -y
```

## Step 3: Activate Conda envirnoment

```bash
source activate ./ollamaHuggingFaceEnv
```
## Step 4: Install HuggingFace CLI  in Conda envirnoment
[https://huggingface.co/docs/huggingface_hub/main/en/guides/cli](https://github.com/mayankchugh-learning/OllamaRAGApp.git)

```bash
pip install -U "huggingface_hub[cli]"
```

## Step 5: Install HuggingFace Transfer in Conda envirnoment

```bash
pip install -U "huggingface_hub[hf_transfer]"
```

## Step 6: Install HuggingFace Transfer in Conda envirnoment

```bash
export HF_HUB_ENABLE_HF_TRANSFER=1
```
or 
- create .env file and save
```bash
HF_HUB_ENABLE_HF_TRANSFER=1
```

## Step 6: Go to HuggingFace.co and click on mondels and then search "uncensored gguf wizard"

```bash
huggingface-cli download TheBloke/WizardLM-7B-uncensored-GGUF WizardLM-7B-uncensored.Q4_K_M.gguf
```

## Step 7: Copy the path where it download, Create Modelfile & save as below 

```bash
FROM /Users/mayankchugh/.cache/huggingface/hub/models--TheBloke--WizardLM-7B-uncensored-GGUF/snapshots/db690b5e11897e4bcbfb5193bb24fd531ab5cd2f/WizardLM-7B-uncensored.Q4_K_M.gguf
```

## Step 8: Create model
```bash
ollama create uncensored_wizard_7b -f ./hugginfaceModelfile
```
```bash
ollama list
```
```bash
ollama run uncensored_wizard_7b
```
