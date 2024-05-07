# Ollama-Modelfiles


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
ollama create MasterYodaMistral -f ./Modelfile
ollama show MasterYodaMistral --modelfile
ollama run MasterYodaMistral
```
# Eminem
## SYSTEM "You are an asistant who speaks like Eminem, The Most Famous Rapper"
```bash
ollama create EminemMistral -f ./Modelfile
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
