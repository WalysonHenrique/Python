from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import bs4
import trabalhoRaparOlx

anuncios = trabalhoRaparOlx.varrerPagina(trabalhoRaparOlx.varrerLinks())
driver = webdriver.Edge()
driver.get("http://weka.inf.ufes.br/IFESTP/login.php")
time.sleep(4)
elem = driver.find_element(By.NAME, "username")

time.sleep(1)   
elem.send_keys("WalysonHenrique")
time.sleep(1)
elem = driver.find_element(By.NAME, "password")
time.sleep(1)
elem.send_keys("447Pirata")
time.sleep(1)
for anuncio in anuncios:
    elem.send_keys(Keys.RETURN)
    time.sleep(4)
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div/button")
    elem.click()
    elem = driver.find_element(By.NAME, "marca")
    time.sleep(1)
    elem.send_keys(anuncio[])
    time.sleep(1)
    elem = driver.find_element(By.NAME, "modelo")
    time.sleep(1)
    elem.send_keys("F-50")
    time.sleep(1)
    elem = driver.find_element(By.NAME, "ano")
    time.sleep(1)
    elem.send_keys("2024")
    time.sleep(1)
    elem = driver.find_element(By.NAME, "valor")
    time.sleep(1)
    elem.send_keys("150.25")
    time.sleep(1)
    elem = driver.find_element(By.NAME, "cambioAutomatico")
    elem.click()
    time.sleep(1)
    elem = driver.find_element(By.NAME, "cor")
    time.sleep(1)
    elem.send_keys("v")
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    elem = driver.find_element(By.NAME, "municipio")
    time.sleep(1)
    elem.send_keys("Sao Paulo")
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    time.sleep(5)


