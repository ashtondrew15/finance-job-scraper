diff --git a//dev/null b/scraping/remotive.py
index 0000000000000000000000000000000000000000..df59f7526dd23b741e3a4968712b3f66f39ad6f4 100644
--- a//dev/null
+++ b/scraping/remotive.py
@@ -0,0 +1,21 @@
+import requests
+
+
+def scrape_remotive(keyword, location=None):
+    """Scrape jobs from Remotive using their public API."""
+    search_term = keyword.replace(" ", "+")
+    url = (
+        "https://remotive.io/api/remote-jobs?search="
+        f"{search_term}"
+    )
+    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
+    data = response.json()
+    jobs = []
+    for job in data.get("jobs", []):
+        jobs.append({
+            "Job Title": job.get("title"),
+            "Company": job.get("company_name"),
+            "Location": job.get("candidate_required_location", "Remote"),
+            "Link": job.get("url"),
+        })
+    return jobs
