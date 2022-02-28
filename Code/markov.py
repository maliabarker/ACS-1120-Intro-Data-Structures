from cleanup import read_file
from dictogram import Dictogram

class MarkovChain(object):
    """  """
    def __init__(self, word_list):
        super(MarkovChain, self).__init__()

        self.corpus = word_list
        self.markov_dict = {}
    
    def markov_chain(self, order):
        ## This is where we make markov chain dict
        ## For i in corpus, create new histogram with i as key and...
        ## new histogram for value with i + 1 as key and count as value
        for index in range(0, len(self.corpus)):
            # assign variables and check if next_word equals none
            word = self.corpus[index]
            if index + 1 in range(0, len(self.corpus)):
                next_word = self.corpus[index + 1]
            else:
                next_word = None

            # check if word is already in markov dictionary
            if word in self.markov_dict.keys():
                # if it is, access dictogram and add next word (will add new key-value pair or increment count)
                dictogram = self.markov_dict[word]
                # check if the next word already in dictogram
                if next_word:
                    if next_word in dictogram.keys():
                        # print(f'{next_word} already there')
                        dictogram.add_count(next_word)
                    else:
                        # print(f'{next_word} not there')
                        dictogram.add_count(next_word)
            else:
                # else create new key value pair with new initalized dictogram
                if next_word:
                    self.markov_dict[word] = Dictogram([next_word])
        print(self.markov_dict)

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


# remember to use if __name__ == '__main__'


if __name__ == '__main__':
    test = MarkovChain(read_file('example_txt/example.txt'))
    print(test.markov_chain(1))