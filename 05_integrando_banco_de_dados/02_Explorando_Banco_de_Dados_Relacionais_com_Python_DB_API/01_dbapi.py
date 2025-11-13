import sqlite3
from pathlib import Path

PATH_ROOT = Path(__file__).parent

conexao = sqlite3.connect(PATH_ROOT / 'meu_banco.db')
cursor = conexao.cursor()


# Criando uma tabela
def criar_tabela(conexao, cursor):
    cursor.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150));')
    conexao.commit()


# Inserindo registros
def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', data)
    conexao.commit()


# Atualizando registros -> não se esqueça de usar o WHERE para não atualizar a tabela inteira
def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?', data)
    conexao.commit()


# Deletando um registro
def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id = ?', data)
    conexao.commit()


dados = [('Jose', 'jose@gmail.com'), ('Maria', 'maria@gmail.com'), ('Oseias', 'oseias@gmail.com')]


# Inserindo registros em lote
def inserir_muitos_registros(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) Values (?, ?)', dados)
    conexao.commit()


# Consultado os registros
def recuperar_cliente_pelo_id(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()


def listando_clientes(cursor):
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchall()


def listando_clientes_em_ordem_nome_decrescente(cursor):
    cursor.execute('SELECT * FROM clientes ORDER BY nome DESC')
    return cursor.fetchall()


# Alterando o row_factory -> retornando o cliente em um dicionario
def recuperar_cliente_pelo_id_row_factory(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()
