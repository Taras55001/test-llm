from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os
import subprocess

local_model_path = "./gemma-1.1-2b-it"
dir_exists = os.path.exists(local_model_path)
if not dir_exists:
    clone_command = ["git", "clone", "https://huggingface.co/google/gemma-1.1-2b-it"]
    subprocess.run(clone_command)


def llm_request(input_text, max_token):
    tokenizer = AutoTokenizer.from_pretrained(local_model_path)
    model = AutoModelForCausalLM.from_pretrained(
        local_model_path,
        device_map="auto",
        torch_dtype=torch.bfloat16
    )

    input_ids = tokenizer(input_text, return_tensors="pt").to("cuda"if torch.cuda.is_available() else "cpu")

    outputs = model.generate(**input_ids, max_new_tokens=max_token)
    return tokenizer.decode(outputs[0])

