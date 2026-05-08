def add(a, b):
    return a + b

def is_even(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    return number % 2 == 0

class BankAccount:
    def __init__(this, balance = 0):
        this.balance = balance

    def deposit(this, amount):
        this.balance += amount
    
    def withdraw(this, amount):
        if amount > this.balance:
            raise ValueError("Not enough funds")
        this.balance -= amount
    
    def transfer(this, otheraccount, amount):
        this.withdraw(amount) 
        otheraccount.deposit(amount)

