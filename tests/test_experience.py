# test_experience.py

from llm_parser import extract_intent

intent = extract_intent(
    "Find Python developers with 3 years experience"
)

print(intent)