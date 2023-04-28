# example for strategy design pattern in python


class strategy:
    def execute(self, firstVar, secondVar):
        pass


class add(strategy):
    def execute(self, firstVar, secondVar):
        return firstVar + secondVar


class subtract(strategy):
    def execute(self, firstVar, secondVar):
        return firstVar - secondVar


class multiply(strategy):
    def execute(self, firstVar, secondVar):
        return firstVar * secondVar


class Calculator:
    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def execute_strategy(self, firstVar, seocndVar):
        return self.strategy.execute(firstVar, seocndVar)


add_strategy = add()
calculator = Calculator(add_strategy)
result = calculator.execute_strategy(2, 3)
print("Add Result: ", result)  # result = 6


subtract_strategy = subtract()
calculator = Calculator(subtract_strategy)
result = calculator.execute_strategy(5, 2)
print("Subtract Result: ", result)  # result = 3


multiply_strategy = multiply()
calculator = Calculator(multiply_strategy)
result = calculator.execute_strategy(1, 2)
print("Multiply Result: ", result)  # result = 2
