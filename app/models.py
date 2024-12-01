class User:
    def __init__(self, username, email, hashed_password):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "hashed_password": self.hashed_password,
        }
