import requests
from bs4 import BeautifulSoup


def get_table_rows():

    url = "https://www.eecigate.in/schedule/"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/149.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    table = soup.find(
        "table",
        id="tablepress-19"
    )

    if table is None:
        raise Exception(
            "Could not find schedule table"
        )

    rows = table.find_all("tr")

    return rows