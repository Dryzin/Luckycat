import mysql.connector
from classe_aposta import *
class DBAgenda:
    def __init__(self):
        self.conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='q1w2e3',
        database='apostas')
        self.meu_cursor = self.conexao.cursor()