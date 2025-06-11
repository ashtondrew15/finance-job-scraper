diff --git a//dev/null b/scraping/weworkremotely.py
index 0000000000000000000000000000000000000000..82cd75baccb88e50007d1294fcf228626b042062 100644
--- a//dev/null
+++ b/scraping/weworkremotely.py
@@ -0,0 +1,30 @@
+import requests
+from bs4 import BeautifulSoup
+
+
+def scrape_weworkremotely(keyword, location=None):
+    """Scrape jobs from We Work Remotely."""
+    search_term = keyword.replace(" ", "+")
+    url = (
+        "https://weworkremotely.com/remote-jobs/search?term="
+        f"{search_term}"
+    )
+    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
+    soup = BeautifulSoup(response.text, "html.parser")
+    jobs = []
+    for section in soup.find_all("section", class_="jobs"):
+        for li in section.find_all("li", class_="feature"):
+            anchor = li.find("a", href=True)
+            if not anchor:
+                continue
+            link = "https://weworkremotely.com" + anchor["href"]
+            company = li.find("span", class_="company")
+            title = li.find("span", class_="title")
+            if company and title:
+                jobs.append({
+                    "Job Title": title.get_text(strip=True),
+                    "Company": company.get_text(strip=True),
+                    "Location": "Remote",
+                    "Link": link,
+                })
+    return jobs
