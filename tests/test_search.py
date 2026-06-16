from llm_parser import extract_intent
from query_builder import build_query
from search import search_resumes

query = "Find Python developers with Django experience"

intent = extract_intent(query)

print("Intent:")
print(intent)

mongo_query = build_query(intent)

print("\nMongo Query:")
print(mongo_query)

results = search_resumes(mongo_query)

print("\nResults:")
for result in results:
    print(result)