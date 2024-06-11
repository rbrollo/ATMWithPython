# Simulador ATM (Caixa Eletrônico)

Este projeto é um simulador de ATM (caixa eletrônico) implementado em Python. Ele permite aos usuários verificar o saldo, fazer depósitos e retiradas, e utilizar cheque especial quando necessário.

## Funcionalidades

- **Login**: Os usuários devem fornecer uma conta e uma senha válidas para acessar as funcionalidades do ATM.
- **Consulta de Saldo**: Verifique o saldo disponível na conta.
- **Depósito**: Faça depósitos na conta. Os depósitos podem reduzir o valor utilizado do cheque especial, se houver.
- **Retirada**: Realize retiradas da conta, incluindo a possibilidade de utilizar cheque especial até um limite pré-definido.
- **Limite de Cheque Especial**: O sistema permite um limite de cheque especial de até R$ 100,00.

## Como usar

1. **Dados do login**:

   - **Conta**: `123456`
   - **Senha**: `123`

2. **Escolha uma das opções**:
   - `1` - Verificar saldo
   - `2` - Fazer depósito
   - `3` - Fazer retirada
   - `4` - Sair

## Exemplo de uso

```sh
Informe sua conta: 123456
Informe sua senha: 123
Informe a opção desejada
1-Saldo
2-Depósito
3-Retirada
4-Sair
```

#### Regras de negócio

- Limite de Tentativas de Login: O usuário tem no máximo 3 tentativas para inserir a conta e a senha corretas. Após isso, o acesso é bloqueado.
- Depósito: Valores depositados devem ser positivos. Se houver valor utilizado do cheque especial, o depósito primeiro reduz esse valor antes de aumentar o saldo.
- Retirada: Valores retirados devem ser positivos. Se o saldo não for suficiente, o cheque especial pode ser utilizado até o limite de R\$ 100,00.
- Cheque Especial: O limite do cheque especial é de R$ 100,00. Não é possível exceder esse valor em retiradas.

#### Observações

O script é um exemplo simples e educativo de um simulador de ATM, sem persistência de dados.
Para uso real, recomenda-se adicionar medidas de segurança adicionais e persistência em banco de dados.
