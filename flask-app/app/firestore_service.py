import firebase_admin

from firebase_admin import credentials, firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users():
    """Get all user in users collection"""
    return db.collection('users').get()


def get_user(user_id: str):
    """
    Get a specific user
    :param user_id: Identifier on database
    :return: User collection
    """
    return db.collection('users').document(user_id).get()


def get_user_todos(user_id: str):
    """Get all the todos from a user"""
    return db.collection('users').document(user_id).collection('todos').get()


def create_user(user_data):
    """

    :param user_data: models.UserData object
    :return: None
    """
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})
