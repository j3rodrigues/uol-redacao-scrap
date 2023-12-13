from bs4 import BeautifulSoup

import requests

#pagina inicial 
url = "https://educacao.uol.com.br/bancoderedacoes/propostas/carnaval-e-apropriacao-cultural.htm"
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

div_link = soup.find_all('div', class_='rt-line-option')

link = [l.find('a').get('href') for l in div_link]

for i in link:
    with open("link.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(i)
        link_url = f'{i}'
        link_html = requests.get(link_url).content
        soup = BeautifulSoup(link_html , 'html.parser')
        div = soup.find('div', attrs={'class':'row'})
        for i in div:
           div1 = div.find_all(class_="text-composition")
        for x in div1:
            with open("redacao1.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(x.text)


