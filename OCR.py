from PIL import Image
import pytesseract

# # Carregar a imagem
img = Image.open('imagem_exemplo.png')

# # Converter a imagem para grayscale
img_gray = img.convert('L')

# # Salvar a imagem em grayscale
img_gray.save('imagem_exemplo_gray.png')

# # Realizar a leitura do texto com OCR
texto = pytesseract.image_to_string(img_gray)

# # Imprimir o texto extraído
print(texto)
