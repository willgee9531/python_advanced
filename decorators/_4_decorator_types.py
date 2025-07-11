import functools
from dataclasses import dataclass
""" 
5 types of decorators to use:
    - @property (enable getter, setter and deleter of private attributes)
    - @static_method
    - @classmethod
    - @functools.cache
    - @dataclass
"""

# 1. @property when applied to a method acts like a getter and then allows that 
# method to also act as a setter and deleter by calling the @method.setter/deleter
# e.g. for a private attribute add an underscore at the beginning: _name_of_the_attr

class MaleStudent:
    def __init__(self, name):
        self._name = name
        self.GENDER = "Male"

    @property
    def naming(self):
        """ gets the name value """
        return self._name
    
    @naming.setter
    def naming(self, value):
        """ sets the name value """
        self._name = value.capitalize()
    
    @naming.deleter
    def naming(self):
        """ deletes the name value """
        self._name = ""
    

male_student1 = MaleStudent("G.C. Williams")
# print(male_student1.naming)

male_student1.naming = "WillGee"
# print(male_student1.naming)

del male_student1.naming
# print(male_student1.naming)



# 2. @staticmethod when used denotes a static inbuilt method for a class
# which does not depend on instance assignment (self param)

class BankAccount1:
    def __init__(self, usd_balance):
        self.usd_balance = usd_balance
        self.currency = "$"

    def balance(self):
        return f"{self.currency}{self.usd_balance}"
    
    @staticmethod
    def convert_to_naira(usd_value, rate=1500):
        return usd_value * rate


# print(BankAccount.convert_to_naira(50))

williams_acct = BankAccount1(3375)

# print(williams_acct.balance())
# print(williams_acct.convert_to_naira(williams_acct.usd_balance))


# 3. @classmethod is used to reference the class itself and not an object instance (cls)
# since self param is not included then it can only access class-defined attributes

class BankAccount:
    acct_type = "Savings"

    def __init__(self, usd_balance):
        self.usd_balance = usd_balance
        self.currency = "$"

    def balance(self):
        # include the class attribute by calling classmethods already defined
        return f"{self.print_acct_type()}\nAccount Balance: {self.currency}{self.usd_balance}"
    
    @classmethod
    def print_acct_type(cls):
        return f"Account type: {cls.acct_type}"
    
    @classmethod
    def change_acct_type(cls, value):
        cls.acct_type = value


my_aza = BankAccount(2000)

# print(my_aza.print_acct_type())
# print(my_aza.balance())

my_aza.change_acct_type("Current")
# print(my_aza.balance())



# 4. @functools.cache serves as an inbuilt cache 

""" def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n < 1:
        return n
    if n == 1:
        return 0
    if n in [2, 3]:
        return 1
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n] """

@functools.cache
def fibonacci(n):
    if n < 1:
        return n
    if n == 1:
        return 0
    if n in [2, 3]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
    

# print(fibonacci(40))


# 5. @dataclass creates the __init__, __repr__, __eq__ methods for your class

@dataclass
class Inventory:
    """ Helps track stocks movement """
    name: str
    amount: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.amount * self.quantity


stock1 = Inventory("Gold necklace", 450000, 3)
stock2 = Inventory("Omen laptop", 1800000, 2)
stock3 = Inventory("Omen laptop", 1800000, 2)
print(stock1, stock2)
print(stock2 == stock3)
help(Inventory)