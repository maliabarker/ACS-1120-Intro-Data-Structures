import re

def tokenize(text):
    no_punc_text = remove_punctuation(text)
    fe_text = flat_earth(no_punc_text)
    decap_text = decapitalize(fe_text)
    recap_text = recapitalize(decap_text)
    tokens = split_on_whitespace(recap_text)
    return tokens

def split_on_whitespace(text):
    split_txt = re.split('\s+', text)
    # split_txt = re.sub('\sM.\sNight\sShyamalan\s', ' M. Night Shyamalan ', split_txt)
    return split_txt

def remove_punctuation(text):
    no_punc_text = re.sub('[,.()?!]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    no_punc_text = re.sub('[”“‘’–…"]', '', no_punc_text)
    no_punc_text = re.sub('\[[0-9]\]', '', no_punc_text)
    return no_punc_text

def flat_earth(text):
    flat_earth = re.sub('fe', ' flat earth ', text)
    return flat_earth

def decapitalize(text):
    decapitalize = re.sub(r'[A-Z]' , lambda m: m.group(0).lower(), text)
    return decapitalize

def recapitalize(text):
    recapitalize = re.sub('i\s', ' I ', text)
    recapitalize = re.sub('hd\s', ' HD ', recapitalize)
    # recapitalize = re.sub('m\snight\sshyamalan', ' M. Night Shyamalan ', recapitalize)
    return recapitalize

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(sys.argv[1])
        filename = sys.argv[1]
        source = open(filename).read()
        tokens = tokenize(source)
        print(tokens)
    else:
        print('No source text filename given as argument')