import requests
from selenium import webdriver
import bs4
import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os




def varrerLinks():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    
    driver = webdriver.Chrome()
    
    driver.get('https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-es?ps=10000&pe=10000&exc=1&ms=0&me=5000')
    time.sleep(3)
    html = driver.page_source
    driver.close()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    linksCarros = [a.get('href') for a in soup.find_all('a', href=True, class_={'AdCard_link__4c7W6'})]
    return linksCarros


def varrerPagina(linksCarros):
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    
  
    
    time.sleep(3)
    countPages = 1
    for linkUrl in linksCarros:
        
        driver = webdriver.Chrome()
        time.sleep(5)
        driver.get(linkUrl)
        time.sleep(3)
        html = driver.page_source
        driver.close()
        
        soup = bs4.BeautifulSoup(html, 'html.parser')
        
        containers = soup.find_all('div', class_={'ad__sc-wuor06-0'})
        divCidades = soup.find_all('li', class_={'olx-breadcrumb__item'})
        for i in divCidades:
            municipio = i.find('a', class_={'olx-link', 'olx-link--caption',' olx-link--grey'})
            
       
        divPreco = soup.find_all('div', class_={'ad__sc-q5xder-0','dWqdGZ'})
        
        for i in divPreco:
            valor = i.find('span',class_={'olx-text',' olx-text--title-medium','olx-text--block'})
        

        for container in containers:
            
            spansDoContainer = container.select('span.ekhFnR')
            
        for link in containers:
            linksDoContainer = link.select('a.olx-link.olx-link--small.olx-link--grey.ad__sc-2h9gkk-3.lkkHCr')
            
        
        
        marca = linksDoContainer[2].text
        modelo = linksDoContainer[1].text
        ano = linksDoContainer[3].text
        cambio = spansDoContainer[3].text
        tipo = spansDoContainer[0].text
        cor = spansDoContainer[5].text
        valor = valor.text
    
        print(f"\n\n####################### Página {countPages} #######################\n#######################          #######################")
        print(linkUrl)
        print(f"Marca : {marca}\nModelo: {modelo}\nAno: {ano}\nCambio: {cambio}\nTipo: {tipo}\nCor: {cor}\nValor: {valor}")
       
        countPages +=1
        
            
        
        
        
    
    
    
    
    
    
    
os.system('cls')
#linkCarro = ['https://es.olx.com.br/norte-do-espirito-santo/autos-e-pecas/carros-vans-e-utilitarios/ford-ecosport-xls-1-6-2007-impecavel-1393112810?lis=listing_2020']
    
varrerPagina(varrerLinks())