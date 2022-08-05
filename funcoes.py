import mysql.connector
from classe_aposta import *
from classe_participantes import *

class funcoes:
    def __init__(self):
        self.conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='q1w2e3',
        database='apostas')
        self.meu_cursor = self.conexao.cursor()

    def salvar_participante(self, cpf, nome, telefone):
        objcontato = Info_participantes(cpf, nome, telefone)
        comando_sql = f'insert into Apostador (cpf, nome, telefone) value ("{objcontato.cpf}", "{objcontato.nome}", "{objcontato.telefone}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()