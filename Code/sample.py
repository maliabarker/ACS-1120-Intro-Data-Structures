import sys, random
from histogram import create_histogram_dict

def random_word(histogram_list):
    tuple = random.choice(histogram_list)
    word = tuple[0]
    return word
    
# def random_word_weighted(histogram):
#     words = list()
#     for key in histogram:
#         i = int(histogram[key])
#         for x in range(0, i):
#             words.append(key)
#     rand_num = random.randint(0, len(words) - 1)
#     return words[rand_num]

def weighted_word(histogram):
    distance = 0
    dart = random.randint(0, sum(histogram.values()))
    for key, value in histogram.items():
        distance += value
        if distance >= dart:
            return key

if __name__ == '__main__':
    file = sys.argv[1]
    histogram = create_histogram_dict(file)
    print(weighted_word(histogram))