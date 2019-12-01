# Script to scrape winning lotto numbers off lotteryleaf.com

from urllib.request import urlopen
from bs4 import BeautifulSoup

years = ['2019']

for year in years:
    quote_page = f'https://www.lotteryleaf.com/on/lotto-649/{year}'
    soup = BeautifulSoup(urlopen(quote_page).read(), 'html.parser')

    rows = soup.find_all('tr')
    for row in rows[1:]:
        date = row.find('td', class_='win-nbr-date').contents[0]
        numbers = row.find('ul', class_='nbr-grp').contents
        out = date.replace(',', '')
        for item in numbers:
            out += f",{item.contents[-1].strip()}"
        print(out)
