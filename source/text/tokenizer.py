import json
import re

def load_resources():
  vocab = []

  try:
    with open("slang.json","r") as f:
      slang_dict = json.load(f)

    with open("5000_common.txt") as f:
      for line in f:
        if len(line.strip()) > 1:
          vocab.append(line.strip().lower())
          
  except FileNotFoundError:
    slang_dict = {}
  
  return slang_dict,vocab
  
def translate_slang(text, slang_dict):
    words = text.split()
    translated = []
    for word in words:
        clean = re.sub(r'[^a-zA-Z0-9]', '', word).upper()
        if clean in slang_dict:
            punct = re.sub(r'[a-zA-Z0-9]', '', word)
            translated.append(slang_dict[clean] + punct)
        else:
            translated.append(word)
    return " ".join(translated)
    
def process_user_input(user_input, slang_dict, vocab):
  corrected_words = translate_slang(user_input, slang_dict)
  words = corrected_words.split()
  return " ".join(words)

if __name__ == "__main__":
    slang_json, valid_vocab = load_resources()
    raw_input = "fr the quamtum forest is op"
    clean_text = process_user_input(raw_input, slang_json, valid_vocab)
    print(f"User wrote: {raw_input}")
    print(f"Numa understands: {clean_text}")
