from app.llm.llm_parser import extract_intent

intent = extract_intent(
    "Find Python developers updated after January 2025"
)

print(intent)