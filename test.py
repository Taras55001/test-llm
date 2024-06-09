from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

local_model_path = "./gemma-1.1-2b-it"

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

