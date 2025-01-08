import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

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


#Initialize Database
cred = credentials.Certificate('/workspaces/Hotdeal/Database/auth.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

collectionID = 'Name' #CollectionID는 Name으로 고정
# 이 둘은 파이썬으로 크롤링해온거로 바꿀거임


site1 = {
    u'photo' : 'photo1', 
    u'name' : 'name1',
    u'price' : 'price1',
    u'link' : 'link1'   
}
site2 = {
    u'photo' : 'photo2', 
    u'name' : 'name2',
    u'price' : 'price2',
    u'link' : 'link2'   
}
site3 = {
    u'photo' : 'photo3', 
    u'name' : 'name3',
    u'price' : 'price3',
    u'link' : 'link3'   
}


documentID_add = [site1, site2, site3]
documentID_delete = [site1, site2, site3]
delete_Data(collectionID,documentID_add)

#db.collection(collectionID).document(documentID_delete).delete()
