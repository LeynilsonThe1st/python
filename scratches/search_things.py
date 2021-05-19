import requests
from bs4 import BeautifulSoup


def search_things(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.thenewboston.com/search.php?type=1&sort=pop&page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'user-name'}):
            href = link.get('href')
            print(href)
        page += 1


search_things(1)
