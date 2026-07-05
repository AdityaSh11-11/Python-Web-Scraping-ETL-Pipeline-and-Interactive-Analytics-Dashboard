import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from database import insert_quote

BASE_URL = "https://quotes.toscrape.com"


def scrape():
    """
    Scrapes all pages from QuotesToScrape
    and stores the data into SQLite.
    """

    url = BASE_URL
    total = 0

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    while url:

        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()

        except requests.RequestException as e:
            print(f"Error: {e}")
            break

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        quotes = soup.find_all(
            "div",
            class_="quote"
        )

        for quote in quotes:

            text_elem = quote.find(
                "span",
                class_="text"
            )
            text = text_elem.get_text(strip=True) if text_elem else ""

            author_elem = quote.find(
                "small",
                class_="author"
            )
            author = author_elem.get_text(strip=True) if author_elem else ""

            tags = ", ".join([
                tag.get_text(strip=True)
                for tag in quote.find_all(
                    "a",
                    class_="tag"
                )
            ])

            insert_quote(
                text,
                author,
                tags
            )

            total += 1

        next_page = soup.find(
            "li",
            class_="next"
        )

        if next_page:
            url = BASE_URL + next_page.find("a")["href"]
        else:
            url = None

    return total


if __name__ == "__main__":

    total = scrape()

    print(f"\nSuccessfully scraped {total} quotes.")