from flask import Flask, jsonify
import json
import sys

# Read the companies name and index numbers into a dict
try:
	infile = 'companies.json'
	companies_data = open (infile)
except:
	print("Missing the company list:", infile)
	sys.exit()

companies_array = json.load(companies_data)

try:
	infile = 'people.json'
	people_data = open (infile)
except:
	print("Missing the people list:", infile)
	sys.exit()

people_array = json.load(people_data)

app = Flask(__name__)

#- Given a company, the API needs to return all their employees. 
# Provide the appropriate solution if the company does not have any employees.
# Example Usage: curl http://127.0.0.1:8080/companyName/LINGOAGE
# Example Usage: curl http://127.0.0.1:8080/companyName/LINGOAGEBLAH # No company
# Example Usage: curl http://127.0.0.1:8080/companyName/BOVIS	# No employees. After editing people.json to change all 'company_id: 13' to 'company_id: 130'
def getEmployees(i, employees):
	id = companies_array[i]['index']
	for j in range(len(people_array)):
		if people_array[j]['company_id'] == id:
			employees.append(people_array[j]['name'])
	return employees


@app.route("/companyName/<name>", methods=["GET"])
def getCompanyByName(name):
	employees = []
	for i in range(len(companies_array)):
		if companies_array[i]['company'] == name:
			employees = getEmployees(i, employees)
			if len(employees):
				return jsonify(employees)
			else:
				return jsonify("Company has no employees")				
	return jsonify("Company is not found")


# Given 2 people, provide their information (Name, Age, Address, phone) 
# and the list of their friends in common which have brown eyes and are still alive.
# Example Usage: curl http://127.0.0.1:8080/persons/Booth%20Haynes,Lila%20Gray # One common friend
# Example Usage: curl http://127.0.0.1:8080/persons/Lila%20Gray,Elinor%20Wiggins # Multiple common friends
def getCommonFriends(persons):
	cf = []
	p1f = persons[0]['friends']
	p2f = persons[1]['friends']
	for i in range (len(p1f)):
		cfd = []
		for j in range (len(p2f)):
			if (p1f[i]['index'] == p2f[j]['index']):
					fi = p1f[i]['index']
					# Is this friend alive?
					if (not people_array[fi]['has_died']):
						# Is the eye color brown?
						if (people_array[fi]['eyeColor'] == 'brown'):
							cfd.append({"name":people_array[fi]['name']})
							cfd.append({"age":people_array[fi]['age']})
							cfd.append({"address":people_array[fi]['address']})
							cfd.append({"phone":people_array[fi]['phone']})
							cf.append(cfd)
					break
	return cf
					
		
@app.route("/persons/<names>", methods=["GET"])
def getPersons(names):
	persons = []
	names = names.split(',')
	for name in names:
		person_details = {}
		for j in range(len(people_array)):
			if people_array[j]['name'] == name:
				person_details['name'] = people_array[j]['name']
				person_details['age'] = people_array[j]['age']
				person_details['address'] = people_array[j]['address']
				person_details['phone'] = people_array[j]['phone']
				person_details['friends'] = people_array[j]['friends']
				persons.append(person_details)
				continue
	common_friends = getCommonFriends(persons)

	# Remove the list of friends in each person  
	del persons[0]['friends']
	del persons[1]['friends']
	
	# Append the common friends
	persons.append({"common_friends":common_friends})
	return jsonify(persons)


# Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: 
#`{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`
# Example Usage: curl http://127.0.0.1:8080/favouriteFoods/Booth%20Haynes
@app.route("/favouriteFoods/<name>", methods=["GET"])
def getFavouriteFoods(name):
	fruits = ["apple", "banana", "orange", "strawberry"]
	vegetables = ["beetroot", "carrot", "celery", "cucumber" ]
	person_details = {}
	fav_fruits = []
	fav_vegs = []
	for j in range(len(people_array)):
		if people_array[j]['name'] == name:
			person_details['username'] = people_array[j]['name']
			person_details['age'] = people_array[j]['age']
			favouriteFood = people_array[j]['favouriteFood']
			for i in range(len(favouriteFood)):
				if (favouriteFood[i] in fruits):
					fav_fruits.append(favouriteFood[i])
				if (favouriteFood[i] in vegetables):
					fav_vegs.append(favouriteFood[i])
			person_details['fruits'] = fav_fruits
			person_details['vegetables'] = fav_vegs
			break
	return person_details
	

if __name__ == '__main__':
	app.run(port=8080)
	
	
