"""Exercise 3 – Group numbers by sign
[4, -2, 0, 7, -5, 3]

-> {
    "positive": [4,7,3],
    "negative": [-2,-5],
    "zero": [0]
}
Write a function that groups numbers based on their sign

def group_numbers(nums: list) -> dict:
    '''

    :param nums: list of numbers
    :return: dictionary with keys:
             "positive", "negative", "zero"
             and lists of numbers for each category
    '''
    pass"""
from pprint import pprint
def group_numbers(nums: list) -> dict:
    '''
    :param nums: list of numbers
    :return: dictionary with keys:
             "positive", "negative", "zero"
             and lists of numbers for each category
    '''
    dict1 = {
        "positive": [],
        "negative": [],
        "zero": []
    }
    for num in nums:
        if num > 0:
            dict1["positive"].append(num)
        elif num < 0:
            dict1["negative"].append(num)
        elif num == 0:
            dict1["zero"].append(num)
    return dict1


list_numbers = [4, -2, 0, 7, -5, 3]
type_num = group_numbers(list_numbers)
print("{")
for key, value in type_num.items():
    print(f"{key}: {value}")
print("}\n")

pprint(type_num, width=30)