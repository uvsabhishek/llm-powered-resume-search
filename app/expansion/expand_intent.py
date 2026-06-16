from app.expansion.title_mapper import TITLE_SYNONYMS
from app.expansion.skill_mapper import SKILL_SYNONYMS


def expand_titles(intent):

    expanded_titles = []

    for title in intent.jobTitles:

        expanded_titles.append(title)

        synonyms = TITLE_SYNONYMS.get(
            title.lower(),
            []
        )

        expanded_titles.extend(
            synonyms
        )

    intent.jobTitles = list(
        set(expanded_titles)
    )

    return intent


def expand_skills(intent):

    expanded_skills = []

    for skill in intent.skills:

        expanded_skills.append(skill)

        synonyms = SKILL_SYNONYMS.get(
            skill.lower(),
            []
        )

        expanded_skills.extend(
            synonyms
        )

    intent.skills = list(
        set(expanded_skills)
    )

    return intent