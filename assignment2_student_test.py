import unittest
import random
import assignment2 as ass2
from assignment2_test import read_data

# Student Declaration
# I [insert name and Student ID here] declare that this is my own work and that
# I have not used any code or logic from other people or from sources outside of the unit.
# I understand that it is ok to look at COMP6010 videos and COMP6010 resources
# and that researching how certain python operators / functions work is ok.
# [x] <== put an x in here to indicate you have read and agree to the above statements.


"""
TODO Your colleague John has unfortunately been let go after a series of disappointing
performance reviews. As a last act of revenge, he has modified one of the companies 
important utility functions (is_in_range, list_contains_even_number, or is_ascending).
The company has not been appropritately using version control software and only has
one copy of the file. Your job is to write a comprehensive set of unit tests to check 
each function to determine which one was modified and to ensure that in future,
if an employee modifies another function maliciously, the company is able to identify 
this quickly!

Your task is to write the unit tests for for each of the functions below. 

Marks will be awarded based on:
- The comprehensiveness of the test cases written. Do the test cases cover a 
  broad range of possible inputs to the related functions in assignment2.py?
- How well structured your test cases are. Is it easy to understand what is being 
  tested and why? Comments will be useful for describing the intent of test cases, 
  but the code should also be well written.
- The correctness of the tests written.

Please answer the following question after completing your unit tests. 
The answers to these questions and your explanations are worth ____ marks.


Which function had the incorrect implementation based on the specifications given? (2 mark)
Your answer: All the functions were correct.


How did you identify this implementation error? Which test case specifically revealed this? (4 marks)
Your answer: All the test case contributed.

"""


def __main__():
    unittest.main()


class TestAssignment2(unittest.TestCase):
    def test_is_in_range(self):
        self.assertTrue(ass2.is_in_range(8, 1, 10))
        self.assertTrue(ass2.is_in_range(1, 1, 10))
        self.assertFalse(ass2.is_in_range(0, 1, 10))
        self.assertTrue(ass2.is_in_range(10, 1, 10))
        self.assertFalse(ass2.is_in_range(11, 1, 10))

    def test_list_contains_even(self):
        self.assertTrue(ass2.list_contains_even([1, 2, 3, 4, 5, 6]))
        self.assertTrue(ass2.list_contains_even([1, 3, 5, 7, 9, 10]))
        self.assertFalse(ass2.list_contains_even([1, 3, 5, 7, 9]))
        self.assertFalse(ass2.list_contains_even([]))

    def test_is_ascending(self):
        self.assertTrue(ass2.is_ascending([1, 2, 3, 4, 5, 6]))
        self.assertFalse(ass2.is_ascending([1, 2, 3, 4, 6, 6]))
        self.assertFalse(ass2.is_ascending([11, 3, 15, 7, 9]))

    def test_average_wam(self):
        student_data = read_data("student3.csv")
        actual_result = ass2.average_wam(student_data)
        expected_result = 74.35
        self.assertAlmostEqual(expected_result, actual_result, 2)

        student_data = read_data("student4.csv")
        actual_result = ass2.average_wam(student_data)
        expected_result = 81.567
        self.assertAlmostEqual(expected_result, actual_result, 2)

        student_data = read_data("student5.csv")
        actual_result = ass2.average_wam(student_data)
        expected_result = 81.5
        self.assertAlmostEqual(expected_result, actual_result, 2)

        student_data = [
            [110, "Olivia", "Harris", 53, "1994-06-28", "Sociology"],
            [117, "William", "Garcia", 64, "1987-04-08", "Philosophy"],
            [130, "Liam", "Martin", 98, "1987-12-03", "Management"],
            [138, "Olivia", "Lopez", 25, "1987-01-31", "Psychiatry"],
            [156, "Harper", "Johnson", 58, "1993-07-17", "Developmental Biology"],
        ]
        actual_result = ass2.average_wam(student_data)
        expected_result = 61.25
        self.assertAlmostEqual(expected_result, actual_result)

        student_data = []
        actual_result = ass2.average_wam(student_data)
        expected_result = 0.0
        self.assertAlmostEqual(expected_result, actual_result)

    def test_highest_wam(self):
        student_data = read_data("student2.csv")
        actual_result = ass2.highest_wam(student_data)
        expected_result = "Liam Martin"
        self.assertEqual(expected_result, actual_result)

        student_data = read_data("student5.csv")
        actual_result = ass2.highest_wam(student_data)
        expected_result = "Grace Hall"
        self.assertEqual(expected_result, actual_result)

        student_data = []
        actual_result = ass2.highest_wam(student_data)
        expected_result = None
        self.assertEqual(expected_result, actual_result)

        student_data = [
            [110, "Olivia", "Harris", 53, "1994-06-28", "Sociology"],
            [117, "William", "Garcia", 64, "1987-04-08", "Philosophy"],
            [130, "Liam", "Martin", 98, "1987-12-03", "Management"],
            [138, "Olivia", "Lopez", 25, "1987-01-31", "Psychiatry"],
            [156, "Harper", "Johnson", 58, "1993-07-17", "Developmental Biology"],
        ]
        actual_result = ass2.highest_wam(student_data)
        expected_result = "Liam Martin"
        self.assertEqual(expected_result, actual_result)

        student_data = []
        actual_result = ass2.highest_wam(student_data)
        expected_result = None
        self.assertEqual(expected_result, actual_result)

        student_data = [
            [13, "Mark", "Davis", 91, "1994-08-28", "History"],
            [43, "Steven", "Clark", 94, "1998-03-09", "Information Technology"],
            [19, "Michelle", "Smith", 82, "1987-03-07", "Marketing"],
            [29, "William", "Garcia", 94, "1987-05-08", "History"],
            [60, "Lauren", "Mitchell", 80, "1991-12-15", "Information Technology"],
            [48, "Sarah", "Thomas", 79, "1988-04-29", "Information Technology"],
            [53, "Andrew", "Jones", 63, "1998-02-28", "History"],
            [128, "Emma", "Davis", 73, "1998-08-22", "History"],
            [2, "Jane", "Doe", 75, "1988-08-23", "History"],
            [107, "Michael", "Johnson", 73, "1993-09-07", "Information Technology"],
        ]

        actual_result = ass2.highest_wam(student_data)
        expected_result = "Steven Clark" # the first one with highest WAM counts even though we have multiple with highest wam value = 94
        self.assertEqual(expected_result, actual_result)

    def test_most_popular_course(self):
        student_data = read_data("student3.csv")
        actual_result = ass2.most_popular_course(student_data)
        expected_result = [
            "Engineering",
            "Mathematics",
            "Computer Science",
            "Psychology",
            "History",
            "English Literature",
            "Economics",
            "Chemistry",
            "Physics",
            "Sociology",
            "Political Science",
            "Statistics",
            "Biology",
            "Geography",
            "Environmental Science",
            "Anthropology",
            "Philosophy",
            "Music",
            "Art",
            "Theater",
            "Architecture",
            "Marketing",
            "Finance",
            "Communications",
            "Graphic Design",
            "Education",
            "Journalism",
            "Linguistics",
            "International Relations",
            "Management",
            "Public Relations",
            "Advertising",
            "Information Technology",
            "Human Resources",
            "Criminal Justice",
            "Nursing",
            "Physical Therapy",
            "Psychiatry",
            "Epidemiology",
            "Social Work",
            "Public Health",
            "Occupational Therapy",
            "Kinesiology",
            "Optometry",
            "Dentistry",
            "Pharmacy",
            "Medicine",
            "Veterinary Medicine",
            "Neuroscience",
            "Genetics",
            "Microbiology",
            "Immunology",
            "Biochemistry",
            "Cell Biology",
            "Molecular Biology",
            "Developmental Biology",
            "Plant Biology",
            "Animal Biology",
            "Ecology",
            "Marine Biology",
        ]
        self.assertEqual(expected_result, actual_result)

        student_data = []
        actual_result = ass2.most_popular_course(student_data)
        expected_result = None
        self.assertEqual(expected_result, actual_result)

    def test_add_spaces(self):
        data = [
            "NewYork",
            "Boston",
            "AndorraLaVella",
            "CapeTown",
            "KualaLumpur",
            "Portonovo",
        ]  # Must not convert to `Porto Novo` even if it is original form.
        expected_answer = [
            "New York",
            "Boston",
            "Andorra La Vella",
            "Cape Town",
            "Kuala Lumpur",
            "Portonovo",
        ]
        ass2.add_spaces(data)
        self.assertEqual(expected_answer, data)

    def test_convert_to_dict(self):
        student_data = read_data("student2.csv")
        actual_result = ass2.convert_to_dict(student_data.copy())

        for row in student_data[1:]:
            id = int(row[0]) - 100  # id starts from 101
            self.assertEqual(row[1], actual_result[id]["first"])
            self.assertEqual(row[2], actual_result[id]["last"])
            self.assertEqual(int(row[3]), actual_result[id]["wam"])
            self.assertEqual(row[4], actual_result[id]["dob"])
            self.assertEqual(row[5], actual_result[id]["course"])

        student_data = []
        actual_result = ass2.convert_to_dict(student_data.copy())
        self.assertEqual(actual_result, [{}])

    def test_validate_dictionary(self):
        input = {
            23234: {
                "first_name": "Liam",
                "last_name": "William",
                "address": {
                    "street_number": 294,
                    "street_name": "Auckland",
                },
            },
            99123: "An example string",
        }
        actual_result = ass2.validate_dictionary(input)
        self.assertEqual(False, actual_result)

        input = {
            99584: {
                "first_name": "Liam",
                "last_name": "William",
                "address": {
                    "street_number": 294,
                    "street_name": "Auckland",
                },
                "country": "New Zealand",  # Extra key here!
            },
        }
        actual_result = ass2.validate_dictionary(input)
        self.assertEqual(False, actual_result)


if __name__ == "__main__":
    __main__()
