#single inheritance
"""class one:
    def show(self):
        print("one is the number")
class two(one):
    def show1(self):
        print("two is the number")

obj = two()
obj.show1()"""
from traceback import print_tb

"""class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog is barking")

obj = Dog()
obj.sound()
obj.sound()"""

"""class A:
    def show(self):
        print("A is one class")
class B(A):
    def show(self):
        super().show()
        print("B is second class")

obj = B()
obj.show()"""


#multi-level inheritance
"""class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
        super().show()
class C(B):
    def show(self):
        super().show()
        print("C")


obj = C()
obj.show()
print(C.mro())"""

"""class Number:
    def get_number(self):
        self.n = int(input("Enter a number: "))
class Square(Number):
    def add_square(self):
        print("square:",self.n ** 2)
class Cube(Square):
    def add_cube(self):
        print("Cube:",self.n ** 3)


obj = Cube()
obj.get_number()
obj.add_square()
obj.add_cube()"""

"""class Student:
    def details(self):
        self.Name = input("Name: ")
        self.rollno = input("Roll no: ")


class Marks(Student):
    def subject_marks(self):
        self.m1 = int(input("Enter marks: "))
        self.m2 = int(input("Enter marks: "))
        self.m3 = int(input("Enter marks: "))
class result(Marks):
    def total_avg(self):
        total = self.m1 + self.m2 + self.m3
        avg = total / 3
        print("Name: ",self.Name)
        print("Roll:",self.rollno)
        print("Total:", total)
        print("Average:", avg)

obj = result()
obj.details()
obj.subject_marks()
obj.total_avg()"""

#hirechracal
"""class Vechicle:
    def wheels(self):
        print("vechicles are moving")
class Car(Vechicle):
    def car_type(self):
        print("car has 4 wheels")
class truck(Vechicle):
    def truck_type(self):
        print("truck has 8 wheels")


obj = truck()
obj.wheels()
obj.truck_type()

obj = Car()
obj.wheels()
obj.car_type()"""


"""class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def Meow(self):
        print("Cat is Meowing")


obj = Cat()
obj.eat()
obj.Meow()

obj = Dog()
obj.eat()
obj.bark()"""


"""class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
        super().show()


obj = C()
obj.show()"""


"""class Animal:
    def sound(self):
        print("Animal is sounding")
class Dog(Animal):
    def sound(self):
        print("Dog is sounding")
class Cat(Animal):
    def sound(self):
        print("Cat is sounding")
class Cow:
    def sound(self):
        print("Cow is sounding")



obj = Cat()
obj.sound()"""


"""class Vehicle:
    def wheels(self):
        print("vehicle have whels")
class  Car(Vehicle):
    def wheels(self):
        print("car have 4 wheels")
class bike(Vehicle):
    def wheels(self):
        super().wheels()
        print("bike have 2 wheels")



obj = bike()
obj.wheels()"""


"""class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,rollno):
        super().__init__(name)
        self.rollno = rollno


obj = Student('ganesh',5789)
print(obj.name,obj.rollno)"""

#multiple inheritance
"""class Father:
    def Skill(self):
        print("father know a driving a car")
class Mother:
    def skill(self):
        print("mother know a cooking")
class child(Father, Mother):
    def skill(self):
        super().Skill()
        print("child knows the both")

obj =child()
obj.skill()
print(child.mro())"""

"""class Employee:
    def salary(self):
        print("salary of employee = 300000")

class Manager(Employee):
    def salary(self):
        print("employee salary = 302000" )

obj = Manager()
obj1 = Employee()

obj1.salary()
obj.salary()"""

"""class Math0ps:
    @staticmethod
    def add(a,b):
        return a+b
class Advanced0ps(Math0ps):
    pass
print(Advanced0ps.add(1,2))"""


"""class University:
    name = "KL University"

    @classmethod
    def show(cls):
        print("university name:",cls.name)

class College(University):
    @classmethod
    def show(cls):
        super().show()


obj = College()
obj.show()"""

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




