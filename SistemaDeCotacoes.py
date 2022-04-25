import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

janela = tk.Tk()

janela.title('Ferramenta de Cotação de Moedas')

listaMoedas = ['USD', 'BTC']

def BuscarCotacao():
    pass

labelCotacaoMoeda = tk.Label(text='Cotação de uma moeda específica', borderwidth=2, relief='solid')
labelCotacaoMoeda.grid(row=0, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3)

labelSelecionarMoeda = tk.Label(text='Selecione a moeda que deseja consulta')
labelSelecionarMoeda.grid(row=1, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

comboboxSelecionarMoeda = ttk.Combobox(values=listaMoedas)
comboboxSelecionarMoeda.grid(row=1, column=2, padx=10, pady=10, sticky='NSEW')

labelSelecionarData = tk.Label(text='Selecione o dia que deseja consultar a cotação')
labelSelecionarData.grid(row=2, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

calendarioMoeda = DateEntry(year=2022, locale='pt_br')
calendarioMoeda.grid(row=2, column=2, padx=10, pady=10, sticky='NSEW')

labelExibirCotacao = tk.Label(text='')
labelExibirCotacao.grid(row=3, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

botaoBsucarCotacao = tk.Button(text='Buscar Cotação', command=BuscarCotacao)
botaoBsucarCotacao.grid(row=3, column=2, padx=10, pady=10, sticky='NSEW')

labelCotacaoVariasMoedas = tk.Label(text='Cotação de múltiplas moedas', borderwidth=2, relief='solid')
labelCotacaoVariasMoedas.grid(row=4, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3)

labelSelecionarArquivo = tk.Label(text='Selecione o arquivo para consulta:')
labelSelecionarArquivo.grid(row=5, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)






janela.mainloop()