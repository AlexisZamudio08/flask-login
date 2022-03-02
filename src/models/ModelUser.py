#import main user entity
from .entities.User import User

class ModelUser():
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.get_db().cursor()
            cursor.execute("SELECT * FROM user WHERE username = %s", (user.username,))
            result = cursor.fetchone()
            if result:
                user = User(result[0], result[2], User.check_password(result[3], user.password), result[1])
                return user
            else:
                return None
        except Exception as e:
            raise Exception(e)
    
    @classmethod
    def get_user_by_id(self, db, id):
        try:
            cursor = db.get_db().cursor()
            cursor.execute("SELECT id, full_name, username FROM user WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:
                return User(result[0], result[2], None, result[1])
            else:
                return None
        except Exception as e:
            raise Exception(e)