from tkinter import *
import os
def clicar():
    while True:
        os.system('python -u "c:/Users/20231stads005/Documents/Codes/Python/interface.py"')
        print(" botao foi clicado")
def limpar():
    os.system('cls')
gui = Tk()


gui.title("Console")
gui.geometry("300x500")
button = Button(gui, text="Clique", command=clicar, width=10, height=2)
btnLimpar = Button(gui, text='Limpar', command=limpar)



#empacota o botao
button.grid(row=0, column=0)
btnLimpar.grid(row=0, column=1)

gui.mainloop()