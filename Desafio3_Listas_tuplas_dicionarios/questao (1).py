perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?", "Devia para a vítima?","Já trabalhou com a vítima?"]
resultado = 0

for pergunta in perguntas:
    opcao = int(input(f"{pergunta}\n0 - não\n1 - sim\n"))
    if opcao == 1:
        resultado+=1

if resultado == 5:
    print("Assassino")
elif resultado == 3 or resultado == 4:
    print("Cúmplice")
elif resultado == 2:
    print("Suspeita")
else:
    print("Inocente")
