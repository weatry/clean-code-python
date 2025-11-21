"""
Small functions are beautiful!

This module demonstrates a messy approach: large, multi-responsibility function, side effects, and poor documentation.
"""
from datetime import datetime

class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.email = None
        self.created_at = None
        self.active = None
        self.login_attempts = 0

class UserService:
    SLOGAN = "Small functions are beautiful!"

    def register_user(self, username, password, email):
        # Does everything in one big function
        if username is None or username.strip() == "":
            return "Username cannot be blank"
        if password is None or len(password) < 6:
            return "Password must be at least 6 characters"
        if email is None or "@" not in email:
            return "Invalid email format"
        if DB.user_exists(username):
            return "Username already exists"
        if DB.email_exists(email):
            return "Email already registered"
        import hashlib
        try:
            md = hashlib.sha256()
            md.update(password.encode())
            hashed_password = md.hexdigest()
        except Exception:
            return "Failed to hash password"
        user = User()
        user.username = username
        user.password = hashed_password
        user.email = email
        user.created_at = datetime.now()
        user.active = True
        try:
            DB.save_user(user)
        except Exception:
            return "Registration failed, please try again later"
        try:
            EmailService.send_welcome_email(email, username)
        except Exception as e:
            print("Failed to send welcome email: " + str(e))
        return "Registration successful"

class DB:
    @staticmethod
    def save_user(user):
        print(f"User {user.username} saved to database.")
        return True
    @staticmethod
    def user_exists(username):
        return False
    @staticmethod
    def email_exists(email):
        return False

class EmailService:
    @staticmethod
    def send_welcome_email(email, username):
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
