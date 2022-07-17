import sqlalchemy
from flask import Flask 
from flask_restful import Api      #reqparse  # it is use to parse the payload set which data attach to the requests
# from flask_jwt import JWT

# from security import authenticate,identity 
from resources.user import UserResiter,Userlist,User
from resources.item import Item, ItemList 
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app) 


"""# Here we insiliaze a JWT object that is going to use our app and authenticate ,identity function together 
to allow to authentication of the user"""

# jwt = JWT(app, authenticate, identity)   # Here Jwt create a endpoint called (/auth)

api.add_resource(Item, '/item/<string:name>')          #http://127.0.0.1:5000/item/name
api.add_resource(ItemList, '/items')                   #http://127.0.0.1:5000/items

api.add_resource(UserResiter, '/resiter')              #http://127.0.0.1:5000/resiter

api.add_resource(Userlist ,'/users')                   #http://127.0.0.1:5000/users
api.add_resource(User ,'/user/<int:id>')               #http://127.0.0.1:5000/user/id

api.add_resource(Store, '/store/<string:name>')        #http://127.0.0.1:5000/store/name
api.add_resource(StoreList, '/stores')                     #http://127.0.0.1:5000/stores



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)