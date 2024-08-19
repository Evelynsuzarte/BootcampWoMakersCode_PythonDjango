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
#cursor.execute('INSERT INTO alunos (ID,nome, idade, curso) VALUES (5,"Bruno Pinheiro", 25, "Engenharia")')

#CONSULTAS
busca1 = cursor.execute('SELECT * FROM alunos ')
print("todos os registros da tabela alunos")
for item in busca1:
    print(item)

busca2 = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
print("\nnome e a idade dos alunos com mais de 20 anos")
for item in busca2:
    print(item)

busca3 = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
print("\nalunos do curso de Engenharia em ordem alfabética.")
for item in busca3:
    print(item)

busca4 = cursor.execute('SELECT COUNT(*) FROM alunos')
print("\nnúmero total de alunos na tabela")
for item in busca4:
    print(item)

# ATUALIZAÇÃO E REMOÇÃO
cursor.execute("UPDATE alunos SET idade = 20 WHERE nome = 'Raquel' ")
cursor.execute('DELETE FROM alunos WHERE ID=3')
busca1 = cursor.execute('SELECT * FROM alunos ')
print("todos os registros da tabela alunos")
for item in busca1:
    print(item)


conexao.commit()
conexao.close()