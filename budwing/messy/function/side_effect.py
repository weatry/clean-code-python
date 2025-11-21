"""
Functions should have no side effects!

This module demonstrates a messy approach: function with side effects, command-query mixed, and poor documentation.
"""
class User:
    def __init__(self):
        self.username = None
        self.login_attempts = 0

class UserService:
    SLOGAN = "Functions should have no side effects!"

    def authenticate_user(self, username, password):
        # Has side effects: modifies user, updates DB, initializes session
        user = DB.get_user_by_username_and_password(username, password)
        if user:
            user.login_attempts += 1
            DB.update_user(user)
            Session.initialize(user.username)
            return True
        return False

class DB:
    @staticmethod
    def get_user_by_username_and_password(username, password):
        if username == "testuser" and password == "password123":
            user = User()
            user.username = username
            return user
        return None
    @staticmethod
    def update_user(user):
        print(f"User {user.username} updated in database.")

class Session:
    @staticmethod
    def initialize(username):
        print(f"Session initialized for user: {username}")
