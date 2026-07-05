import streamlit as st
import pandas as pd

from database import get_all_quotes
from utils.helper import dataframe

st.set_page_config(
    page_title="History",
    page_icon="📜",
    layout="wide"
)

st.title("Scraping History")

df = dataframe(get_all_quotes())

if df.empty:
    st.warning("No scraped data available.")
    st.stop()

# -----------------------------
# Search
# -----------------------------

search = st.text_input(
    "Search Quote / Author / Tag"
)

if search:

    mask = (

        df["Quote"].str.contains(search, case=False)

        |

        df["Author"].str.contains(search, case=False)

        |

        df["Tags"].str.contains(search, case=False)

    )

    df = df[mask]

# -----------------------------
# Author Filter
# -----------------------------

authors = ["All"] + sorted(df["Author"].unique())

selected = st.selectbox(
    "Author",
    authors
)

if selected != "All":

    df = df[df["Author"] == selected]

# -----------------------------
# Date Filter
# -----------------------------

dates = sorted(

    pd.to_datetime(

        df["Scraped At"]

    ).dt.date.unique()

)

selected_date = st.selectbox(

    "Scraping Date",

    ["All"] + [str(d) for d in dates]

)

if selected_date != "All":

    df = df[

        pd.to_datetime(

            df["Scraped At"]

        ).dt.date.astype(str)

        == selected_date

    ]

# -----------------------------
# Metrics
# -----------------------------

c1, c2, c3 = st.columns(3)

c1.metric(
    "Records",
    len(df)
)

c2.metric(
    "Authors",
    df["Author"].nunique()
)

c3.metric(
    "Tags",
    df["Tags"].str.split(",").explode().nunique()
)

st.divider()

st.dataframe(
    df,
    use_container_width=True,
    height=600
)

st.write(f"Showing {len(df)} records.")