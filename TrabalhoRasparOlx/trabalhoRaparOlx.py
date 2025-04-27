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
    
    driver.get('https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-es?ps=30000&pe=60000&ms=0&me=0&gb=2&gb=1&rs=2020&re=2025')
    time.sleep(3)
    html = driver.page_source
    driver.quit()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    linksCarros = [a.get('href') for a in soup.find_all('a', href=True, class_={'olx-adcard__link'})]
    return linksCarros


def varrerPagina(linksCarros):
    
    anuncios = []
    
    time.sleep(4)
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
            
       
        valor = soup.select_one("#price-box-container > div.ad__sc-q5xder-1.hoJpM > div:nth-child(1) > span.olx-text.olx-text--title-medium.olx-text--block")
        

        
        divDosDados = soup.find_all('div', class_={'ad__sc-2h9gkk-1','bdpQSX','olx-d-flex',' olx-ai-flex-start',' olx-fd-column',' olx-flex'})
            
        for link in containers:
            linksDoContainer = link.select('a.olx-link.olx-link--small.olx-link--grey.ad__sc-2h9gkk-3.lkkHCr')
            
            
        marcas = []
        modelos = []
        anos = []
        cambios = []
        tiposVeiculos = []
        cores = []
    
        marca_encontrada = None
        modelo_encontrado = None
        ano_encontrado = None
        cambio_encontrado = None
        tipoVeiculo_encontrado = None
        cor_encontrada = None
   
        for div in divDosDados:
            spans = div.find_all('span', class_={'olx-text', 'olx-text--overline', 'olx-text--block', 'olx-mb-0-5', 'olx-color-neutral-120'})
            
            for span in spans:
                if  span.text.strip() == "Marca":
                    link_marca = div.find('a', class_={'olx-link', 'olx-link--small', 'olx-link--grey', 'ad__sc-2h9gkk-3', 'lkkHCr'})
                    if link_marca:
                        marca_encontrada = link_marca.text.strip()
                    break
                
            for span in spans:
                if  span.text.strip() == "Modelo":
                    link_modelo = div.find('a', class_={'olx-link', 'olx-link--small', 'olx-link--grey', 'ad__sc-2h9gkk-3', 'lkkHCr'})
                    if link_modelo:
                        modelo_encontrado = link_modelo.text.strip()
                    break  
                
            for span in spans:
                if  span.text.strip() == "Ano":
                    link_ano = div.find('a', class_={'olx-link', 'olx-link--small', 'olx-link--grey', 'ad__sc-2h9gkk-3', 'lkkHCr'})
                    if link_ano:
                        ano_encontrado = link_ano.text.strip()
                    break 
                
            for span in spans:
                if  span.text.strip() == "Câmbio":
                    link_cambio = div.find('span', class_={'ad__sc-hj0yqs-0','ekhFnR'})
                    if link_cambio:
                        cambio_encontrado = link_cambio.text.strip()
                    break
                
            for span in spans:
                if  span.text.strip() == "Tipo de veículo":
                    link_tipoVeiculo = div.find('span', class_={'ad__sc-hj0yqs-0','ekhFnR'})
                    if link_tipoVeiculo:
                        tipoVeiculo_encontrado = link_tipoVeiculo.text.strip()
                    break
                
            for span in spans:
                if  span.text.strip() == "Cor":
                    link_cor = div.find('span', class_={'ad__sc-hj0yqs-0','ekhFnR'})
                    if link_cor:
                        cor_encontrada = link_cor.text.strip()
                    break

            marcas = [marca_encontrada if marca_encontrada else 'null']
            modelos = [modelo_encontrado if modelo_encontrado else 'null']
            anos = [ano_encontrado if ano_encontrado else 'null']
            cambios = [cambio_encontrado if cambio_encontrado else 'null']
            tiposVeiculo = [tipoVeiculo_encontrado if tipoVeiculo_encontrado else 'null']
            cores = [cor_encontrada if cor_encontrada else 'null']
            
            
            for i in range(len(marcas)):
                anuncio = [
                    marcas[i],
                    modelos[i],
                    anos[i],
                    cambios[i],
                    tiposVeiculo[i],
                    cores[i],
                    valor.text.replace(".","").replace("R$","").strip(),
                    municipio.text
                    ]
        anuncios = anuncios+[anuncio]
        print(f"\n\n####################### Página {countPages} #######################\n#######################          #######################")
        print(linkUrl)
        countPages +=1
    return anuncios

print(varrerPagina(varrerLinks()))