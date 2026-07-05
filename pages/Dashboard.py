import streamlit as st
import pandas as pd
import plotly.express as px

from database import (
    get_all_quotes,
    count_quotes,
    unique_authors
)

from scraper import scrape
from utils.helper import (
    dataframe,
    search,
    author_statistics,
    tag_statistics
)

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Dashboard")

st.write("Analyze and explore the scraped data.")

st.divider()

# --------------------------------------------------
# Refresh Data
# --------------------------------------------------

def load_data():
    data = get_all_quotes()
    return dataframe(data)


df = load_data()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("Dashboard")

if st.sidebar.button("Refresh Data"):
    st.rerun()

if st.sidebar.button("Scrape Website"):

    progress = st.progress(0)
    status = st.empty()

    status.info("Scraping website...")

    progress.progress(25)

    total = scrape()

    progress.progress(100)

    status.success(f"{total} quotes scraped successfully!")

    st.balloons()

    st.rerun()

# --------------------------------------------------
# Metrics
# --------------------------------------------------

total_quotes = count_quotes()
total_authors = unique_authors()

total_tags = 0

if not df.empty:
    total_tags = (
        df["Tags"]
        .str.split(",")
        .explode()
        .str.strip()
        .nunique()
    )

c1, c2, c3 = st.columns(3)

c1.metric(
    "Quotes",
    total_quotes
)

c2.metric(
    "Authors",
    total_authors
)

c3.metric(
    "Tags",
    total_tags
)

st.divider()

# --------------------------------------------------
# Search
# --------------------------------------------------

st.subheader("Search")

keyword = st.text_input(
    "Search Quote / Author / Tag"
)

filtered = df.copy()

if keyword:
    filtered = search(filtered, keyword)

# --------------------------------------------------
# Author Filter
# --------------------------------------------------

authors = ["All"]

if not df.empty:
    authors += sorted(df["Author"].unique())

selected_author = st.selectbox(
    "Filter by Author",
    authors
)

if selected_author != "All":
    filtered = filtered[
        filtered["Author"] == selected_author
    ]

st.divider()

# --------------------------------------------------
# Data Table
# --------------------------------------------------

st.subheader("Quotes")

st.dataframe(
    filtered,
    use_container_width=True,
    height=400
)

st.write(f"Showing **{len(filtered)}** records.")

st.divider()

# --------------------------------------------------
# Charts
# --------------------------------------------------

left, right = st.columns(2)

# --------------------------
# Quotes per Author
# --------------------------

with left:

    st.subheader("📈 Quotes per Author")

    if not df.empty:

        author_df = author_statistics(df)

        fig = px.bar(
            author_df.head(10),
            x="Author",
            y="Quotes",
            title="Top 10 Authors"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# --------------------------
# Tags
# --------------------------

with right:

    st.subheader("🏷 Popular Tags")

    if not df.empty:

        tag_df = tag_statistics(df)

        fig = px.pie(
            tag_df.head(10),
            names="Tag",
            values="Count",
            title="Top Tags"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.divider()

# --------------------------------------------------
# Recent Records
# --------------------------------------------------

st.subheader("🕒 Recently Scraped")

if not df.empty:

    recent = df.sort_values(
        "ID",
        ascending=False
    ).head(10)

    st.table(
        recent[
            [
                "Author",
                "Quote",
                "Scraped At"
            ]
        ]
    )

else:

    st.warning(
        "No data found. Run the scraper first."
    )

st.divider()

# --------------------------------------------------
# Statistics
# --------------------------------------------------

st.subheader("📊 Dataset Summary")

if not df.empty:

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            f"""
Total Quotes: {total_quotes}

Unique Authors: {total_authors}

Unique Tags: {total_tags}
"""
        )

    with col2:

        longest = df["Quote"].str.len().max()

        avg = round(
            df["Quote"].str.len().mean(),
            2
        )

        st.info(
            f"""
Longest Quote Length: {longest}

Average Quote Length: {avg}
"""
        )

else:

    st.warning("Database is empty.")