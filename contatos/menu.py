import contact_manager
def main():
    while True:
        print("""Gerenciador de Contatos:
        1. Adicionar Contato
        2. Listar Contatos
        3. Remover Contato
        4. Sair""")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            contact_manager.adicionar_contato(nome, telefone, email)
        elif escolha == '2':
            contact_manager.listar_contatos()
        elif escolha == '3':
            nome = input("Nome do contato a remover: ")
            contact_manager.remover_contato(nome)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()