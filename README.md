diff --git a/README.md b/README.md
index 489dae5ffb3baaffa527251e6b476f2ac0227048..782157831e9965adba47254a6abec1cb37cba03a 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,23 @@
 # finance-job-scraper
-Auto-job scraper for finance roles
+
+Auto-job scraper for finance roles. Provides a Streamlit interface for running web scrapers that gather remote finance job postings.
+
+## Setup
+
+1. **Create a virtual environment** (recommended):
+   ```bash
+   python3 -m venv .venv
+   source .venv/bin/activate
+   ```
+2. **Install dependencies** from `requirements.txt`:
+   ```bash
+   pip install -r requirements.txt
+   ```
+3. **Launch Streamlit**:
+   ```bash
+   streamlit run app.py
+   ```
+
+### Job boards
+
+The code defines scrapers for a few boards such as Remote OK, Remotive and We Work Remotely. Many other boards listed in the code are placeholders awaiting future implementation.
