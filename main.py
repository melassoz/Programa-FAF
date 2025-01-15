from login import login  # Importa a função login do módulo login
from usuarios import verificar_usuario  # Importa a função verificar_usuario do módulo usuarios

def main():
    """Função principal que chama o login."""
    print("Bem-vindo ao sistema!")
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    if verificar_usuario(nome, senha):  # Aqui você usa a função 'verificar_usuario'
        print("Login realizado com sucesso!")
    else:
        print("Falha no login. Tente novamente.")

if __name__ == "__main__":
    main()
