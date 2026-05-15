import streamlit as st
import requests


st.title("SmartSearch Ranker")

query = st.text_input(
    "Enter your search query"
)


if st.button("Search"):

    response = requests.get(
    "http://127.0.0.1:8000/search",
    params={"q": query}
)

if response.status_code != 200:
    st.error(response.text)
else:
    data = response.json()

    st.subheader(
        f"Results for: {query}"
    )

    for result in data["results"]:

        st.markdown("---")

        st.markdown(
            f"### {result['title']}"
        )

        st.write(result["content"])

        st.write(
            f"Score: {result['score']:.3f}"
        )