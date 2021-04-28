import sqlite3

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse


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
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[1], 'price': row[2]}}

    def post(self, name):
        if self.find_by_name(name):
            return {'message': f"An item with name {name} already exists."}, 400

        data = Item.parser.parse_args()

        item = {
            'name': name,
            'price': data['price']
        }

        try:
            self.insert(item)
        except Exception as e:
            return {"message": f"An error occurred inserting the item. {e}"}, 500

        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (NULL, ?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {
                'name': name,
                'price': data['price']
            }
            items.append(item)
        else:
            item.update(data)
        return item

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
        return {'items': items}
