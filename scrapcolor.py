import requests
from bs4 import BeautifulSoup
import execjs

# Fetch the HTML content of the website
url = "https://educacao.uol.com.br/bancoderedacoes/redacoes/monopolio-cultural.htm"
response = requests.get(url)
html_content = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

div = soup.find('div', attrs={'class':'col-sm-24 col-md-16 col-lg-17 content-article'})

print(len(div))
paragrafos = []
for i in div:
    
    div_par = div.find(class_="text-composition")

    paragrafos = div_par.find_all("p")
for x in paragrafos:
  s=""
  all_spans = x.find_all('span')
  
  for span in all_spans:
    #print(span)
    style = span.get('style')
    if style:
        #rgb_value = style.split('color:rgb(')[1].split(')')[0]
        print(style)
  print('\n\n')
  
#print('paragrafos:', paragrafos)


