from bs4 import BeautifulSoup

import requests

#pagina inicial 
#url = "https://educacao.uol.com.br/bancoderedacoes/propostas/ciencia-tecnologia-e-superacao-dos-limites-humanos.htm"
url = "https://educacao.uol.com.br/bancoderedacoes/propostas/carnaval-e-apropriacao-cultural.htm"
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

div_link = soup.find_all('div', class_='rt-line-option')

link = [l.find('a').get('href') for l in div_link]

numRedacao = 0
tema = "Carnaval"

for i in link:
    link_url = f'{i}'
    link_html = requests.get(link_url).content
    soup1 = BeautifulSoup(link_html , 'html.parser')
    div = soup1.find('div', attrs={'class':'col-sm-24 col-md-16 col-lg-17 content-article'})
    
    article = soup1.find('article', class_ = 'rt-body')

    span_pontos = article.find_all('span', class_="points")

    divH2 = soup1.find('div', class_="container-composition")
    h2 = divH2.find_all('h2') #titulos das redações
    
    print(len(div))
    paragrafos = []
    for i in div:
        
        div_par = div.find(class_="text-composition")

        paragrafos = div_par.find_all("p")

    numRedacao += 1
    #print(numRedacao)
    with open(f"Tema {tema} ({numRedacao})" + '.txt', "a", encoding="utf-8") as arquivo:
        for h in h2:
            arquivo.write(h.text + '\n\n')
       
        for x in paragrafos:
            s=""
            all_spans = x.find_all('span')
            
            for span in all_spans:
                #print(span)
                if span['style']=='color:#00b050' or span['style']=='color:#00b050':
                    #print(span)
                    span.decompose()
            arquivo.write(x.text)
            arquivo.write('\n\n')
        arquivo.write('COMPETÊNCIAS')
        arquivo.write('\n\n')
        
        numCompetencia = 0
        for aFinal in span_pontos:
            numCompetencia += 1
            if (numCompetencia == 6):
                arquivo.write('Nota final - ' + aFinal.text)
            else:
                arquivo.write(f'Competência {numCompetencia} - ' + aFinal.text)
                arquivo.write('\n\n')
            
