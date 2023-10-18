# #1 Write a program to implement all built-in methods of list

# # Adds List Element as value of List.
# List = ['Mathematics', 'chemistry', 1997, 2000]
# List.append(20544)
# print(List)

# List = ['Mathematics', 'chemistry', 1997, 2000]
# # Insert at index 2 value 10087
# List.insert(2, 10087)
# print(List)
# #sum
# List = [1, 2, 3, 4, 5]
# print(sum(List))
# #count
# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# print(List.count(1))
# #len
# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# print(len(List))
# #index
# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# print(List.index(2))
# #min
# numbers = [5, 2, 8, 1, 9]
# print(min(numbers))
# #max
# numbers = [5, 2, 8, 1, 9]
# print(max(numbers))
# #pop
# List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
# print(List.pop())
# #delete
# List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
# del List[0]
# print(List)
# #remove
# List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
# List.remove(3)
# print(List)
# #2 write a program tofind the sum of all elements in a list

# # Python program to find sum of elements in list
 
# total = 0
 
# # creating a list
# list1 = [11, 5, 17, 18, 23]
 
# # Iterate each element in list
# # and add them in variable total
# for ele in range(0, len(list1)):
#     total = total + list1[ele]
 
# # printing total value
# print("Sum of all elements in given list: ", total)
# #3 write a program to list comprehension

# numbers = [1, 2, 3, 4, 5]
# squared = [x ** 2 for x in numbers]
# print(squared)
# #4 write a program to find largest and smallest element from a list
# def find_len(list1):
#     length = len(list1)
#     list1.sort()
#     print("Largest element is:", list1[length-1])
#     print("Smallest element is:", list1[0])
    
 
# # Driver Code
# list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
# Largest = find_len(list1)
# #5write python program to print the numbers of specified list after removing even number from it

# # Python program to print Even Numbers in a List
 
# # list of numbers
# # list1 = [10, 21, 4, 45, 66, 93]
 
# # # iterating each number in list
# # for num in list1:
 
# #     # checking condition
# #     if num % 2 == 0:
# #         print(num, end="")
#  #8 write a program to iterate over two lists simultaneously
# num = [1, 2, 3]
# color = ['red', 'white', 'black']
# for (a,b) in zip(num, color):
    #  print(a, b)
#8 Write a Python program to generate and print a list of first and last 5 elements where the values

l = list()
for i in range(11,25):
	l.append(i**2)
print(l[:5])
print(l[-5:])