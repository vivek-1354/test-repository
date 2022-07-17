import sqlalchemy
from flask_restful import Resource, reqparse

from models.user import UserModel

class UserResiter(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("username",
    type = str,
    required = True,
    help = "This field can not be empty"
    )

    parser.add_argument("password",
    type = str,
    required = True,
    help = "This field can not be empty")


    def post(self):
        data = UserResiter.parser.parse_args()
        
        if UserModel.find_by_username(data["username"])  is not None:
            return {"message": "A user with this username already exists"}
        
        new_user = UserModel(data['username'],data['password'])  # or UserModel(**data)
        
        new_user.save_to_db()
        
        return {"message":"User created successfully"},201

    # def put(self):
    #     data = UserResiter.parser.parse_args()

    #     connection = sqlite3.connect('data.sqlite')
    #     cursor = connection.cursor()

    #     user = UserModel.find_by_username(data["username"])

    #     if user is not None:

    #         query = 'UPDATE users SET password = ? WHERE username = ?'
    #         cursor.execute(query,(data["password"],data["username"]))
            
    #         connection.commit()
    #         connection.close()
    #         return {"message":"Password updated"}
            
    #     return {"message":"User not Resitered"}
    
class User(Resource):
    def get(self,id):                      # return all user in the users table
        user = UserModel.find_by_id(id)
        if user is not None:
            return user.json()
        return {"message": 'user not found'}
    
    def delete(self,id):
        user = UserModel.find_by_id(id)
        if user is not None:
            user.delete_from_db()
            return {"message": 'user deleted successfully'}       
        return {"message": 'user not found'}       
    
class Userlist(Resource):
      def get(self):                                      # return all user in the users table
        return {'users': [x.json() for x in UserModel.query.all()]}