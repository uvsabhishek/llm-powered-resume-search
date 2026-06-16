from fastapi import FastAPI

from app.models import SearchRequest
from app.llm.llm_parser import extract_intent
from app.expansion.expand_intent import (
    expand_titles,
    expand_skills
)
from app.search.query_builder import build_query
from app.search.ranked_search import ranked_search

app = FastAPI(
    title="Resume Search API"
)


@app.get("/")
def health_check():

    return {
        "message": "Resume Search API Running"
    }


@app.post("/search")
def search_candidates(
    request: SearchRequest
):

    # Stage 1
    intent = extract_intent(
        request.query
    )

    # Stage 2
    intent = expand_titles(
        intent
    )

    intent = expand_skills(
        intent
    )

    # Stage 3 + Stage 5
    mongo_query = build_query(
        intent
    )

    # Stage 6
    results = ranked_search(
        mongo_query,
        intent
    )

    # Stage 7
    return {
        "query": request.query,
        "expanded_skills": intent.skills,
        "expanded_titles": intent.jobTitles,
        "mongo_query": mongo_query,
        "count": len(results),
        "results": results
    }