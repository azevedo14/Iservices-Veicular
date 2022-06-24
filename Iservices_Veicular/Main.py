from flask import request, Flask

from Conexao import Conexao
from Entidades.Servico import Servico
from Entidades.User import User

app = Flask(__name__)

conexao = Conexao.connection()

# querys do PostreSQL com a tabela de usuarios
select_all_user = '''SELECT * FROM usuarios'''
select_id_user\
    = '''SELECT id, nome, email, senha FROM usuarios WHERE id = %s;'''
select_name_user = '''SELECT id, nome, email, senha FROM usuarios WHERE name = %s'''
select_email_user = '''SELECT id, nome, email, senha FROM usuarios WHERE email = %s'''
insert_query_user = '''INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)'''
update_query_user = '''UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s;'''
delete_query_user = '''DELETE FROM usuarios WHERE id = %s;'''

# querys do PostgreSQL com a tabela de servicos
select_all_services = '''SELECT * FROM servicos'''
select_id_service = '''SELECT id, nome, valor FROM servicos WHERE id = %s;'''
insert_query_service = '''INSERT INTO servicos (nome, valor) VALUES (%s, %s)'''
update_query_service = '''UPDATE servicos SET nome = %s, valor = %s WHERE id = %s;'''
delete_query_service = '''DELETE FROM servicos WHERE id = %s;'''


@app.route('/')
def index():
    return "Iservice \n" \
           "Um app para facilitar a vida dos amantes de carros"


@app.route('/users', methods=['POST'])
def cria_user():
    _json = request.json
    user = User(None, _json["nome"], _json["email"], _json["senha"])
    if user.nome and user.email and user.senha and request.method == 'POST':
        cursor = conexao.cursor()
        record_to_insert = (user.nome, user.email, user.senha)
        cursor.execute(insert_query_user, record_to_insert)
        conexao.commit()
        resp = "usuario criado"
    else:
        resp = "usuario nao pode ser criado"
    return resp

@app.route('/users/login', methods=['POST'])
def valida_user():
    _json = request.json
    user = User(None, None, _json["email"], _json["senha"])
    try:
        busca_user = busca_email_user(user.email)
        if user.email == busca_user[2]:
            if user.senha == busca_user[3]:
                user.id = busca_user[0]
                user.nome = busca_user[1]
                return str(user)
            else: raise Exception
        else: raise Exception
    except Exception:
        print("usuario nao encontrado")

@app.route('/users', methods=['GET'])
def select_users():
    cursor = conexao.cursor()
    cursor.execute(select_all_user)
    record = cursor.fetchall()
    mostrar = ""

    for row in record:
        mostrar += str(row[0]) + " "
        mostrar += str(row[1]) + " "
        mostrar += str(row[2]) + " "
        mostrar += str(row[3]) + "\n"

    return mostrar


@app.route('/users/<id>', methods=['GET'])
def busca_id_user(id):
    cursor = conexao.cursor()
    record_to_insert = (id)
    cursor.execute(select_id_user, record_to_insert)
    record = cursor.fetchone()
    return str(record)

@app.route('/users/email/<email>', methods=['GET'])
def busca_email_user(email):
    cursor = conexao.cursor()
    record_to_insert = email
    teste = "SELECT id, nome, email, senha FROM usuarios WHERE email = '{}'".format(email)
    cursor.execute(teste)
    record = cursor.fetchone()
    print(str(record))
    return record

@app.route('/users/name/<name>', methods=['GET'])
def busca_nome_user(name):
    cursor = conexao.cursor()
    record_to_insert = name
    teste = "SELECT id, nome, email, senha FROM usuarios WHERE nome = '{}'".format(name)
    cursor.execute(teste)
    record = cursor.fetchone()
    print(str(record))
    return record


@app.route('/users/<id>', methods=['PUT'])
def modifica_user(id):
    _json = request.json
    user = User(id, _json["nome"], _json["email"], _json["senha"])
    record_to_insert = (user.nome, user.email, user.senha, id)
    cursor = conexao.cursor()
    cursor.execute(update_query_user, record_to_insert)
    conexao.commit()
    record_to_insert = (id)
    cursor.execute(select_id_user, record_to_insert)
    record = cursor.fetchone()
    return str(record)


@app.route('/users/<id>', methods=['DELETE'])
def deleta_user(id):
    cursor = conexao.cursor()
    record_to_insert = (id)
    cursor.execute(delete_query_user, record_to_insert)
    conexao.commit()
    mostrar = "usuario de id: {} deletado".format(id)
    return mostrar


@app.route('/services', methods=['POST'])
def cria_servico():
    _json = request.json
    servico = Servico(None, _json["nome"], _json["valor"])
    if servico.nome and servico.valor and request.method == 'POST':
        cursor = conexao.cursor()
        record_to_insert = (servico.nome, servico.valor)
        cursor.execute(insert_query_service, record_to_insert)
        conexao.commit()
        resp = "servico criado"
    else:
        resp = "Servico nao pode ser criado"
    return resp


@app.route('/services', methods=['GET'])
def select_services():
    cursor = conexao.cursor()
    cursor.execute(select_all_services)
    record = cursor.fetchall()
    mostrar = ""

    for row in record:
        mostrar += str(row[0]) + " "
        mostrar += str(row[1]) + " "
        mostrar += str(row[2]) + "\n"

    return mostrar


@app.route('/services/<id>', methods=['GET'])
def busca_id_service(id):
    cursor = conexao.cursor()
    record_to_insert = (id)
    cursor.execute(select_id_service, record_to_insert)
    record = cursor.fetchone()
    return str(record)


@app.route('/services/<id>', methods=['PUT'])
def modifica_service(id):
    _json = request.json
    service = Servico(id, _json["nome"], _json["valor"])
    record_to_insert = (service.nome, service.valor, id)
    cursor = conexao.cursor()
    cursor.execute(update_query_service, record_to_insert)
    conexao.commit()
    record_to_insert = (id)
    cursor.execute(select_id_service, record_to_insert)
    record = cursor.fetchone()
    return str(record)


@app.route('/services/<id>', methods=['DELETE'])
def deleta_service(id):
    cursor = conexao.cursor()
    record_to_insert = (id)
    cursor.execute(delete_query_service, record_to_insert)
    conexao.commit()
    mostrar = "servico de id: {} deletado".format(id)
    return mostrar


if __name__ == "__main__":
    app.run(debug=True)
