def calculate_score(
    resume,
    intent
):

    score = 0

    resume_skills = []

    for skill in resume.get(
        "hardSkillsList",
        []
    ):
        resume_skills.append(
            skill["skillName"].lower()
        )

    for skill in intent.skills:

        if skill.lower() in resume_skills:

            score += 10

    resume_title = resume.get(
        "jobTitle",
        ""
    ).lower()

    for title in intent.jobTitles:

        if title.lower() in resume_title:

            score += 20

    total_exp = 0

    for exp in resume.get(
        "workExperience",
        []
    ):
        total_exp += exp.get(
            "acquiredExperienceInMonths",
            0
        )

    if intent.minExperienceMonths:

        if total_exp >= intent.minExperienceMonths:

            score += 15

    return score