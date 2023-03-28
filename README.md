The elevator system is built completely from the user perspective. There are elevator systems(Equivalent to buildings) that contains some elevators. Now some user comes in and makes a request to an elevator. The elevator automatically moves UP/DOWN as per the request of the user.The elevator's algorithm to process the requests can be optimized further. The status of an elevator like it is currently operational or not can be updated using API calls. Visit the DOCS.md for further information.

Installation :
Make a python virtual enviornment in your preferred Linux/WSL2...any system
Recommended python version -----> 3.11.1 (The LATEST STABLE RELEASE)

Clone the repo and navigate to the directory where the manage.py file is located
git clone https://github.com/nikhilkotiya/Elevator_problem.git

cd elevator

Please read the special note point number 2 below, and go through the entire notes once.

Install the requirements

pip install -r requirements.txt


Run the development server

python manage.py runserver


Make sure your redis is running


The elevator is running in a different threads.

sqlite3 DB is used

Please check the models representation and API endpoints at DOCS.md