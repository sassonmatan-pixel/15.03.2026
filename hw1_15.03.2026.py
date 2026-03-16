"""Write a function that groups words by number of letters

The key should be the length of the word, and the value should be a list of all words with that length"""
from pprint import pprint
def group_words_by_length(words: list) -> dict:
    '''

    :param words: list of words
    :return: dict { <length>: [list of words with that length] }
    '''
    dict_fruits = {}
    for word in words:
        if len(word) not in dict_fruits:
            dict_fruits[len(word)] = [word]
        else:
            dict_fruits[len(word)].append(word)
    return dict_fruits
""""
-> {
    5: ["apple","grape","melon"],
    6: ["banana"],
    4: ["kiwi","pear"]
}"""
list_fruits = ["apple","banana","kiwi","grape","melon","pear"]
list_fruits_sorted = group_words_by_length(list_fruits)
pprint(list_fruits_sorted, width=60)
