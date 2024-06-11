# Lista de Compras

Este projeto é um simples gerenciador de lista de compras em Python. Ele permite aos usuários inserir itens, listar os itens da lista, apagar itens e sair do programa.

## Funcionalidades

- **Listar itens**: Exibe todos os itens presentes na lista de compras.
- **Inserir itens**: Adiciona novos itens à lista de compras.
- **Apagar itens**: Remove itens da lista de compras especificando a posição do item.
- **Sair**: Sai do programa.

## Como usar

1. **Escolha uma das opções**:
   - `[i]` - Inserir item
   - `[a]` - Apagar item
   - `[l]` - Listar itens
   - `[s]` - Sair

## Exemplo de uso

```sh
Selecione uma opção:
[i]nserir [a]pagar [l]istar [s]air : i
Insira o nome do novo item: Maçã
Maçã inserido na lista de compra

Selecione uma opção:
[i]nserir [a]pagar [l]istar [s]air : l
1 - Maçã

Selecione uma opção:
[i]nserir [a]pagar [l]istar [s]air : a
Insira a posição do item que deseja remover: 1
O item: Maçã, foi removido da lista de compra

Selecione uma opção:
[i]nserir [a]pagar [l]istar [s]air : s
Saindo...
```

#### Regras de negócio

- Inserir Itens: O usuário pode inserir qualquer nome de item.
- Listar Itens: Exibe todos os itens adicionados à lista. Se a lista estiver vazia, uma mensagem será exibida.
- Apagar Itens: O usuário deve informar a posição do item na lista para removê-lo. Se a posição não for válida ou a lista estiver vazia, uma mensagem de erro será exibida.
- Sair: Finaliza a execução do programa.

#### Observações

O script é um exemplo simples e educativo de um gerenciador de lista de compras.
Não há persistência de dados; os itens são armazenados apenas em memória durante a execução do script.
