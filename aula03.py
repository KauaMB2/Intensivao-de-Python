import pandas as pd
from IPython.display import display
import pandas as pd
import plotly.express as px
tabela=pd.read_csv("telecom_users.csv")
tabela=tabela.drop("Unnamed: 0",axis=1)#axis=0 ->linha|axis=1 ->coluna
display(tabela)
tabela["TotalGasto"]=pd.to_numeric(tabela["TotalGasto"],errors="coerce")
#tabela[coluna]=pd.to_numeric(tabela[coluna],errors="coerce")
#Passa os valores para numericos(string->float)
#Se não tiver nenhum valor, fica nulo(errors="coerce")
tabela=tabela.dropna(how="all",axis=1)#Exclui as colunas vazias
tabela=tabela.dropna(how="any",axis=0)#Exclui as linhas com algum dado vazio
display(tabela.info())
print(tabela["Churn"].value_counts())#Calcula a quantidade de "Sim"´s e de "Não"´s da coluna Churn
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))#Também cálcula quantidade, só que em porcentagem
for coluna in tabela.columns:
    grafico=px.histogram(tabela,x=coluna,color="Churn")
    grafico.show()
tabela=pd.read_csv("telecom_users.csv")
tabela=tabela.drop("Unnamed: 0",axis=1)#axis=0 ->linha|axis=1 ->coluna
tabela["TotalGasto"]=pd.to_numeric(tabela["TotalGasto"],errors="coerce")
#tabela[coluna]=pd.to_numeric(tabela[coluna],errors="coerce")
#Passa os valores para numericos(string->float)
#Se não tiver nenhum valor, fica nulo(errors="coerce")
tabela=tabela.dropna(how="all",axis=1)#Exclui as colunas vazias
tabela=tabela.dropna(how="any",axis=0)#Exclui as linhas com algum dado vazio
for coluna in tabela.columns:
    grafico=px.histogram(tabela,x=coluna,color="Churn")
    grafico.show()