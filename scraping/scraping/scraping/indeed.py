diff --git a//dev/null b/scraping/indeed.py
index 0000000000000000000000000000000000000000..db21ba98a34944f625a9196bd876e09be3ff1a9c 100644
--- a//dev/null
+++ b/scraping/indeed.py
@@ -0,0 +1,28 @@
+import requests
+from bs4 import BeautifulSoup
+
+
+def scrape_indeed(keyword, location=None):
+    """Scrape job listings from Indeed."""
+    search_term = keyword.replace(" ", "+")
+    loc_term = (location or "").replace(" ", "+") if location else ""
+    url = (
+        "https://www.indeed.com/jobs?q="
+        f"{search_term}&l={loc_term}"
+    )
+    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
+    soup = BeautifulSoup(response.text, "html.parser")
+    jobs = []
+    for card in soup.select("a.tapItem"):
+        title = card.find("h2", class_="jobTitle")
+        company = card.find("span", class_="companyName")
+        loc = card.find("div", class_="companyLocation")
+        link = "https://www.indeed.com" + card.get("href", "")
+        if title and company:
+            jobs.append({
+                "Job Title": title.get_text(strip=True),
+                "Company": company.get_text(strip=True),
+                "Location": loc.get_text(strip=True) if loc else location,
+                "Link": link,
+            })
+    return jobs
