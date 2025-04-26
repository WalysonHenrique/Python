import requests
from selenium import webdriver
import bs4
import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
os.environ['WDM_LOG_LEVEL'] = '0'




def varrerLinks():    
    driver = webdriver.Edge()
    
    driver.get('https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-es?ps=10000&pe=10000&exc=1&ms=0&me=5000')
    time.sleep(3)
    html = driver.page_source
    driver.quit()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    linksCarros = [a.get('href') for a in soup.find_all('a', href=True, class_={'olx-adcard__link'})]
    return linksCarros


def varrerPagina(linksCarros):
    
    anuncios = []
    
    
  
    
    time.sleep(3)
    countPages = 1
    for linkUrl in linksCarros:
        
        anuncio = []
        driver = webdriver.Edge()
        time.sleep(5)
        driver.get(linkUrl)
        time.sleep(3)
        html = driver.page_source
        driver.quit()
        
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
            
        
        anuncio = anuncio+[
            linksDoContainer[2].text,
            linksDoContainer[1].text,
            linksDoContainer[3].text,
            spansDoContainer[3].text,
            spansDoContainer[0].text,
            spansDoContainer[5].text,
            valor.text.replace("R$ ","").replace(".","").strip(),
            municipio.text
            ]
        anuncios = anuncios+[anuncio]
        print(f"\n\n####################### Página {countPages} #######################\n#######################          #######################")
        print(linkUrl)
        countPages +=1
    return anuncios

print(varrerPagina(varrerLinks()))