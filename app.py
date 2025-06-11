# app.py (main Streamlit UI)
import streamlit as st
import pandas as pd
import time
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from scraping.scraper_loader import load_scrapers
st.set_page_config(page_title="Finance Job Scraper", layout="wide")

st.title("📊 Finance Job Scraper + Auto Apply")
st.markdown("Scrapes top finance job boards and applies using resume profile.")

st.sidebar.title("👤 Chris Vitale")
st.sidebar.markdown("📍 Myrtle Beach, SC")
st.sidebar.markdown("✉️ vitalechris32@gmail.com")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/chris-vitale-ou/)", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.header("🔍 Filters")
keyword = st.sidebar.text_input("Keywords", "financial analyst")
location = st.sidebar.selectbox("Location", ["Orlando, FL", "Remote", "Hybrid"])
test_mode = st.sidebar.checkbox("🧪 Test mode", value=True)
selected_boards = st.sidebar.multiselect("Select job boards", ["Remote OK"], default=["Remote OK"])
run_button = st.sidebar.button("🚀 Run Job Search")

if run_button:
    st.info("🔧 Job scraping will be wired here.")
else:
    st.info("Click 'Run Job Search' to begin.")
