# Resume Search Engine

## Overview

An AI-powered resume search system that converts recruiter natural language queries into structured MongoDB searches.

Example:

Find Python developers with Django experience and 3 years experience

The system extracts intent using an LLM, expands skills and job titles, generates MongoDB queries, ranks resumes, and returns the best candidates through a FastAPI API.

---

## Features

* Natural Language Search
* Intent Extraction using LangChain + Groq
* Skill Extraction
* Job Title Extraction
* Experience Parsing
* Skill Expansion
* Title Expansion
* MongoDB Query Generation
* Resume Ranking
* FastAPI REST API
* Swagger Documentation

---

## Tech Stack

* Python
* FastAPI
* LangChain
* Groq
* MongoDB
* PyMongo
* Pydantic

---

## Project Structure

```text
app/
├── llm/
├── search/
├── expansion/

tests/
sample_data/
```

---

## Installation

```bash
pip install -r requirements.txt
```

Create:

```bash
.env
```

using:

```bash
.env.example
```

---

## Load Sample Data

```bash
python load_data.py
```

---

## Run API

```bash
uvicorn app.main:app --reload
```

---

## Swagger

```text
http://127.0.0.1:8000/docs
```

---

## Example Request

```json
{
  "query": "Find Python developers with Django experience and 3 years experience"
}
```

---

## Processing Flow

Recruiter Query
↓
Intent Extraction
↓
Skill & Title Expansion
↓
MongoDB Query Generation
↓
Resume Retrieval
↓
Resume Ranking
↓
API Response
