from werkzeug.security import check_password_hash, generate_password_hash 
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, name="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.name = name
    
    #This way to declare a method is used to use this method outside the class withouth the need to create an object.
    @classmethod
    def check_password(self, hashed_password, password):
        print(hashed_password)
        return check_password_hash(hashed_password, password)

    @classmethod
    def crate_hash(self, password):
        hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
        return hash
