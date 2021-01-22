from bs4 import BeautifulSoup
import requests
import re

# faz um novo request sempre que um comando é usado no telegram.
def new_soup():
    r = requests.get('https://www.folha.uol.com.br/')
    r.encoding = 'UTF-8'
    HTML = r.text
    soup = BeautifulSoup(HTML, 'html.parser')
    return soup

# pega só o título das notícias.
def scrap_title():
    soup = new_soup()
    a = soup.find_all('a', {'class':"c-main-headline__url"}) + soup.find_all('a', {'class':"c-list-links__url"})
    Titles = []
    for i in range(15):
        x = re.sub(r'<.*?>', '', str(a[i]))
        x = re.sub(r'\s+\s.*?\s+\s', '', x)
        Titles.append(x.strip())
    return Titles

# pega o link das notícias.
def scrap_title_link():
    soup = new_soup()
    b = soup.find_all('a', {'class':"c-main-headline__url"}, href=True) + soup.find_all('a', {'class':"c-list-links__url"}, href=True)
    links = []
    for i in range(15):
        links.append(b[i]['href'])
    return links
