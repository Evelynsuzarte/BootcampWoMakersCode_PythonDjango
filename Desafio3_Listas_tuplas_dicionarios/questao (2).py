i= 0 
j= 0 
alunos = 0
notas = []
for i in range(5):
    total = 0
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} do aluno {i}= "))
        total+=nota
    media = total/4
    notas.append(media)

print(notas)

for nota in notas:
    if nota >= 7.0:
        alunos +=1

print(f"Alunos com média maior ou igual a 7.0 = {alunos} ")
