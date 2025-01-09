import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

#Initialize Database
cred = credentials.Certificate('/workspaces/Hotdeal/Database/auth.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


#Add data to Firebase
def add_Data(collectionID, documentADD):
        for i in range(len(documentADD)):
            doc_ref = db.collection(collectionID).document(f'site{i + 1}')
            doc_ref.set(documentADD[i])


#Delete data to Firebase
def delete_Data(collectionID, documentDelete):
        for i in range(len(documentDelete)):
            doc_ref = db.collection(collectionID).document(f'site{i + 1}')
            doc_ref.delete()

