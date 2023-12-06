from bs4 import BeautifulSoup

import requests

html = requests.get("https://educacao.uol.com.br/bancoderedacoes/propostas/carnaval-e-apropriacao-cultural.htm").content

soup = BeautifulSoup(html, 'html.parser')
titulosRedacao = soup.findAll("article" ,class_='rt-body')

for x in titulosRedacao:
   with open("senha.txt", "a", encoding="utf-8") as arquivo:
       arquivo.write(x.text)
#print(soup.prettify())
# adiciona uma informação ao texto original


# Primeiro listar todos os links das redacoes da url acima
# Segundo entrar em cada link e capturar o texto da redacao e as notas de cada competencia