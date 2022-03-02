#To managa web app
from flask import Flask, render_template, request, flash, redirect, url_for
#login and logout management
from flask_login import LoginManager, login_user, logout_user, login_required
#Create a token to protect the web app.
from flask_wtf.csrf import CSRFProtect

#To handle connections to the database.
from flaskext.mysql import MySQL

#class to add config to the web app itself. 
from config import config

#Models
from models.ModelUser import ModelUser

#Entities
from models.entities.User import User

#Instantiate the web app.
app = Flask(__name__)

#Intansciate the token generator, db and login manager.
csrf = CSRFProtect()
db = MySQL(app)
loginManagerApp = LoginManager(app)


#This function is used to get user info to be used in session.
@loginManagerApp.user_loader
def load_user(user_id):
    return ModelUser.get_user_by_id(db, user_id)

@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Obtain Parameters from request and build a User object
        user = User(0, request.form['username'], request.form['password'])
        #Call the login method of ModelUser
        loggedUser = ModelUser.login(db, user)
        #debug
        #print(loggedUser.password)
        if loggedUser:
            if loggedUser.password:
                login_user(loggedUser)
                return redirect(url_for('home'))
            else:
                flash('Invalid password')
                return render_template('auth/login.html')
        else:
            flash('User not found')
            return render_template('auth/login.html')
    else:
        print('Here')
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

def status_404(error):
    return render_template('404.html'), 404

#send to login page if user is not logged in   
loginManagerApp.login_view = 'login'

if __name__ == '__main__':
    #add configuration to the web app
    app.config.from_object(config['development'])
    #add token generator to secure sessions
    csrf.init_app(app)
    #manage page 404
    app.register_error_handler(404, status_404)
    #start the web app
    app.run()