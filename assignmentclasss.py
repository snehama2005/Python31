#1. Define a class which has at least two methods one, to get a string from console  input and other is to print the string in uppercase.
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""

#     def getString(self):
#         self.s = input()
    
#     def printString(self):
#         print(self.s.upper())
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()
#2 Define a class, which have a class parameter and have a same instance parameter.
# class sampleclass: 
#     count = 0     # class attribute 
  
#     def increase(self): 
#         sampleclass.count += 1
  
# # Calling increase() on an object 
# s1 = sampleclass() 
# s1.increase()         
# print(s1.count) 
  
# # Calling increase on one more 
# # object 
# s2 = sampleclass() 
# s2.increase() 
# print(s2.count) 
  
# print(sampleclass.count) 
#3 Define a class named Circle which can be constructed by radius. The Circle class has a method which can compute the area
# class Circle():
#     def radius(self,radius):
#         r = radius
#     def area(self,r):
#         area = 3.142*r*r
#         print("Area of the circle is: ",area)
#     def peri(self,r):
#         peri = 2*3.14*r
#         print("Perimeter of the circle is: ",peri)
# c = Circle()
# radius = int(input("Enter the radius of circle: "))
# c.area(radius)
# c.peri(radius)
#           4Define a class named BankAccount. This class should contain methods withdraw() and deposit to calculate the balance amount remained in your account.
# class Bank_Account:
#     def __init__(self):
#         self.balance=0
#         print("Hello!!! Welcome to the Deposit & withdrawl Machine")
#     def deposit(self):
#         amount=float(input("Enter amount to be Deposited: "))
#         self.balance += amount
#         print("\n Amount Deposited:",amount)
#     def withdraw(self):
#         amount = float(input("Enter amount to be Withdrawn: "))
#         if self.balance>=amount:
#             self.balance-=amount
#             print("\n You Withdrew:", amount)
#         else:
#             print("\n Insufficient balance  ")
#     def display(self):
#             print("\n Net Available Balance=",self.balance)
# s = Bank_Account()
# s.deposit()
# s.withdraw()
# s.display()
# #5Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# Example usage:
shape = Shape()
print("Area of Shape:", shape.area())

square = Square(5)
print("Area of Square:", square.area())
