import re

import requests
from bs4 import BeautifulSoup

#URL = 'http://www.columbia.edu/~fdc/sample.html'
URL = 'http://localhost:8000/'
response = requests.get(URL)
print(response)
page = BeautifulSoup(response.text, 'html.parser')

print(page.title)
print(page.title.string)
print(page.find_all('h3'))
print(page.find_all(re.compile('^h(2|3)')))  # this search uses the h2 and h3 tags

link_section = page.find_all('href', attrs={'name': "links"})  # DON'T work ????????!!!!!!!!!!!
section = []
for element in link_section:
    if element.name == 'h3':
        break
    section.append(element.string or '')

result = ''.join(section)
print(result)
