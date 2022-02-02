import re
from string import punctuation
# –––––––––––––––––––––––––––––––––DICT––––––––––––––––––––––––––––––––––––––––––––
def create_histogram_dict(file):
    with open(file) as f:
        text = f.read()
        punct = punctuation + '”“‘’'
        mod_str = ' '.join(filter(None, (word.strip(punct) for word in text.split())))
        str_list = mod_str.lower().split()
        # print(str_list)
        # re.sub('[^A-Za-z0-9\s]+', '', text).lower().split()
        histogram = {}
        for word in str_list:
            if word in histogram:
                histogram[word]+=1
            else:
                histogram[word] = 1
        return histogram

def find_unique_words_dict(histogram):
    unique_words_int = 0
    for key in histogram:
        if histogram[key] == 1:
            unique_words_int += 1
    return unique_words_int

def find_word_frequency_dict(word, histogram):
    frequency = 0
    for key in histogram:
        if key == word:
            frequency = histogram[key]
    return frequency

# –––––––––––––––––––––––––––––––––TUPLE––––––––––––––––––––––––––––––––––––––––––––
def create_histogram_tuple(file):
    with open(file) as f:
        words = f.read().lower().strip(".").replace(",", "").split()
        histogram = []
        for word in words:
            matching_tuple = [i for i in histogram if i[0]==word]
            if matching_tuple:
                histogram.remove(matching_tuple[0])
                histogram.append((word, int(matching_tuple[0][1]) + 1))
            else:
                histogram.append((word, 1))
        return histogram

def find_unique_words_tuple(histogram):
    unique_words_int = 0
    for tuple in histogram:
        if tuple[1] == 1:
            unique_words_int += 1
    return unique_words_int

def find_word_frequency_tuple(word, histogram):
    frequency = 0
    for tuple in histogram:
        if tuple[0] == word:
            frequency = tuple[1]
    return frequency




if __name__ == "__main__":
    example_histogram = create_histogram_dict('example_txt/example.txt')
    print(example_histogram)
    
    # print(find_unique_words_dict(example_histogram))
    # print(find_word_frequency_dict('sherlock', example_histogram))

    # example_2_histogram = create_histogram_tuple('example.txt')
    # print(example_2_histogram)
    # print(find_unique_words_tuple(example_2_histogram))
    # print(find_word_frequency_tuple('two', example_2_histogram))
