from bs4 import BeautifulSoup
import requests

url_site = 'https://globo.com'


response = requests.get(url_site)


soup = BeautifulSoup(response.text, 'html.parser')
noticias = soup.find_all('div', attrs={'data-tracking-action':'esporte'})


"""
for noticia in noticias:
    noticiaEsporte = noticia.find('h2')
    if(noticiaEsporte != None):
        print(noticiaEsporte.text)
"""

for noticia in noticias:
    noticiaEsporte = noticia.find('h2')
   
    print(noticiaEsporte)

