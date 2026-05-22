# SmartSearch Ranker

An intelligent full-stack search engine built with Python.

SmartSearch Ranker combines modern search ranking techniques with user interaction signals to improve relevance over time.

Users can search content, generate ranking scores, simulate learning through clicks, and understand why each result appears.

---

## Live Demo

Frontend:
[[LIVE_STREAMLIT_LINK](https://smartsearch-ranker-kvcnqpck5vhlvor98dxvhv.streamlit.app/)]

Backend API:
[[LIVE_RENDER_LINK](https://smartsearch-ranker.onrender.com)]

---

## Features

### Intelligent Search
- BM25 ranking algorithm
- Query relevance scoring
- Document retrieval

### Adaptive Learning
- Click tracking
- User feedback signals
- Dynamic score boosting

### Explainable Results
- BM25 score display
- Click boost analysis
- Final ranking breakdown

### Analytics Dashboard
- Trending searches
- Search history
- Most clicked results

### Full Stack Architecture
- FastAPI backend
- Streamlit frontend
- SQLite persistence

---

## Architecture

User
↓
Streamlit Frontend
↓
FastAPI API
↓
Search Engine
↓
SQLite Database

---

## Tech Stack

Backend:
- Python
- FastAPI
- SQLite

Frontend:
- Streamlit

Ranking:
- BM25

Data:
- Pandas

Deployment:
- Render
- Streamlit Cloud

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn api.app:app --reload
```

Run frontend:

```bash
streamlit run frontend/app.py
```

---

## Project Structure

SmartSearch-ranker/

api/

frontend/

database/

search/

data/

requirements.txt

---

## What I Learned

This project helped me gain experience in:

- Search systems
- Ranking algorithms
- API development
- Frontend engineering
- Database integration
- Cloud deployment
- Debugging production issues

---

## Future Improvements

- Semantic search
- Embedding-based ranking
- User accounts
- Personalization
- Search autocomplete
- A/B testing

---

## Author

Smit Anghan

