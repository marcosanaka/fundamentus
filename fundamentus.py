######################################################################################
# Dev: Marcos Roberto Batista de Souza
# Email: marcos_anaka@hotmail.com
# Simples codigo em python para scraping na pagina da fundamentus
######################################################################################

#!/usr/bin/env python
# coding: utf-8

# imports

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

#WEB SCRAPING
url = 'http://www.fundamentus.com.br/resultado.php'
r = requests.get(url)

#Verifica a importação dos dados

if r.status_code == 200:
    print('Requisição bem sucedida!')
    content = r.content

#utilizar a biblioteca BeautifulSoup para extrair a tabela. 
res = BeautifulSoup(content, 'html.parser')


#Acessar o elemento chamando o método find passando como argumento o nome da tag, no caso table 
table = res.find(name='table')


#Converter para string

table_str = str(table)

#Agora que temos o código HTML da tabela, podemos utilizar o Pandas para carregar os dados em um Data Frame, utilizando o método read_html.

df = pd.read_html(table_str)[0]


# In[112]:


#Converter os valores para numericos
numeric_cols = df.columns.drop(['Papel','Div.Yield','Mrg Ebit','Mrg. Líq.','ROIC','ROE','Liq.2meses','Cresc. Rec.5a','Patrim. Líq'])
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)


#ordena Data Frame por P/L do menor para o maior
sorted_df = df.sort_values(by=['P/L'],axis=0, ascending=False)



#imprime os resultador
df.head(900)