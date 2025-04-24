import re
import testeum

texto = testeum.extrair_texto_pdf('OCR/notas/nota2.pdf')
quantidade = re.search(r'([K][G]|[U][N])[ ][0-9]+[.|,][0-9]{2}', texto)
quantidade = quantidade.group()
item = re.search(r'^[0-9]{4}[ ][A-Z]', texto)

print(quantidade)
print(item)
