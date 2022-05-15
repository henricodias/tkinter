import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkcalendar import DateEntry
import pandas as pd
import requests
from datetime import datetime
import numpy as np

janela = tk.Tk()

janela.title('Ferramenta de Cotação de Moedas')

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionarioMoedas = requisicao.json()

listaMoedas = list(dicionarioMoedas.keys())

varCaminhoArquivo = tk.StringVar(value='Vazio')

def BuscarCotacao():
    moeda = comboboxSelecionarMoeda.get()
    dataCotacao = calendarioMoeda.get()
    ano = dataCotacao[-4:]
    mes = dataCotacao[3:5]
    dia = dataCotacao[:2]
    link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}"
    requisicaoMoeda = requests.get(link)
    cotacao = requisicaoMoeda.json()
    valorMoeda = cotacao[0]['bid']
    labelExibirCotacao['text'] = f"Cotação de {moeda} em {dataCotacao}: R$ {valorMoeda}"

def SelecionarArquivo():
    caminhoArquivo = askopenfilename(title='Selecione o arquivo')
    varCaminhoArquivo.set(caminhoArquivo)
    if caminhoArquivo:
        labelArquivoSelecionado['text'] = f"Arquivo selecionado: {caminhoArquivo}"

def AtualizarCotacoes():
    try:
        # ler o dataframe de moedas
        df = pd.read_excel(varCaminhoArquivo.get())
        moedas = df.iloc[:,0]

        #pegar a data de inicio e a data final das cotações
        dataInicial = calendarioDataInicial.get()
        dataFinal = calendarioDataFinal.get()
        anoInicial = dataInicial[-4:]
        mesInicial = dataInicial[3:5]
        diaInicial = dataInicial[:2]
        anoFinal = dataFinal[-4:]
        mesFinal = dataFinal[3:5]
        diaFinal = dataFinal[:2]

        for moeda in moedas:
            link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?" \
                   f"start_date={anoInicial}{mesInicial}{diaInicial}&" \
                   f"end_date={anoFinal}{mesFinal}{diaFinal}"
            requisicaoMoeda = requests.get(link)
            cotacoes = requisicaoMoeda.json()

            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in df:
                    df[data] = np.nan

                df.loc[df.iloc[:,0] == moeda, data] = bid
        df.to_excel("moedas.xlsx")
        labelCotacaoAtualizada['text'] = "Arquivo atualizado com sucesso."
    except:
        labelCotacaoAtualizada['text'] = "Selecione um arquivo no formato xlsx"



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

botaoSelecionarArquivo = tk.Button(text='Selecionar Arquivo', command=SelecionarArquivo)
botaoSelecionarArquivo.grid(row=5, column=2, padx=10, pady=10, sticky='NSEW')

labelArquivoSelecionado = tk.Label(text='Nenhum arquivo selecionado', anchor='e')
labelArquivoSelecionado.grid(row=6, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3)

labelDataInicial = tk.Label(text='Data Inicial')
labelDataInicial.grid(row=7, column=0, padx=10, pady=10, sticky='NSEW')

labelDataFinal = tk.Label(text='Data Final',)
labelDataFinal.grid(row=8, column=0, padx=10, pady=10, sticky='NSEW')

calendarioDataInicial = DateEntry(year=2022, locale='pt_br')
calendarioDataInicial.grid(row=7, column=1, padx=10, pady=10, sticky='NSEW')

calendarioDataFinal = DateEntry(year=2022, locale='pt_br')
calendarioDataFinal.grid(row=8, column=1, padx=10, pady=10, sticky='NSEW')

botaoAtualizarCotacoes = tk.Button(text='Atualizar Cotações', command=AtualizarCotacoes)
botaoAtualizarCotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='NSEW')

labelCotacaoAtualizada = tk.Label(text='')
labelCotacaoAtualizada.grid(row=9, column=1, padx=10, pady=10, sticky='NSEW', columnspan=2)

botaoFechar = tk.Button(text='Fechar', command=janela.quit)
botaoFechar.grid(row=10, column=2, padx=10, pady=10, sticky='NSEW')

janela.mainloop()