import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
cred = credentials.Certificate('')
firebase_admin.initialize_app(cred)

db = firestore.client()
# 데이터 쓰기
doc_ref = db.collection(u'Name').document(u'site1')
doc_ref.set({
            u'site' : 'site', 
            u'name' : 'name',
            u'price' : 'price',
            u'link' : 'link'   
})
doc_ref = db.collection(u'Name').document(u'site2')
doc_ref.set({
            u'site' : 'site2', 
            u'name' : 'name2',
            u'price' : 'price2',
            u'link' : 'link2'   
})
doc_ref = db.collection(u'Name').document(u'site3')
doc_ref.set({
            u'site' : 'site3', 
            u'name' : 'name3',
            u'price' : 'price3',
            u'link' : 'link3'  
})
