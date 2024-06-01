# from transformers import AutoTokenizer, pipeline
# import torch
from huggingface_hub import login
HF_TOKEN = "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"
login(token=HF_TOKEN, add_to_git_credential=True)
# model = "google/gemma-2b"
# pipeline = pipeline(
#     "text-generation",
#     model=model,
#     model_kwargs={
#         "torch_dtype": torch.float16,
#         "quantization_config": {"load_in_4bit": True}
#     }, token=HF_TOKEN
# )
#
# messages = [
#     {"role": "user", "content": "Tell me about ChatGPT"},
# ]
# prompt = pipeline.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
# outputs = pipeline(
#     prompt,
#     max_new_tokens=256,
#     do_sample=True,
#     temperature=0.7,
#     top_k=50,
#     top_p=0.95
# )
# print(outputs[0]["generated_text"][len(prompt):])
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2b",
    torch_dtype=torch.bfloat16
)

input_text = "Write me a poem about CNC Machinist."
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids, max_new_tokens=500)
print(tokenizer.decode(outputs[0]))
