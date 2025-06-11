import requests
from bs4 import BeautifulSoup


def scrape_weworkremotely(keyword: str, location: str | None = None) -> list:
    """Scrape jobs from We Work Remotely."""
    search_term = keyword.replace(" ", "+")
    url = f"https://weworkremotely.com/remote-jobs/search?term={search_term}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    for section in soup.find_all("section", class_="jobs"):
        for li in section.find_all("li", class_="feature"):
            anchor = li.find("a", href=True)
            if not anchor:
                continue
            link = "https://weworkremotely.com" + anchor["href"]
            company = li.find("span", class_="company")
            title = li.find("span", class_="title")
            if company and title:
                jobs.append({
                    "Job Title": title.get_text(strip=True),
                    "Company": company.get_text(strip=True),
                    "Location": "Remote",
                    "Link": link,
                })
    return jobs
