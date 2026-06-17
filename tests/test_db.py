from app.database import collection

for doc in collection.find():
    print(doc)