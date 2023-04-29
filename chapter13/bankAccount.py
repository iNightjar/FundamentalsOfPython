"""
To streamline our example, we will model bank accounts that maintain just three attributes:
    • Every account has a unique identifier, the account number.
    • Each account's owner has a name.
    • Each account has a current balance.
"""


class BankAccount:
    """Models a bank account"""

    def __init__(self, number, name, balance) -> None:
        """ Initialize the instance variables of a bank account object. 
        disallows a negative initial balance."""
        if balance < 0:
            raise ValueError("Negative initial number. ")
        self.__account_number = number  # account number
        self.__name = name  # customer name
        self.__balance = balance  # funds available in the account

    def id(self):
        """ Returns the account number of this bank account object."""
        return self.__account_number

    def deposit(self, amount):
        """ add funds to the account. there is no limit to the size of the deposit"""
        self.__balance += amount

    def withdraw(self, amount):
        """ Remove funds from the account, if possible. 
        only completes the withdrawal succesfully if there are enough funds in the account to fulfill the withdrawal.
        return true if succesful, false otherwise. """
        result = False
        if self.__balance - amount >= 0:
            self.__balance -= amount
            result = True
        return result

    def __str__(self) -> str:
        """ Return the string representation of the object. """
        return '[{:>5} {:<10} {:>7}]'.format(self.__account_number, self.__name, self.__balance)


# ------------------------------------------- #
# global functions that uses bankaccount objects

def open_db(filename, db):
    """ Read account information from a given file and store it in the given list. """
    with open(filename) as file:
        for line in file:
            line.strip()
            number, name, balance = line.split(",")
            db.append(BankAccount(int(number), name, int(balance)))


def print_db(db):
    """ Display the contents of the database. """
    for acc in db:
        print(acc)


def get_account(db, account_number):
    """ retrieve an account object with a given account number. """
    for acc in db:
        if acc.id() == account_number:
            return acc


def main():
    """ simple bank account database. """
    database = []
    try:
        # open the database of accounts
        open_db('accountsRecords.txt', database)
        print_db(database)
        print(" ---------------------------- ")
        customer = get_account(database, 129)
        # print(customer)
        if customer:  # True of objects returnted
            print("Account 129 before withdraw of $80000: ", end="")
            print(customer)
            customer.withdraw(100)
            print(" ---------------------------- ")
            print("Account 129 after withdraw of $80000: ", end="")
            print(customer)
    except Exception:
        print("Error in account database. ")
        raise


main()
