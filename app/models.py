from pydantic import BaseModel


class Intent(BaseModel):
    skills: list[str] = []
    jobTitles: list[str] = []
    minExperienceMonths: int | None = None


class SearchRequest(BaseModel):
    query: str


class SearchResponse(BaseModel):
    query: str
    intent: dict
    mongo_query: dict
    count: int
    results: list