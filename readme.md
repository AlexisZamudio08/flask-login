#For this project we are using MySQL, please follow a youtube tutorial(e.g. Install MySQL for mac or windows). 
Once you have created root users and password 
    * EXECUTE script.sql on your SQL script.

#Python version used for this project. 
    * Python 3.9.7

#Install virtualenv tool (global). 
    * pip install virtualenv

#Go to Flask-login folder and create and activate environment. 
    * python -m venv venv 
    * cd venv/bin source activate

#Install requirements needed for this project 
    * pip install -r requirements.txt

#Under flask_login/src, in config.py modify your credentials for db connection.

#Run server, under flask_login/src in command prompt execute 
    * python index.py

#As response, the previous execution will generate a localhost url, 
#Copy and paste that url in your browser and you must to get access to the main login window

#Finally test the login access with credentials: 
    * user: admin 
    * password: test#01
