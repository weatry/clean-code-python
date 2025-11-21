"""
Small functions are beautiful!

This module demonstrates the clean approach: small, single-responsibility functions, clear separation of concerns, and Google-style docstrings.
"""
from datetime import datetime
from typing import Optional

class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email
        self.created_at = datetime.now()
        self.active = True
        self.login_attempts = 0

class UserService:
    """
    Clean UserService with small, testable functions.
    """
    SLOGAN = "Small functions are beautiful!"

    def register_user(self, username: str, password: str, email: str) -> str:
        """
        Registers a new user after validating input, checking uniqueness, hashing password, and sending welcome email.

        Args:
            username (str): The username.
            password (str): The password.
            email (str): The email address.

        Returns:
            str: Result message.
        """
        validation_error = self._validate_input(username, password, email)
        if validation_error:
            return validation_error
        uniqueness_error = self._check_uniqueness(username, email)
        if uniqueness_error:
            return uniqueness_error
        hashed_password = self._hash_password(password)
        if not hashed_password:
            return "Failed to hash password"
        user = self._build_user(username, hashed_password, email)
        if not self._persist_user(user):
            return "Registration failed, please try again later"
        self._send_welcome_email(email, username)
        return "Registration successful"

    def _validate_input(self, username: str, password: str, email: str) -> Optional[str]:
        if not username or username.strip() == "":
            return "Username cannot be blank"
        if not password or len(password) < 6:
            return "Password must be at least 6 characters"
        if not email or "@" not in email:
            return "Invalid email format"
        return None

    def _check_uniqueness(self, username: str, email: str) -> Optional[str]:
        if DB.user_exists(username):
            return "Username already exists"
        if DB.email_exists(email):
            return "Email already registered"
        return None

    def _hash_password(self, password: str) -> Optional[str]:
        import hashlib
        try:
            return hashlib.sha256(password.encode()).hexdigest()
        except Exception:
            return None

    def _build_user(self, username: str, hashed_password: str, email: str) -> User:
        return User(username, hashed_password, email)

    def _persist_user(self, user: User) -> bool:
        try:
            DB.save_user(user)
            return True
        except Exception:
            return False

    def _send_welcome_email(self, email: str, username: str) -> None:
        try:
            EmailService.send_welcome_email(email, username)
        except Exception as e:
            print(f"Failed to send welcome email: {e}")

class DB:
    @staticmethod
    def save_user(user: User) -> bool:
        print(f"User {user.username} saved to database.")
        return True
    @staticmethod
    def user_exists(username: str) -> bool:
        return False
    @staticmethod
    def email_exists(email: str) -> bool:
        return False

class EmailService:
    @staticmethod
    def send_welcome_email(email: str, username: str) -> None:
        print(f"send welcome mail to: {email}")
        subject = f"Welcome to Our Service, {username}!"
        body = f"Dear {username},\n\nThank you for registering with our service. We're excited to have you on board!\n\nBest regards,\nThe Team"
        EmailService.send_email(email, "system@noreply", username, subject, body)
    @staticmethod
    def send_email(to, from_addr, reply_to, subject, body):
        print(f"Sending email from {from_addr} to {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        return True
