from email import charset
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='usuario',
                             password='Db123@2022',
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

criar_tabela('TESTE2')
remover_tabela('TESTE2')
connection.close()
