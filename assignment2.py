from typing import Union

"""
Please note the following assignment guidelines
1. You are not allowed to use any additional libraries other than the ones already imported. 
    Importing other libraries will result in a mark of 0 for this assignment.
2. You are not allowed to change any function names or their parameters
    Changing any function names or their parameters will result in 0 marks for the relevant function.
3. You must not hardcode any values inside your functions (this will be manually checked)
    Hardcoding values will result in 0 marks for the relevant function.

Datasets were taken from the following sources:
https://www.kaggle.com/neuromusic/avocado-prices
"""

avocados = "avocado.csv"


def is_in_range(number: int, left: int, right: int) -> bool:
    """
    Checks if a given number is between two other passed numbers (inclusive on both sides)

    TODO Your task is to write the unit tests for this function in the 
    assignment2_student_test.py file. More information is available in
    the assignment2_student_test.py file or in the assignment specification
    on ilearn.

    Args:
        number (int): the number to check is in range
        left (int): the lower side of the range
        right (int): the upper side of the range

    Returns:
        bool: True if number is between left and right (inclusive), False otherwise
    """
    if number >= left and number <= right:
        return True
    else:
        return False


def list_contains_even(numbers: list[int]) -> bool:
    """
    Checks if a given list contains at least one even number

    TODO Your task is to write the unit tests for this function in the 
    assignment2_student_test.py file. More information is available in
    the assignment2_student_test.py file or in the assignment specification
    on ilearn.

    Args:
        numbers (list[int]): the list to check

    Returns:
        bool: True if the list contains at least one even, False otherwise
    """
    for value in numbers:
        if value % 2 == 0:
            return True
    return False


def is_ascending(numbers: list[int]) -> bool:
    """
    Checks if a given list is in ascending order. For each number in the list, 
    the following value should be more then or equal to the current value

    TODO Your task is to write the unit tests for this function in the 
    assignment2_student_test.py file. More information is available in
    the assignment2_student_test.py file or in the assignment specification
    on ilearn.

    Args:
        numbers (list[int]): the list to check

    Returns:
        bool: True if the list is ascending, False otherwise
    """
    for i in range(0, len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            return False
    return True


def average_wam(data: list[list[str]]) -> float:
    """_summary_
    Given a list of lists where each sublist contains data about students using the following scheme:
    [id, first, last, wam, dob, age, course]
    Calculate the average wam of all students in the list.
    The first row in the passed list contains the column names. This should be ignored.

    Args:
        data (list[list[str]]): the list to process

    Returns:
        float: the average wam of all students in the list
    """
    _sum = 0.0

    try:
        for ix, dp in enumerate(data):
            if ix > 0:
                _sum += float(dp[3])
        return _sum / (len(data) - 1)
    except:
        return _sum



def highest_wam(data: list[list[str]]) -> Union[str, None]:
    """_summary_
    Given a list of lists where each sublist contains data about students using the following scheme:
    [id, first, last, wam, dob, age, course]
    Return the full name of the student with the highest wam. If there are multiple students tied for 
    the highest wam, the first students name should be returned. Return None if there is no valid data
    The first row in the passed list contains the column names. This should be ignored.

    Args:
        data (list[list[str]]): the list to process

    Returns:
        Union[str, None]: the full name of the student with the highest wam, or None if there is no valid data
    """

    full_name = None
    curr_max = -1e10  # starting with a minimum

    try:
        for ix, cursor in enumerate(data):
            if ix > 0:
                dp = float(cursor[3])
                if dp > curr_max:
                    full_name = cursor[1] + ' ' + cursor[2]
                    curr_max = dp

    except:
        pass
    
    return full_name


def most_popular_course(data: list[list[str]]) -> Union[str, list[str], None]:
    """_summary_
    Given a list of lists where each sublist contains data about students using the following scheme:
    [id, first, last, wam, dob, age, course]
    Determine the most popular course and return it as a string. If multiple courses are equally popular, return a list of courses based on their order in the original list.
    Return None if there is no valid data.
    The first row in the passed list contains the column names. This should be ignored.

    Args:
        data (list[list[str]]): the list to process

    Returns:
        Union[str, list[str], None]: the name of the most popular course, or a list of the most popular courses if there is more than one
    """
    course_counter = {}

    
    try:
        # storing course count info.
        for ix, cursor in enumerate(data):
            if ix > 0:
                course = cursor[-1]
                if course in course_counter:
                    course_counter[course] += 1
                else:
                    course_counter[course] = 1
        
        max_count = -1e9
        for key in course_counter:
            val = course_counter[key]

            if val > max_count:
                max_count = val

        max_occured_courses = []
        for key in course_counter:
            val = course_counter[key]

            if val == max_count:
                max_occured_courses.append(key)

        
        #retur only single value if the list is of single value. Otherwise, return the whole list.
        if len(max_occured_courses) == 0:
            return None
        elif len(max_occured_courses) == 1:
            return max_occured_courses[0]
        else:
            return max_occured_courses
    
    except:
        return None    # if no list provided, return none.

def get_distinct_regions(list: list[str]) -> list[str]:
    """
    Returns all distinct regions from the list passed. The order of the regions should be the same as the order in which they appear in the list.

    Args:
        list (str): a list of region names (strings)

    Returns:
        list[str]: a list of all unique regions from the list passed
    """

    disctinct_regions = []
    for rg in list:
        if rg not in disctinct_regions:
            disctinct_regions.append(rg)

    return disctinct_regions


def add_spaces(list: list[str]):
    """
    Add a space before any capital letters in each string in the list passed.
    A space should not be added before the first letter of the string. This 
    function should modify the original list.

    Args:
        list (list[str]): a list of strings  
    """
    return []  # TODO Remove me to get started!


def convert_to_dict(list: list[list[str]]) -> dict:
    """_summary_
    Given a list of lists where each sublist contains data about students using the following scheme:
    [id, first, last, wam, dob, age, course]

    Return a dictionary using the following scheme:
    {
        id: {  # A combination of the id combined with the region and year with no spaces
            "first" : first,
            "last" : last,
            "wam" : wam,
            "dob" : dob,
            "course" : course,  # The extra comma at the end is okay in Python! 
        },
        ...
    }
    Numeric data should be converted to integers and floats where appropriate
    The first row in the passed list contains the column names. Your returned dictionary should not include this row.



    Args:
        list (list[list[str]]): the list to convert

    Returns:
        dict: a dictionary with the scheme described above
    """
    return {}  # TODO Remove me to get started!


def validate_dictionary(data) -> bool:
    """
    Passed a dictionary, validate that the dictionary follows the given scheme below:

    {
        id  : {    # as an integer
            "first_name" : first,  # as a string
            "last_name" : last,  # as a string
            "address" : {
                "street_number" : number # as an integer,
                "street_name" : name # as a string
            },
        },
        id  : {    # as an integer
            "first_name" : first,  # as a string
            "last_name" : last,  # as a string
            "address" : {
                "street_number" : number # as an integer,
                "street_name" : name # as a string
            },
        },
        ...
    }

    Args:
        data (_type_): the dictionary to verify

    Returns:
        bool: True if the passed dictionary follows the scheme specified above, False otherwise
    """
    return False  # TODO Remove me to get started!
