import sqlite3
from flask_restful import Resource, reqparse
from models.item import ItemModel 
# from db import db


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
    type=float,
    required=True,
    help="This field cannot be empty")

    # @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item is not None:
            return item.json()
        return {"message": 'item not found'}

    def post(self, name):
        if ItemModel.find_by_name(name) is not None:
            return {"item": f"Item name {name} is already exits" },400
        
        data = Item.parser.parse_args()
        item = ItemModel(name ,data['price'])
        
        item.save_to_db()


        return {"message": "Item created successfully"}

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": f"Item name {name} is deleted successfully"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name ,data["price"])

        if item is None:
            # updated_item.save_to_db()
            item = ItemModel(name ,data['price'])
            # return {"message": "Item created successfully"}
        else:
            item.price = data['price']
            # updated_item.update()
            # return {"message": "Item Updated successfully"}
        item.save_to_db()
        return  item.json()

class ItemList(Resource):
    def get(self):
        # pass
        return {'items': [item.json() for item in  ItemModel.query.all()]}
        # return {"items ": list(map(lambda x: x.json(), ItemModel.query.all()))}
