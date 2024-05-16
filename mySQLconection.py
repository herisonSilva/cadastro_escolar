import mysql.connector
# CRUD


def insert(nome, matricula, nome_curso):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='cadastropython',
    )
    cursor = conexao.cursor()
    comando = f'INSERT INTO usuarios_python(nome, matricula, nome_curso) VALUES ("{nome}", "{matricula}", "{nome_curso}")'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    inserido = f'{nome} inserido com sucesso. '
    return inserido


def exibir():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='cadastropython',
    )
    cursor = conexao.cursor()
    comando = f'SELECT * FROM usuarios_python'
    cursor.execute(comando)
    resultado = cursor.fetchall()# ler o banco de dados
    cursor.close()
    conexao.close()
    return resultado


def update(nome_curso, nome):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='cadastropython',
    )
    cursor = conexao.cursor()
    comando = f'UPDATE `cadastropython`.`usuarios_python` SET `nome_curso` = "{nome_curso}" WHERE (`nome` = "{nome}");'
    cursor.execute(comando)
    conexao.commit()
    att = f'o usuario {nome} agora está matriculado no curso: {nome_curso}. '
    cursor.close()
    conexao.close()
    return att


def delete(deletar_nome):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='cadastropython',
    )
    cursor = conexao.cursor()
    comando = f'DELETE FROM `cadastropython`.`usuarios_python` WHERE (`nome` = "{deletar_nome}")'
    cursor.execute(comando)
    conexao.commit()  # editando o banco de dados
    resultado = f"{deletar_nome} exluido com sucesso. "
    cursor.close()
    conexao.close()
    return resultado


def lista_de_comandos():
    print('-'*30)
    print(' '*10, 'MENU')
    print('1 - inserir nome do aluno no banco de dados. ')
    print('2 - editar informações do aluno no banco de dados. ')
    print('3 - visualizar banco de dados. ')
    print('4 - Deletar um nome do banco de dados. ')
    print('0 - sair. ')
    print('-'*30)
