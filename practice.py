import transformers
import sentence_transformers
import tiktoken

from transformers import pipeline
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)
prompt="I Love Walking"

result=generator(
    prompt,
    max_new_tokens=3,
    num_return_sequences=1
)
for i,output in enumerate(result,1):
  print(f"\nOutput {i}:")
  print(output["generated_text"])


from transformers import AutoTokenizer

tokenizer=AutoTokenizer.from_pretrained("gpt2")

text = "I love Hyderabad biryani!I love eating it."

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print("Original Text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nToken IDs:")
print(token_ids)

print("\nNumber of Tokens:")
print(len(token_ids))