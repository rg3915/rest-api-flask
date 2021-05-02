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
python contrib/env_gen.py
python app.py
```

```python
# POST /store data: {name:}
# GET /store/<string:name>
# GET /store
# POST /store/<string:name>/item {name:, price:}
# GET /store/<string:name>/item
```

## Chamando a API com Postman


```
POST
http://localhost:5000/store
Content-Type:application/json

{
    "name": "Another Store"
}
```

```
POST
http://localhost:5000/store/My Wonderful Store/item
Content-Type:application/json

{
    "name": "Another item",
    "price": 10.99
}
```

```
POST
http://localhost:5000/item/<name>
Content-Type:application/json

{
    "price": 12.99
}
```


## Usando sqlite

```
python test.py
```

## Rodando a aplicação novamente

```
python section5/code/app.py
```

## Section 5

```
cd section5/code
python create_tables.py
python app.py
```

## Section 6

```
cd section6/code
python create_tables.py
python app.py
```

### Advanced Postman

Defina url como `{{url}}`.

E em Manage environments defina

```
url: http://127.0.0.1:5000
```

E em `{{url}}/item/test` defina `JWT {{jwt_token}}`.

Em `/auth` crie um `Tests`.

```js
var jsonData = JSON.parse(responseBody);
tests["Your test name"] = jsonData.access_token !== undefined;

pm.environment.set("jwt_token", jsonData.access_token);
```

Crie um test em `/items`

```js
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});
```

Crie um test em `POST /items/<name>`

```
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});
```