import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#CRIAR TABELA
#cursor.execute('CREATE TABLE alunos (ID INT, nome VARCHAR(30), idade INT, curso VARCHAR(30))')

#INSERIR DADOS
# cursor.execute('INSERT INTO alunos (ID,nome, idade, curso) VALUES (1,"Raquel Morais", 19, "Nutrição")')
# cursor.execute('INSERT INTO alunos (ID,nome, idade, curso) VALUES (2,"Miguel Lima", 24, "Nutrição")')
# cursor.execute('INSERT INTO alunos (ID,nome, idade, curso) VALUES (3,"Ester Rocha", 28, "Engenharia")')
# cursor.execute('INSERT INTO alunos (ID,nome, idade, curso) VALUES (4,"Pietro Moura", 19, "Medicina")')
# cursor.execute('INSERT INTO alunos (ID,nome, idade, curso) VALUES (5,"Bruno Pinheiro", 25, "Engenharia")')

#CONSULTAS
# busca1 = cursor.execute('SELECT * FROM alunos ')
# print("todos os registros da tabela alunos")
# for item in busca1:
#     print(item)

# busca2 = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
# print("\nnome e a idade dos alunos com mais de 20 anos")
# for item in busca2:
#     print(item)

# busca3 = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
# print("\nalunos do curso de Engenharia em ordem alfabética.")
# for item in busca3:
#     print(item)

# busca4 = cursor.execute('SELECT COUNT(*) FROM alunos')
# print("\nnúmero total de alunos na tabela")
# for item in busca4:
#     print(item)

# ATUALIZAÇÃO E REMOÇÃO
# cursor.execute("UPDATE alunos SET idade = 20 WHERE nome = 'Raquel' ")
# cursor.execute('DELETE FROM alunos WHERE ID=3')
# busca1 = cursor.execute('SELECT * FROM alunos ')
# print("todos os registros da tabela alunos")
# for item in busca1:
#     print(item)


# CRIAR TABELA 'CLIENTES' E INSERIR DADOS
# cursor.execute('CREATE TABLE clientes (ID INT PRIMARY KEY, nome VARCHAR(30), idade INT, saldo FLOAT)')
# cursor.execute('INSERT INTO clientes (ID, nome, idade, saldo) VALUES (1,"Cirilo Morais", 48, 970.00)')
# cursor.execute('INSERT INTO clientes (ID, nome, idade, saldo) VALUES (2,"Titina Lima", 55, 1542.70)')
# cursor.execute('INSERT INTO clientes (ID, nome, idade, saldo) VALUES (3,"Marina Uva", 26, 320.45)')
# cursor.execute('INSERT INTO clientes (ID, nome, idade, saldo) VALUES (4,"Carlinhos Moura", 21, 4800.50)')
# cursor.execute('INSERT INTO clientes (ID, nome, idade, saldo) VALUES (5,"Carla Costa", 36, "210.99")')

# #CONSULTAS E FUNÇÕES AGREGADAS
# busca1 = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30 ')
# print("clientes com idade superior a 30 anos")
# for item in busca1:
#     print(item)

# busca2 = cursor.execute('SELECT AVG(saldo) FROM clientes')
# print("\nCalcule o saldo médio dos clientes.")
# for item in busca2:
#     print(item)

# busca3 = cursor.execute('SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
# print("\no cliente com o saldo máximo.")
# for item in busca3:
#     print(item)

# busca4 = cursor.execute('SELECT COUNT(saldo) FROM clientes WHERE saldo>1000')
# print("\nclientes têm saldo acima de 1000")
# for item in busca4:
#     print(item)


# ATUALIZAÇÃO E REMOÇÃO
# cursor.execute("UPDATE clientes SET saldo = 100.00 WHERE nome = 'Marina Uva' ")
# cursor.execute('DELETE FROM clientes WHERE ID=2')
# busca1 = cursor.execute('SELECT * FROM clientes ')
# print("todos os registros da tabela clientes")
# for item in busca1:
#     print(item)


# JUNÇÃO DE TABELAS
# cursor.execute('CREATE TABLE compras (ID INT PRIMARY KEY, cliente_id INT, produto VARCHAR(30), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes(ID))')
# cursor.execute('INSERT INTO compras (ID, cliente_id, produto, valor) VALUES (10, 1, "celular samsung", 1700.00)')
# cursor.execute('INSERT INTO compras (ID, cliente_id, produto, valor) VALUES (11, 3, "impressora a jato", 1050.01)')
# cursor.execute('INSERT INTO compras (ID, cliente_id, produto, valor) VALUES (12, 4, "computador gamer", 3804.50)')
# cursor.execute('INSERT INTO compras (ID, cliente_id, produto, valor) VALUES (13, 3, "mesa escritório", 460.00)')

busca0 = cursor.execute('SELECT * FROM compras')
print("todos os registros da tabela compras")
for item in busca0:
    print(item)

busca6 = cursor.execute('SELECT nome FROM compras INNER JOIN clientes ON compras.cliente_id = clientes.ID ')
print("todos os registros de junção")
for item in busca6:
    print(item)
   

conexao.commit()
conexao.close()