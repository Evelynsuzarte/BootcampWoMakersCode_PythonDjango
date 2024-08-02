par = 0
impar = 0

n = int(input("Digite um número "))

while(n != 0):
    if n%2 == 0:
        print("Número par")
        par+=1
    else:
        print("Número ímpar")
        impar+=1
    n = int(input("Digite um número "))

print (f"Contagem de numeros:\npar = {par}\nimpar = {impar}")
