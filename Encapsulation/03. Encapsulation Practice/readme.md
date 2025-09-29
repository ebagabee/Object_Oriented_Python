# Encapsulation Practice

Age of Dragons is a game about resource management and strategy. The game has a feature that allows players to manage their resources in a bank. The bank has a feature that allows players to deposit and withdraw funds.

## Assignment

Complete the `BankAccount` class.

1. [ ] Complete the constructor
   1. [ ] Set `__account_number` to `account_number`
   2. [ ] Set `__balance` to `initial_balance`
2. [ ] Complete the public getters
   1. [ ] Complete the `get_account_number` method to get the value of the private variable `__account_number` and `return` it.
   2. [ ] Complete the `get_balance` method to get the value of the private variable `__balance` and `return` it.
3. [ ] Complete the `deposit` method
   1. [ ] It should accept an `amount` as input and add it to the account `balance`.
   2. [ ] If the deposit amount isn't positive, it should `raise` a [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) exception with the message `cannot deposit zero or negative funds`. Otherwise, it should add the amount to the balance.
4. [ ] Complete the `withdraw` method
   1. [ ] It should accept an `amount` and check if there is enough money in the account for the withdrawal.
   2. [ ] If the withdrawal amount isn't positive, it should `raise` a `ValueError` exception with the message `cannot withdraw zero or negative funds`.
   3. [ ] Then, if there are *not* enough funds it should `raise` a `ValueError` exception with the message `insufficient funds`.
   4. [ ] Otherwise, it should deduct the `amount` from the balance.
