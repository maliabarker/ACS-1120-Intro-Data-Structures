from string import punctuation
from tokens import tokenize

def read_file(file):
    with open(file) as f:
        text = f.read()
        punct = punctuation + '”“‘’–…'
        mod_str = ' '.join(filter(None, (word.strip(punct) for word in text.split())))
        str_list = mod_str.lower().split()
    return str_list

def clean_up(file):
    with open(file) as f:
        text = f.read()
        tokens = tokenize(text)
    return tokens

if __name__ == '__main__':
    print(clean_up('example_txt/example.txt'))