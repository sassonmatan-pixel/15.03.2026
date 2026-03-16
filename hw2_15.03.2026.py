"""Exercise 2 – Average grade
grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}

-> 82.5
Write a function that calculates the average grade of all students

def get_average_grade(grades: dict) -> float:
    '''

    :param grades: {<name>: <grade>}
    :return: average grade of all students
    '''
    pass"""


import statistics
def get_average_grade(grades: dict) -> float:
    '''
    :param grades: {<name>: <grade>}
    :return: average grade of all students
    '''
    list_grades = []
    for grade in grades.values():
        list_grades.append(grade)
    avg = statistics.mean(list_grades)
    return avg

grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}
avg_grade = get_average_grade(grades)
print("The avg is:",avg_grade)