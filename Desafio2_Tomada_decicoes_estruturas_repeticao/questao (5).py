lado1 = int(input("Digite o tamanho do lado 1: "))
lado2 = int(input("Digite o tamanho do lado 2: "))
lado3 = int(input("Digite o tamanho do lado 3: "))

if lado1 == lado2 == lado3:
    print("equilátero: todos os lados com o mesmo valor")
elif lado1 == lado2 or lado2 == lado3 or lado3==lado1:
    print("isósceles: dois lados com o mesmo valor")
elif lado1 != lado2 != lado3:
    print("escaleno: todos os lados com medidas distintas")