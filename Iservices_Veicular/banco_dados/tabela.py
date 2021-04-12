import psycopg2
from psycopg2 import Error
from psycopg2._psycopg import DatabaseError
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "admin",
                                  host = "localhost",
                                  port = "5432",
                                  database = "teste")
    cursor = connection.cursor()

    create_tabble_query = '''CREATE TABLE usuarios(
        id SERIAL NOT NULL,
         nome VARCHAR(255),
         email VARCHAR(255),
         senha VARCHAR(255)
         ); '''

    cursor.execute(create_tabble_query)
    connection.commit()
    print("tabela criada com sucesso no PostgreSQL")
except (Exception, psycopg2/DatabaseError) as error :
    print("erro ao criar tabela no PostgreSQL", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("conexao ao PostgreSQL foi encerrada")
