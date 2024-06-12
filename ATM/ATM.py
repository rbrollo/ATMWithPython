ACCOUNT = '123456'
PASSWORD = '123'
balance = 0.0
OVERDRAFT_LIMIT = 100.0
overdraft_used = 0.0
attempts = 0
MAX_ATTEMPTS = 3
login_running = True

while login_running:
    entered_account = input("Enter your account number: ")
    entered_password = input("Enter your password: ")

    if entered_account == ACCOUNT and entered_password == PASSWORD:
        running = True

        while running:
            selected_option = input(
                "Select the desired option \n"
                "1-Balance \n"
                "2-Deposit \n"
                "3-Withdrawal \n"
                "4-Exit \n"
            )

            if selected_option == '4':
                print('Exiting...')
                running = login_running = False

            elif selected_option == '1':
                print(f'Your balance is: ${balance} \n')

            elif selected_option == '2':
                deposit_amount = input('How much would you like to deposit? \n')

                try:
                    deposit_amount = float(deposit_amount)
                    if deposit_amount >= 0:
                        if overdraft_used > 0.0:
                            overdraft_used -= deposit_amount
                            if overdraft_used < 0:
                                overdraft_used = 0
                            balance += deposit_amount
                            print(f"Your new balance is ${balance} \n")
                            continue
                        balance += deposit_amount
                        print(f"Your new balance is ${balance} \n")
                    else:
                        print("Please enter a valid number \n")
                except ValueError:
                    print("Please enter a valid number \n")

            elif selected_option == '3':
                withdrawal_amount = input('How much would you like to withdraw? \n')

                try:
                    withdrawal_amount = float(withdrawal_amount)
                    if withdrawal_amount > 0:
                        if overdraft_used == OVERDRAFT_LIMIT:
                            print(
                                f"You have reached the overdraft limit of ${OVERDRAFT_LIMIT} \n"
                            )
                            continue
                        if abs(balance - withdrawal_amount) > OVERDRAFT_LIMIT:
                            print(
                                f"This withdrawal amount exceeds the overdraft limit of ${OVERDRAFT_LIMIT} \n"
                            )
                            continue
                        if balance <= 0:
                            overdraft_used += withdrawal_amount
                            balance -= withdrawal_amount
                            print(
                                f"Your new balance is ${balance}, you are in overdraft "
                                f"which has a limit of up to ${OVERDRAFT_LIMIT} and you can still "
                                f"use ${OVERDRAFT_LIMIT - overdraft_used}\n"
                            )
                            continue
                        if balance >= 0 and balance - withdrawal_amount < 0:
                            overdraft_used = abs(balance)
                            balance -= withdrawal_amount
                            print(
                                f"Your new balance is ${balance}, you are in overdraft "
                                f"which has a limit of up to ${OVERDRAFT_LIMIT} and you can still "
                                f"use ${OVERDRAFT_LIMIT - overdraft_used}\n"
                            )
                            continue

                        balance -= withdrawal_amount
                        print(f"Your new balance is ${balance} \n")
                    else:
                        print("Please enter a valid number \n")
                except ValueError:
                    print("Please enter a valid number \n")

    else:
        attempts += 1
        if attempts == MAX_ATTEMPTS:
            print(
                f"You have entered incorrect username/password {attempts}/{MAX_ATTEMPTS} times, please try again later"
            )
            break
        print(
            f"Incorrect account number or password, you have made {attempts} out of a maximum of {MAX_ATTEMPTS} attempts"
        )
        continue
