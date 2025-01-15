from usuarios import verificar_usuario

def login(nome, senha):
    """Função de login que verifica as credenciais do usuário."""
    if verificar_usuario(nome, senha):
        print(f"Bem-vindo, {nome}!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False
