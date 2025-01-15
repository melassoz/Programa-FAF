ARQUIVO_USUARIOS = 'app/usuarios.txt'

def carregar_usuarios():
    """Carrega os usuários do arquivo de texto."""
    usuarios = []
    try:
        with open(ARQUIVO_USUARIOS, 'r') as file:
            for linha in file.readlines():
                nome, senha = linha.strip().split(',')
                usuarios.append((nome, senha))
    except FileNotFoundError:
        print(f"O arquivo {ARQUIVO_USUARIOS} não foi encontrado.")
    return usuarios

def adicionar_usuario(nome, senha):
    """Adiciona um novo usuário ao arquivo."""
    with open(ARQUIVO_USUARIOS, 'a') as file:
        file.write(f"{nome},{senha}\n")

def verificar_usuario(nome, senha):
    """Verifica se o usuário e senha estão corretos."""
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario[0] == nome and usuario[1] == senha:
            return True
    return False
