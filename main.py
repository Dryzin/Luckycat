
'''create database apostas;
use apostas;

create table apostador(
cpf varchar (17),
nome varchar(50),
telefone varchar(30),
primary key (cpf)
);
create table tabelas(
sequencia int(5),
cpf1 varchar(17),
foreign key (cpf1) references apostador(cpf)
);

select * from apostador;

select * from tabelas;'''

