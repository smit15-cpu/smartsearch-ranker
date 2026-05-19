import streamlit as st
import requests


st.set_page_config(
    page_title="SmartSearch Ranker",
    layout="wide"
)


# SESSION STATE SETUP

if "results" not in st.session_state:
    st.session_state.results = []

if "query" not in st.session_state:
    st.session_state.query = ""


st.title("SmartSearch Ranker")

st.write(
    "Adaptive Search Ranking System"
)


query = st.text_input(
    "Enter your search query",
    value=st.session_state.query
)


# SEARCH BUTTON

if st.button("Search"):

    response = requests.get(
        "http://127.0.0.1:8000/search",
        params={"q": query}
    )

    if response.status_code == 200:

        data = response.json()

        st.session_state.results = data["results"]
        st.session_state.query = query

    else:

        st.error(
            f"Backend Error: {response.text}"
        )


# DISPLAY RESULTS

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

        st.write(result["content"])

        st.write(
            f"Score: {result['score']:.3f}"
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

            else:

                st.error(
                    "Failed to register click."
                )