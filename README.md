# relomate-shippingForm

required: Flask, WTForms, Firestore

to run locally, make a new file called "init.py", and copy paste the following code:

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def dbinit():

    # Use a service account
    cred = credentials.Certificate('[json key address]')
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

