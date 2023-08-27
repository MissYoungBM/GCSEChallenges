"""
Write a program that lets the user input a list of numbers. Every time they input a new number, the program should give
a message about what the maximum and minimum numbers in the list are.
"""

number = ""
max_value = -999999999999999999  # the initial max value should be the smallest possible number. Can use float("-inf")
min_value = 999999999999999999  # the initial min value should be the largest possible number. Can use float("inf")

while number != "q":
    number = input("Enter a number: ")
    # this does not do error checking, but it allows negative numbers
    value = int(number)
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value
    # end if
    print("The current maximum is " + str(max_value) + " and the minimum is " + str(min_value))
#end while

# with error checking:

# while number != "q":
#     try:
#         number = input("Enter a number: ")
#         value = int(number)
#         if value > max_value:
#             max_value = value
#         if value < min_value:
#             min_value = value
#         # end if
#         print("The current maximum is " + str(max_value) + " and the minimum is " + str(min_value))
#     except:
#         print("not a valid number")
#     #end try
# #end while



