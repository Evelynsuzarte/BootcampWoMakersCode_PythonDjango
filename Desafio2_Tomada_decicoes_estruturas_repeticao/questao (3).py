nota = int(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Valor inválido. Tente novamente.")
    nota = int(input("Digite uma nota entre 0 e 10: "))

print(f"A nota digitada foi {nota}")
