import re

running = True

while running:
    cpf_input = input("Enter your CPF:\n")
    formatted_cpf_input = re.sub(r'[^0-9]', "", cpf_input)
    repeat_check = formatted_cpf_input[0] * len(formatted_cpf_input)

    if repeat_check == formatted_cpf_input:
        print("Enter a valid CPF\n")
        continue

    if len(cpf_input) == 14 or len(cpf_input) == 11:
        formatted_cpf_without_digit = re.sub(r'[^0-9]', "", cpf_input)
        formatted_cpf_without_digit = formatted_cpf_without_digit[:-2]
        print(formatted_cpf_without_digit)
    else:
        print("Enter a valid CPF\n")
        continue

    # FIRST DIGIT
    decrement_start = 10
    sum_of_numbers = 0

    for n in formatted_cpf_without_digit:
        sum_of_numbers += int(n) * decrement_start
        decrement_start -= 1

    if sum_of_numbers == 0:
        print("Enter a valid CPF")
    else:
        first_digit = ((sum_of_numbers * 10) % 11) if ((sum_of_numbers * 10) % 11) <= 9 else 0

        # SECOND DIGIT
        decrement_start_second_digit = 11
        sum_second_digit = 0
        cpf_with_first_digit = formatted_cpf_without_digit + str(first_digit)

        for n in cpf_with_first_digit:
            sum_second_digit += int(n) * decrement_start_second_digit
            decrement_start_second_digit -= 1

        if sum_second_digit == 0:
            print("Enter a valid CPF")
        else:
            second_digit = ((sum_second_digit * 10) % 11) if ((sum_second_digit * 10) % 11) <= 9 else 0
            cpf_validator = formatted_cpf_without_digit + str(first_digit) + str(second_digit)
            if formatted_cpf_input == cpf_validator:
                print("Your CPF is valid")
            else:
                print("Invalid CPF")
