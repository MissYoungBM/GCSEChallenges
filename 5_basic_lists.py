"""
Make a program that lets a user input a series of names into a list. The program should then ask the user whether they
want to print out the list in the original order, or in reverse.
"""

name: str = ""
names: list = []
while name != "q":
    name = input("Enter a name, or enter q to finish: ")
    if name != "" and name != "q":
        names.append(name)
    #end if
#end while

direction = input("Do you want to print in reverse (y/n): ")
if direction.lower() == "y":
    for i in range(len(names)-1, -1, -1):
        print(names[i])
    #next i
else:
    for i in range(len(names)):
        print(names[i])
    #next i
#end if

