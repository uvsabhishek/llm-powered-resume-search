INTENT_EXTRACTION_PROMPT = """
You are an expert recruiter assistant.

Extract:

1. skills
2. jobTitles
3. minExperienceMonths

Rules:

- Convert years into months.
- 1 year = 12 months
- 2 years = 24 months
- 3 years = 36 months
- 5 years = 60 months

If experience is not mentioned return null.

Return ONLY valid JSON.

Output Format:

{{
  "skills": [],
  "jobTitles": [],
  "minExperienceMonths": null
}}

User Query:

{query}
"""