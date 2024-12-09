from bs4 import BeautifulSoup
import requests
import json
import sqlite3


url_gov = "https://www.ohiohouse.gov/legislation/acts"
response = requests.get(url_gov)

if response.status_code != 200:
    print("uh oh stinky")
    exit()

html = response.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

table = soup.find('table', class_='data-grid acts-table')
# print(table)

rows = table.find_all('tr')[1:]
data = []
for row in rows:
    columns = row.find_all('td')
    data.append({
        'bill_number': row.find('th').find('a').get_text(),
        'bill_title': columns[0].get_text(),
        'bill_pdf': columns[1].find('a')['href']
    })
print(json.dumps(data, indent=4))