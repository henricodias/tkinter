from tkinter.filedialog import askopenfilename
import pandas as pd

caminhoArquivo = askopenfilename(title='Selecione um arquivo em Excel para abrir')

df = pd.read_excel(caminhoArquivo)

print(df)