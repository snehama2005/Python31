#1 How do you open a file for reading in python, and what is the purpose of the'r' mode in the open() function ?
# f = open("rain.txt","r")
# print(f.read())
# f=open("C:/Users/C J/Documents/example.txtt","r")
# print(f.read())
# print(f.read())
# print(f.read(2))
# print(f.readline())
# print(f.readline(3))
# print(f.readlines())
# print(f.readlines(3))
# print(f.read())
# print(f.read(2))
# print(f.readline())
# print(f.readline(3))
# print(f.readlines())
# print(f.readlines(3))
#2 How can you read the contents of a file in Python after opening it for reading?
#Open function to open the file "MyFile1.txt"  
# (same directory) in read mode and 
# file1 = open("MyFile.txt", "r") 
   
# store its reference in the variable file1  
# and "MyFile2.txt" in D:\Text in file2 
# file2 = open("D:\Text\MyFile2.txt", "r+") 

#3file1 = open('myfile.txt', 'w')
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# s = "Hello\n"
# filee1.write(s)
 
# # Writing multiple strings
# # at a time
# filee1.writelines(L)
 
# # Closing file
# filee1.close()
 
# # Checking if the data is
# # written to file or not
# filee1 = open('myfile.txt', 'r')
# print(file1.read())
# filee1.close()

#4
# file = open('myfile.txt', 'a')

# # Perform operations on the file (e.g., write or read)

# # Close the file
# file.close()

#5 
# import pandas as pd

# # dictionary of lists
# d = {'Car': ['BMW', 'Lexus', 'Audi', 'Mercedes', 'Jaguar', 'Bentley'],'Date_of_purchase': ['2020-10-10', '2020-10-12', '2020-10-17', '2020-10-16', '2020-10-19', '2020-10-22']
# }

# # creating dataframe from the above dictionary of lists
# dataFrame = pd.DataFrame(d)
# print("DataFrame...\n",dataFrame)

# # write dataFrame to SalesRecords CSV file
# dataFrame.to_csv("C:\Users\amit_\Desktop\SalesRecords.csv")

# # display the contents of the output csv
# print("The output csv file written successfully and generated...")

# 6 
# import csv
# data_list = [["SN", "Name", "Contribution"],
#              [1, "Linus Torvalds", "Linux Kernel"],
#              [2, "Tim Berners-Lee", "World Wide Web"],
#              [3, "Guido van Rossum", "Python Programming"]]
# with open('innovators.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter='|')
#     writer.writerows(data_list)

#7
# try:
    # numerator = 10
    # denominator = 0

    # result = numerator/denominator
# 
    # print(result)
# except:
    # print("Error: Denominator cannot be 0.")
#8 

# try:
    # file1 = open("Myfolder/abc.txt")
 
# except:
    # print("file not found")
#9
# def divide(x, y): 
    # try: 
        # Floor Division : Gives only Fractional
        # Part as Answer 
        # result = x // y 
        # print("Yeah ! Your answer is :", result) 
    # except ZeroDivisionError: 
        # print("Sorry ! You are dividing by zero ") 
#10

# import json 
    
# # Data to be written 
# dictionary ={ 
#     "name" : "sathiyajith", 
#     "rollno" : 56, 
#     "cgpa" : 8.6, 
#     "phonenumber" : "9976770500"
# } 
    
# with open("sample.json", "w") as outfile: 
#     json.dump(dictionary, outfile)


   