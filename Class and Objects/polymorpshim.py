#polymorpishm
"""class Animal:
    def make_sound(self):
        print("animal makes sound")
class Dog(Animal):
    def make_sound(self):
        print("dog is barking")
class Cat(Animal):
    def make_sound(self):
        print("cat is mewoming")
class Cow(Animal):
    def make_sound(self):
        print("cow is moooooooooow")


obj = [Dog(),Cat(),Cow()]
for i in obj:
    i.make_sound()"""


"""class car:
    def start(self):
        print("car is starting")
class Computer:
    def start(self):
        print("computer is boosting")
class washingmachine:
    def start(self):
        print("washinhg is running")

def operate(device):
    device.start()

operate(car())
operate(Computer())
operate(washingmachine())"""


"""class Transport:
    def show(self):
        print("transport is moving")
class Car(Transport):
    def show(self):
        super().show()
        print("car is moving")
class bike(Transport):
    def show(self):
        super().show()
        print("bike is moving")

obj = Car()
obj.show()
obj = bike()
obj.show()"""

"""class payment:
    def process(self,amount):
        print(f"processing payment of {amount}")
class creditcardpayment(payment):
    def process(self,amount,card_type):
        super().process(amount)
        print(f"processing payment of {amount} with {card_type}")

obj = creditcardpayment()
obj.process(1000,'visa')"""

"""class BS:
    def logic(self,data):
        print("buble sort:",sorted(data))
class MS:
    def logic(self,data):
        print("merged sort",sorted(data))
class QS:
    def logic(self,data):
        print("quick sort:",sorted(data))

class Sorter:
    def change(self,strategy,data):
        strategy.logic(data)

num = [2,3,4,5,7,8]
l = [BS(),MS(),QS()]
for i in l:
    Sorter().change(i,num)"""

"""class Account:
    def withdraw(self,amount):
        print(f"account withdrawing {amount}")
class SavingAccount(Account):
    def withdraw(self,amount):
        print(f"saving account rules {amount}")
        super().withdraw(amount)
class PremiumSavingsAccount(SavingAccount):
    def withdraw(self,amount):
        print(f"premium saving account: Extra benefits appiled")
        super().withdraw(amount)

obj = PremiumSavingsAccount()
obj.withdraw(100)"""




