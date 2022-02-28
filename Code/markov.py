from cleanup import read_file
from dictogram import Dictogram

class MarkovChain(object):
    """  """
    def __init__(self, word_list):
        super(MarkovChain, self).__init__()
        self.corpus = word_list
        self.markov_dict = {}

    
    def markov_chain(self, order):
        for index in range(0, len(self.corpus) - order + 1):
            # assign variables and check if next_word equals none
            word = self.corpus[index]
            words = []
            for i in range(0, order):
                if index+i in range(0, len(self.corpus)):
                    words.append(self.corpus[index+i])
                else:
                    i = 0
                    words.append(self.corpus[index+i])
            word_tuple = tuple(words)
            
            if index + 1 in range(0, len(self.corpus) - order):
                next_word = self.corpus[index + order]
            else:
                next_word = self.corpus[0]

            # check if word is already in markov dictionary
            if word_tuple in self.markov_dict.keys():
                # if it is, access dictogram and add next word (will add new key-value pair or increment count)
                dictogram = self.markov_dict[word_tuple]
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
                    self.markov_dict[word_tuple] = Dictogram([next_word])
        return self.markov_dict
    
    def walk_chain(self, starting_word, word_count):
        # start with matching key in markov chain as condition
        count = 0
        str = []
        current = starting_word
        while count in range(0, word_count):
            i = [item for item in self.markov_dict.keys() if current in item]
            # print(self.markov_dict.keys())
            # print(i[0])
            # print(self.markov_dict[i[0]])
            # if current_word in self.markov_dict.keys():
                # print('word found')
            str.append(current)
            current = self.markov_dict[i[0]].sample()
            count += 1
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


# remember to use if __name__ == '__main__'


if __name__ == '__main__':
    test = MarkovChain(read_file('example_txt/sherlock-holmes.txt'))
    test.markov_chain(2)
    print('___________')
    print(test.walk_chain('earth', 20))