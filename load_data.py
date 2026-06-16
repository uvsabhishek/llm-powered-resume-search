import json

from app.database import collection

collection.delete_many({})

with open(
    "sample_data/resumes.json",
    "r",
    encoding="utf-8"
) as file:

    resumes = json.load(file)

collection.insert_many(resumes)

print("Data Loaded Successfully")