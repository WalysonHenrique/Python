import re
import testeum

texto = testeum.extrair_texto_pdf('C:/Users/henrique/Documents/Codes/Python/OCR/notas/nota2.pdf')

# Extrair data de saída
data_saida = re.search(r"DATA DA SAÍDA.*?(\d{2}/\d{2}/\d{4})", texto)
if data_saida:
    data_saida = data_saida.group(1).strip()
    print(f"Data de saída: {data_saida}")

# Extrair número da nota de empenho
nota_empenho = re.search(r"NOTA DE EMPENHO (\d{4}NE\d+)", texto)
if nota_empenho:
    nota_empenho = nota_empenho.group(1).strip()
    print(f"Nota de empenho: {nota_empenho}")

# Extrair quantidade e nome do item
itens = []
linhas = texto.split('\n')
for linha in linhas:
    match = re.search(r"(?:.*?\|){3}(.{7})", linha)
    if match:
        quantidade = match.group(1)
        nome_item = match.group(2)
        valores = re.findall(r"(\d{1,}\.\d{2})", linha)
        if len(valores) > 1:
            valor_item = valores[1]
            itens.append({
                "quantidade": quantidade,
                "nome_item": nome_item,
                "valor_item": valor_item
            })
  

for item in itens:
     print(f"Quantidade: {item['quantidade']}, Nome do item: {item['nome_item']}, Valor item: {item['valor_item']}")