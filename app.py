import streamlit as st
from database import create_tables, count_quotes, unique_authors
from scraper import scrape

# -------------------------------------------------
# Initial Setup
# -------------------------------------------------
create_tables()

st.set_page_config(
    page_title="Web Scraper Dashboard",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------
st.markdown("""
<style>

.main-title{
    font-size:42px;
    font-weight:bold;
    color:#0E76FD;
}

.metric-card{
    background:#F4F6F8;
    padding:15px;
    border-radius:12px;
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.title("Web Scraper Dashboard")


st.sidebar.markdown("---")

st.sidebar.success("Status: Ready")

# -------------------------------------------------
# Main Title
# -------------------------------------------------
st.markdown(
'<p class="main-title">🌐 Web Scraper Dashboard</p>',
unsafe_allow_html=True
)

st.write(
"""
This application demonstrates an **end-to-end Python web scraping project**.

Features:

- Scrape website data
- Save into SQLite
- Search records
- Visualize with charts
- Export CSV/Excel/JSON
- View scraping history
"""
)

st.divider()

# -------------------------------------------------
# Metrics
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Quotes",
        count_quotes()
    )

with col2:
    st.metric(
        "Unique Authors",
        unique_authors()
    )

st.divider()

# -------------------------------------------------
# Scraper Section
# -------------------------------------------------
st.subheader("Start Scraping")

st.write(
"""
Click the button below to scrape all quotes from
https://quotes.toscrape.com
"""
)

if st.button("Start Scraping", use_container_width=True):

    progress = st.progress(0)

    status = st.empty()

    status.info("Starting scraper...")

    progress.progress(20)

    total = scrape()

    progress.progress(100)

    status.success(f"Successfully scraped {total} quotes!")

    st.balloons()

st.divider()


# -------------------------------------------------
# Features
# -------------------------------------------------
st.subheader("Features")

c1, c2 = st.columns(2)

with c1:

    st.success("✔ SQLite Database")

    st.success("✔ BeautifulSoup")

    st.success("✔ Requests")

    st.success("✔ Streamlit UI")

with c2:

    st.success("✔ Charts")

    st.success("✔ Search")

    st.success("✔ Export")

    st.success("✔ Scheduler (Phase 3)")

st.divider()

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown(
"""
<div class='footer'>
Made with using Python, Streamlit, SQLite and BeautifulSoup.
</div>
""",
unsafe_allow_html=True
)