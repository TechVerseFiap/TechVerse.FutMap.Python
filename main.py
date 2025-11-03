import json

usuarios = {}
eventos = []

ARQUIVO_EVENTOS = "eventos.json"

# Função para salvar eventos em arquivo
def salvar_eventos():
    with open(ARQUIVO_EVENTOS, "w", encoding="utf-8") as f:
        json.dump(eventos, f, ensure_ascii=False, indent=4)

# Função para carregar eventos do arquivo (caso exista)
def carregar_eventos():
    global eventos
    try:
        with open(ARQUIVO_EVENTOS, "r", encoding="utf-8") as f:
            eventos = json.load(f)
    except FileNotFoundError:
        eventos = []

# Função para cadastrar novos usuários
def cadastro_usuarios(nome, email, senha):
    if email in usuarios:
        return False, """Você já está cadastrado(a)! Tente fazer o login."""
    usuarios[email] = {"Nome": nome, "Senha": senha}
    return True, f"Você foi cadastrado(a) com sucesso! Seja bem vindo {nome}."

# Função para login de usuários
def login_usuarios(email, senha):
    if email in usuarios and usuarios[email]["senha"] == senha:
        return True, """Seja bem vindo, {usuarios[email]['nome']}!"""
    return False, """Email e senha inválidos. Tente novamente ou cadastr-se caso ainda não tenha uma conta!"""

# Função para cadastrar eventos
def cadastro_eventos(nome, sub, cidade, data):
    evento = {"nome": nome, "sub(idade)": sub, "cidade": cidade, "data": data}
    eventos.append(evento)
    return """Evento '{nome}' cadastrado com sucesso e ocorrerá na cidade '{cidade}' em '{data}'!"""

# Função para listar todos os eventos cadastrados
def listar_eventos():
    """Lista todos os eventos cadastrados."""
    if not eventos:
        return """Nenhum evento cadastrado ainda! Cadastre um novo evento para que ele seja exibido aqui."""
    resultado = "/n Eventos /n"
    for i, e in enumerate(eventos, 1):
        resultado += f"{i}, {e['nome']} - ({e['sub']}) - ({e['cidade']}) - {e['data']} /n"
        return resultado
    
# Função para editar um evento existente
def editar_evento():
    if not eventos:
        print("Nenhum evento cadastrado para editar.")
        return
    
    print("=== Eventos Cadastrados ===")
    for i, e in enumerate(eventos, start=1):
        print(f"{i}. {e['nome']} - {e['cidade']} - {e['data']}")
    
    try:
        escolha = int(input("Digite o número do evento que deseja editar: ")) - 1
        if escolha < 0 or escolha >= len(eventos):
            print("Número inválido.")
            return
        
        evento = eventos[escolha]
        print(f"Editando evento: {evento['nome']}")
        
        novo_nome = input(f"Novo nome (ou Enter para manter '{evento['nome']}'): ")
        nova_cidade = input(f"Nova cidade (ou Enter para manter '{evento['cidade']}'): ")
        nova_data = input(f"Nova data (ou Enter para manter '{evento['data']}'): ")
        nova_sub = input(f"Nova categoria (ou Enter para manter '{evento['sub(idade)']}'): ")
        
        # Atualiza apenas o que o usuário alterar
        if novo_nome: evento['nome'] = novo_nome
        if nova_cidade: evento['cidade'] = nova_cidade
        if nova_data: evento['data'] = nova_data
        if nova_sub: evento['sub(idade)'] = nova_sub
        
        print("Evento atualizado com sucesso!")
    
    except ValueError:
        print("Digite um número válido.")


# Função para excluir um evento
def excluir_evento():
    if not eventos:
        print("Nenhum evento cadastrado para excluir.")
        return
    
    print("=== Eventos Cadastrados ===")
    for i, e in enumerate(eventos, start=1):
        print(f"{i}. {e['nome']} - {e['cidade']} - {e['data']}")
    
    try:
        escolha = int(input("Digite o número do evento que deseja excluir: ")) - 1
        if escolha < 0 or escolha >= len(eventos):
            print("Número inválido.")
            return
        
        evento_removido = eventos.pop(escolha)
        print(f"Evento '{evento_removido['nome']}' removido com sucesso!")
    
    except ValueError:
        print("Digite um número válido.")

def menu():
    """Interface principal do sistema."""
    while True:
        print("\n======= Sistema Futebol Feminino =======")
        print("1. Cadastrar Usuária")
        print("2. Login")
        print("3. Cadastrar Evento")
        print("4. Listar Eventos")
        print("5. Editar Evento")
        print("6. Excluir Evento")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            ok, msg = cadastro_usuarios(nome, email, senha)
            print(msg)

        elif opcao == "2":
            email = input("Email: ")
            senha = input("Senha: ")
            ok, msg = login_usuarios(email, senha)
            print(msg)

        elif opcao == "3":
            nome = input("Nome do evento: ")
            sub = input("Categoria de idade das jogadoras: ")
            cidade = input("Cidade: ")
            data = input("Data (DD/MM/AAAA): ")
            print (cadastro_eventos(nome, sub, cidade, data))

        elif opcao == "4":
            print(listar_eventos())
        
        elif opcao == "5":
            editar_evento()

        elif opcao == "6":
            excluir_evento()

        elif opcao == "0":
            print("Saindo do sistema, agradecemos por estar aqui!")
            break

        else:
            print ("Opção inválida, insira um número de 1 a 5 e tente novamente.")

# Ponto de entrada do programa
# Só executa o menu se o arquivo for rodado diretamente
if __name__ == "__main__":
    carregar_eventos()  # Carrega os eventos salvos, se houver
    menu()