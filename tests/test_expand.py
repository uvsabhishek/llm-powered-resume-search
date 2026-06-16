from llm_parser import extract_intent
from expand_intent import expand_titles

intent = extract_intent(
    "Find Python developers"
)

intent = expand_titles(
    intent
)

print(intent.jobTitles)