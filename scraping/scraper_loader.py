from scraping.remoteok import scrape_remoteok
from scraping.weworkremotely import scrape_weworkremotely
from scraping.remotive import scrape_remotive
from scraping.remoteco import scrape_remoteco
from scraping.indeed import scrape_indeed
from scraping.extra_scrapers import EXTRA_SCRAPERS


def load_scrapers() -> dict:
    """Return available job board scrapers."""
    scrapers = {
        "Remote OK": scrape_remoteok,
        "We Work Remotely": scrape_weworkremotely,
        "Remotive": scrape_remotive,
        "Remote.co": scrape_remoteco,
        "Indeed": scrape_indeed,
    }
    scrapers.update(EXTRA_SCRAPERS)
    return scrapers
