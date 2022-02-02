import random, sys

def sentence(word_count, file):
    with open(file) as f:
        # lines = f.readlines()
        # lines = [line.rstrip() for line in lines]
        lines = f.read().splitlines()
        rand_sent = random.choices(lines, k=int(word_count))
        lst_to_str = ""
        for i in rand_sent:
            lst_to_str += f'{i} '
    return print(lst_to_str)
        # for i in rand_sent:
        #     print(str(i), end=" ")

if __name__ == '__main__':
    params = sys.argv[1]
    sentence(params, '/usr/share/dict/words')