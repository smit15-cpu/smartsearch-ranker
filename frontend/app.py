import streamlit as st
import requests


# PAGE CONFIG


st.set_page_config(
    page_title="SmartSearch Ranker",
    layout="wide"
)



# SESSION STATE


if "results" not in st.session_state:
    st.session_state.results = []

if "query" not in st.session_state:
    st.session_state.query = ""


# FETCH TRENDING


trending_queries = []

try:
    trend_response = requests.get(
        "http://127.0.0.1:8000/trending"
    )

    if trend_response.status_code == 200:

        trends = trend_response.json()

        trending_queries = [
            item[0] for item in trends["queries"]
        ]

except:
    pass


# HEADER


st.title("🔍 SmartSearch Ranker")

st.write("Adaptive Search Ranking System")



# SIDEBAR

st.sidebar.title("🔥 Trending Searches")

if trending_queries:
    for item in trending_queries:
        st.sidebar.write(item)
else:
    st.sidebar.write("No search history yet")



# SEARCH INPUT


default_suggestions = [
    "python",
    "python backend",
    "machine learning",
    "android",
    "data science"
]

all_suggestions = list(
    dict.fromkeys(default_suggestions + trending_queries)
)

query = st.selectbox(
    "Search Query",
    [""] + all_suggestions
)



# SEARCH BUTTON


if st.button("Search") and query != "":

    with st.spinner("Searching intelligent index..."):

        response = requests.get(
            "http://127.0.0.1:8000/search",
            params={"q": query}
        )

    if response.status_code == 200:

        data = response.json()

        st.session_state.results = data["results"]
        st.session_state.query = query

    else:

        st.error(response.text)



# DISPLAY RESULTS


if st.session_state.results:

    st.subheader(
        f"Results for: {st.session_state.query}"
    )

    for index, result in enumerate(st.session_state.results):

        st.markdown("---")

        # TITLE
        st.markdown(f"### 📄 {result['title']}")

        # CONTENT
        st.write(result["content"])

        # SCORE + CLICK METRICS
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Score",
                f"{result['score']:.3f}"
            )

        with col2:
            clicks = result.get("explanation", {}).get("clicks", 0)

            st.metric(
                "Clicks",
                clicks
            )

        # EXPLANATION (SAFE)
        if "explanation" in result:

            with st.expander("Why this ranked"):

                exp = result["explanation"]

                st.write(f"BM25 Score: {exp.get('bm25_score', 0)}")
                st.write(f"Click Boost: {exp.get('click_boost', 0)}")
                st.write(f"Total Clicks: {exp.get('clicks', 0)}")
                st.write(f"Final Score: {exp.get('final_score', 0)}")

        # CLICK BUTTON
        if st.button(f"Open Result {index}"):

            click_response = requests.post(
                "http://127.0.0.1:8000/click",
                json={
                    "query": st.session_state.query,
                    "title": result["title"]
                }
            )

            if click_response.status_code == 200:

                st.success(f"Clicked: {result['title']}")

                # IMPORTANT: refresh UI state
                st.rerun()

            else:
                st.error("Failed to register click")