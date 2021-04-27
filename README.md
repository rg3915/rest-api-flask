# rest-api-flask

Learning REST API Flask


## Este projeto foi feito com:

* [Python 3.8.9](https://www.python.org/)
* [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/rest-api-flask.git
cd rest-api-flask
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

```python
# POST /store data: {name:}
# GET /store/<string:name>
# GET /store
# POST /store/<string:name>/item {name:, price:}
# GET /store/<string:name>/item
```