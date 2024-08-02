n1 = int(input("Digite o n1: "))
n2 = int(input("Digite o n2: "))
n3 = int(input("Digite o n3: "))

if n1 <= n2 <= n3:
    print(f"Ordem crescente: {n1}, {n2}, {n3}")
elif n1 <= n3 <= n2:
    print(f"Ordem crescente: {n1}, {n3}, {n2}")
elif n2 <= n1 <= n3:
    print(f"Ordem crescente: {n2}, {n1}, {n3}")
elif n2 <= n3 <= n1:
    print(f"Ordem crescente: {n2}, {n3}, {n1}")
elif n3 <= n1 <= n2:
    print(f"Ordem crescente: {n3}, {n1}, {n2}")
else:  # n3 <= n2 <= n1
    print(f"Ordem crescente: {n3}, {n2}, {n1}")
