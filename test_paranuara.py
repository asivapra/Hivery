"""
Unit test for 'paranuara.py'

Five tests:
    1. List all employees in a specified company
    2. Say 'Company is not found' if not found in 'companies.json'
    3. Say 'Company has no employees', if this company ID is not in 'people.json.
    4. List two persons (name, age, address, phone) and their common friends (name, age, address, phone)
    5. List the favourite fruits of one person as (username, age, fruits, vegetables)
"""
import unittest
import os


class MyTestCase(unittest.TestCase):
    def test_companyName(self):
        """
        List all employees in a specified company.
        :return: List of names as a JSON object
        """
        stream = os.popen('curl -s curl http://127.0.0.1:8080/companyName/LINGOAGE')
        output = stream.read()
        stream.close()
        print("Test1: Employees in company, LINGOAGE:", output)
        exp_output = '["Sue Tyson","Hobbs Lang","Shelly Koch","Santiago Baker",' \
                     '"Lolita Walls","Shari Farrell","Gordon Wolfe"]\n'
        self.assertEqual(output, exp_output)

    def test_companyNameNotExits(self):
        """
        Say 'Company is not found' if not found in 'companies.json'
        :return: "Company is not found" as a string
        """
        stream = os.popen('curl -s curl http://127.0.0.1:8080/companyName/LINGOAGE_NOTEXIST')
        output = stream.read()
        stream.close()
        print("Test2: Non-existing company, LINGOAGE_NOTEXIST:", output)
        exp_output = '\"Company is not found\"\n'
        self.assertEqual(output, exp_output)

    def test_companyHasNoEmployees(self):
        """
        Say 'Company has no employees', if this company ID is not in 'people.json.
        :return: "Company has no employees" as a string
        """
        stream = os.popen('curl -s curl curl http://127.0.0.1:8080/companyName/BOVIS')
        output = stream.read()
        stream.close()
        exp_output = '\"Company has no employees\"\n'
        self.assertEqual(output, exp_output)
        print("Test3: No employees in company, BOVIS:", output)

    def test_persons(self):
        """
        List two persons (name, age, address, phone) and their common friends (name, age, address, phone)
        :return: Details as a JSON object of two persons and their common friends.
        """
        stream = os.popen('curl -s http://127.0.0.1:8080/persons/Lila%20Gray,Elinor%20Wiggins')
        output = stream.read()
        stream.close()
        print("Test4: Common friends between two persons, Lila Gray and Elinor Wiggins:", output)
        exp_output = '[{"address":"477 Amersfort Place, Rivera, Nebraska, 2569",' \
                     '"age":21,"name":"Lila Gray","phone":"+1 (883) 414-3615"},' \
                     '{"address":"625 Oxford Street, Rosedale, Palau, 6678",' \
                     '"age":41,"name":"Elinor Wiggins","phone":"+1 (906) 541-3699"},' \
                     '{"common_friends":[[{"name":"Decker Mckenzie"},{"age":60},' \
                     '{"address":"492 Stockton Street, Lawrence, Guam, 4854"},' \
                     '{"phone":"+1 (893) 587-3311"}],[{"name":"Mindy Beasley"},' \
                     '{"age":62},{"address":"628 Brevoort Place, Bellamy, Kansas, 2696"},' \
                     '{"phone":"+1 (862) 503-2197"}]]}]\n'
        self.assertEqual(output, exp_output)

    def test_favouriteFoods(self):
        """
        List the favourite fruits of one person as (username, age, fruits, vegetables)
        :return: Details as a JSON object of one person and their favourite fruits and vegetables
        """
        stream = os.popen('curl -s http://127.0.0.1:8080/favouriteFoods/Booth%20Haynes')
        output = stream.read()
        stream.close()
        print("Test5: Favourite fruits and vegetables of a person, Booth Haynes:", output)
        exp_output = '{"age":46,"fruits":["apple","strawberry"],"username":"Booth Haynes",' \
                     '"vegetables":["cucumber","carrot"]}\n'
        self.assertEqual(output, exp_output)


if __name__ == '__main__':
    unittest.main()
