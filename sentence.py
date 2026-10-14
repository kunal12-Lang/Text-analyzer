import string
from wordfrequencies import strip_gutenberg

def sentence_lst(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read().lower()
    text = strip_gutenberg(text)
    text = text.replace('!', '.').replace('?', '.')

    pieces = text.split('.')
    sentences = []

    for p in pieces:
        for ch in string.punctuation + "“”‘’—–…":
            p = p.replace(ch, " ")
        if len(p.split()) > 0:
            sentences.append(p)
    return sentences

def sentence_count(sentences):
    return len(sentences)

def avg_sentence_count(sentences):
    denominator = sentence_count(sentences)
    numerator = 0

    for i in sentences:
        numerator += len(i.split())

    return numerator / denominator
