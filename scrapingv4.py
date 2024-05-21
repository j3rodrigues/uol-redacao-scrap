from bs4 import BeautifulSoup
from colordetection import detectar_verde

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
temaCompleto = "Carnaval e apropriação cultural"

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
    numArquivos = [1, 2, 3, 4, 5, 6]
    prompt = ""
    caminho_incompleto = "C:/Users/paixa/.vscode/desenvolvimento/textosCompetencias/"
    #salvar o texto de cada competeência numa pasta e colocar o caminho aqui. cada competência deve estar num arquivo diferente.
    
    with open(f"Tema {tema} ({numRedacao})" + '.txt', "a", encoding="utf-8") as arquivo:
        for num in numArquivos:
            
            with open(caminho_incompleto + f"Competencia {num}" + '.txt', "r", encoding="utf-8") as arquivoCompetencia:
                prompt = arquivoCompetencia.read()
            
            with open(caminho_incompleto + 'Fuga do tema.txt', "r", encoding="utf-8") as arquivoFuga:
                textoFuga = arquivoFuga.read()
                
            arquivo.write(prompt)
            arquivo.write(f'\n Tema: "{temaCompleto}". \n')
            arquivo.write(textoFuga)
            arquivo.write('\n\n') 
            arquivo.write(f'Redação {numRedacao}: ')
            for h in h2:
                arquivo.write('"' + h.text + '"\n\n')
        
            for x in paragrafos:
                s=""
                all_spans = x.find_all('span')
                
                for span in all_spans:
                    #print(span)
                    style = span.get('style')
                    if style:
                        if (style != 'color:black') and (style != 'color:red'):
                        #testar se a cor é verde
                            hex = style.removeprefix('color:#')
                            
                            if (detectar_verde(hex)):
                                print(hex, 'é verde')
                                #print(span)
                                span.decompose()
                            else:
                                print(hex, 'não é verde')
                arquivo.write(x.text)
                x = str(x)
                print('tipo de X', type(x))
                arquivo.write('\n\n')
            arquivo.write('\n\n\n\n\n')
                
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