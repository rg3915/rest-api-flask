from user import User

users = [
    {
        'id': 1,
        'username': 'admin',
        'password': '1234'
    }
]

username_mapping = {
    'admin': {
        'id': 1,
        'username': 'admin',
        'password': '1234'
    }
}

userid_mapping = {
    1: {
        'id': 1,
        'username': 'admin',
        'password': '1234'
    }
}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
