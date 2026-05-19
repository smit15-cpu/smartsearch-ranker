import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import pandas as pd
from collections import Counter
from database.db import (
    get_search_history,
    get_clicks
)


st.set_page_config(
    page_title="Search Analytics",
    layout="wide"
)


st.title("SmartSearch Analytics")


# SEARCH HISTORY

search_data = get_search_history()

search_df = pd.DataFrame(
    search_data,
    columns=[
        "Query",
        "Document",
        "Score"
    ]
)

st.subheader("Search History")

st.dataframe(search_df)


# TOP SEARCHES

query_counts = Counter(
    search_df["Query"]
)

top_queries = pd.DataFrame(
    query_counts.items(),
    columns=["Query", "Count"]
).sort_values(
    by="Count",
    ascending=False
)

st.subheader("Top Queries")

st.bar_chart(
    top_queries.set_index("Query")
)


# CLICKS

click_data = get_clicks()

click_df = pd.DataFrame(
    click_data,
    columns=[
        "Query",
        "Document"
    ]
)

st.subheader("Click History")

st.dataframe(click_df)


# MOST CLICKED DOCS

doc_counts = Counter(
    click_df["Document"]
)

top_docs = pd.DataFrame(
    doc_counts.items(),
    columns=["Document", "Clicks"]
).sort_values(
    by="Clicks",
    ascending=False
)

st.subheader("Most Clicked Documents")

st.bar_chart(
    top_docs.set_index("Document")
)