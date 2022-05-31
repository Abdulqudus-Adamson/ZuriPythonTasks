class Calculator():
    def __init__(self):
        self.first_number = int(input("Enter number: "))
        self.second_number = int(input("Enter another number: "))

    def add(self): return (self.first_number + self.second_number)

    def minus(self): return (self.first_number - self.second_number)

    def divide(self): return (self.first_number / self.second_number)

    def multiply(self): return (self.first_number * self.second_number)

    def modulus(self): return (self.first_number % self.second_number)


calculator = Calculator()
