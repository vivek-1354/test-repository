
from flask_restful import Resource

from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store is not None:
            return store.json()
        return {"message": 'store not found'}

    def post(self, name):
        if StoreModel.find_by_name(name) is not None:
            return {"message": f"store name {name} is already exits" },400
        
        store = StoreModel(name)
        
        store.save_to_db()
        return {"message": "store created successfully"}

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": f"store name {name} is deleted successfully"}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in  StoreModel.query.all()]}
        # return {"items ": list(map(lambda x: x.json(), StoreModel.query.all()))}