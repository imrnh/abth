import unittest
import random
import assignment2 as ass2

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


if __name__ == "__main__":
    __main__()
