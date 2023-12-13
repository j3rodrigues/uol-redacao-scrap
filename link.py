from bs4 import BeautifulSoup

import requests

#pagina inicial 
url = "https://educacao.uol.com.br/bancoderedacoes/propostas/carnaval-e-apropriacao-cultural.htm"
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

div = soup.find_all('div', class_='rt-line-option')

link = [l.find('a').get('href') for l in div]
for i in link:
    with open("link1.txt", "a", encoding="utf-8") as arquivo:
       arquivo.write(i)