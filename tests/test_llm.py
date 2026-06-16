from llm_parser import extract_intent

intent = extract_intent(
    "Find Python developers with Django experience"
)

print(intent)
print(intent.skills)
print(intent.jobTitles)