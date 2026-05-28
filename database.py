import sqlite3 as sq
from pathlib import Path

pasta = Path(__file__).parent
caminho = pasta / "escola.db"

def conectar():
    conexao = sq.connect(caminho)
    cursor = conexao.cursor()

    return conexao, cursor