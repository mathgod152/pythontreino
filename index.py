
import mysql.connector
import numpy as np 
import pandas as pd
import plotly.express as px

con = mysql.connector.connect(host='localhost',db='financecontrol',user='root',password='Mhbl2@@2')

if con.is_connected():
    db_info = con.get_server_info()
    print("conectado")


cursor = con.cursor()

cursor.execute('SELECT * FROM tb_dividas_fixas')
dividas = cursor.fetchall()


loop = len(dividas)
x = 0
lista_dividas = []


#while x < loop:
#    lista_dividas.append(resultado[x][0])
#    x = x + 1



df = pd.DataFrame(dividas, columns = ['id','id_usuario','gasto','valor','data' ])
print(df)


#px.bar(x=[1, 2, 3, 4, 5], y=[10, 40, 20, 50, 5])

fig = px.bar(df, x="gasto", y='valor', color='data')



fig.show()