
contatos = []

def adicionar_contato(nome, telefone, email):
    contato = {
        'nome': nome, 'telefone': telefone, 'email': email
    }
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    if not contatos:
        print("Nenhum contato na lista.")
    else:
        for indice, contato in enumerate(contatos):
            print(f"{indice + 1}. {contato['nome']} - {contato['telefone']} - {contato['email']}")

def remover_contato(nome):
    global contatos
    contatos = [contato for contato in contatos if contato['nome'] != nome]
    print(f"Contato {nome} removido com sucesso!")


