"""
Paranuara Challenge
Created by: Dr. Arapaut V. Sivaprasad on 17 May, 2020
Last modified on: 18 May, 2020

Your API must provides these end points:

- Given a company, the API needs to return all their employees. Provide the
appropriate solution if the company does not have any employees.

- Given 2 people, provide their information (Name, Age, Address, phone) and
the list of their friends in common which have brown eyes and are still alive.

- Given 1 people, provide a list of fruits and vegetables they like.
This endpoint must respect this interface for the output:
{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"],
"vegetables": ["beetroot", "lettuce"]}
"""

from flask import Flask, jsonify
import json
import sys

# Read the company names and index numbers into a dict
try:
    infile = 'companies.json'
    companies_json = open(infile)

except FileNotFoundError as e1:
    print("Missing the company list.", e1)
    sys.exit()

companies_dict = json.load(companies_json)

# Read the people names and index numbers into a dict
try:
    infile = 'people.json'
    people_json = open(infile)

except FileNotFoundError as e2:
    print("Missing the people list.", e2)
    sys.exit()

people_dict = json.load(people_json)

app = Flask(__name__)


# Given a company, the API needs to return all their employees.
# Provide the appropriate solution if the company does not have any employees.
# Example Usage: curl http://127.0.0.1:8080/companyName/LINGOAGE
# Example Usage: curl http://127.0.0.1:8080/companyName/LINGOAGE_NOTEXIST # No company exists
# Example Usage: curl http://127.0.0.1:8080/companyName/BOVIS	# No employees in the company.
#   After editing people.json to change all 'company_id: 13' to 'company_id: 130'


@app.route("/companyName/<name>", methods=["GET"])
def getCompanyByName(name):
    # Get the index of the company
    for idx in range(len(companies_dict)):
        if companies_dict[idx]['company'] == name:
            # Pass the idx to a function to retrieve all employees
            employees = getEmployees(idx)
            # Return the employees, if any, as an array
            if len(employees):
                return jsonify(employees)
            # Company exists but there is no employee.
            else:
                return jsonify("Company has no employees")
    # The company does not exist. It could be a typo in the name
    return jsonify("Company is not found")


def getEmployees(idx):
    employees = []  # Initialise an empty array
    for j in range(len(people_dict)):
        if people_dict[j]['company_id'] == idx:
            # Add the names of all employees. Use a dict if more details are required
            employees.append(people_dict[j]['name'])
    return employees


# ------------------------------------------------------------------------------
# Given 2 people, provide their information (Name, Age, Address, phone) 
# and the list of their friends in common which have brown eyes and are still alive.
# Example Usage: curl http://127.0.0.1:8080/persons/Booth%20Haynes,Lila%20Gray # One common friend
# Example Usage: curl http://127.0.0.1:8080/persons/Lila%20Gray,Elinor%20Wiggins # Multiple common friends


@app.route("/persons/<names>", methods=["GET"])
def getPersons(names):
    persons = []
    names = names.split(',')

    # Check that two names are given as comma-separated.
    if len(names) != 2:
        return "Error: Exactly two names must be given.\n"

    for name in names:
        person_details = {}
        for j in range(len(people_dict)):
            if people_dict[j]['name'] == name:
                person_details['name'] = people_dict[j]['name']
                person_details['age'] = people_dict[j]['age']
                person_details['address'] = people_dict[j]['address']
                person_details['phone'] = people_dict[j]['phone']
                person_details['friends'] = people_dict[j]['friends']
                persons.append(person_details)
                continue

    # Check that two names have been retrieved
    if len(persons) != 2:
        return "Error: One/nil person was found.\n"

    common_friends = getCommonFriends(persons)

    # Remove the list of friends in each person so that only Name, Age, Address and Phone are displayed
    del persons[0]['friends']
    del persons[1]['friends']

    # Append the common friends
    persons.append({"common_friends": common_friends})
    return jsonify(persons)


def getCommonFriends(persons):
    """
    Find the common friends who are still alive and have brown eyes.
    :param persons: List of names
    :return: Array of dict objects for each common friend (name, age, address, phone)
    """
    cf = []  # Empty list to hold the common friends
    p1f = persons[0]['friends']  # List of friends for person 1
    p2f = persons[1]['friends']  # List of friends for person 2
    for i in range(len(p1f)):
        cfd = []  # Empty array to hold common friends
        for j in range(len(p2f)):
            if p1f[i]['index'] == p2f[j]['index']:
                fi = p1f[i]['index']
                # Is this friend alive?
                if not people_dict[fi]['has_died']:
                    # Is the eye color brown?
                    if people_dict[fi]['eyeColor'] == 'brown':
                        # Name, Age, Address and Phone for all common friends are added
                        cfd.append({"name": people_dict[fi]['name']})
                        cfd.append({"age": people_dict[fi]['age']})
                        cfd.append({"address": people_dict[fi]['address']})
                        cfd.append({"phone": people_dict[fi]['phone']})
                        cf.append(cfd)
                break
    return cf


# Given 1 people, provide a list of fruits and vegetables they like.
# This endpoint must respect this interface for the output:
# `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`
# Example Usage: curl http://127.0.0.1:8080/favouriteFoods/Booth%20Haynes


@app.route("/favouriteFoods/<name>", methods=["GET"])
def getFavouriteFoods(name):
    """
    Given a name, return the details (username, age) and the favourite fruits and vegetables.
        There are only 4 fruits and 4 vegetables in 'people.json'.
        This code will not work properly if 'people.json' lists other fruits or vegetables
    :param name: name of person. Spaces changed to %20
    :return: JSON object of person's details plus favourite fruits and vegetables.
    """
    person_details = {}
    for j in range(len(people_dict)):
        if people_dict[j]['name'] == name:
            person_details['username'] = people_dict[j]['name']
            person_details['age'] = people_dict[j]['age']
            favouriteFood = people_dict[j]['favouriteFood']
            fav_fruits = getFruits(favouriteFood)
            fav_vegis = getVegetables(favouriteFood)
            person_details['fruits'] = fav_fruits
            person_details['vegetables'] = fav_vegis
            break

    person_details = checkDetails(name, person_details)
    return person_details


def getFruits(favouriteFood):
    """
    Find the items in 'favouriteFood' belonging to the fruits list.
    :param favouriteFood: List of items
    :return: fav_fruits: List of items
    """
    fruits = ["apple", "banana", "orange", "strawberry"]
    fav_fruits = []
    for i in range(len(favouriteFood)):
        if favouriteFood[i] in fruits:
            fav_fruits.append(favouriteFood[i])
    return fav_fruits


def getVegetables(favouriteFood):
    """
    Find the items in 'favouriteFood' belonging to the vegetables list.
    :param favouriteFood: List of items
    :return: fav_vegis: List of items
    """
    vegetables = ["beetroot", "carrot", "celery", "cucumber"]
    fav_vegis = []
    for i in range(len(favouriteFood)):
        if favouriteFood[i] in vegetables:
            fav_vegis.append(favouriteFood[i])
    return fav_vegis


def checkDetails(name, person_details):
    """
    Check whether the name exists and the person has any favourite fruit and/or vegetables
    Send as 'fruits: Not Found' if the person has no key for 'favouriteFood' or it has no fruits.
    Send as 'vegetables: Not Found' if the person has no key for 'favouriteFood' or it has no vegetabless.
    Send as 'name: Not Found if name is misspelled or missing
    :param name: Name of the person.
    :param person_details: Dict object.
    :return: Send altered dict object
    """
    # If the person is not found, say 'Not Found'
    keys = person_details.keys()
    try:
        if len(person_details.keys()) == 0:
            person_details[name] = "Not Found"
        elif 'fruits' not in keys:
            person_details['fruits'] = "Not Found"
        elif 'vegetables' not in keys:
            person_details['vegetables'] = "Not Found"
    except Exception as err:
        print("Error:", err)
    return person_details


if __name__ == '__main__':
    app.run(port=8080)
