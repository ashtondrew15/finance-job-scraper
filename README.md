# finance-job-scraper

Auto-job scraper for finance roles. Provides a Streamlit interface for running web scrapers that gather remote finance job postings.

## Setup

1. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. **Install dependencies** from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch Streamlit**:
   ```bash
   streamlit run app.py
   ```

### Job boards

The code defines scrapers for a few boards such as Remote OK, Remotive and We Work Remotely. Many other boards listed in the code are placeholders awaiting future implementation.
