from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-v0.3",
    torch_dtype=torch.float16,
    token="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",
    device_map="cuda:0"
)

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.3", token="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")