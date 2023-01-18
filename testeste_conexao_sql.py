from multiprocessing.resource_sharer import stop
import pyodbc
import mysql.connector
import mysqlx

con = mysql.connector.connect(host='localhost',db='financecontrol',user='root',password='Mhbl2@@2')

if con.is_connected():
    db_info = con.get_server_info()
    print("conectado")


cursor = con.cursor()

#idusuario = int(input("Digite seu id"))


#cursor.execute(f'SELECT valor_dividasF FROM tb_dividas_fixas WHERE id_usuario = {idusuario}') 
cursor.execute('SELECT valor_dividasF FROM tb_dividas_fixas')
resultado = cursor.fetchall()
loop = len(resultado)
x = 0
lista_dividas = []


while x < loop:
    lista_dividas.append(resultado[x][0])
    x = x + 1

print(lista_dividas)






#def consulta(conexao, sql):
#    c=con.cursor()
#    c.execute(sql)
#    resultado=c.fetchall()
#    return resultado

#vsql="SELECT * FROM tb_dividas_fixas"
#res=consulta(con,vsql)

#for r in res:
#    print(r)
#    print('-------------------')
#    dividas = r
#    dividas = list(r)
    #print (dividasL)

#print (dividas)





    