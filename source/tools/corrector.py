import difflib

def correct_word(word, dictionary):
    matches = difflib.get_close_matches(word.lower(), dictionary, n=1, cutoff=0.75)

    if matches:
        return matches[0] # Returns the single best match
    else:
        return word # No close match found, return original word
