"""
Functions should have no side effects!

This module demonstrates the clean approach: pure functions, command-query separation, and Google-style docstrings.
"""
from typing import Optional

class User:
    def __init__(self, username: str):
        self.username = username
        self.login_attempts = 0

class AuthenticateResult:
    """
    Result object for authentication describing the effects that should be applied by caller.
    """
    def __init__(self, success: bool, user: Optional[User], updated_login_attempts: int, should_initialize_session: bool):
        self.success = success
        self.user = user
        self.updated_login_attempts = updated_login_attempts
        self.should_initialize_session = should_initialize_session

class UserService:
    SLOGAN = "Functions should have no side effects!"

    def authenticate_user(self, username: str, password: str) -> AuthenticateResult:
        """
        Pure version: does not perform updates or side effects. It only queries and returns an AuthenticateResult describing what should be done.

        Args:
            username (str): The username.
            password (str): The password.

        Returns:
            AuthenticateResult: The result describing intended effects.
        """
        user = DB.get_user_by_username_and_password(username, password)
        if user:
            new_login_attempts = user.login_attempts + 1
            return AuthenticateResult(True, user, new_login_attempts, True)
        return AuthenticateResult(False, None, 0, False)

class DB:
    @staticmethod
    def get_user_by_username_and_password(username: str, password: str) -> Optional[User]:
        if username == "testuser" and password == "password123":
            return User(username)
        return None
    @staticmethod
    def update_user(user: User):
        print(f"User {user.username} updated in database.")

class Session:
    @staticmethod
    def initialize(username: str):
        print(f"Session initialized for user: {username}")

# Example client usage
if __name__ == "__main__":
    user_service = UserService()
    username = "john_doe"
    password = "password123"
    result = user_service.authenticate_user(username, password)
    if result.success:
        user = result.user
        user.login_attempts = result.updated_login_attempts
        DB.update_user(user)
        if result.should_initialize_session:
            Session.initialize(user.username)
        print(f"User {username} authenticated successfully.")
    else:
        print(f"Authentication failed for user {username}.")
