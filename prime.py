import mysql.connector
import numpy as np 
import pandas as pd
import plotly.express as px

con = mysql.connector.connect(host='localhost',db='financecontrol',user='root',password='Mhbl2@@2')

cursor = con.cursor()

def bd_dataframe(nome_tb, nome_lista, funcao,nomedf):
    cursor.execute(f'SELECT * FROM {nome_tb}')
    nome_lista = cursor.fetchall()
    nomedf = pd.DataFrame(nome_lista, columns = ['id','id_usuario',f'{funcao}','valor','data' ])
    fig = px.bar(nomedf, x=f"{funcao}", y='valor', color='data')
    fig.show()



    
    






bd_dataframe('tb_dividas_fixas', 'dividas', 'dividas','df_dividas')
bd_dataframe('tb_entradas_fixas', 'dividas', 'entradas','df_entradas')


