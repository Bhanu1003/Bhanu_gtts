from transformers import MarianMTModel, MarianTokenizer

# Choose a model for English to Telugu translation
model_name = 'Helsinki-NLP/opus-mt-en-te'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

text = "Hello Pramod, can you please test my accent and confirm once"
translated = tokenizer.prepare_seq2seq_batch([text], return_tensors="pt")
translated_tokens = model.generate(**translated)
translation = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
print("Translated Text:", translation)
print("Hi")