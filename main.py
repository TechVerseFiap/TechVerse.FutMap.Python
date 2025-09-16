# Dicionário para armazenar usuárias cadastradas (email como chave)
usuarios = {}
# Lista para armazenar os eventos cadastrados
eventos = []

# Função para cadastrar novas usuárias
def cadastro_usuarios(nome, email, senha):
    # Verifica se o email já está cadastrado
    if email in usuarios:
        return False, """Você já está cadastrado(a)! Tente fazer o login."""
    # Se não estiver, adiciona no dicionário
    usuarios[email] = {"nome": nome, "senha": senha}
    return True, f"Você foi cadastrado(a) com sucesso! Seja bem vindo {nome}."

# Função para login de usuárias
def login_usuarios(email, senha):
    # Confere se o email existe e se a senha está correta
    if email in usuarios and usuarios[email]["senha"] == senha:
        return True, f"""Seja bem vindo(a), {usuarios[email]['nome']}!"""
    # Caso contrário, retorna erro de login
    return False, """Email e senha inválidos. Tente novamente ou cadastr-se caso ainda não tenha uma conta!"""

# Função para cadastrar eventos
def cadastro_eventos(nome, sub, cidade, data):
    # Cria um dicionário com os dados do evento
    evento = {"nome": nome, "sub": sub, "cidade": cidade, "data": data}
    # Adiciona o evento na lista
    eventos.append(evento)
    return f"""Evento '{nome}' cadastrado com sucesso e ocorrerá na cidade '{cidade}' em '{data}'!"""

# Função para listar todos os eventos cadastrados
def listar_eventos():
    if not eventos:
        return """Nenhum evento cadastrado ainda! Cadastre um novo evento para que ele seja exibido aqui."""
    resultado = "\n Eventos \n"
    # Percorre a lista de eventos e monta o texto de saída
    for i, e in enumerate(eventos, 1):
        resultado += f"{i}: {e['nome']} - {e['sub']} - {e['cidade']} - {e['data']} \n"
    return resultado

# Função principal do sistema (menu interativo)
def menu():
    while True:
        print("\n Sistema Futebol Feminino ")
        print("1. Cadastrar Usuária")
        print("2. Login")
        print("3. Cadastrar Evento")
        print("4. Listar Eventos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        # Cadastro de usuária
        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            ok, msg = cadastro_usuarios(nome, email, senha)
            print(msg)

        # Login de usuária
        elif opcao == "2":
            email = input("Email: ")
            senha = input("Senha: ")
            ok, msg = login_usuarios(email, senha)
            print(msg)

        # Cadastro de evento
        elif opcao == "3":
            nome = input("Nome do evento: ")
            sub = input("Categoria de idade das jogadoras: ")
            cidade = input("Cidade: ")
            data = input("Data (DD/MM/AAAA): ")
            print (cadastro_eventos(nome, sub, cidade, data))

        # Listar eventos cadastrados
        elif opcao == "4":
            print(listar_eventos())
        
        # Sair do sistema
        elif opcao == "5":
            print("Saindo do sistema, agradecemos por estar aqui!")
            break

        # Caso digite uma opção inválida
        else:
            print ("Opção inválida, insira um número de 1 a 5 e tente novamente.")

# Ponto de entrada do programa
# Só executa o menu se o arquivo for rodado diretamente
if __name__ == "__main__":
    menu()