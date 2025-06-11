from scraping.remoteok import scrape_remoteok

def load_scrapers():
    return {
        "Remote OK": scrape_remoteok
    }
