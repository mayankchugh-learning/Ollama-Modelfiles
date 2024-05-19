# Use a pipeline as a high-level helper
from transformers import pipeline
import torch

pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", torch_dtype=torch.bfloat16)