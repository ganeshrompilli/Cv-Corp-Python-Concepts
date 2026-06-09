# Error handling
# class Person:
#     def __init__(self,age):
#         if age<0:
#             raise ValueError("age is greater or equal to 0")
#         else:
#             self.age = age
#
#
# obj = Person(78)
# obj1 = Person(-1)
#
#
# class Student:
#     def __init__(self):
#         self.marks = 0
#     def set_marks (self,marks):
#         if marks<0 or marks > 100:
#             raise ValueError("Marks is not range in 0 to 100")
#         else:
#             self.marks = marks
#
# s1 = Student()
# s1.set_marks(80)
# print(s1.marks)
# s1.set_marks(120)


#
# class InvalidAgeError(Exception):
#     pass
# class Voter:
#     def check_eligibilty(self,age):
#         if age < 18:
#             raise InvalidAgeError("age is greater than 18")
#         else:
#             self.age = age
#
#
# obj = Voter()
# obj.check_eligibilty(48)
# print(obj.age)
# obj1= Voter()
# obj1.check_eligibilty(5)
# print(obj.age)
#
# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance
#     def withdraw(self,amount):
#         if amount > self.balance:
#             raise ValueError("insuffient balance")
#         else:
#             self.balance -= amount
#
#
# obj = BankAccount(5000)
# obj.withdraw(6000)
# print(obj.balance)
#
#
# class PasswordValidator:
#     def validate(self,password):
#         if len(password) > 8:
#             raise ValueError("Length of the passord is than 8 charcters")
#         else:
#             self.password = password
#             print("validate")
#
# obj = PasswordValidator()
# obj.validate("979876899")
# print(obj.password)
#
#
# class UserInput:
#     def get_integer(self,value):
#         try:
#             num = int(value)
#             print(num)
#         except ValueError:
#             print("ValueError: invalid integer value")
#         except TypeError:
#             print("TypeError: value type is not supported")
#
#
# obj = UserInput()
# obj.get_integer(None)
# obj.get_integer("ABC")
#
#
#
# class shape:
#     def area(self):
#         raise NotImplementedError("class is not implemented")
# class Rectangle(shape):
#     def area(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#         print(f"{self.length * self.breadth}")
#
# obj = shape()
# obj.area()
# obj1 = Rectangle()
# obj1.area(10,30)
#
# class Transcation:
#     def process(self):
#         try:
#             print("transcation started")
#             amount = 100/0
#             print("transcation successful")
#         except ZeroDivisionError:
#             print("zde")
#         finally:
#             print("message is alredy printed")
#
# obj = Transcation()
# obj.process()
#
#
# class LoginSystem:
#     def login(self,password):
#         correct_password = "admin123"
#         if password != correct_password:
#             raise Exception("password is incorrect")
#         print("login successful")
#
# obj = LoginSystem()
# try:
#     obj.login("hello123")
# except Exception as e:
#     print(e)
#
#




