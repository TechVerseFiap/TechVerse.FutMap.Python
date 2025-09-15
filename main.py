usuarios = {}
eventos = []

def cadastro_usuarios(nome, email, senha):
    if email in usuarios:
        return False, """Você já está cadastrado(a)! Tente fazer o login."""
    usuarios[email] = {"Nome": nome, "Senha": senha}
    return True, f"Você foi cadastrado(a) com sucesso! Seja bem vindo {nome}."

def login_usuarios(email, senha):
    if email in usuarios and usuarios[email]["senha"] == senha:
        return True, """Seja bem vindo, {usuarios[email]['nome']}!"""
    return False, """Email e senha inválidos. Tente novamente ou cadastr-se caso ainda não tenha uma conta!"""

def cadastro_eventos(nome, sub, cidade, data):
    evento = {"nome": nome, "sub(idade)": sub, "cidade": cidade, "data": data}
    eventos.append(evento)
    return """Evento '{nome}' cadastrado com sucesso e ocorrerá na cidade '{cidade}' em '{data}'!"""

def listar_eventos():
    if not eventos:
        return """Nenhum evento cadastrado ainda! Cadastre um novo evento para que ele seja exibido aqui."""
    resultado = "/n Eventos /n"
    for i, e in enumerate(eventos, 1):
        resultado += f"{i}, {e['nome']} - ({e['sub']}) - ({e['cidade']}) - {e['data']} /n"
        return resultado
    
def menu():
    while True:
        print("\n Sistema Futebol Feminino ")
        print("1. Cadastrar Usuária")
        print("2. Login")
        print("3. Cadastrar Evento")
        print("4. Listar Eventos")
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
            print("Saindo do sistema, agradecemos por estar aqui!")
            break

        else:
            print ("Opção inválida, insira um número de 1 a 5 e tente novamente.")

if __name__ == "__main__":
    menu()