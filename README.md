# Paranuara Challenge

## Solution and How to Test
The program is written in Python and uses Flask. It can be
tested on any server where Python 3 and Flask are installed.

### Steps to install and run the API
-   Copy these files into the same directory
    -   paranuara.py
    -   companies.json
    -   people.json   
- Check Python version
    - $ python --version
        - Python 3.7.4
- Check Flash version
    - $ python
        - \>>> import pkg_resources
        - \>>> pkg_resources.get_distribution('flask').version
            - '1.1.1'
- Run the API
    - $ python paranuara.py&
         * Serving Flask app "paranuara" (lazy loading)
         * Environment: production
           WARNING: This is a development server. Do not use it in a production deployment.
           Use a production WSGI server instead.
         * Debug mode: off
         * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)

### Call the API to get outputs
- Get all employees in a specified company
    - curl http://127.0.0.1:8080/companyName/LINGOAGE
- Find common friends between two people
    - curl http://127.0.0.1:8080/persons/Lila%20Gray,Elinor%20Wiggins
        - Note: Comma separated names. Spaces in names must be encoded as %20    
- Find favourite foods of a specified person
    - curl http://127.0.0.1:8080/favouriteFoods/Booth%20Haynes
    
# Project specifications
        
Paranuara is a class-m planet. Those types of planets can support human life, for that reason the president of the Checktoporov decides to send some people to colonise this new planet and
reduce the number of people in their own country. After 10 years, the new president wants to know how the new colony is growing, and wants some information about his citizens. Hence he hired you to build a rest API to provide the desired information.

The government from Paranuara will provide you two json files (located at resource folder) which will provide information about all the citizens in Paranuara (name, age, friends list, fruits and vegetables they like to eat...) and all founded companies on that planet.
Unfortunately, the systems are not that evolved yet, thus you need to clean and organise the data before use.
For example, instead of providing a list of fruits and vegetables their citizens like, they are providing a list of favourite food, and you will need to split that list (please, check below the options for fruits and vegetables).

## New Features
Your API must provides these end points:
- Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.
- Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: 
`{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`

## Delivery
To deliver your system, you need to send the link on GitHub. Your solution must provide tasks to install dependencies, build the system and run. Solutions that does not fit this criteria **will not be accepted** as a solution. Assume that we have already installed in our environment Java, Ruby, Node.js, Python, MySQL, MongoDB and Redis; any other technologies required must be installed in the install dependencies task. Moreover well tested and designed systems are one of the main criteria of this assessement 

## Evaluation criteria
- Solutions written in Python would be preferred.
- Installation instructions that work.
- During installation, we may use different companies.json or people.json files.
- The API must work.
- Tests

Feel free to reach to your point of contact for clarification if you have any questions.
