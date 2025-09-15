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
    evento = {"nome": nome, "sub(idade)": sub, "cidade": cidade, "data(DD/MM/AAAA)": data}
    eventos.append(evento)
    return """Evento '{nome}' cadastrado com sucesso e ocorrerá na cidade '{cidade}' em '{data}'!"""

def listar_eventos():
    if not eventos:
        return """Nenhum evento cadastrado ainda! Cadastre um novo evento para que ele seja exibido aqui."""
    resultado = "/n Eventos /n"
    for i, e in enumerate(eventos, 1):
        resultado += f"{i}, {e['nome']} - ({e['sub']}) - ({e['cidade']}) - {e['data']} /n"
        return resultado