#importar base de dados - passo 1 OK

#visualizar base de dados - passo 2
#entender a inf disponivel
#descobrir as cagadas

#tratamento de dados - passo 3
#resolver valores errados
#resolver valores vazios

#analise inicial - passo 4

#analise detalhada - passo5 / descobrir relações

import pandas as pd
import plotly.express as px

tabela = pd.read_csv('cartaocorporativo.csv', sheets=1)
tabela = tabela.drop(["CPF SERVIDOR", "TIPO", "CDIC"], axis=1)

tabela["VALOR"] = pd.to_numeric(tabela["VALOR"], errors="ignore")
tabela["VALOR"] = tabela["VALOR"].str.replace('[R$]', '') 

#print(tabela["VALOR"].sum()) precisa transformar em float
print(tabela["SUBELEMENTO DE DESPESA"].value_counts())
print(tabela["SUBELEMENTO DE DESPESA"].value_counts(normalize=True).map("{:.1%}".format))

print(tabela.info())
print(tabela)
#cria o grafico

#para cada coluna da minha tabela, quero criar um grafico

for coluna in tabela.columns:
    #coluna = "SUBELEMENTO DE DESPESA"
    grafico = px.histogram(tabela, x=coluna, color="DATA PGTO", text_auto=True)
#px.barplot
#px.piechart
#exibi o grafico
    grafico.show()