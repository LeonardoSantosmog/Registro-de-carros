import sqlite3 as sq

DB_PATH = 'Carros.db'

def get_connection():
    return sq.connect(DB_PATH)

def criar_tabela():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_do_carro TEXT NOT NULL,
                valor REAL NOT NULL,
                ano INTEGER NOT NULL,
                marca TEXT NOT NULL
            );     
        ''')

def inserir_aluno(nome_do_carro, valor, ano, marca):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO alunos (nome_do_carro, valor, ano, marca) VALUES (?, ?, ?, ?)', (nome_do_carro, valor, ano, marca))
        conn.commit()
        return cur.lastrowid

if __name__ == '__main__':
    criar_tabela()
    print("### Bem-vindo ao Sistema de Cadastro de Alunos ###")
    nome = input("Nome do carro: ")
    idade = int(input("Valor do carro: "))
    email = input("ano do carro: ")
    curso = input("marca do carro: ")
   
    novo_id = inserir_aluno(nome_do_carro=nome, valor=idade, ano=email, marca=curso)
    print(f"✅ Aluno inserido com ID: {novo_id}")

