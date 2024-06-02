from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("google/gemma-1.1-2b-it")
model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-1.1-2b-it",
    device_map="auto",
    torch_dtype=torch.bfloat16
)

input_text = "Write me a poem about CNC Machinist."
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda"if torch.cuda.is_available() else "cpu")

outputs = model.generate(**input_ids, max_new_tokens=500)
print(tokenizer.decode(outputs[0]))
