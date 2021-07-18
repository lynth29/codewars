from collections import Counter
import re

def top_3_words(text):
    word_regex = re.findall("[\s]?([']?[a-z]+'?[a-z']*)[\s,:]?", text.lower())
    # Count unique word
    c = Counter(word_regex)
    result = [word for word, count in c.most_common(3)]
    return result
