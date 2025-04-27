from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import bs4
import trabalhoRaparOlx
import fileinput


def cadastrarUsuario(nome, email, senha):
    driver = webdriver.Edge()
    driver.get("http://weka.inf.ufes.br/IFESTP/index.php")
    time.sleep(2)
    elem = driver.find_element(By.NAME, "username")
    time.sleep(1)   
    elem.send_keys(nome)
    elem = driver.find_element(By.NAME, "email")
    time.sleep(1)
    elem.send_keys(email)
    elem = driver.find_element(By.NAME, "password")
    time.sleep(1)
    elem.send_keys(senha)
    elem = driver.find_element(By.NAME, "passwordConfirm")
    time.sleep(1)
    elem.send_keys(senha)
    elam = driver.find_element(By.NAME, "submit")
    time.sleep(1)
    elam.click()
    time.sleep(1)
    driver.quit()


def inserirCarros(url, nome, email, senha):
    cadastrarUsuario(nome, email, senha)
    anuncios = trabalhoRaparOlx.varrerPagina(trabalhoRaparOlx.varrerLinks(url))
    driver = webdriver.Edge()
    print(anuncios)
    driver.get("http://weka.inf.ufes.br/IFESTP/login.php")
    time.sleep(2)
    elem = driver.find_element(By.NAME, "username")
    time.sleep(1)   
    elem.send_keys(nome)
    elem = driver.find_element(By.NAME, "password")
    elem.send_keys(senha)
    elem.send_keys(Keys.RETURN)

    for anuncio in anuncios:
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div/div/div/button")
        elem.click()
        elem = driver.find_element(By.NAME, "marca")
        time.sleep(1)
        elem.send_keys(anuncio[0])
        time.sleep(1)
        elem = driver.find_element(By.NAME, "modelo")
        time.sleep(1)
        elem.send_keys(anuncio[1])
        time.sleep(1)
        elem = driver.find_element(By.NAME, "ano")
        time.sleep(1)
        elem.send_keys(anuncio[2])
        time.sleep(1)
        elem = driver.find_element(By.NAME, "cambioAutomatico")
        if anuncio[3] == "Automático":
            elem.click()
        time.sleep(1)
        
        if anuncio[4] == "Sedã":
            elem = driver.find_element(By.ID, "c_sedan")
            elem.click()
        elif anuncio[4] == "Hatch":
            elem = driver.find_element(By.ID, "c_hatch")
            elem.click() 
        time.sleep(1)
        select = Select(driver.find_element(By.NAME, 'cor'))
        opcoes_dropdown = [option.text for option in select.options]

        if anuncio[5] in opcoes_dropdown:
            select.select_by_visible_text(anuncio[5])
        else:
            select.select_by_visible_text('Outro')
            print(anuncio[5])
        time.sleep(1)
        elem = driver.find_element(By.NAME, "valor")
        time.sleep(1)
        elem.send_keys(anuncio[6])
        elem = driver.find_element(By.NAME, "municipio")
        time.sleep(1)
        elem.send_keys(anuncio[7])
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

    driver.quit()
    print("Carros cadastrados com sucesso")


inserirCarros('https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-es?ps=50000&pe=50000&exc=1&ms=0&me=40000&gb=2&gb=1&cac=3&cac=1&cac=4&cac=2&ctp=8&ctp=9&ctp=3',
              'Walysinn',
              'walysinn@gmail.com',
              '12345')