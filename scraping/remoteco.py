import requests


def scrape_remotive(keyword: str, location: str | None = None) -> list:
    """Scrape jobs from Remotive using their public API."""
    search_term = keyword.replace(" ", "+")
    url = f"https://remotive.io/api/remote-jobs?search={search_term}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    data = response.json()
    jobs = []
    for job in data.get("jobs", []):
        jobs.append({
            "Job Title": job.get("title"),
            "Company": job.get("company_name"),
            "Location": job.get("candidate_required_location", "Remote"),
            "Link": job.get("url"),
        })
    return jobs
