contatos =[]

def adicionar_contatos(nome, numero, email):
    contato = {'nome': nome, 'numero':numero, 'email':email}
    contatos.append(contato)
    print(f'Contato {nome} adicionado com sucesso')

def lista_contatos():
    if not contatos:
        print('Nenhum contato na lista')
    else:
        for index, contato in enumerate(contatos):
            print(f"{index + 1}. {contato['nome']} - {contato['telefone']} - {contato['email']}")

def remove_contato(nome):
    global contatos
    contatos = [contato for contato in contatos if contato['name'] !=nome ]
    print(f'Contatos {nome} removido com  sucesso !')   
             

def menu():
    while True:
        print("\nGerenciador de Contatos")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Remover Contato")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_contatos(nome, telefone, email)
        elif escolha == '2':
           lista_contatos()
        elif escolha == '3':
            nome = input("Nome do contato a remover: ")
            remove_contato(nome)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")