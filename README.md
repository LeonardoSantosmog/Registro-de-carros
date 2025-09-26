# Sistema de Cadastro de Carros

Um sistema simples em Python para cadastrar carros em um banco de dados SQLite. Permite adicionar informações como nome do carro, valor, ano e marca.

---

## Código do Projeto

```python
import sqlite3 as sq

DB_PATH = 'Carros.db'

def get_connection():
    return sq.connect(DB_PATH)

def criar_tabela():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS carros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_do_carro TEXT NOT NULL,
                valor REAL NOT NULL,
                ano INTEGER NOT NULL,
                marca TEXT NOT NULL
            );     
        ''')

def inserir_carro(nome_do_carro, valor, ano, marca):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO carros (nome_do_carro, valor, ano, marca) VALUES (?, ?, ?, ?)', 
                    (nome_do_carro, valor, ano, marca))
        conn.commit()
        return cur.lastrowid

if __name__ == '__main__':
    criar_tabela()
    print("### Bem-vindo ao Sistema de Cadastro de Carros ###")
    nome = input("Nome do carro: ")
    valor = float(input("Valor do carro: "))
    ano = int(input("Ano do carro: "))
    marca = input("Marca do carro: ")

    novo_id = inserir_carro(nome_do_carro=nome, valor=valor, ano=ano, marca=marca)
    print(f"✅ Carro inserido com ID: {novo_id}")
