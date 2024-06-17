from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
import time



'''url = "https://educacao.uol.com.br/bancoderedacoes/"
html = requests.get(url).content'''

#def scroll_to_element(driver):
    


# Abra o navegador
driver = webdriver.Chrome()

# Acesse a página
driver.get('https://educacao.uol.com.br/bancoderedacoes/')

# Localize o botão
botao = driver.find_element(By.CLASS_NAME, "btn")

print("cheguei")
btnCbl = WebDriverWait(driver, 10).until( #chamar função scroll
    EC.visibility_of(botao) 
)
'''
1-rolar até achar o botao "ver mais "
laco
2-clicar
3-esperar até o botao "carregando"
4-rolar até achar o botao "ver mais "'''

print(btnCbl.text)

# Clique no botão
btnCbl.click()
#chamar função scroll

time.sleep(10)

botao = driver.find_element(By.CLASS_NAME, "btn")
print(botao.text)

page_content = driver.page_source

soup = BeautifulSoup(page_content, 'html.parser')

#soup = BeautifulSoup(html, 'html.parser')

div_link = soup.find_all('div', class_='thumbnails-wrapper')

link = [l.find('a').get('href') for l in div_link]

print(len(link))

for x in link:
    print(x, '\n')

