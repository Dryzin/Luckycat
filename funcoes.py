import mysql.connector
from classe_aposta import *
from classe_participantes import *
import random 

class funcoes:
    def __init__(self):
        self.conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='q1w2e3',
        database='apostas')
        self.meu_cursor = self.conexao.cursor()
    
    

    def cadastrar_participante(self, cpf, nome, telefone):
        obj_apostador = Info_participantes (cpf, nome, telefone)
        comando_sql = f'insert into apostador ' \
                    f'(cpf, nome, telefone) value ' \
                    f'("{obj_apostador.cpf}", "{obj_apostador.nome}","{obj_apostador.telefone}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def sortear (self, cpf, sequencia):
        x = random.sample(range(1,30),5)
        

