import json

# ============================
# VARIÁVEIS GLOBAIS
# ============================
usuarios = {}
eventos = []
ARQUIVO_EVENTOS = "eventos.json"

# ============================
# FUNÇÕES DE PERSISTÊNCIA
# ============================
def salvar_eventos():
    """Salva os eventos em um arquivo JSON."""
    with open(ARQUIVO_EVENTOS, "w", encoding="utf-8") as f:
        json.dump(eventos, f, ensure_ascii=False, indent=4)

def carregar_eventos():
    """Carrega os eventos do arquivo JSON, se existir."""
    global eventos
    try:
        with open(ARQUIVO_EVENTOS, "r", encoding="utf-8") as f:
            eventos = json.load(f)
    except FileNotFoundError:
        eventos = []

# ============================
# FUNÇÕES DE USUÁRIOS
# ============================
def cadastro_usuarios(nome, email, senha):
    if email in usuarios:
        return False, "Você já está cadastrada! Tente fazer login."
    usuarios[email] = {"nome": nome, "senha": senha}
    return True, f"Usuária {nome} cadastrada com sucesso! Seja bem-vinda!"

def login_usuarios(email, senha):
    if email in usuarios and usuarios[email]["senha"] == senha:
        return True, f"Seja bem-vinda, {usuarios[email]['nome']}!"
    return False, "Email e/ou senha inválidos. Tente novamente ou cadastre-se!"

# ============================
# FUNÇÕES DE EVENTOS
# ============================
def cadastro_eventos(nome, sub, cidade, data):
    evento = {
        "nome": nome,
        "sub": sub,
        "cidade": cidade,
        "data": data
    }
    eventos.append(evento)
    salvar_eventos()
    return f"Evento '{nome}' cadastrado com sucesso! Local: {cidade}, Data: {data}."

def listar_eventos():
    if not eventos:
        return "Nenhum evento cadastrado ainda!"
    
    resultado = "\n===== EVENTOS CADASTRADOS =====\n"
    for i, e in enumerate(eventos, 1):
        resultado += f"{i}. {e['nome']} - Categoria: {e['sub']} - Cidade: {e['cidade']} - Data: {e['data']}\n"
    return resultado

def editar_evento(indice, novo_nome, novo_sub, nova_cidade, nova_data):
    try:
        evento = eventos[indice - 1]
        evento["nome"] = novo_nome
        evento["sub"] = novo_sub
        evento["cidade"] = nova_cidade
        evento["data"] = nova_data
        salvar_eventos()
        return f"Evento '{novo_nome}' atualizado com sucesso!"
    except IndexError:
        return "Índice inválido. Nenhum evento foi editado."

def excluir_evento(indice):
    try:
        evento_removido = eventos.pop(indice - 1)
        salvar_eventos()
        return f"Evento '{evento_removido['nome']}' foi removido com sucesso!"
    except IndexError:
        return "Índice inválido. Nenhum evento foi excluído."

# ============================
# MENU PRINCIPAL
# ============================
def menu():
    while True:
        print("\n======= SISTEMA FUTEBOL FEMININO =======")
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
            sub = input("Categoria (ex: Sub-15, Sub-17...): ")
            cidade = input("Cidade: ")
            data = input("Data (DD/MM/AAAA): ")
            print(cadastro_eventos(nome, sub, cidade, data))

        elif opcao == "4":
            print(listar_eventos())

        elif opcao == "5":
            print(listar_eventos())
            try:
                indice = int(input("Digite o número do evento que deseja editar: "))
                novo_nome = input("Novo nome: ")
                novo_sub = input("Nova categoria: ")
                nova_cidade = input("Nova cidade: ")
                nova_data = input("Nova data (DD/MM/AAAA): ")
                print(editar_evento(indice, novo_nome, novo_sub, nova_cidade, nova_data))
            except ValueError:
                print("Por favor, digite um número válido.")

        elif opcao == "6":
            print(listar_eventos())
            try:
                indice = int(input("Digite o número do evento que deseja excluir: "))
                print(excluir_evento(indice))
            except ValueError:
                print("Por favor, digite um número válido.")

        elif opcao == "0":
            print("Saindo do sistema... Obrigada por participar!")
            break

        else:
            print("Opção inválida. Escolha um número de 0 a 6.")

# ============================
# PONTO DE ENTRADA
# ============================
if __name__ == "__main__":
    carregar_eventos()
    menu()