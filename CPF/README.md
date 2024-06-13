### README em Inglês

# CPF Generator and Validator

This repository contains two Python scripts:

1. **CPF Generator**: Generates a valid Brazilian CPF number.
2. **CPF Validator**: Validates a given Brazilian CPF number.

The CPF (Cadastro de Pessoas Físicas) is an 11-digit number used for individual taxpayer identification in Brazil.

## CPF Generator

### How It Works

1. The script generates the first 9 digits of the CPF randomly.
2. It calculates the first verification digit based on the CPF algorithm.
3. It appends the first verification digit to the 9 initial digits.
4. It calculates the second verification digit.
5. Finally, it prints the full 11-digit CPF.

### Usage

1. Make sure you have Python installed on your system.
2. Save the generator script to a file, e.g., `cpf_generator.py`.
3. Run the script using the command:

```bash
python cpf_generator.py
```

4. The script will print a valid CPF number.

### Example

```text
CPF: 12345678909
```

## CPF Validator

### How It Works

1. The user is prompted to input their CPF.
2. The script formats the input by removing any non-numeric characters.
3. It checks if the input contains all the same digits (e.g., "111.111.111-11"), which is invalid.
4. The script verifies the length of the CPF, ensuring it has 11 digits.
5. It calculates the first and second verification digits based on the CPF algorithm.
6. The script validates the CPF by comparing the calculated verification digits with the input.

### Usage

1. Make sure you have Python installed on your system.
2. Save the validator script to a file, e.g., `cpf_validator.py`.
3. Run the script using the command:

```bash
python cpf_validator.py
```

4. Enter your CPF when prompted.

### Example

```text
Enter your CPF:
123.456.789-09
Your CPF is valid
```
