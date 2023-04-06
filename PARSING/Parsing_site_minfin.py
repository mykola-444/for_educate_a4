import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'
HOST = 'https://minfin.com.ua/'
URL = 'https://minfin.com.ua/cards/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='sc-14ydfjo-0 jYdA-De')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='bfjox4-15 grpvgp').find(class_='sc-6nr3q5-0 iyqRre').get('alt'),
                'link_prodact': HOST + item.find('div', class_='bfjox4-15 grpvgp').find(
                    class_='sc-6nr3q5-0 iyqRre').get('href'),
                'Brend': item.find('div', class_='bfjox4-16 bfjox4-17 dUjQSe hrBtlP').find(
                    class_='bfjox4-21 hnGYMy').get_text(),
                'Imagen': item.find('div', class_='bfjox4-9 kJaWjv').find(
                    class_='sc-6nr3q5-0 gpMICG').find('img').get('src')
            }
        )
    return cards

def save_doc(items, path):
    with open(path, "w", newline='') as file:
        writer = csv.writer(file, delimiter=':')
        writer.writerow(['Title', 'Link', 'Bank', 'Image'])
        for item in items:
            writer.writerow([item['title'], item['link_prodact'], item['Brend'], item['Imagen']])




def parser():
    PAGENATION = input(" How mach: ")
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        cards.extend(get_content(html.text))
        save_doc(cards, CSV)

        pass
    else:
        print("Error")

parser()


#     print(item)
#
#
# html = get_html(URL)
# print(get_content(html.text))
