from cleanup import read_file, clean_up
from dictogram import Dictogram
import random

class MarkovChain(object):
    def __init__(self, word_list, order):
        super(MarkovChain, self).__init__()
        self.corpus = word_list
        self.dict = {}
        self.markov_dict = self.markov_chain(order)
        

    def markov_chain(self, order):
        word_tuples = []
        for index in range(0, len(self.corpus) - 1):
            ### CREATE KEYS ###
            # initialize empty list to store tuple in
            words = []

            # iterate through numbers by the order given (example, iterate twice for a 2nd order chain)
            for i in range(0, order):
                # append a word for every n in order to words list
                if index+i in range(0, len(self.corpus)):
                    # print(self.corpus[index+i])
                    words.append(self.corpus[index+i])
                else:
                    # index = 0
                    words.append(self.corpus[index+i - len(self.corpus)])
                    # print(index+i)
                    # print(self.corpus[index+i])
                    

            # create tuple from words list
            word_tuple = tuple(words)
            word_tuples.append(word_tuple)


            ### CREATE VALUES ###
            # check if there is a following word 
            if index+order in range(0, len(self.corpus)):
                next_word = self.corpus[index+order]
                # print(f'following word: {self.corpus[index+order]}')
            # if there is not, loop around to the beginning
            else:
                next_word = self.corpus[index+order - len(self.corpus)]
                # print(f'looping back: {self.corpus[0]}')
            
            ### CREATE DICT###
            # check if the word tuple is already in the dictionary
            if word_tuple in self.dict.keys():
                # if it is, access dictogram and add next word
                dictogram = self.dict[word_tuple]
                # check if the next word already in dictogram
                if next_word:
                    if next_word in dictogram.keys():
                        # if it is, increment count
                        # print(f'{next_word} already there')
                        dictogram.add_count(next_word)
                    else:
                        # print(f'{next_word} not there')
                        # if it is not, add to value and increment count
                        dictogram.add_count(next_word)
            else:
                # if word tuple not found in dict, create new key value pair with new initalized dictogram
                if next_word:
                    self.dict[word_tuple] = Dictogram([next_word])
        return self.dict
    
    def walk_chain(self, starting_word, word_count):
        # start with matching key in markov chain as condition
        count = 0
        str = []
        current = starting_word
        while count in range(0, word_count):
            # i = [item for item in self.markov_dict.keys() if current == item[0]]
            tuples = []
            for i in self.markov_dict.keys():
                # print(f'i is {i}')
                if current == i[0]:
                    tuples.append(i)
            # print(len(tuples))
            if len(tuples) == 0:
                return str
            # print(tuples)
            random_tuple = random.choice(tuples)
            # print(f'i used is :{random_tuple}')
            for n in random_tuple:
                # print(f'now being appended: {n}')
                str.append(n)
                count += 1
            # print(f'possible options: {self.markov_dict[random_tuple]}')
            current = self.markov_dict[random_tuple].sample()
            # print(f'sampled word that is now being used: {current}')
        return str


# create markov chain class (or use functions)
# start with dictionary that represents markov chain
# pass in corpus (already cleaned up and in list)

# create word tuples & word windows?
# iterate over corpus (make last in range the length of corpus minus the # order of markov chain)
# create tuples with 0 as the word there (index = n) and 1 as the word there + 1 (index = n+1)
# create window? (maybe all words that come after word in tuple?)

# use tuple as key for markov dictionary
# use 

# create separate method/function to walk the markov chain
# sample from markov chain's index of current word


if __name__ == '__main__':
    test = MarkovChain(clean_up('example_txt/flat_earth.txt'), 6)
    # print(tokenize('example_txt/flat_earth.txt'))
    # print(test.markov_chain(4))
    # test.markov_chain(3)
    # print('___________')
    # print(len(test.markov_chain(3)))
    print(test.walk_chain('you', 50))