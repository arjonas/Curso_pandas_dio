# -*- coding: utf-8 -*-
"""Visualização de dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v0lnoHwosgRBXhHzAYisRis841kfmCeq
"""

import pandas as pd

p1 = pd.read_excel("/content/drive/MyDrive/curso pandas dio/datasets/Aracaju.xlsx")
p2 = pd.read_excel("/content/drive/MyDrive/curso pandas dio/datasets/Fortaleza.xlsx")
p3 = pd.read_excel("/content/drive/MyDrive/curso pandas dio/datasets/Natal.xlsx")
p4 = pd.read_excel("/content/drive/MyDrive/curso pandas dio/datasets/Recife.xlsx")
p5 = pd.read_excel("/content/drive/MyDrive/curso pandas dio/datasets/Salvador.xlsx")

p5.head()

# concateia os dataframes p1,p2,p3,p4,p5

df = pd.concat([p1,p2,p3,p4,p5])

df

#amostra de dados de df

df.sample(5)

#tipo de dados de cada coluna
df.dtypes

#Alterando otipo de dado da coluna LojaID
df['LojaID'] = df['LojaID'].astype("object")

df.dtypes

#Consultando se há linhas com valores faltantes 
df.isnull().sum()

#Subustituindo os valores nulos pela média
df['Vendas'].fillna(df['Vendas'].mean(), inplace=True)

#Substituindo os valores nulos por 0

df["Vendas"].fillna(0,inplace=True)

df.isnull().sum()

df['Vendas'].mean()

#Apagando as linhas com valores nulos com base apaenas em uma coluna
df.dropna(subset=["Vendas"],inplace=True)

#Apagando as linhas com valores nulos 
df.dropna(inplace=True)

#Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

"""**Criando colunas novas **

"""

#Criando coluna de Receitas

df["Receita"] = df["Vendas"].mul(df['Qtde'])

df

#Maior receita

df["Receita"].max()

#Menor receita

df["Receita"].min()

#retorna as 4 linhas com maiores  da coluna receitas

df.nlargest(4,"Receita")

#Retorna as 3 linhas com menores  da coluna receitas

df.nsmallest(5,"Receita")

#agrupamento por cidade
df.groupby("Cidade")["Receita"].sum()

#Ordenando conjunto de dados
df.sort_values("Receita", ascending=False)



#Tranformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype('int64')

#verificando o tipo de data em data
df.dtypes

#Transformando a coluna de data em data
df['Data'] = pd.to_datetime(df["Data"])

df.dtypes

#agrupamento por ano 
df.groupby(df["Data"].dt.year)["Receita"].sum()

#criando uma nova coluna com o ano
df["Ano_Vendas"] = df["Data"].dt.year

df



# Extraindo o mês e os dia de uma venda
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

df

df.sample(13)

#retornando a data mais antiga 
df["Data"].min()

#retornando a data mais recente
df["Data"].max()

#Calculando a diferença de dias entre a primeira data(inicio da contagem)
df["Diferenca_dias"] = df["Data"] - df["Data"].min()

df.sample(13)

#Criando uma coluna trimestre
df["trimestre_venda"] = df["Data"].dt.quarter

#Filtrando as vendas de 2019 do mês de março

vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

df.sample(10)

vendas_marco_19

df.sample(15)

df['LojaID'].value_counts(ascending=False).plot.bar()

df['LojaID'].value_counts(ascending=False).plot.barh()

df['LojaID'].value_counts(ascending=True).plot.bar()

df['LojaID'].value_counts(ascending=True).plot.barh();

#Grafico Pizza

df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie();

#Total de vendas por cidade
df["Cidade"].value_counts()

#Adicionando um titulo

from numpy.lib.shape_base import tile
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade");

#Adicionando um titulo e alterando o nome dos eixos
df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade");
plt.xlabel("Cidade");
plt.ylabel("Total de vendas");

#Alterando color  do grafico para laranja

#Adicionando um titulo e alterando o nome dos eixos
df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade",color='orange');
plt.xlabel("Cidade");
plt.ylabel("Total de vendas");

#Alterando estilo do grafico
plt.style.use('dark_background')

df.groupby(df['mes_venda'])['Qtde'].sum().plot(title= "total de produtos vendidos por mês");
plt.xlabel('Mês');
plt.ylabel('Total de produtos vendidos');
plt.legend();

df.groupby(df['mes_venda'])['Qtde'].sum()



#Selecionando apenas o ano de 2019

df_2019 = df[df['Ano_Vendas'] == 2019 ]

df_2019.groupby(df_2019['mes_venda'])['Qtde'].sum()

df_2019.groupby(df_2019['mes_venda'])['Qtde'].sum().plot(marker ="v");
plt.xlabel('Mês');
plt.ylabel("Toltal de produtos vendidos");
plt.legend();

#Histograma
plt.hist(df['Qtde'],color='purple');

df

df['Qtde'].max()

#Alterando estilo do grafico
plt.style.use('Solarize_Light2')

#Grafico de disperção

plt.scatter(x=df_2019['dia_venda'], y = df_2019['Receita']);

#Salvando png

df_2019.groupby(df_2019['mes_venda'])['Qtde'].sum().plot(marker = "o");
plt.title("Quantidade de produtos vendidos x mês ")
plt.xlabel('Mês');
plt.ylabel('Total de produtos vendidos');
plt.legend()
plt.savefig('Grafico QTDE X MES.png')

