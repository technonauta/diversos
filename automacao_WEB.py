#google chrome -> chromedriver
#este é para automação na internet
#o pyautogui é para automacao local

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()

#passo1: pegar a cotação do dolar
#entrar no google
navegador.get("https://www.google.com/") #link tem q ser completo

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(f"cotação dólar comercial R$ {cotacao_dolar}")


#passo2: pegar a cotação do euro
navegador.get("https://www.google.com/") #link tem q ser completo

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(f"cotação euro comercial €$ {cotacao_euro}")


#passo3: pegar a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje") #link tem q ser completo

cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",",".") #python formato USA faz conta com . e não com ,

print(f"cotação ouro 1g - R$ {cotacao_ouro}")


#passo4: importar a base de dados e atualizar a base
tabela = pd.read_excel("Produtos.xlsx")



#passo5: recalcular os preços
#atualizar a cotação
#dolar
tabela.loc[tabela["Moeda"]=="Dólar", "Cotação"] = float(cotacao_dolar)
#euro
tabela.loc[tabela["Moeda"]=="Euro", "Cotação"] = float(cotacao_euro)
#ouro
tabela.loc[tabela["Moeda"]=="Ouro", "Cotação"] = float(cotacao_ouro)

#recalcular os preços compra*preço original
tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]

#preço venda = preço compra*margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)

#passo6: exportar a base atualizada
tabela.to_excel("Produtos_Novos.xlsx", index=False)#se usar o mesmo nome substitui o arquivo usado