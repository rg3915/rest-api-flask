from flask import Flask


app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    # POST /store data: {name:}
    ...


@app.route('/store/<string:name>')
def get_store(name):
    # GET /store/<string:name>
    ...


@app.route('/store')
def get_stores():
    # GET /store
    ...


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    # POST /store/<string:name>/item {name:, price:}
    ...


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    # GET /store/<string:name>/item
    ...

# @app.route('/')
# def home():
#     return "Hello"


app.run(port=5000)
