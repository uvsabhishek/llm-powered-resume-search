from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from app.models import Intent
from app.llm.prompts import INTENT_EXTRACTION_PROMPT

load_dotenv()

prompt = PromptTemplate(
    template=INTENT_EXTRACTION_PROMPT,
    input_variables=["query"]
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(Intent)

chain = prompt | structured_llm


def extract_intent(query: str) -> Intent:
    return chain.invoke(
        {"query": query}
    )