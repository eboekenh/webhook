from notify import notify

def scrape():
    # burada gercek scraping kodun olur
    rows_collected = 340
    return rows_collected


if __name__ == "__main__":
    try:
        rows = scrape()
        notify(f"Scraper finished. {rows} rows.")
    except Exception as e:
        notify(f"Scraper crashed: {e}")
        raise
