def start_app():
    print("App is starting...")

def login(username, password):
    # I forgot to add password length validation!
    if username == "admin" and password == "123":
        return True
    return False
