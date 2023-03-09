import pandas as pd
import plotly.io as pio
import plotly.express as px

#from os.path import dirname, join
#current_dir = dirname(__file__)
#file_path = join(current_dir, "./test.txt")
#with open(file_path, 'r') as f:

tabela = pd.read_csv('cartaocorporativo.csv') # importar o arquivo csv
print(tabela) # imprimir os dados da tabela

print(tabela.info()) # imprime os dados das colunas e tipos

print(tabela['CPF/CNPJ FORNECEDOR'].value_counts(normalize=True).map('{:.1%}'.format))
print(tabela['NOME FORNECEDOR'].value_counts(normalize=True).map('{:.1%}'.format))
print(tabela['VALOR'].value_counts(normalize=True).map('{:.1%}'.format))
print(tabela['SUBELEMENTO DE DESPESA'].value_counts(normalize=True).map('{:.1%}'.format))


for coluna in tabela:
    if coluna != "customerID":
        fig = px.histogram(tabela, x=coluna, color="CPF/CNPJ FORNECEDOR")
        fig.show()
        print(tabela.pivot_table(index="CPF/CNPJ FORNECEDOR", columns=coluna, aggfunc='cont')["customerID"])

for coluna in tabela:
    if coluna != "customerID":
        fig = px.density_mapbox(tabela, x=coluna, color="VALOR")
        fig.show()
        print(tabela.pivot_table(index="VALOR", columns=coluna, aggfunc='cont')["customerID"])