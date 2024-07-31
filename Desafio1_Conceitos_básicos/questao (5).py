salario_bruto = float(input("Digite seu salário bruto:"))
salario_liquido = 0

if salario_bruto <= 1903.98:
    salario_liquido = salario_bruto
elif salario_bruto >= 1903.99 and salario_bruto <= 2826.65:
    salario_liquido = salario_bruto - ((7.5*salario_bruto)/100)
elif salario_bruto >= 2826.66 and salario_bruto <= 3751.05:
    salario_liquido = salario_bruto - ((15*salario_bruto)/100)
elif salario_bruto >= 3751.06 and salario_bruto <= 4664.68:
    salario_liquido = salario_bruto - ((22.5*salario_bruto)/100)
elif salario_bruto >= 4664.68:
    salario_liquido = salario_bruto - ((27.5*salario_bruto)/100)

print(f"O salário líquido é igual a: {salario_liquido:.2f}")

