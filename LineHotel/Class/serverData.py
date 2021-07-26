import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("Class/firebase.json")
firebase_admin.initialize_app(cred,{
        'databaseURL':'************************************'
        })

def writ(path,json):
    try:
        ref=db.reference(path)
        ref.update(json)
        return 1
    except :
        return 0

def read(path):
    try:
         read=db.reference(path)
         get=read.get("")
         return get
    except :
        return 0

def addList(path,_f,newData):
    ad=read(path)
    ad[_f].append(newData)
    print(ad)
    writ(path,ad)
