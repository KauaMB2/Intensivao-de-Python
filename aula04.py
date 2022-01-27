import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
from IPython.display import display

tabela = pd.read_csv("advertising.csv")
display(tabela)
sns.heatmap(tabela.corr(), annot=True, cmap="Wistia")
plt.show()
# outra forma de ver a mesma análise
# sns.pairplot(tabela)
# plt.show()
y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1)#Indica que todo o dataframe com exceção da coluna ‘Vendas’ irão
                                 #compor os valore de X (inputs)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# cria as inteligencias aritificiais
modeloRegressaoLinear = LinearRegression()#Inteligencia 1
modeloArvoreDecisao = RandomForestRegressor()#Inteligencia 2

# treina as inteligencias artificias
modeloRegressaoLinear.fit(x_treino, y_treino)
modeloArvoreDecisao.fit(x_treino, y_treino)

# Faz as previsoes com a variável x_teste
previsaoRegressaoLinear = modeloRegressaoLinear.predict(x_teste)
previsaoArvoreDecisao = modeloArvoreDecisao.predict(x_teste)

# Comparar os modelos
comparacao1=metrics.r2_score(y_teste, previsaoRegressaoLinear)
comparacao2=metrics.r2_score(y_teste, previsaoArvoreDecisao)
print(comparacao1)
print(comparacao2) 
#Modelo árvore de decisão é melhor!!
tabelaAuxiliar=pd.DataFrame()
tabelaAuxiliar["y_teste"]=y_teste
tabelaAuxiliar["Previsoes Arvore Decisao"]=previsaoArvoreDecisao
tabelaAuxiliar["Previsoes Regressao Linear"]=previsaoRegressaoLinear

plt.figure(figsize=(15,6))
sns.lineplot(data=tabelaAuxiliar)
plt.show()