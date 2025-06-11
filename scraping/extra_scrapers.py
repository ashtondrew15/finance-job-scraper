diff --git a//dev/null b/scraping/extra_scrapers.py
index 0000000000000000000000000000000000000000..b11d3600d4acec781c2b86881aef0bee54924e69 100644
--- a//dev/null
+++ b/scraping/extra_scrapers.py
@@ -0,0 +1,57 @@
+"""Placeholder scrapers for additional job boards."""
+
+from typing import Callable, Dict, List
+
+
+def _placeholder_scraper(keyword: str, location: str | None = None) -> List[dict]:
+    """Return no results; real implementation pending."""
+    return []
+
+
+EXTRA_SCRAPERS: Dict[str, Callable[[str, str | None], List[dict]]] = {
+    "FlexJobs": _placeholder_scraper,
+    "Jobs in Social Impact": _placeholder_scraper,
+    "Virtual Vocations": _placeholder_scraper,
+    "Outsourcely": _placeholder_scraper,
+    "Working Nomads": _placeholder_scraper,
+    "Jobspresso": _placeholder_scraper,
+    "PowerToFly": _placeholder_scraper,
+    "Dynamite Jobs": _placeholder_scraper,
+    "ARC": _placeholder_scraper,
+    "AngelList": _placeholder_scraper,
+    "NoDesk": _placeholder_scraper,
+    "JustRemote": _placeholder_scraper,
+    "Himalayas": _placeholder_scraper,
+    "Remote Woman": _placeholder_scraper,
+    "Jobgether": _placeholder_scraper,
+    "SkipTheDrive": _placeholder_scraper,
+    "LinkedIn": _placeholder_scraper,
+    "Glassdoor": _placeholder_scraper,
+    "ZipRecruiter": _placeholder_scraper,
+    "Monster": _placeholder_scraper,
+    "CareerBuilder": _placeholder_scraper,
+    "SimplyHired": _placeholder_scraper,
+    "eFinancialCareers": _placeholder_scraper,
+    "Accounting Jobs Today": _placeholder_scraper,
+    "Financial Jobs Web": _placeholder_scraper,
+    "OneWire": _placeholder_scraper,
+    "AFWA Career Center": _placeholder_scraper,
+    "Financial Job Bank": _placeholder_scraper,
+    "iHireAccounting": _placeholder_scraper,
+    "Accountingfly": _placeholder_scraper,
+    "Corporate Finance Institute Jobs": _placeholder_scraper,
+    "IMA Career Center": _placeholder_scraper,
+    "AICPA/CIMA Career Center": _placeholder_scraper,
+    "Robert Half": _placeholder_scraper,
+    "Kforce": _placeholder_scraper,
+    "Randstad": _placeholder_scraper,
+    "Insight Global": _placeholder_scraper,
+    "Beacon Hill Staffing": _placeholder_scraper,
+    "Vaco": _placeholder_scraper,
+    "Addison Group": _placeholder_scraper,
+    "CF Staffing": _placeholder_scraper,
+    "Toptal Finance": _placeholder_scraper,
+    "Atrium": _placeholder_scraper,
+    "Wellfound": _placeholder_scraper,
+    "Workday": _placeholder_scraper,
+}
