import random, sys

def rearrange(words_list):
    random.shuffle(words_list)
    
    lst_to_str = ""
    for i in words_list:
        lst_to_str += f'{i} '
    
    return print(lst_to_str)
    
    
    # for i in words_list:
    #     print(str(i), end=" ")
    # return print(words_list)

if __name__ == "__main__":
    params = sys.argv[1:]
    rearrange(params)

