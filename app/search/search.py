from app.database import collection

def search_resumes(mongo_query):

    results = list(
        collection.find(
            mongo_query,
            {
                "_id": 0
            }
        )
    )

    return results