import requests
from bs4 import BeautifulSoup

r = requests.get('https://education.github.com/experts')
print(r.url)
print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())