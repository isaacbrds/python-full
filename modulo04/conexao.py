from email import charset
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='usuario',
                             password='S3cr3t4#',
                             database='pythonfullcursos',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def criar_tabela(nome):
  with connection.cursor() as cursor:
    try:
      sql = f"CREATE TABLE {nome}(nome varchar(30))"
      cursor.execute(sql)
      print('Tabela criada com sucesso!')

    except Exception as e:
      print(f"Erro aconteceu {e}")

def remover_tabela(nome):
  with connection.cursor() as cursor:
    try:
      sql = f"DROP TABLE {nome}"
      cursor.execute(sql)
      print(f'Tabela {nome} removida com sucesso!')

    except Exception as e:
      print(f"Erro aconteceu {e}")

def insere_dado(nome):
  with connection.cursor() as cursor:
    try:
      sql = f"INSERT INTO TESTE VALUES ('{nome}')"
      cursor.execute(sql)
      print(f'Dados inseridos com sucesso!')

    except Exception as e:
      print(f"Erro aconteceu {e}")

def recupera_dados():
  with connection.cursor() as cursor:
    try:
      sql = f"SELECT * FROM TESTE"
      cursor.execute(sql)
      resultado = cursor.fetchall()
      print(resultado)
    except Exception as e:
      print(f"Erro aconteceu{e}")

def atualiza_dados(nome, novoNome):
  with connection.cursor() as cursor:
    try:
      sql = f"UPDATE TESTE set nome=('{novoNome}') where nome=('{nome}')"
      cursor.execute(sql)
      print(f'Dados alterados com sucesso!')

    except Exception as e:
      print(f"Erro aconteceu{e}")

def remove_dados(nome):
  with connection.cursor() as cursor:
    try:
      sql = "DELETE FROM TESTE where nome=('{nome}')"
      cursor.execute(sql)
      print('Nome foi excluido!')
    except Exception as e:
      print(f'Aconteceu um erro {e}')
#criar_tabela('TESTE')
#remover_tabela('TESTE2')
# insere_dado('Jão')
# recupera_dados()
# atualiza_dados('Jão', 'Pedro')
# recupera_dados()
# remove_dados('Pedro')
#recupera_dados()
connection.close()
