# ide/firebase.py
from firebase_admin import firestore

def get_firestore_client():
    """Returns the Firestore client instance."""
    return firestore.client()