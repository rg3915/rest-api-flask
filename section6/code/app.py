from decouple import config
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from resources.item import Item, ItemList
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = config('SECRET_KEY')
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    # Evita circular import.
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
