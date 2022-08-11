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

    def cadastrar_jogo(self, cpf1, sequencia):
            obj_jogo = Info_apostas (cpf1, sequencia)
            comando_sql = f'insert into tabelas ' \
                        f'(cpf1,sequencia) value ' \
                        f'("{obj_jogo.cpf1}", "{obj_jogo.sequencia}")'
            self.meu_cursor.execute(comando_sql)
            self.conexao.commit() 

    def sortear_a (self):
        global z,x
        x = random.sample (range(1,30),5)
        comando_sql = f'select sequencia from tabelas'
        self.meu_cursor.execute(comando_sql)
        z=self.meu_cursor.fetchall()
        for i in range(len(z)):    
            a=int(z[i][0])
            b=x[0]
        if a==b:
            print('Você ganhou') 
        else: print('Você perdeu')