from app.models import Intent


def build_query(intent: Intent):

    or_conditions = []
    and_conditions = []

    if intent.skills:

        or_conditions.extend([
            {
                "hardSkillsList.skillName": {
                    "$in": intent.skills
                }
            },
            {
                "candidateSkillsList.skillName": {
                    "$in": intent.skills
                }
            },
            {
                "resumeSummary": {
                    "$regex": "|".join(intent.skills),
                    "$options": "i"
                }
            }
        ])

    if intent.jobTitles:

        or_conditions.extend([
            {
                "jobTitle": {
                    "$in": intent.jobTitles
                }
            },
            {
                "jobTitles": {
                    "$in": intent.jobTitles
                }
            },
            {
                "workExperience.jobTitles": {
                    "$in": intent.jobTitles
                }
            }
        ])

    if intent.minExperienceMonths:

        and_conditions.append(
            {
                "workExperience.acquiredExperienceInMonths": {
                    "$gte": intent.minExperienceMonths
                }
            }
        )

    if or_conditions:
        and_conditions.append(
            {
                "$or": or_conditions
            }
        )

    return {
        "$and": and_conditions
    }