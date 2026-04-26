def find_user(name):
    return db.execute('SELECT * FROM users WHERE name = ' + name)