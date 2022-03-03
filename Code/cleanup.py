from string import punctuation
import re
from tokens import tokenize

def read_file(file):
    with open(file) as f:
        text = f.read()
        punct = punctuation + '”“‘’–…'
        mod_str = ' '.join(filter(None, (word.strip(punct) for word in text.split())))
        lower_str = mod_str.lower()
        recapitalized_str = re.sub('i\s', ' I ', lower_str)
        str_list = recapitalized_str.split()
    return str_list

def clean_up(file):
    with open(file) as f:
        text = f.read()
        tokens = tokenize(text)
    return tokens

if __name__ == '__main__':
    print(read_file('example_txt/example.txt'))