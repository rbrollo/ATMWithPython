lista = []
rodando = True
OPCOES = {
    "listar" : "l", 
    "inserir" : "i", 
    "apagar" : "a", 
    "sair" : "s",
    }

while rodando:
    opcao_escolhida = input("Selecione uma opção: \n [i]nserir [a]pagar [l]istar [s]air : ")
    if opcao_escolhida == OPCOES['listar']:
        if not lista :
            print("Sua lista está vazia")
        else:
            for i, item in enumerate(lista, start=1):
                print(i, '-', item)

    elif opcao_escolhida == OPCOES["inserir"]:
        item_add = input("Insira o nome do novo item: ")
        lista.append(item_add)
        print(f'{item_add} inserido na lista de compra')

    elif opcao_escolhida == OPCOES["apagar"]:
        if not lista :
            print("Sua lista está vazia, portanto não há o que apagar \n")
            continue
        item_remove = input("Insira a posição do item que deseja remover: ")
        try:
            int(item_remove)
            if int(item_remove) > len(lista):
                print("Indique uma posição válida \n")
                continue
        except ValueError:
            print("Indique uma posição válida \n")
            continue
        item_removido = lista[int(item_remove) - 1]
        print(f" O item:{item_removido}, foi removido da lista de compra")
        lista.pop(int(item_remove) - 1)

    elif opcao_escolhida == OPCOES["sair"]:
        print("Saindo...")
        rodando = False

    else:
        print("Selecione uma opção válida \n")
