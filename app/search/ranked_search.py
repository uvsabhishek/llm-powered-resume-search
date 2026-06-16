from app.search.search import search_resumes
from app.search.ranking import calculate_score


def ranked_search(
    mongo_query,
    intent
):

    results = search_resumes(
        mongo_query
    )

    ranked = []

    for result in results:

        score = calculate_score(
            result,
            intent
        )

        result["score"] = score

        ranked.append(
            result
        )

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked