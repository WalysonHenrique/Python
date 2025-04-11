import requests
from selenium import webdriver
import bs4
import time
import mysql.connector

driver = webdriver.Chrome()
driver.get('https://es.olx.com.br/norte-do-espirito-santo/autos-e-pecas/carros-vans-e-utilitarios/c4-glx-2-0-automatico-bancos-em-couro-4-pneus-novos-muito-novo-confira-2012-1382607261?lis=listing_2020')
time.sleep(3)
html = driver.page_source
driver.close()
soup = bs4.BeautifulSoup(html, 'html.parser')

container = soup.find_all('div', class_={'ad__sc-1l883pa-1'})
detalhes = soup.find_all('div' , class_={'ad__sc-2h9gkk-1'})
detalhesFiltrados = soup.find_all('a', class_={'olx-link', 'ad__sc-2h9gkk-3', 'lkkHCr'})
#span = soup.find_all('span', class_={'olx-text--title-medium'})
for i in detalhesFiltrados:
    print(i.text)