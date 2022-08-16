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
        self.x = self.sortear_a()
        self.y = self.sortear_a2()

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
        global b, g
        x = random.sample (range(1,30),5)

        b = str(x[0]) + str(x[1]) + str(x[2])+ str(x[3])+ str(x[4])
        b = '2'
        str(b)
        

        comando_sql = f'select sequencia from tabelas where sequencia = {b}'
        self.meu_cursor.execute(comando_sql)
        z=self.meu_cursor.fetchall()

        if z == []:
            return b

        else:
            comando_sql = f'select cpf1 from tabelas where sequencia = {b}'
            self.meu_cursor.execute(comando_sql)
            g=self.meu_cursor.fetchall()
            print("Ganhou")
            print(g)
            return  b
        
    def sortear_a2 (self):

        comando_sql = f'select sequencia from tabelas where sequencia = {b}'
        self.meu_cursor.execute(comando_sql)
        z=self.meu_cursor.fetchall()

        if z == []:
            return "nenhum ganhador"

        else:
            comando_sql = f'select cpf1 from tabelas where sequencia = {b}'
            self.meu_cursor.execute(comando_sql)
            g=self.meu_cursor.fetchall()
            print("Ganhou")
            print(g)
            return g

#####

'''        for i in range(len(z)):    
            a=int(z[i][0])'''
'''
            if a==b:
                print(a)
            else: 
                print(a)
                print(b)'''