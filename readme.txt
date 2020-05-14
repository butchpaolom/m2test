1. Install xampp and run the mysql server, copy the port and replace the current port in the settings.py at ../crudmysql
2. Install the packages required using pip. I used python 3.7.4.
Open the cli in ../crudmysql and type pip install -r requirements.txt
3. at ../crudmysql, open the cli and type the commands
python manage.py makemigrations
python manage.py migrate
python manage.py runserver localhost:8080
4. to test the backend these are the following endpoints
GET - /api/people/ - returns list of records
GET - /api/people/'id'/ - returns specific record using id parameter, ex. /api/people/1
POST - /api/people/ - creates an instance, requires json. 
	ex. {"first_name":"Test", "last_name":"John", "middle_name": "Cruz", "age":"15", "gender":"M"}
	for the gender, it accepts, M, F, O. Male, Female, Others respectively.
PUT - /api/people/'id'/ - updates an existing record using id, requires json. 
	ex. {"first_name":"Test", "last_name":"John", "middle_name": "Cruz", "age":"15", "gender":"M"}
	for the gender, it accepts, M, F, O. Male, Female, Others respectively.
DELETE - /api/people/'id/ - deletes a selected record based on id

5. For the scripts, I created a script that automatically makes records. It is in the test folder.
run it using the command, python testscript.py


