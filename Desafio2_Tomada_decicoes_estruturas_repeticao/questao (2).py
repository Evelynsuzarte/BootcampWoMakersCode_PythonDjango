turno = input("Digite o turno que você estuda:\n M - MATUTINO\nV - VESPERTINO\nN - NOTURNO\nDigite:")

if turno == 'm':
    print("Bom dia!")
elif turno == "v":
    print("Boa tarde!")
elif turno == "n":
    print("Boa noite!")
else:
    print("Valor inválido!")