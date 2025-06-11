diff --git a/scraping/scraper_loader.py b/scraping/scraper_loader.py
index c5e35529370501300b6606f0c5ba97afaf900731..f448d8fdad35ee1092b69206d3e262ff578dd15f 100644
--- a/scraping/scraper_loader.py
+++ b/scraping/scraper_loader.py
@@ -1,6 +1,19 @@
 from scraping.remoteok import scrape_remoteok
+from scraping.weworkremotely import scrape_weworkremotely
+from scraping.remotive import scrape_remotive
+from scraping.remoteco import scrape_remoteco
+from scraping.indeed import scrape_indeed
+from scraping.extra_scrapers import EXTRA_SCRAPERS
+
 
 def load_scrapers():
-    return {
-        "Remote OK": scrape_remoteok
+    """Return available job board scrapers."""
+    scrapers = {
+        "Remote OK": scrape_remoteok,
+        "We Work Remotely": scrape_weworkremotely,
+        "Remotive": scrape_remotive,
+        "Remote.co": scrape_remoteco,
+        "Indeed": scrape_indeed,
     }
+    scrapers.update(EXTRA_SCRAPERS)
+    return scrapers
