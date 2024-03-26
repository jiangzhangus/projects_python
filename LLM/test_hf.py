import sys
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForSeq2SeqLM, GenerationConfig

line = "What color is the undoubtedly beautiful sky?"
model_name = "google/flan-t5-base"
# model_name = "google/flan-t5-xl" 10G, too large
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

config = GenerationConfig(max_new_tokens=200)

for line in sys.stdin:
    tokens = tokenizer(line, return_tensors="pt")
    output = model.generate(**tokens, generation_config=config)
    print(tokenizer.batch_decode(output, skip_special_tokens=True))

# input_embeddings = model.get_input_embeddings()
# token_ids = tokens["input_ids"][0]
# our_embeddings = input_embeddings(token_ids)
# print(our_embeddings)
# print(our_embeddings.size())
