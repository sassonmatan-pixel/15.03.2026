
'''
1
["apple","banana","kiwi","grape","kiwi"] -> {"apple":5, "banana":6, "kiwi":4, "grape":5 }
'''
def get_len_word(list1: list) -> dict:
    '''

    :param list1: list of words
    :return: dict { <word>: <how many letters (len) > }
    '''
    dict1 = {}
    for word in list1:
        dict1[word] = len(word)
    return dict1

'''
2
grades = {"Tom":80, "Anna":95, "John":70} -> (Anna , 95)
'''
def get_max(dict1: dict) -> tuple:
    '''

    :param dict1: {<name>: <grade> ... }
    :return: (<name>, <grade>) of the max student
    '''
    x = max(dict1.values())
    for k, v in dict1.items():
        if v == x:
            return k, x

'''
3
count repetition
[4, 2, 1, 2, 3, -1, 3, 2, 2] -> { 1: 1, 2: 4, 3: 2, 4: 1, -1: 1}
'''
def get_count(list1: list) -> dict:
    '''

    :param list1: list of numbers
    :return: dict { <number>: <how many times appear> }
    '''
    dict1 = {}
    for number in set(list1):
        dict1[number] = list1.count(number)
    return dict1

list1 = ["apple","banana","kiwi","grape","kiwi"]
len_word = get_len_word(list1)
print(len_word)

grades = {"Tom":80, "Anna":95, "John":70}
max_grades = get_max(grades)
print(max_grades)

list2 = [4, 2, 1, 2, 3, -1, 3, 2, 2]
dict2 = get_count(list2)
print(dict2)