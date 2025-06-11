"""Streamlit interface for running job scrapers."""

import streamlit as st
import pandas as pd

from scraping.scraper_loader import load_scrapers

st.set_page_config(page_title="Finance Job Scraper", layout="wide")

st.title("📊 Finance Job Scraper + Auto Apply")
st.markdown("Scrapes top finance job boards and applies using resume profile.")

st.sidebar.title("👤 Chris Vitale")
st.sidebar.markdown("📍 Myrtle Beach, SC")
st.sidebar.markdown("✉️ vitalechris32@gmail.com")
st.sidebar.markdown(
    "[🔗 LinkedIn](https://www.linkedin.com/in/chris-vitale-ou/)",
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")

scrapers = load_scrapers()

st.sidebar.header("🔍 Filters")
keyword = st.sidebar.text_input("Keywords", "financial analyst")
location = st.sidebar.selectbox(
    "Location", ["Orlando, FL", "Remote", "Hybrid"]
)
test_mode = st.sidebar.checkbox("🧪 Test mode", value=True)
board_names = list(scrapers.keys())
selected_boards = st.sidebar.multiselect(
    "Select job boards", board_names, default=board_names[:1]
)
run_button = st.sidebar.button("🚀 Run Job Search")

if run_button:
    all_jobs = []
    for board in selected_boards:
        scraper = scrapers.get(board)
        if scraper:
            try:
                jobs = scraper(keyword, location)
                all_jobs.extend(jobs)
            except Exception as e:
                st.warning(f"{board} scraper error: {e}")
    if all_jobs:
        df = pd.DataFrame(all_jobs)
        st.dataframe(df)
    else:
        st.info("No jobs found.")
else:
    st.info("Click 'Run Job Search' to begin.")
