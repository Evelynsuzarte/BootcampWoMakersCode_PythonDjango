login = input("Digite um login: ")
senha = input("Digite a senha: ")

while (login != "admin" or senha != "admin123"):
    print("Senha ou usuário errado, digite novamente!")
    login = input("Digite um login: ")
    senha = input("Digite a senha: ")

print("Login correto!")
