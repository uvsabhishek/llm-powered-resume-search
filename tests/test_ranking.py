from llm_parser import extract_intent
from query_builder import build_query
from ranked_search import ranked_search

query = (
    "Find Python developers "
    "with Django experience "
    "and 3 years experience"
)

intent = extract_intent(
    query
)

mongo_query = build_query(
    intent
)

results = ranked_search(
    mongo_query,
    intent
)

for r in results:

    print(
        r["candidateIdentifier"],
        r["score"]
    )