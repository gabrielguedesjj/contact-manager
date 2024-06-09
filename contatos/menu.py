import contact_manager

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
            contact_manager.adicionar_contatos(nome, telefone, email)
        elif escolha == '2':
            contact_manager.lista_contatos()
        elif escolha == '3':
            nome = input("Nome do contato a remover: ")
            contact_manager.remove_contato(nome)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

