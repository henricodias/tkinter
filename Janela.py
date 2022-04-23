import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='#7E40C8', width=40, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

# moeda = tk.Entry()
# moeda.grid(row=1, column=1)

dicionarioCotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000,
}

moedas = list(dicionarioCotacoes.keys())
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)


def buscar_cotacao():
    moedaPreenchida = moeda.get()
    cotacaoMoeda = dicionarioCotacoes.get(moedaPreenchida)
    mensagemCotacao = tk.Label(text="Cotação não encontrada")
    mensagemCotacao.grid(row=3, column=0)
    if cotacaoMoeda:
        mensagemCotacao["text"] = f"Cotação do {moedaPreenchida} é de {cotacaoMoeda} reais"


botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

mensagem3 = tk.Label(text="Para mais de 1 cotação, digite uma moeda em cadas linha")
mensagem3.grid(row=4, column=0, columnspan=2)

caixaTexto = tk.Text(width=10, height=5)
caixaTexto.grid(row=5, column=0, sticky='NSEW')

def buscar_cotacoes():
    texto = caixaTexto.get("1.0", tk.END)
    listaMoedas = texto.split('\n')
    mensagemCotacoes = []
    for item in listaMoedas:
        cotacao = dicionarioCotacoes.get(item)
        if cotacao:
            mensagemCotacoes.append(f'{item} : {cotacao}')
    mensagem4 = tk.Label(text='\n'.join(mensagemCotacoes))
    mensagem4.grid(row=6, column=1)


botaoMultiplasCotacoes = tk.Button(text="Buscar Cotações", command=buscar_cotacoes)
botaoMultiplasCotacoes.grid(row=5, column=1)
janela.mainloop()
