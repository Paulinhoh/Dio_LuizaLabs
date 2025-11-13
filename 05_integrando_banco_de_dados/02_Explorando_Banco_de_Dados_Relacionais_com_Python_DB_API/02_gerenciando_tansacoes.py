import sqlite3
from pathlib import Path

PATH_ROOT = Path(__file__).parent

conexao = sqlite3.connect(PATH_ROOT / 'meu_banco.db')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('Test 01', 'test01@gmail.com'))
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)', (2, 'Test 02', 'test02@gmail.com'))
    conexao.commit()
except Exception as exc:
    print(f'Ops! um erro ocorreu! {exc}')
    conexao.rollback()
