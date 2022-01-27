# Intensivão de Python
>  O intuito desse commit é deixar salvo a resolução de todos os exercícios das 10 horas de aulas do Intensivão de Python, feito pela galera da <a href="https://www.youtube.com/c/HashtagPrograma%C3%A7%C3%A3o">Hashtag Programação</a>.

![GitHub repo size](https://img.shields.io/github/repo-size/KauaMB2/CPlusPlus-CFBCursos?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/KauaMB2/CPlusPlus-CFBCursos?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/KauaMB2/CPlusPlus-CFBCursos?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/KauaMB2/CPlusPlus-CFBCursos?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/KauaMB2/CPlusPlus-CFBCursos?style=for-the-badge)
<hr>

Os programas foram feitos no Jupyter Notebook, mas meu Github sempre buga quando posto algum arquivo Jupyter. Então passei para arquivos .py. <br> Além disso não consegui fazer o commit junto com os arquivos Excel, caso queiram dar olha olhada nos programas com os arquivos, cliquem <a href="https://drive.google.com/drive/folders/1JLa3vHvF_U4J4wTVkjKy0wn6NrrHAkPK"> aqui</a>.

## Bibliotecas usadas

 - [X] import pandas
 - [X] import selenium
 - [X] import pyautogui
 - [X] import pyperclip
 - [X] from IPython.display import display
 - [X] import plotly.express
 - [X] import time
 - [X] import os
 - [X] import matplotlib.pyplot
 - [X] import seaborn
 - [X] from sklearn.model_selection import train_test_split
 - [X] from sklearn.linear_model import LinearRegression
 - [X] from sklearn.ensemble import RandomForestRegressor

<hr>

### Aula 1

<ul>Na aula 1, foi feito um programa que entra no Google Drive, faz o download do relatório em Excel e após isso, entra no E-mail e envia o relatório para alguém específico com um texto de explicação. Tudo isso foi feito de forma automática!
</ul>

### Aula 2

<ul>Na aula 2, fizemos o tratamento de erros dentro de uma tabela em Excel e após isso fezemos a análise dos dados com gráficos que o próprio programa constrói.
</ul>

### Aula 3

<ul>
Na aula três fizemos outra automação. Desta vez,fizemos um programa que entra no Google, pega a cotação do dolar, euro e do ouro e após isso preenche uma tabela em Excel com os valores da cotação e faz os cálculos dos preços dos produtos em relação à cotação das moedas.
</ul>

### Aula 4

<ul>
Na aula 4, trabalhamos com Inteligência Artificial e Machine Learning. <br><br>Desenvolvemos um programa que mostra o nível de relação entre os produtos(Rádio, Jornal e TV) e a quantidade de vendas.
<img src= "img\imgRelacao.png">
Quanto mais alaranjado e maior for o valor(que varia de 0 até 1), maior será a venda do produto.<br><br>
Após isso, sabendo que a venda dos produtos estavam relacionadas entre si, treinamos duas I.A's para fazer uma previsão de quantos produtos iremos vender(Y) se investirmos em outro produto diferente(X). O primeiro modelo de I.A foi o modelo de "Árvore de decisão", e o segundo foi um de "Regressão Linear". Após treiná-las, pedimos para as duas fazerem uma previão e após isso comparamos o quão próximos as suas respectivas previsões estavam da realidade. Segue abaixo o gráfico da previsão:
<img src="img\imgPrevisao.png">

O modelo "Regressão Linear" teve 89,5% de coerência com a realidade.<br>
O modelo "Árvore de decisão" teve incríveis 93,0% de coerência com a realidade.
> Logo, podemos concluir que o modelo Árvore de decisão está mais ápto para ser usado.

<br>
Após isso só basta fazer novas previsões e usar a I.A melhor!
</ul>