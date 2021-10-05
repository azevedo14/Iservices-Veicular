import psycopg2
from psycopg2 import Error

class Conexao:
    def connection():
        try:
            cnxn = psycopg2.connect(user="postgres",
                                    password="admin",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
            return cnxn

        except (Exception, Error) as e:
            print("erro ao conectar com o BD")
            print(e)
