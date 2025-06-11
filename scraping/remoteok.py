import requests
from bs4 import BeautifulSoup

def scrape_remoteok(keyword, location):
    url = f"https://remoteok.com/remote-{keyword.replace(' ', '-')}-jobs"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for row in soup.select("tr.job"):
        title = row.get("data-position")
        company = row.get("data-company")
        link = "https://remoteok.com" + row.get("data-url", "")
        if title and company:
            jobs.append({
                "Job Title": title,
                "Company": company,
                "Location": "Remote",
                "Link": link
            })
    return jobs
  add remoteok scraper
