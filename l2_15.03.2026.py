'''
4
{"apple":5, "banana":6, "kiwi":4} -> {5:"apple", 6:"banana", 4:"kiwi"}
'''
def reverse_dict(dict1: dict) -> dict:
    '''

    :param dict1: {<word>: <number> ... }
    :return: dict { <number>: <word> }
    '''
    dict2 = {}
    for key, value in dict1.items():
        dict2[value] = key
    return dict2
'''
5
[1,2,3,4,5,6]
-> {"even":3, "odd":3}
'''
def count_even_odd(nums: list) -> dict:
    '''
    :param nums: list of numbers
    :return: dict {"even": count_even, "odd": count_odd}
    '''
    dict1 = {"even":0, "odd":0}
    for number in nums:
        if number % 2 == 0:
            dict1["even"] += 1
        else:
            dict1["odd"] += 1
    return dict1
'''
6
cities = {
    "Tokyo": {"language": "Japanese", "population": 37_400_000, "size": 2194, "country": "Japan"},
    "Paris": {"language": "French", "population": 2_140_000, "size": 105, "country": "France"},
    "New York": {"language": "English", "population": 8_419_000, "size": 783, "country": "USA"},
    "London": {"language": "English", "population": 8_982_000, "size": 1572, "country": "UK"},
    "Madrid": {"language": "Spanish", "population": 3_223_000, "size": 604, "country": "Spain"},
    "Rome": {"language": "Italian", "population": 2_873_000, "size": 1285, "country": "Italy"}
}

-> ["Paris", "Rome", "Madrid", "New York", "London", "Tokyo"]
(sorted by population from small to big)
'''

def get_cities_sorted_by_population(cities: dict) -> list:
    '''

    :param cities: {
        <city_name>: {
            "language": <language>,
            "population": <population>,
            "size": <city_area_km2>,
            "country": <country>
        }
    }

    :return: list of city names sorted by population (small → big)
    '''
    pass

dict1 = {"apple":5, "banana":6, "kiwi":4}
rd1 = reverse_dict(dict1)
print(rd1)

list1 = [1,2,3,4,5,6]
count = count_even_odd(list1)
print(count)

cities = {
    "Tokyo": {"language": "Japanese", "population": 37_400_000, "size": 2194, "country": "Japan"},
    "Paris": {"language": "French", "population": 2_140_000, "size": 105, "country": "France"},
    "New York": {"language": "English", "population": 8_419_000, "size": 783, "country": "USA"},
    "London": {"language": "English", "population": 8_982_000, "size": 1572, "country": "UK"},
    "Madrid": {"language": "Spanish", "population": 3_223_000, "size": 604, "country": "Spain"},
    "Rome": {"language": "Italian", "population": 2_873_000, "size": 1285, "country": "Italy"}
}
list2= []
for keys, values in cities.items():
    for key, value in values.items():
        if value["population"]

