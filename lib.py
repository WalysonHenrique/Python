def verificarNumeroLista(y):
    x = [1,2,3,4,5,6,7,8,9,11,12]
    verificador = False
    for i in x:
        if i == y:
            print("O numero esta na lista")
            verificador = True
            break
        
    if verificador == False:
        print("O numero nao esta na lista")
            
            

            
            

def somarVetores(x,y):
    z = []
    if len(x) != len(y):
        print("Isto é impossível")
        return False
    
    
    for i in range(len(x)):
        z.append(x[i] + y[i])
    print(z)
    