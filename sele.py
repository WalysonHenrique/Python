from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import bs4
driver = webdriver.Firefox()
driver.get("https://academico.ifes.edu.br/qacademico/index.asp?t=1001")
time.sleep(4)
elem = driver.find_element(By.NAME, "LOGIN")
elem.clear()
elem.send_keys("20231stads005")
elem = driver.find_element(By.NAME, "SENHA")
elem.clear()
elem.send_keys("2023_W@lyson")
elem.send_keys(Keys.RETURN)
time.sleep(4)
elem = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[8]/td[3]/a")
elem.click()

HTML = driver.page_source
soup = bs4.BeautifulSoup(HTML, 'html.parser')

linhas = soup.find_all('tr', class_={"conteudoTexto"})

for linha in linhas:
    dados = linha.find_all('td')
    disciplinas = dados[0]
    faltas = dados[4]
    print(disciplinas.text, faltas.text)