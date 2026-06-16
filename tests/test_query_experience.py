from llm_parser import extract_intent
from query_builder import build_query

intent = extract_intent(
    "Find Python developers with 3 years experience"
)

query = build_query(intent)

print(query)