import requests
from bs4 import BeautifulSoup

# Lista de tags ultrapassadas
deprecated_tags = ["font", "center", "bgsound", "marquee", "applet", "basefont", "blink"]

def verificar_tags_obsoletas(url):
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        soup = BeautifulSoup(resposta.text, 'html.parser')
        
        tags_encontradas = []
        for tag in deprecated_tags:
            if soup.find_all(tag):
                tags_encontradas.append(tag)
        
        if tags_encontradas:
            print(f"⚠️ Tags ultrapassadas encontradas em {url}: {tags_encontradas}")
        else:
            print(f"✅ Nenhuma tag obsoleta detectada em {url}")
    
    except Exception as e:
        print(f"❌ Erro ao acessar {url}: {e}")

# Teste com um site qualquer
verificar_tags_obsoletas("https://bcsupermercados.com.br")
