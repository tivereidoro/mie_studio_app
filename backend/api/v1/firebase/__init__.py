#!/usr/bin/env python3
import json
import os
import pyrebase
from dotenv import load_dotenv


load_dotenv()
service_account_json = os.getenv('FIREBASE_SERVICE_ACCOUNT')
service_account = json.loads(service_account_json)
config_attrs = ['apiKey', 'authDomain', 'databaseURL', 'projectId',
                'storageBucket', 'messagingSenderId', 'appId',
                'measurementId']
firebaseConfig = {attr: os.getenv(attr) for attr in config_attrs}
firebaseConfig['serviceAccount'] = service_account
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
media_store = firebase.storage()
