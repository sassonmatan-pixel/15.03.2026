"""7
["apple","banana","avocado","blueberry","apricot","corn"]

-> {
    "a": ["apple","avocado","apricot"],
    "b": ["banana","blueberry"],
    "c": ["corn"]
}
'''
def group_by_letter(words: list) -> dict:
    '''

    :param words: list of words
    :return: dictionary where:
             key = first letter of the word
             value = list of all words that start with that letter
    '''
    pass
    """
from pprint import pprint


def group_by_letter(words: list) -> dict:
    '''

    :param words: list of words
    :return: dictionary where:
             key = first letter of the word
             value = list of all words that start with that letter
    '''
    words.sort()
    dict1 = {}
    for word in words:
        if word[0] not in dict1:
            dict1[word[0]] = [word]
        else:
            dict1[word[0]].append(word)
    return dict1



list1 = ["apple","banana","avocado","blueberry","apricot","corn"]
gp = group_by_letter(list1)
pprint(gp)


def group_by_letter(words: list) -> dict:
    '''

    :param words: list of words
    :return: dictionary where:
             key = first letter of the word
             value = list of all words that start with that letter
    '''
    dict1 = {}
    words.sort()
    for word in words:
        for letter in word:
            if word[0] == letter:
                dict1[letter] = dict1.get(letter, []) + [word]
                break
            else:
                break
    return dict1



list1 = ["apple","banana","avocado","blueberry","apricot","corn"]
gp = group_by_letter(list1)
pprint(gp)