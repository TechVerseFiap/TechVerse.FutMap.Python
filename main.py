import json
import os

# ==============================
# Funções utilitárias de arquivo JSON
# ==============================

def carregar_dados(arquivo, tipo_dado):
    """Carrega os dados de um arquivo JSON, caso exista."""
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo {arquivo}. Criando um novo arquivo vazio.")
    # Retorna vazio caso não exista ou haja erro
    return {} if tipo_dado == "usuarios" else []


def salvar_dados(arquivo, dados):
    """Salva os dados em formato JSON."""
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


# ==============================
# Carregamento inicial dos dados
# ==============================
usuarios = carregar_dados('usuarios.json', "usuarios")
eventos = carregar_dados('eventos.json', "eventos")


# ==============================
# Funções de validação
# ==============================

def pegar_numero(msg):
    """Solicita um número inteiro ao usuário com tratamento de erro."""
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("A opção precisa ser um número, tente novamente!")


def pegar_texto(msg):
    """Solicita texto e evita campos vazios."""
    while True:
        texto = input(msg).strip()
        if texto:
            return texto
        print("Este campo não pode ficar vazio!")


# ==============================
# Funções principais
# ==============================

def cadastro_usuarios(nome, email, senha):
    """Cadastra uma nova usuária se o e-mail ainda não estiver registrado."""
    if email in usuarios:
        return False, "Você já está cadastrada! Tente fazer login."
    
    usuarios[email] = {"Nome": nome, "Senha": senha}
    salvar_dados('usuarios.json', usuarios)
    return True, f"Usuária {nome} cadastrada com sucesso!"


def login_usuarios(email, senha):
    """Valida o login de uma usuária existente."""
    if email in usuarios and usuarios[email]["Senha"] == senha:
        nome = usuarios[email]["Nome"]
        return True, f"Seja bem-vinda, {nome}!"
    return False, "Email ou senha inválidos. Tente novamente."


def cadastro_eventos(nome, sub, cidade, data):
    """Cadastra um novo evento e salva no JSON."""
    evento = {
        "Nome": nome,
        "Categoria": sub,
        "Cidade": cidade,
        "Data": data
    }
    eventos.append(evento)
    salvar_dados('eventos.json', eventos)
    return f"Evento '{nome}' cadastrado com sucesso em {cidade} na data {data}!"


def listar_eventos():
    """Lista todos os eventos cadastrados."""
    if not eventos:
        return "Nenhum evento cadastrado ainda!"
    
    resultado = "\n=== Lista de Eventos ===\n"
    for i, e in enumerate(eventos, start=1):
        resultado += f"{i}. {e['Nome']} ({e['Categoria']}) - {e['Cidade']} - {e['Data']}\n"
    return resultado


# ==============================
# Função principal (menu)
# ==============================

def menu():
    """Interface principal do sistema."""
    while True:
        print("\n======= Sistema Futebol Feminino =======")
        print("1. Cadastrar Usuária")
        print("2. Login")
        print("3. Cadastrar Evento")
        print("4. Listar Eventos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = pegar_texto("Nome: ")
                email = pegar_texto("Email: ")
                senha = pegar_texto("Senha: ")
                ok, msg = cadastro_usuarios(nome, email, senha)
                print(msg)

            elif opcao == "2":
                email = pegar_texto("Email: ")
                senha = pegar_texto("Senha: ")
                ok, msg = login_usuarios(email, senha)
                print(msg)

            elif opcao == "3":
                nome = pegar_texto("Nome do evento: ")
                sub = pegar_texto("Categoria de idade das jogadoras (ex: Sub-17): ")
                cidade = pegar_texto("Cidade: ")
                data = pegar_texto("Data (DD/MM/AAAA): ")
                print(cadastro_eventos(nome, sub, cidade, data))

            elif opcao == "4":
                print(listar_eventos())

            elif opcao == "0":
                print("Saindo do sistema. Obrigado por participar!")
                break

            else:
                print("Opção inválida. Digite um número entre 0 e 4.")

        except Exception as e:
            # Captura qualquer erro inesperado e evita que o programa quebre
            print(f"Ocorreu um erro inesperado: {e}")


# ==============================
# Execução do programa
# ==============================

if __name__ == "__main__":
    menu()