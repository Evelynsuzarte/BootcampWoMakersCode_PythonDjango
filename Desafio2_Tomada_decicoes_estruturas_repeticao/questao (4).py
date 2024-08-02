nota = int(input("Digite uma nota entre 0 e 10: "))
i = 0

while i<8:
    if nota >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    
    i = i+1
    nota = int(input("Digite uma nota entre 0 e 10: "))
    
