import requests
import bs4


response = requests.get('https://www.lexico.pt/')

soup = bs4.BeautifulSoup(response.text, 'html.parser')

links = [a.get('href') for a in soup.find_all('a', href=True)]

urls = ['www.lexico.pt'.links]


        

linksLimpos = soup.find_all('a', attrs={'class':'sinonimo'})






