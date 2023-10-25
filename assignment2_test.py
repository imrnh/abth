import unittest
import random
import assignment2 as ass2
from pprint import pprint

# Student Declaration
# I [insert name and Student ID here] declare that this is my own work and that 
# I have not used any code or logic from other people or from sources outside of the unit. 
# I understand that it is ok to look at COMP6010 videos and COMP6010 resources 
# and that researching how certain python operators / functions work is ok. 
# [] <== put an x in here to indicate you have read and agree to the above statements. 

def __main__():
    unittest.main()


class TestAssignment2(unittest.TestCase):

    def test_average_wam(self):
        student_data = read_data("student1.csv")
        actual_result = ass2.average_wam(student_data)
        expected_result = 53
        self.assertEqual(expected_result, actual_result)

        student_data = read_data("student2.csv")
        actual_result = ass2.average_wam(student_data)
        expected_result = 63.166
        self.assertAlmostEqual(expected_result, actual_result, 2)

        student_data = []
        actual_result = ass2.average_wam(student_data)
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

        student_data = None
        actual_result = ass2.average_wam(student_data)
        expected_result = 0
        self.assertEqual(expected_result, actual_result)


    def test_highest_wam(self):
        student_data = read_data("student1.csv")
        actual_result = ass2.highest_wam(student_data)
        expected_result = "Stephanie Hall"
        self.assertEqual(expected_result, actual_result)

        student_data = read_data("student4.csv")
        actual_result = ass2.highest_wam(student_data)
        expected_result = "Grace Hall"
        self.assertEqual(expected_result, actual_result)

        student_data = []
        actual_result = ass2.highest_wam(student_data)
        expected_result = None
        self.assertEqual(expected_result, actual_result)

        student_data = None
        actual_result = ass2.highest_wam(student_data)
        expected_result = None
        self.assertEqual(expected_result, actual_result)


    def test_most_popular_course(self):
        student_data = read_data("student4.csv")
        actual_result = ass2.most_popular_course(student_data)
        expected_result = ['Computer Science', 'Marketing']
        self.assertEqual(expected_result, actual_result)

        student_data = read_data("student5.csv")
        actual_result = ass2.most_popular_course(student_data)
        expected_result = 'Information Technology'
        self.assertEqual(expected_result, actual_result)

        student_data = []
        actual_result = ass2.most_popular_course(student_data)
        expected_result = None
        self.assertEqual(expected_result, actual_result)

        student_data = None
        actual_result = ass2.most_popular_course(student_data)
        expected_result = None
        self.assertEqual(expected_result, actual_result)


    def test_get_distinct_regions(self):
        random_obj = random.Random(28184)

        with open(ass2.avocados) as f:
            data = f.readlines()
        data = [x.strip() for x in data]
        data = [x.split(",") for x in data]
        regions = [x[13] for x in data][1:]  # Extract regions only

        expected_answer = [
            "Albany",
            "Atlanta",
            "BaltimoreWashington",
            "Boise",
            "Boston",
            "BuffaloRochester",
            "California",
            "Charlotte",
            "Chicago",
            "CincinnatiDayton",
            "Columbus",
            "DallasFtWorth",
            "Denver",
            "Detroit",
            "GrandRapids",
            "GreatLakes",
            "HarrisburgScranton",
            "HartfordSpringfield",
            "Houston",
            "Indianapolis",
            "Jacksonville",
            "LasVegas",
            "LosAngeles",
            "Louisville",
            "MiamiFtLauderdale",
            "Midsouth",
            "Nashville",
            "NewOrleansMobile",
            "NewYork",
            "Northeast",
            "NorthernNewEngland",
            "Orlando",
            "Philadelphia",
            "PhoenixTucson",
            "Pittsburgh",
            "Plains",
            "Portland",
            "RaleighGreensboro",
            "RichmondNorfolk",
            "Roanoke",
            "Sacramento",
            "SanDiego",
            "SanFrancisco",
            "Seattle",
            "SouthCarolina",
            "SouthCentral",
            "Southeast",
            "Spokane",
            "StLouis",
            "Syracuse",
            "Tampa",
            "TotalUS",
            "West",
            "WestTexNewMexico",
        ]
        actual_answer = ass2.get_distinct_regions(regions)
        self.assertEqual(expected_answer, actual_answer)
        

        random_obj.shuffle(regions)
        expected_answer = [
            "Jacksonville",
            "Southeast",
            "California",
            "Spokane",
            "SanDiego",
            "HartfordSpringfield",
            "LosAngeles",
            "Detroit",
            "Roanoke",
            "RichmondNorfolk",
            "Portland",
            "Chicago",
            "Sacramento",
            "RaleighGreensboro",
            "Columbus",
            "GrandRapids",
            "Plains",
            "MiamiFtLauderdale",
            "Boston",
            "Houston",
            "LasVegas",
            "Albany",
            "Atlanta",
            "Louisville",
            "BaltimoreWashington",
            "GreatLakes",
            "SanFrancisco",
            "SouthCentral",
            "WestTexNewMexico",
            "DallasFtWorth",
            "PhoenixTucson",
            "Nashville",
            "SouthCarolina",
            "NorthernNewEngland",
            "Philadelphia",
            "Boise",
            "HarrisburgScranton",
            "CincinnatiDayton",
            "Pittsburgh",
            "Midsouth",
            "TotalUS",
            "Indianapolis",
            "NewYork",
            "Seattle",
            "NewOrleansMobile",
            "West",
            "BuffaloRochester",
            "Denver",
            "Tampa",
            "StLouis",
            "Northeast",
            "Orlando",
            "Charlotte",
            "Syracuse",
        ]
        actual_answer = ass2.get_distinct_regions(regions)
        self.assertEqual(expected_answer, actual_answer)

        random_obj.shuffle(regions)
        expected_answer = [
            "Southeast",
            "Columbus",
            "RichmondNorfolk",
            "Boston",
            "StLouis",
            "Orlando",
            "GreatLakes",
            "RaleighGreensboro",
            "HartfordSpringfield",
            "HarrisburgScranton",
            "Atlanta",
            "Nashville",
            "Denver",
            "Boise",
            "Spokane",
            "Detroit",
            "Sacramento",
            "DallasFtWorth",
            "West",
            "GrandRapids",
            "LasVegas",
            "NewOrleansMobile",
            "Roanoke",
            "SanDiego",
            "Jacksonville",
            "Tampa",
            "MiamiFtLauderdale",
            "Chicago",
            "Philadelphia",
            "Charlotte",
            "BuffaloRochester",
            "California",
            "Indianapolis",
            "Midsouth",
            "Albany",
            "NorthernNewEngland",
            "BaltimoreWashington",
            "LosAngeles",
            "CincinnatiDayton",
            "Portland",
            "Northeast",
            "TotalUS",
            "SanFrancisco",
            "Syracuse",
            "WestTexNewMexico",
            "NewYork",
            "Louisville",
            "Pittsburgh",
            "Seattle",
            "PhoenixTucson",
            "Plains",
            "SouthCentral",
            "SouthCarolina",
            "Houston",
        ]
        actual_answer = ass2.get_distinct_regions(regions)
        self.assertEqual(expected_answer, actual_answer)


    # def test_add_spaces(self):
    #         data = ["HelloWorld", "CatDog", "ThisIsATestString", "LOTSOFCAPITALS"]
    #         expected_answer = [
    #             "Hello World",
    #             "Cat Dog",
    #             "This Is A Test String",
    #             "L O T S O F C A P I T A L S",
    #         ]
    #         ass2.add_spaces(data)
    #         self.assertEqual(expected_answer, data)

    #         data = expected_answer = [
    #             "Albany",
    #             "Atlanta",
    #             "BaltimoreWashington",
    #             "Boise",
    #             "Boston",
    #             "BuffaloRochester",
    #             "California",
    #             "Charlotte",
    #             "Chicago",
    #             "CincinnatiDayton",
    #             "Columbus",
    #             "DallasFtWorth",
    #             "Denver",
    #             "Detroit",
    #             "GrandRapids",
    #             "GreatLakes",
    #             "HarrisburgScranton",
    #             "HartfordSpringfield",
    #             "Houston",
    #             "Indianapolis",
    #         ]
    #         expected_answer = [
    #             "Albany",
    #             "Atlanta",
    #             "Baltimore Washington",
    #             "Boise",
    #             "Boston",
    #             "Buffalo Rochester",
    #             "California",
    #             "Charlotte",
    #             "Chicago",
    #             "Cincinnati Dayton",
    #             "Columbus",
    #             "Dallas Ft Worth",
    #             "Denver",
    #             "Detroit",
    #             "Grand Rapids",
    #             "Great Lakes",
    #             "Harrisburg Scranton",
    #             "Hartford Springfield",
    #             "Houston",
    #             "Indianapolis",
    #         ]
    #         ass2.add_spaces(data)
    #         self.assertEqual(expected_answer, data)


#     def test_convert_to_dict(self):
#         student_data = read_data("student1.csv")
#         actual_result = ass2.convert_to_dict(student_data.copy())

#         for row in student_data[1:]:
#             id = int(row[0])
#             self.assertEqual(row[1], actual_result[id]["first"])
#             self.assertEqual(row[2], actual_result[id]["last"])
#             self.assertEqual(int(row[3]), actual_result[id]["wam"])
#             self.assertEqual(row[4], actual_result[id]["dob"])
#             self.assertEqual(row[5], actual_result[id]["course"])


#     def test_validate_dictionary(self):
#         input = {
#             51231 : {    # as a string
#                 "first_name" : "michael",  # as a string
#                 "last_name" : "lay",  # as a string
#                 "address" : {
#                     "street_number" : 231, # as an integer,
#                     "street_name" : "Delhi", # as a string
#                 },
#             },
#         }
#         actual_result = ass2.validate_dictionary(input)
#         self.assertEqual(True, actual_result)

#         input = {
#             51231 : {    # as a string
#                 "first_name" : "michael",  # as a string
#                 "last_name" : "lay",  # as a string
#                 "address" : {
#                     "street_number" : 231, # as an integer,
#                     "street_name" : "Delhi", # as a string
#                 },
#             },
#             65161 : {    # as a string
#                 "first_name" : "john",  # as a string
#                 "last_name" : "gray",  # as a string
#                 "address" : {
#                     "street_number" : 312, # as an integer,
#                     "street_name" : "George", # as a string
#                 },
#             },
#             3123 : {    # as a string
#                 "first_name" : "phill",  # as a string
#                 "last_name" : "crew",  # as a string
#                 "address" : {
#                     "street_number" : 31, # as an integer,
#                     "street_name" : "York", # as a string
#                 },
#             },
#             71231 : {    # as a string
#                 "first_name" : "daniel",  # as a string
#                 "last_name" : "marks",  # as a string
#                 "address" : {
#                     "street_number" : 21, # as an integer,
#                     "street_name" : "Pitt", # as a string
#                 },
#             },
#         }
#         actual_result = ass2.validate_dictionary(input)
#         self.assertEqual(True, actual_result)

#         input = {
#             51231 : {    # as a string
#                 "first_name" : "michael",  # as a string
#                 "last_name" : "lay",  # as a string
#                 "address" : {
#                     "street_number" : 231, # as an integer,
#                     "street_name" : "Delhi", # as a string
#                 },
#             },
#             65161 : {    # as a string
#                 "first_name" : "john",  # as a string
#                 "last_name" : "gray",  # as a string
#                 "address" : {
#                     "street_number" : 312, # as an integer,
#                     "street_name" : "George", # as a string
#                 },
#             },
#             3123 : {    # as a string
#                 "first_name" : "phill",  # as a string
#                 "last_name" : "crew",  # as a string
#                 "address" : {
#                     "street_number" : "31", # Incorrect type here!
#                     "street_name" : "York", # as a string
#                 },
#             },
#             71231 : {    # as a string
#                 "first_name" : "daniel",  # as a string
#                 "last_name" : "marks",  # as a string
#                 "address" : {
#                     "street_number" : 21, # as an integer,
#                     "street_name" : "Pitt", # as a string
#                 },
#             },
#         }
#         actual_result = ass2.validate_dictionary(input)
#         self.assertEqual(False, actual_result)

#         input = {
#             51231 : {    
#                 "first_name" : "michael",  
#                 "last_name" : "lay",  
#                 "address" : {
#                     "street_number" : 231, 
#                     "street_name" : "Delhi",
#                 },
#             },
#             65161 : {   
#                 "first_name" : 65123,  # this is incorrect!
#                 "last_name" : "gray",  
#                 "address" : {
#                     "street_number" : 312,
#                     "street_name" : "George", 
#                 },
#             },
#         }
#         actual_result = ass2.validate_dictionary(input)
#         self.assertEqual(False, actual_result)

#         input = {
#             51231 : {    
#                 "first_name" : "michael",  
#                 "last_name" : "lay",  
#                 "address" : {
#                     "street_number" : 231, 
#                     "street_name" : "Delhi",
#                 },
#             },
#             65161 : {   
#                 "first_name" : "Sarah",
#                 "last_name" : "gray",  
#                 "dob" : "14/02/95", # Extra key here!
#                 "address" : {
#                     "street_number" : 312,
#                     "street_name" : "George", 
#                 },
#             },
#         }
#         actual_result = ass2.validate_dictionary(input)
#         self.assertEqual(False, actual_result)

#         input = {
#             51231 : {    
#                 "first_name" : "michael",  
#                 "last_name" : "lay",  
#                 "address" : {
#                     "street_number" : 231, 
#                     "street_name" : "Delhi",
#                 },
#             },
#             65161 : {   
#                 "first_name" : "Sarah",
#                 "last_name" : "gray",  
#                 "address" : {
#                     "street_number" : 312,
#                     "street_name" : "George", 
#                     "street_type" : "road", # Extra key here!
#                 },
#             },
#         }
#         actual_result = ass2.validate_dictionary(input)
#         self.assertEqual(False, actual_result)


def read_data(file: str) -> list[list[str]]:
    """
    Reads the data from the file and returns a list of lists
    :param file: the file to read from
    :return: a list of lists
    """
    with open(file) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    data = [x.split(",") for x in data]
    return data


if __name__ == "__main__":
    __main__()
