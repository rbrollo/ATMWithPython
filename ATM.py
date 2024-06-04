CONTA = '123456'
SENHA = '123'
saldo = 0.0
LIMITE_CHEQUE_ESPECIAL = 100.0
cheque_especial_utilizado = 0.0
tentativas = 0
TENTATIVAS_MAXIMAS = 3
rodando_login = True

while rodando_login:
    conta_digitada = input("Informe sua conta: ")
    senha_digitada = input("Informe sua senha: ")

    if conta_digitada == CONTA and senha_digitada == SENHA:
        rodando = True

        while rodando:
            opcao_selecionada = input(
                "Informe a opção desejada \n"
                "1-Saldo \n"
                "2-Depósito \n"
                "3-Retirada \n"
                "4-Sair \n"
            )

            if opcao_selecionada == '4':
                print('Saindo...')
                rodando = rodando_login = False

            elif opcao_selecionada == '1':
                print(f'Seu saldo é de: R${saldo} \n')

            elif opcao_selecionada == '2':
                qtd_depositar = input('Quanto deseja depositar? \n')

                try:
                    qtd_depositar = float(qtd_depositar)
                    if qtd_depositar >= 0:
                        if cheque_especial_utilizado > 0.0:
                            cheque_especial_utilizado -= qtd_depositar
                            if cheque_especial_utilizado < 0:
                                cheque_especial_utilizado = 0
                            saldo += qtd_depositar
                            print(f"Seu novo saldo é de R${saldo} \n")
                            continue
                        saldo += qtd_depositar
                        print(f"Seu novo saldo é de R${saldo} \n")
                    else:
                        print("Por favor, informe um número válido \n")
                except ValueError:
                    print("Por favor, informe um número válido \n")

            elif opcao_selecionada == '3':
                qtd_retirar = input('Quanto deseja retirar? \n')

                try:
                    qtd_retirar = float(qtd_retirar)
                    if qtd_retirar > 0:
                        if cheque_especial_utilizado == LIMITE_CHEQUE_ESPECIAL:
                            print(
                                f"Já atingiu o limite do cheque especial que é de R$ {LIMITE_CHEQUE_ESPECIAL} \n"
                            )
                            continue
                        if abs(saldo - qtd_retirar) > LIMITE_CHEQUE_ESPECIAL:
                            print(
                                f"Este valor de retirada excede o limite do cheque especial que é de R$ {LIMITE_CHEQUE_ESPECIAL} \n"
                            )
                            continue
                        if saldo <= 0:
                            cheque_especial_utilizado += qtd_retirar
                            saldo -= qtd_retirar
                            print(
                                f"Seu novo saldo é de R${saldo}, você está no cheque especial "
                                f"que tem um limite de até R${LIMITE_CHEQUE_ESPECIAL} e você ainda pode "
                                f"utilizar R${LIMITE_CHEQUE_ESPECIAL - cheque_especial_utilizado}\n"
                            )
                            continue
                        if saldo >= 0 and saldo - qtd_retirar < 0:
                            cheque_especial_utilizado = abs(saldo)
                            saldo -= qtd_retirar
                            print(
                                f"Seu novo saldo é de R${saldo}, você está no cheque especial "
                                f"que tem um limite de até R${LIMITE_CHEQUE_ESPECIAL} e você ainda pode "
                                f"utilizar R${LIMITE_CHEQUE_ESPECIAL - cheque_especial_utilizado}\n"
                            )
                            continue

                        saldo -= qtd_retirar
                        print(f"Seu novo saldo é de R${saldo} \n")
                    else:
                        print("Por favor, informe um número válido \n")
                except ValueError:
                    print("Por favor, informe um número válido \n")

    else:
        tentativas += 1
        if tentativas == TENTATIVAS_MAXIMAS:
            print(
                f"Você errou: {tentativas}/{TENTATIVAS_MAXIMAS} vezes seu usuário/senha, tente novamente mais tarde"
            )
            break
        print(
            f"Conta ou Senha incorreta(s), você errou: {tentativas} de no máximo: {TENTATIVAS_MAXIMAS}"
        )
        continue
