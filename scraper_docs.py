import os

import requests
from bs4 import BeautifulSoup

from notify import notify

URL = "https://python.langchain.com/docs/introduction/"
DATA_DIR = "data"
OUTPUT_FILE = os.path.join(DATA_DIR, "langchain_links.txt")


def scrape():
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    links = [a.get("href") for a in soup.select("a") if a.get("href")]

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(links))

    return len(links)


if __name__ == "__main__":
    try:
        count = scrape()
        notify(f"LangChain docs scraper finished. {count} links found.")
    except Exception as e:
        notify(f"LangChain docs scraper crashed: {e}")
        raise
