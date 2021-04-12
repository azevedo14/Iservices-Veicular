import psycopg2

class Conexao():

    def get_conexao(self):
        connection = psycopg2.connect(
                        user="postgres",
                        password="admin",
                        host="localhost",
                        port="5432",
                        database="teste")
        return connection
