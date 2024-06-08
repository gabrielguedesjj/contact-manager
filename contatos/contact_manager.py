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
            print(f'{index + 1}. {contato['nome']} - {contato['numero']}' - {contato['email']})

def remove_contato(nome):
    global contatos
    contatos = [contato for contato in contatos if contato['name'] !=nome ]
    print(f'Contatos {nome} removido com  sucesso !')   
             