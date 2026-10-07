USERS = {
    "admin": "1234",
    "ravi": "python123",
}


def authenticate_user(username, password):
    return USERS.get(username) == password