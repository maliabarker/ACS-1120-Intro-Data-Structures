from cleanup import read_file
from dictogram import Dictogram
import random

# Choose starting point (word in list)
# Initialize float numbers for each word in list (float represents probability of word being next)
    # Initialize count = 0
    # Initialize dictionary = {}
    # following_words_list = all words that follow starting word
    # total_following_words = sum of all words that follow
    # increment words by i = 1/total_following_words
    # check if dictionary keys in 
    # for each word in following_words_list
        # add to dictionary[word] = count += i
    # For all other words assign count (0)
# Generate random float number between 0 and 1


words_list = read_file('example_txt/example1.txt')
# print(words_list)

histogram = Dictogram(words_list)
# print(histogram)

states = list(histogram.keys())
# print(states)

starting_state = 'fish'

following_words = []

for i, word in enumerate(words_list):
    if word == starting_state:
        # print(word)
        # print(i)
        if i != len(words_list) - 1:
            next_word = words_list[int(i+1)]
            following_words.append(next_word)
            # print(next_word)
            
print(following_words)
total_routes = len(following_words)

following_histogram = Dictogram(following_words)

possible_routes = []

for key, value in following_histogram.items():
    probability = value / total_routes
    possible_routes.append((key, probability))

print(possible_routes)

def sample(list_of_tuples):
    distance = 0
    dart = random.uniform(0, 1)
    print(dart)
    for word, count in list_of_tuples:
        print(word)
        print(count)
        distance += count
        if distance >= dart:
            return word
        

print(sample(possible_routes))