#1o passo: improta a biblioteca sqlite3
import sqlite3

#2o passo: VAmos estabelecer uma
#conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

#4o. passo: Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5o.passo: Executar o comando SQl no SQLite (no cursor)
cursor.execute(sql)

#6o. passe: Exibir a consulta com tofos os nomes de hérois e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")