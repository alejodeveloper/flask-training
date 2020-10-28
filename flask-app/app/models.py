# Models
from flask_login import UserMixin

from app.firestore_service import get_user


class UserData:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data: UserData):
        """
        Model for user loader
        :param user_data: UserData obj instance
        """
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id: str):
        user_doc = get_user(user_id)
        user_data = UserData(
            username=user_doc.id,
            password=user_doc.to_dict().get('password'),
        )

        return UserModel(user_data)
