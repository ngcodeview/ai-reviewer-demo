
def get_user_secure(user_id):
    # GOOD: Using parameters (?) instead of f-strings
    query = "SELECT * FROM users WHERE id = ?"
    return db.execute(query, (user_id,))
