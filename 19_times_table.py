"""
Create a program which will produce the times table for a number entered by the user up to 10 times
eg if the user enters ‘2’ it should produce:
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
4 x 2 = 8
5 x 2 = 10
6 x 2 = 12
7 x 2 = 14
8 x 2 = 16
9 x 2 = 18
10 x 2 = 20
"""


number = input("Enter the number to create the times table for: ")
number = int(number)
for i in range(1, 11):
    print(str(i) + " x " + str(number) + " = " + str(number * i))
#next i


# extension

for i in range(1, 11):
    print("+----+---+----+---+------+")
    formatted_str = str(i)
    if i < 10: formatted_str += " "
    print("| " + formatted_str + " | x | ", end="")
    formatted_number = str(number)
    if number < 10: formatted_number += " "
    print(formatted_number + " | = | ", end="")
    answer = number * i
    formatted_answer = str(number * i)
    if answer < 10:
        formatted_answer += "   "
    elif answer < 100:
        formatted_answer += "  "
    elif answer < 1000:
        formatted_answer += " "
    #end if
    print(formatted_answer + " |")
#next i
print("+----+---+----+---+------+")


# with f strings for A level, we can replace all of the above
# extension code with these lines few lines
# for i in range(1, 11):
#     print("+----+---+----+---+------+")
#     print(f"| {i:<2} | x | {number:<2} | = | {number*i:<4} |")
# #next i