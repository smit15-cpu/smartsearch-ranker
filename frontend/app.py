import streamlit as st
import requests


st.set_page_config(
    page_title="SmartSearch Ranker",
    layout="wide"
)


# -----------------------------
# SESSION STATE
# -----------------------------

if "results" not in st.session_state:
    st.session_state.results = []

if "query" not in st.session_state:
    st.session_state.query = ""


# -----------------------------
# LOAD TRENDING SEARCHES
# -----------------------------

trending_queries = []

try:

    trend_response = requests.get(
        "http://127.0.0.1:8000/trending"
    )

    if trend_response.status_code == 200:

        trends = trend_response.json()

        trending_queries = [
            item[0]
            for item in trends["queries"]
        ]

except:
    pass


# -----------------------------
# UI HEADER
# -----------------------------

st.title("🔍 SmartSearch Ranker")

st.write(
    "Adaptive Search Ranking System"
)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title(
    "🔥 Trending Searches"
)

if trending_queries:

    for item in trending_queries:

        st.sidebar.write(item)

else:

    st.sidebar.write(
        "No search history yet"
    )


# -----------------------------
# SEARCH INPUT
# -----------------------------

default_suggestions = [
    "python",
    "python backend",
    "machine learning",
    "android",
    "data science"
]

all_suggestions = list(
    dict.fromkeys(
        default_suggestions +
        trending_queries
    )
)

query = st.selectbox(
    "Search",
    [""] + all_suggestions
)


# -----------------------------
# SEARCH
# -----------------------------

if st.button("Search"):

    response = requests.get(
        "http://127.0.0.1:8000/search",
        params={
            "q": query
        }
    )

    if response.status_code == 200:

        data = response.json()

        st.session_state.results = (
            data["results"]
        )

        st.session_state.query = query

    else:

        st.error(
            f"Backend Error: {response.text}"
        )


# -----------------------------
# DISPLAY RESULTS
# -----------------------------

if st.session_state.results:

    st.subheader(
        f"Results for: {st.session_state.query}"
    )

    for index, result in enumerate(
        st.session_state.results
    ):

        st.markdown("---")

        st.markdown(
            f"### {result['title']}"
        )

        st.write(
            result["content"]
        )

        st.write(
            f"Final Score: {result['score']:.3f}"
        )

        if "explanation" in result:

            with st.expander(
                "Why this ranked"
            ):

                st.write(
                    f"BM25 Score: {result['explanation']['bm25_score']}"
                )

                st.write(
                    f"Click Boost: {result['explanation']['click_boost']}"
                )

                st.write(
                    f"Total Clicks: {result['explanation']['clicks']}"
                )

                st.write(
                    f"Final Score: {result['explanation']['final_score']}"
                )

        if st.button(
            f"Open Result {index}"
        ):

            click_response = requests.post(
                "http://127.0.0.1:8000/click",
                json={
                    "query": st.session_state.query,
                    "title": result["title"]
                }
            )

            if click_response.status_code == 200:

                st.success(
                    f"Clicked: {result['title']}"
                )

                st.session_state.results = []

            else:

                st.error(
                    "Failed to register click."
                )