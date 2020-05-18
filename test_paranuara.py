import unittest
import os


class MyTestCase(unittest.TestCase):
    def test_companyName(self):
        stream = os.popen('curl -s curl http://127.0.0.1:8080/companyName/LINGOAGE')
        output = stream.read()
        stream.close()
        print("Test1: Employees in company, LINGOAGE:", output)
        exp_output = '["Sue Tyson","Hobbs Lang","Shelly Koch","Santiago Baker",' \
                     '"Lolita Walls","Shari Farrell","Gordon Wolfe"]\n'
        self.assertEqual(output, exp_output)

    def test_companyNameNotExits(self):
        stream = os.popen('curl -s curl http://127.0.0.1:8080/companyName/LINGOAGE_NOTEXIST')
        output = stream.read()
        stream.close()
        print("Test2: Non-existing company, LINGOAGE_NOTEXIST:", output)
        exp_output = '\"Company is not found\"\n'
        self.assertEqual(output, exp_output)

    def test_companyHasNoEmployees(self):
        stream = os.popen('curl -s curl curl http://127.0.0.1:8080/companyName/BOVIS')
        output = stream.read()
        stream.close()
        print("Test3: No employees in company, BOVIS:", output)
        exp_output = '\"Company has no employees\"\n'
        self.assertEqual(output, exp_output)

    def test_persons(self):
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
        stream = os.popen('curl -s http://127.0.0.1:8080/favouriteFoods/Booth%20Haynes')
        output = stream.read()
        stream.close()
        print("Test5: Favourite fruits and vegetables of a person, Booth Haynes:", output)
        exp_output = '{"age":46,"fruits":["apple","strawberry"],"username":"Booth Haynes",' \
                     '"vegetables":["cucumber","carrot"]}\n'
        self.assertEqual(output, exp_output)


if __name__ == '__main__':
    unittest.main()
