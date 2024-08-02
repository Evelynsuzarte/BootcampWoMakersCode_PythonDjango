idade = int(input("Digite a idade:"))

if idade < 14:
    print("Idade de criança")
elif idade >= 14 and idade < 18:
    print("Idade adolescente")
elif idade >=18 and idade <= 65:
    print("Idade adulta")
else:
    print("Idade idoso")