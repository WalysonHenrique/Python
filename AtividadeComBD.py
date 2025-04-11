import mysql.connector
import re
conn = mysql.connector.connect(host="localhost" ,database="bdpython", port="3306", user="root", password="root")
mycursor = conn.cursor()


def validador(cpf):
  #Retira apenas os dígitos do CPF, ignorando os caracteres especiais
  numeros = [int(digito) for digito in cpf if digito.isdigit()]

  quant_digitos = False
  validacao1 = False
  validacao2 = False

  

  if len(numeros) == 11:
      quant_digitos = True
  
      soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
      digito_esperado = (soma_produtos * 10 % 11) % 10
      if numeros[9] == digito_esperado:
          validacao1 = True

      soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
      digito_esperado1 = (soma_produtos1 *10 % 11) % 10
      if numeros[10] == digito_esperado1:
          validacao2 = True

      if quant_digitos ==  True and validacao1 == True and validacao2 == True:
          return True
      else:
          return False
  else:
      return False


while True:
    print("1 - Inserir dados")
    print("2 - Visualizar dados")
    print("0 - Sair")
    option = int(input("Escolha uma opção: "))
    if option == 1:
        nome = input("Digite seu nome: " )
        cpf = input("Digite seu cpf: ")
        if validador(cpf):
          
            nascimento = input("Digite o seu nascimento: ")
            altura = float(input("Digite a sua altura: "))
            peso = float(input("Digite o seu peso: "))
            
            try:
                sql = "insert into pessoa(nome, cpf, nascimento, altura, peso) values (%s,%s,%s,%s,%s)"
                val = (nome, cpf, nascimento,altura, peso)
                mycursor.execute(sql, val)
                conn.commit()
                print("Usuario inserido com sucesso!")
            except Exception as e:
                print(f"Erro {e}")
        
    if option ==2:
        
        mycursor.execute("select * from pessoa")
        result = mycursor.fetchall()
        
        for i in result:
            print(i)
        
    if option == 0:
        print("Saindo ...")
        break
        
        