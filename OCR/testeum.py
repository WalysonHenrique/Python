from PIL import Image
import pytesseract
import os
from pdf2image import convert_from_path

# Define o caminho para o executável do Tesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:/Users/20231stads005/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


def extrair_texto_pdf(caminho_pdf):
    try:
        imagens = convert_from_path(caminho_pdf)
        texto = ""
        for imagem in imagens:
            texto += pytesseract.image_to_string(imagem, lang='por')
        return texto
    except Exception as e:
        print(f"Erro: {e}")
        return None

 # Exemplo de uso:
# caminho_pdf = 'OCR/notas/nota3.pdf'
# if os.path.exists(caminho_pdf):
#     texto_extraido = extrair_texto_pdf(caminho_pdf)
#     if texto_extraido:
#         print("Extracao feita \n\n")
#         # Salvar o texto extraído em um arquivo de texto
#         with open('OCR/extraidos/texto_extraido3.txt', 'w', encoding='utf-8') as arquivo:
#             arquivo.write(texto_extraido)
# else:
#      print(f"Erro: O arquivo '{caminho_pdf}' não foi encontrado.")
  