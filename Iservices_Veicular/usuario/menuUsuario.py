import psycopg2

while True:
    print("MENU \n"
          "0. finalizar programa \n"
          "1. cadastrar usuario\n"
          "2. editar usuario\n"
          "3. excluir usuario\n"
          "4. consultar dados\n"
          "5. consultar um usuario\n")

    opcao = int(input("Digite qual a opcao desejada: "))


    if opcao == 0:
        break
    elif opcao == 1:
        chave = 0
        while chave == 0:
            pergunta = input("Digite o nome do usuario: ")
            nome = pergunta
            chave = 1
        chave = 0
        while chave  == 0:
            pergunta = input("Digite o email do usuario: ")
            email = pergunta
            chave = 1
        chave = 0
        while chave  == 0:
            pergunta = input("Digite a senha do usuario: ")
            senha = pergunta
            chave = 1
        print(nome, email, senha)

        try:
            connection = psycopg2.connect(
                user="postgres",
                password="admin",
                host="localhost",
                port="5432",
                database="teste")

            cursor = connection.cursor()

            postgresInsertQuery = '''INSERT INTO usuarios
            (nome, email, senha)
            VALUES (%s, %s, %s)'''
            recordToInsert = (nome, email, senha)
            cursor.execute(postgresInsertQuery,recordToInsert)

            connection.commit()
            print("dados inseridos com sucesso")
        except (Exception, psycopg2.Error) as e:
            if(connection):
                print("Falha ao inserir dados na tabela", e)
        finally:
            if(connection):
                cursor.close()
                connection.close()
                print("conexao encerrada")

    elif opcao == 2:
        coluna = int(input("1. mudar o nome do usuario\n"
                           "2. mudar o email do usuario\n"
                           "3. mudar a senha do usuario\n"
                           "* "))

        if coluna == 1:
            valorVelho = input("Digite o valor que deve ser trocado: ")
            valorNovo = input("Digite o valor novo que sera adicionado: ")

            try:
                connection = psycopg2.connect(
                    user="postgres",
                    password="admin",
                    host="localhost",
                    port="5432",
                    database="teste")
                cursor = connection.cursor()

                sqlUpdateQuery = '''UPDATE usuarios\
                SET nome = %s where nome = %s'''
                cursor.execute(sqlUpdateQuery, (valorNovo, valorVelho))
                connection.commit()
                print("mudanca feita com sucesso")
            except (Exception, psycopg2.Error) as e:
                print("Erro ao modificar usuario", e)
            finally:
                if(connection):
                    cursor.close()
                    connection.close()
                    print("conexao encerrada")

        elif coluna == 2:
            valorVelho = input("Digite o valor que deve ser trocado: ")
            valorNovo = input("Digite o valor novo que sera adicionado: ")

            try:
                connection = psycopg2.connect(
                    user="postgres",
                    password="admin",
                    host="localhost",
                    port="5432",
                    database="teste")
                cursor = connection.cursor()

                sqlUpdateQuery = '''UPDATE usuarios\
                SET email = %s where email = %s'''
                cursor.execute(sqlUpdateQuery, (valorNovo, valorVelho))
                connection.commit()
                print("mudanca feita com sucesso")
            except (Exception, psycopg2.Error) as e:
                print("Erro ao modificar usuario", e)
            finally:
                if(connection):
                    cursor.close()
                    connection.close()
                    print("conexao encerrada")

        elif coluna == 3:
            valorVelho = input("Digite o valor que deve ser trocado: ")
            valorNovo = input("Digite o valor novo que sera adicionado: ")

            try:
                connection = psycopg2.connect(
                    user="postgres",
                    password="admin",
                    host="localhost",
                    port="5432",
                    database="teste")
                cursor = connection.cursor()

                sqlUpdateQuery = '''UPDATE usuarios\
                SET senha = %s where senha = %s'''
                cursor.execute(sqlUpdateQuery, (valorNovo, valorVelho))
                connection.commit()
                print("mudanca feita com sucesso")
            except (Exception, psycopg2.Error) as e:
                print("Erro ao modificar usuario", e)
            finally:
                if(connection):
                    cursor.close()
                    connection.close()
                    print("conexao encerrada")

    elif opcao == 3:
        valor = input("Digite o id que sera deletado: ")

        try:
            connection = psycopg2.connect(
                    user="postgres",
                    password="admin",
                    host="localhost",
                    port="5432",
                    database="teste")
            cursor = connection.cursor()

            sql_delete_query = '''DELETE FROM usuarios WHERE id = %s'''
            cursor.execute(sql_delete_query, valor)
            connection.commit()
            print("Dado deletado com sucesso")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao deletar os dados", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("conexao com PostgreSQL encerrada")
    elif opcao == 4:
        try:
            connection = psycopg2.connect(
                    user="postgres",
                    password="admin",
                    host="localhost",
                    port="5432",
                    database="teste")
            cursor = connection.cursor()

            postgresSelectQuery = "SELECT * from usuarios"
            cursor.execute(postgresSelectQuery)
            print("buscando as linhas da tabela")
            tabelaSalva = cursor.fetchall()

            for row in tabelaSalva:
                print("id: ", row[0])
                print("nome: ", row[1])
                print("email: ", row[2])
                print("senha: ", row[3], "\n")

        except(Exception, psycopg2.Error) as e:
            print("erro ao mostrar os dados na tabela", e)
        finally:
            if(connection):
                cursor.close
                connection.close()
                print("conexao com PostgreSQL encerrada")

    elif opcao == 5:
        try:
            connection = psycopg2.connect(
                    user="postgres",
                    password="admin",
                    host="localhost",
                    port="5432",
                    database="teste")
            cursor = connection.cursor()

            id = input("Digite o id a ser procurado: ")

            postgresSelectQuery = "SELECT u from usuarios u WHERE id= %s"
            cursor.execute(postgresSelectQuery, id)
            print("buscando as linhas da tabela")
            tabelaSalva = cursor.fetchall()

            for row in tabelaSalva:
                print(row[0])

        except(Exception, psycopg2.Error) as e:
            print("erro ao mostrar os dados na tabela", e)
        finally:
            if(connection):
                cursor.close
                connection.close()
                print("conexao com PostgreSQL encerrada")
