# netflix-API

## Technology Used:
    Python, Flask-Restful, Pandas, Postman for testing

## Instructions:

### Prerequisites:
    1. Python3 should be installed on the system.

### To run the project locally, follow the following steps:
    1. Setup a virtual environment:
        For ubuntu:
            1. sudo apt install virtualenv
            2. virtualenv -p python3 name_of_environment
            3. To activate: source name_of_environment/bin/activate
        For windows:
            1.	pip install virtualenv
            2.	python -m venv <path for creating virtualenv>
            3.	To activate: <virtualenv path>\Scripts\activate

    2. Clone the repository: git clone https://github.com/Pirate2606/netflix-API
    3. Change the directory: cd netflix-API
    4. Install the requirements: pip install -r requirements.txt
    5. Run the server: python3 app.py
    6. Use Postman to fetch results from API using following endpoints:
        -> Get all show titles: http://127.0.0.1:5000/titles
        -> Get data about specific show: http://127.0.0.1:5000/title/<string:title>
        -> Get shows based on their type: http://127.0.0.1:5000/type/<string:type_>
        -> Get shows by director name: http://127.0.0.1:5000/director/<string:director>
        -> Get shows based on their release year: http://127.0.0.1:5000/years
        -> Get shows for a particular year: http://127.0.0.1:5000/year/<int:year>