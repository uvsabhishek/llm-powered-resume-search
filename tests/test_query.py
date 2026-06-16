from llm_parser import extract_intent
from query_builder import build_query

intent = extract_intent(
    "Find Python developers with Django experience"
)

mongo_query = build_query(intent)

print(mongo_query)