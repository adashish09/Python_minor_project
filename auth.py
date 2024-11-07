# auth.py

# In-memory storage for user credentials
users = {}

def register_user(username, password):
    """Registers a new user."""
    if username in users:
        return False  # Username already exists
    users[username] = password
    return True

def login_user(username, password):
    """Logs in a user if credentials are valid."""
    return users.get(username) == password
