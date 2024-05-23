#!/usr/bin/env python3
import os
import pyrebase
from dotenv import load_dotenv


load_dotenv()
config_attrs = ['apiKey', 'authDomain', 'databaseURL', 'projectId',
                'storageBucket', 'messagingSenderId', 'appId',
                'measurementId']
firebaseConfig = {attr: os.getenv(attr) for attr in config_attrs}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
media_store = firebase.storage()
