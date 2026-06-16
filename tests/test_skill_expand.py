# test_skill_expand.py

from llm_parser import extract_intent
from expand_intent import expand_skills

intent = extract_intent(
    "Find Spark developers"
)

intent = expand_skills(
    intent
)

print(intent.skills)