#1Write a program to define a function that can accept an integernumber as input and print the "It is an even number" if the
# number is even, otherwise print "It is odd".
# def is_even(number):
#   if number % 2 == 0:
#     return True
#   else:
#     return False

# number = int(input("Enter a number: "))

# if is_even(number):
#   print("It is an even number")
# else:
#   print("It is an odd number")
#2 Write a program to define a function which can print a dictionarywhere the keys are numbers between 1 and 20 (both included)and the values are square of keys
# d=dict()
# for x in range(1,16):
#     d[x]=x**2
# print(d)  
# 3 Write a program to take a string as input and return a string with vowels removed
# string = input("Enter any string: ")
# if string == 'x':
#     exit();
# else:
#     newstr = string;
#     print("\nRemoving vowels from the given string");
#     vowels = ('a', 'e', 'i', 'o', 'u');
#     for x in string.lower():
#         if x in vowels:
#             newstr = newstr.replace(x,"");
#     print("New string after successfully removed all the vowels:");
#     print(newstr);
#4  Write a program to display Powers of 2  using Anonymous functions?
# Display the powers of 2 using anonymous function

# terms = 10

# Uncomment code below to take input from the user
# terms = int(input("How many terms? "))

# use anonymous function
# result = list(map(lambda x: 2 ** x, range(terms)))

# print("The total terms are:",terms)
# for i in range(terms):
#    print("2 raised to power",i,"is",result[i])
# 5  Write a program to implement bubble-sort algorithm

# def bubblesort(elements):
#     swapped = False
#     # Looping from size of array from last index[-1] to index [0]
#     for n in range(len(elements)-1, 0, -1):
#         for i in range(n):
#             if elements[i] > elements[i + 1]:
#                 swapped = True
#                 # swapping data if the element is less than next element in the array
#                 elements[i], elements[i + 1] = elements[i + 1], elements[i]        
#         if not swapped:
#             # exiting the function if we didn't make a single swap
#             # meaning that the array is already sorted.
#             return
 
# elements = [39, 12, 18, 85, 72, 10, 2, 18]
 
# print("Unsorted list is,")
# print(elements)
# bubblesort(elements)
# print("Sorted Array is, ")
# print(elements)
# 6 Write a program to implement binary-search algorithm
# def binary_search(arr, low, high, x):
 
#     # Check base case
#     if high >= low:
 
#         mid = (high + low) // 2
 
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
 
#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)
 
#     else:
#         # Element is not present in the array
#         return -1
 
# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
 
# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")
# 7 Write a program to take two list of same length as input and return a dictionary with one as keys and other as values.
# index = [1, 2, 3]
# languages = ['python', 'c', 'c++']

# dictionary = dict(zip(index, languages))
# print(dictionary)
#8 Write a program to print fibonocci series using recursion.
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 10

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))
# 9Write a program to find the factorial of a number using recursion.
# Factorial of a number using recursion

# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# num = 7

# # check if the number is negative
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", recur_factorial(num))

# #10 Program to implement concept of decorator to calculate the time needed to execute one or more function in a program.

# def my_decorator(func): 
#     def wrapper_function(*args, **kwargs): 
#         print("*"*10) 
#         func(*args,  **kwargs) 
#         print("*"*10) 
#     return wrapper_function 
  
  
# def say_hello(): 
#     print("Hello Geeks!") 
  
# @my_decorator
# def say_bye(): 
#     print("Bye Geeks!") 
  
  
# say_hello = my_decorator(say_hello) 
# say_hello() 
# say_bye() 
#11 Write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console
# nl=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         nl.append(str(x))
# print (','.join(nl))
#12Write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console
# def my_generator(n):

#     # initialize counter
#     value = 0

#     # loop until counter is less than n
#     while value < n:

#         # produce the current value of the counter
#         yield value

#         # increment the counter
#         value += 1

# # iterate over the generator object produced by my_generator
# for value in my_generator(3):

#     # print each value produced by generator
#     print(value)

#13Write a program to implement Insertion-Sort algorithm in python.
# def insertionSort(array):

#     for step in range(1, len(array)):
#         key = array[step]
#         j = step - 1
        
#         # Compare key with each element on the left of it until an element smaller than it is found
#         # For descending order, change key<array[j] to key>array[j].        
#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j = j - 1
        
#         # Place key at after the element just smaller than it.
#         array[j + 1] = key


# data = [9, 5, 1, 4, 3]
# insertionSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)

#14Program to implement Linear-Search Algorithm.
# def linearSearch(array, n, x):

#     # Going through array sequencially
#     for i in range(0, n):
#         if (array[i] == x):
#             return i
#     return -1


# array = [2, 4, 0, 1, 9]
# x = 1
# n = len(array)
# result = linearSearch(array, n, x)
# if(result == -1):
#     print("Element not found")
# else:
#     print("Element found at index: ", result)

#15Program to implement Selection-Sort Algorithm.
# def selectionSort(array, size):
   
#     for step in range(size):
#         min_idx = step

#         for i in range(step + 1, size):
         
#             # to sort in descending order, change > to < in this line
#             # select the minimum element in each loop
#             if array[i] < array[min_idx]:
#                 min_idx = i
         
#         # put min at the correct position
#         (array[step], array[min_idx]) = (array[min_idx], array[step])


# data = [-2, 45, 0, 11, -9]
# size = len(data)
# selectionSort(data, size)
# print('Sorted Array 

#16 Write a Python program to find the second smallest number in a list using function.
# def find_len(list1):
#     length = len(list1)
#     list1.sort()
#     print("Largest element is:", list1[length-1])
#     print("Smallest element is:", list1[0])
#     print("Second Largest element is:", list1[length-2])
#     print("Second Smallest element is:", list1[1])
 
# # Driver Code
# list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
# Largest = find_len(list1)


