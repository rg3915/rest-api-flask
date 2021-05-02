import sqlite3

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f"An item with name {name} already exists."}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])

        try:
            item.insert()
        except Exception as e:
            return {"message": f"An error occurred inserting the item. {e}"}, 500

        return item.json(), 201

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                updated_item.insert()
            except Exception as e:
                return {"message": f"An error occurred inserting the item. {e}"}, 500
        else:
            try:
                updated_item.update()
            except Exception as e:
                return {"message": f"An error occurred updating the item. {e}"}, 500
        return updated_item.json()

    def delete(self, name):
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}


class ItemList(Resource):

    def get(self):
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)

        items = []
        for row in result:
            items.append({'name': row[1], 'price': row[2]})

        connection.close()

        return {'items': items}