import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def dbinit():

    # Use a service account
    cred = credentials.Certificate('/Users/feliciamaureen/Downloads/tourbotsgcp-5de05b17a27c.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db
