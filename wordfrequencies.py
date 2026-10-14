import string

def strip_gutenberg(text):
    start = text.find('*** start of')
    if start != -1:
        newline = text.find('\n', start)
        text = text[newline + 1:]
    end = text.find('*** end of')
    if end != -1:
        text = text[:end]
    return text

def read_file(filename):
    with open(filename , encoding='utf-8') as f:
        text = f.read().lower()
    text = strip_gutenberg(text)
    for ch in string.punctuation + "“”‘’—–…":
        text = text.replace(ch, " ")
    return text.split()
    

def word_frequency(words):
    d={}

    for i in words:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1

    return d 
