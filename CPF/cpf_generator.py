import random

cpf = ''

for _ in range(9):
    cpf += str(random.randint(0, 9))

# FIRST DIGIT
decrement_start = 10
sum_of_numbers = 0

for n in cpf:
    sum_of_numbers += int(n) * decrement_start
    decrement_start -= 1

first_digit = ((sum_of_numbers * 10) % 11) if ((sum_of_numbers * 10) % 11) <= 9 else 0

# SECOND DIGIT
decrement_start_second_digit = 11
sum_second_digit = 0
cpf_with_first_digit = cpf + str(first_digit)

for n in cpf_with_first_digit:
    sum_second_digit += int(n) * decrement_start_second_digit
    decrement_start_second_digit -= 1

second_digit = ((sum_second_digit * 10) % 11) if ((sum_second_digit * 10) % 11) <= 9 else 0
cpf += str(first_digit) + str(second_digit)

print(f"CPF: {cpf}")
