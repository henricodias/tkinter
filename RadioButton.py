import tkinter as tk
from tkinter import ttk

def enviar():
    print(varAviao.get())

janela = tk.Tk()

varAviao = tk.StringVar(value='Vazio')

botaoClasseEconomica = tk.Radiobutton(text='Classe Econômica', variable=varAviao, value='Classe Econômica', command=enviar)
botaoClasseEconomica.grid(row=0, column=0)

botaoClasseExecutiva = tk.Radiobutton(text='Classe Executiva', variable=varAviao, value='Classe Executiva', command=enviar)
botaoClasseExecutiva.grid(row=0, column=1)

botaoPrimeiraClasse = tk.Radiobutton(text='Primeira Classe', variable=varAviao, value='Primeira Classe', command=enviar)
botaoPrimeiraClasse.grid(row=0, column=2)


# botaoEnviar = tk.Button(text='Enviar', command=enviar)
# botaoEnviar.grid(row=1, column=1)

janela.mainloop()