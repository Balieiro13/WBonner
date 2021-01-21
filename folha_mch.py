from bs4 import BeautifulSoup
import requests
import re

def scrap():
    r = requests.get('https://www.folha.uol.com.br/')
    r.encoding = 'UTF-8'
    HTML = r.text
    soup = BeautifulSoup(HTML, 'html.parser')

    h2 = soup.find_all(['h2'])
    Titles = []
    for i in range(15):
        h2[i] = re.sub(r'<.*?>', '', str(h2[i]))
        h2[i] = re.sub(r'(\s+\s)*', '', h2[i])
        Titles.append(h2[i])
    return Titles