#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
moraes = Pessoa(1, "Kauã Moraes")
print(moraes)

#Quero mostrar só o nome
print(moraes.nome)

print("DAQUI PRA FRENTE É ACESSO AO BANCO...")

#Chama o objeto de banco de dados
db = Database()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)

