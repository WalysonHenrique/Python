class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    def exibir(self):
        print(f"O produto {self.__nome} custa R${self.__preco}")



# produto1 = Produto("Lapis", 3.50)
# produto1.exibir()

# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
#     def Apresentar(self):
#         print(f"Ola, meu nome e {self.nome}")
        
# class Funconario(Pessoa):
#     def __init__(self, nome, salario):
#         super().__init__(nome)
#         self.salario = salario
        
#     def Apresentar(self):
#         super().Apresentar()
#         print(f"O meu salario e {self.salario}")
    
        
# funconario1 = Funconario("Wallyson", 1000)
# funconario1.Apresentar()



class animal():
    def emitirSom(self):
        print("Animal emitindo som")
    
    

# class cachorro(animal):
#     def emitirSom(self):
#         print("Cachorro latindo")
    
    
# class gato(animal):
#     def emitirSom(self):
#         print("Gato miando")
        
# animais = {cachorro(), gato(), animal()}

# for i in animais:
#     i.emitirSom()



# class Banco():
#     def __init__(self):
#         self.saldo = 0
#         self._limite = 1000
#         self.__saque = 500
    
    
# banco = Banco()

# print(banco.saldo)
# print(banco._limite)
# ##print(banco.__saque) ## Erro

# print(banco._Banco__saque)##correta




class A:pass
class B(A):pass
class C(A):pass
class D(B,C):pass


print(D.__mro__)