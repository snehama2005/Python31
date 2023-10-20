#1
#1Write a program to check whether the entered number is postive or
# negative
# def check(n):
    # if n > 0:
        # print("Positive")
         
    # elif n < 0:
        # print("Negative")
#2Write a program to swap two variables.


        # x = 10
# y = 50
 
# Swapping of two variables
# Using third variable
# temp = x
# x = y
# y = temp
 
# print("Value of x:", x)
# print("Value of y:", y)
#3Write a program to Determine If Year Is Leap year
# year = int (input ("Enter any year that is to be checked for leap year"))

# if (year % 4) == 0:

#               if (year % 100) == 0:

#                              if (year % 400) == 0:

#                                             print (“The given year is a leap year”)

#                              else:

#                                             print (“It is not a leap year”)

#               else:

#                              print (“It is not a leap year”)

# else:     

#             print (“It is not a leap year”)
#4Write a program check whether the given number is odd or even.
# x = 24
   
# if x % 24 == 0:
#     print(x,"Is Even Number")
# else:
#     print(x, "Is Odd Number")
     
# y = 19
   
# if y % 19 == 0:
#     print(y,"Is Even Number")
# else:
#     print(y, "Is Odd Number")
#5Write a program to print the fibonocci series.
# n = 10
# num1 = 0
# num2 = 1
# next_number = num2  
# count = 1
 
# while count <= n:
#     print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
# print()
#7. Write a program to print the prime numbers between given interval.
# def prime(x, y):
#     prime_list = []
#     for i in range(x, y):
#         if i == 0 or i == 1:
#             continue
#         else:
#             for j in range(2, int(i/2)+1):
#                 if i % j == 0:
#                     break
#             else:
#                 prime_list.append(i)
#     return prime_list
 
# # Driver program
# starting_range = 2
# ending_range = 7
# lst = prime(starting_range, ending_range)
# if len(lst) == 0:
#     print("There are no prime numbers in this range")
# else:
#     print("The prime numbers in this range are: ", lst)

#8.  Write a program to find the factorial of the given number.
# def factorial(n):
     
#     # single line to find factorial
#     return 1 if (n==1 or n==0) else n * factorial(n - 1) 
 
# # Driver Code
# num = 5
# print("Factorial of",num,"is",factorial(num))
#9 .Write a program to Check if the given string is Palindrome or not.
# def isPalindrome(s):
#     return s == s[::-1]
 
 
# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)
 
# if ans:
#     print("Yes")
# else:
#     print("No")

#     #10Write a program to find sum of all integers greater than 100 and lessthan 200 that are divisible by 7
#     min_val = 100
# max_val = 200
 
# # Check each number within the range
# for num in range(min_val, max_val+1):
#     if num % 7 == 0:
#         print(num, "is divisible by 7 ")
#11.Write a program to Display Multiplication table


# Multiplication table (from 1 to 10) in Python


                   # Multiplication table (from 1 to 10) in Python

# num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)
   #12write a program to find the perimeter of a rectangle
# length = int(input("Enter the length of the rectangle: "))
# width = int(input("Enter the width of the rectangle: "))
        
# area = length * width
# perimeter = 2 * (length + width)
        
# print("The area of the rectangle is:", area)
# print("The perimeter of the rectangle is:", perimeter)
#13 Write a program to find the sum of n' Natural Numbers.
# Sum of natural numbers up to num

# num = 16

# if num < 0:
#    print("Enter a positive number")
# else:
#    sum = 0
#    # use while loop to iterate until zero
#    while(num > 0):
#        sum += num
#        num -= 1
#    print("The sum is", sum)
#14 15.Write a program to find whether given no. is Armstrong or not.
# Python program to check if the number is an Armstrong number or not

# take input from the user
# num = int(input("Enter a number: "))

# # initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
#15Write a program to find the largest among 3 numbers
# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
# num1 = 10
# num2 = 14
# num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3

# print("The largest number is", largest)
#16Write a program to remove all punctuations from given string
# define punctuation
# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
# no_punct = ""
# for char in my_str:
#    if char not in punctuations:
    #    no_punct = no_punct + char

# display the unpunctuated string
# print(no_punct)
#16 Write a program to find the largest among 3 numbers.



# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
# num1 = 10
# num2 = 14
# num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3

# print("The largest number is", largest)
#17 Write a program to remove all punctuations from given string
 #define punctuation
# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# my_str = "Hello!!!, he said ---and went."

# # To take input from the user
# # my_str = input("Enter a string: ")

# # remove punctuation from the string
# no_punct = ""
# for char in my_str:
#    if char not in punctuations:
#        no_punct = no_punct + char

# # display the unpunctuated string
# print(no_punct)
#18 Write a program to count the no:of each vowel in a given string.
# string = "GeekforGeeks!"
# vowels = "aeiouAEIOU"
 
# count = sum(string.count(vowel) for vowel in vowels)
# print(count)
#19Program to perform Addition,Subtraction,Multiplication and division on complex-no's
def addComplex( z1, z2):
    return z1 + z2
 
# Driver's code
z1 = complex(2, 3)
z2 = complex(1, 2)
print( "Addition is : ", addComplex(z1, z2))
def subComplex( z1, z2):
    return z1-z2
 
# driver program
z1 = complex(2, 3)
z2 = complex(1, 2)
print( "Subtraction is : ", subComplex(z1, z2))
def complex_addition(num1, num2):
    return num1 + num2
 
# Define a function to subtract two complex numbers
def complex_subtraction(num1, num2):
    return num1 - num2
 
# Read the two complex numbers from the user
num1 = complex(2, 3)
num2 = complex(1, 2)
 
# Call the two functions with the two complex numbers as arguments
addition = complex_addition(num1, num2)
subtraction = complex_subtraction(num1, num2)
 
# Print the results
print("Addition is :", addition)
print("Subtraction is :", subtraction)




