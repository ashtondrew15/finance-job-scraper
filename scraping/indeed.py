diff --git a//dev/null b/scraping/indeed.py
index 0000000000000000000000000000000000000000..3ed4dd1910d1bfc725ad31e0f9f10b62376145f8 100644
--- a//dev/null
+++ b/scraping/indeed.py
@@ -0,0 +1,25 @@
+import requests
+from bs4 import BeautifulSoup
+
+
+def scrape_indeed(keyword: str, location: str | None = None) -> list:
+    """Scrape job listings from Indeed."""
+    search_term = keyword.replace(" ", "+")
+    loc_term = (location or "").replace(" ", "+") if location else ""
+    url = f"https://www.indeed.com/jobs?q={search_term}&l={loc_term}"
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
