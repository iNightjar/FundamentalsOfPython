class customer(object):
    """
    A customer of ABC bank with a checking account.
    Customers have the following properties:
        name: string respresenting the customer's name.
        balance: float tracking the current balance of the customer's account
    """

    def __init__(self, name) -> None:
        """
        return a customer object whose name is *name* and starting balance is *balance*
        """
        self.name = name

    def set_balance(self, balance=0.0):
        self.balance = balance

    def withdraw(self, amount):
        """
        Returns the balance ramaining after withdrawing *amount* dollars.
        """
        if amount > self.balance:
            raise RuntimeError('amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposite(self, amount):
        """returns the balance remaining after depositing *amount* dollars."""
        self.balance += amount
        return self.balance


inightjar = customer('inightjar')
inightjar.set_balance(1010)
print(inightjar.withdraw(500))
print(inightjar.deposite(500))
