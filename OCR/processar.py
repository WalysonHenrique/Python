import re
import testeum

# Extração de texto do PDF
texto = testeum.extrair_texto_pdf('OCR/notas/nota3.pdf')

# Capturar todas as quantidades e itens
quantidades = re.findall(r'([K][G]|[U][N]) ([0-9]+[.|,][0-9]{2})', texto)
itens = re.findall(r'\n(\d{4}) ([^0-9\n]+)', texto)

# Converter a lista de tuplas para lista de apenas os valores
valores = [match[1] for match in quantidades]

# Criar um dicionário associando código, descrição e quantidade
dados = []
for i, item in enumerate(itens):
    codigo, descricao = item
    quantidade = valores[i] if i < len(valores) else "N/A"  # Evita erro se faltar uma quantidade
    dados.append({"Código": codigo, "Descrição": descricao.strip(), "Quantidade": quantidade})

# Exibir dados organizados
print("\nItens organizados:")
for produto in dados:
    print(produto)