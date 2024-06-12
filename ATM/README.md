# ATM Simulator

This project is an ATM (automated teller machine) simulator implemented in Python. It allows users to check their balance, make deposits and withdrawals, and use an overdraft when necessary.

## Features

- **Login**: Users must provide a valid account number and password to access the ATM functionalities.
- **Balance Inquiry**: Check the available balance in the account.
- **Deposit**: Make deposits into the account. Deposits can reduce the overdraft amount used if applicable.
- **Withdrawal**: Make withdrawals from the account, including the possibility of using an overdraft up to a predefined limit.
- **Overdraft Limit**: The system allows an overdraft limit of up to $100.00.

## How to Use

1. **Login Credentials**:

   - **Account**: `123456`
   - **Password**: `123`

2. **Choose an option**:
   - `1` - Check balance
   - `2` - Make a deposit
   - `3` - Make a withdrawal
   - `4` - Exit

## Usage Example

```sh
Enter your account number: 123456
Enter your password: 123
Select the desired option
1-Balance
2-Deposit
3-Withdrawal
4-Exit
```

#### Business Rules

- **Login Attempt Limit**: The user has a maximum of 3 attempts to enter the correct account number and password. After this, access is blocked.
- **Deposit**: Deposited amounts must be positive. If there is an overdraft amount used, the deposit first reduces this amount before increasing the balance.
- **Withdrawal**: Withdrawn amounts must be positive. If the balance is insufficient, the overdraft can be used up to the limit of $100.00.
- **Overdraft**: The overdraft limit is $100.00. It is not possible to exceed this amount in withdrawals.

#### Notes

The script is a simple and educational example of an ATM simulator, without data persistence.
For real use, it is recommended to add additional security measures and database persistence.
