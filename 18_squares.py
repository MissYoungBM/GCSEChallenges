"""
Create a program that will ask the user for a number and then print out a list of numbers from 1 to the number entered
and the square of the number.

For example, if the user entered ‘3’ then the program would output:
1 squared is 1
2 squared is 4
3 squared is 9
"""

number = input("Enter the total number to square: ")
number = int(number)
for i in range(1, number+1):
    print(str(i) + " squared is " + str(i**2))
#next i
