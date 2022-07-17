from hmac import compare_digest
from resources.user import UserModel

# username_mapping ={u.username: u.__str__() for u in users}

# username_mapping ={u.username: u for u in users} 

# userid_mapping ={u.id: u for u in users}

def authenticate(username, password):
    # user = username_mapping.get(username, None)
    # if user and user.password == password:
    user = UserModel.find_by_username(username)
    if user and compare_digest(UserModel.password, password):
        return user 
    # return {"message":"username not found"}

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


