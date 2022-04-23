import tkinter as tk

janela = tk.Tk()

varPromocoes = tk.IntVar()
checkboxPromocoes = tk.Checkbutton(text='Deseja receber e-mail promocionais?', variable=varPromocoes)
checkboxPromocoes.grid(row=0, column=0)

varPoliticas = tk.IntVar()
checkboxPoliticas = tk.Checkbutton(text='Aceitar Termos de Uso e Políticas de Privacidade', variable=varPoliticas)
checkboxPoliticas.grid(row=1, column=0)


def enviar():
    if varPromocoes.get():
        print("Usuário deseja receber promoções.")
    else:
        print("Usuário não deseja receber promoções.")
    if varPoliticas.get():
        print("Usuário concordou com Termos de Uso e Políticas de Privacidade.")
    else:
        print("Usuário NÃO concordou com Termos de Uso e Políticas de Privacidade.")


botaoEnviar = tk.Button(text='Enviar', command=enviar)
botaoEnviar.grid(row=2, column=0)

janela.mainloop()