import json
import re
from corrector import correct_word

def load_resources():
    try:
        with open("slang.json", "r") as f:
            slang_dict = json.load(f)
    except FileNotFoundError:
        slang_dict = {}

    with open("5000_common.txt", "r") as f:
        vocab = [line.strip().lower() for line in f if len(line.strip()) > 1]

    return slang_dict, vocab

def translate_slang(text, slang_dict):
    words = text.split()
    translated = []
    for word in words:
        clean = re.sub(r'[^a-zA-Z0-9]', '', word).upper()
        translated.append(slang_dict.get(clean, word))
    return " ".join(translated)

def process_input(user_input, slang_dict, vocab):
    expanded_text = translate_slang(user_input, slang_dict)
    words = expanded_text.split()
    corrected_words = [correct_word_from_scratch(w, vocab) for w in words]
    return " ".join(corrected_words)
