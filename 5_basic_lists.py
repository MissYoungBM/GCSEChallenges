"""
Make a program that lets a user input a series of names into a list. The program should then ask the user whether they
want to print out the list in the original order, or in reverse.
"""
MAX_ITEMS = 100
total_items: int = 0
names: list = ["" for i in range(MAX_ITEMS)]

name: str = input("Enter a name, or enter q to finish: ")
while name != "q" and total_items < MAX_ITEMS:
    names[total_items]= name
    total_items = total_items + 1
    name = input("Enter a name, or enter q to finish: ")
#end while

direction = input("Do you want to print in reverse (y/n): ")
if direction.lower() == "y":
    for i in range(total_items-1, -1, -1):
        print(names[i])
    #next i
    #alternatively:
    # for i in range(total_items):
    #     print(names[total_items - i - 1])
    #next i
else:
    for i in range(total_items):
        print(names[i])
    #next i
#end if

"""
CONSTANT MAX_ITEMS <-- 100
DECLARE TotalItems, i: INTEGER
DECLARE Name, Direction: STRING
DECLARE Names: ARRAY[1:100] OF STRING

TotalItems <-- 1

OUTPUT "Enter a name, or enter q to finish: "
INPUT Name
WHILE name <> "q" AMD TotalItems < MAX_ITEMS DO
    Names[TotalItems] <-- Name
    TotalItems <-- TotalItems + 1
    
    OUTPUT "Enter a name, or enter q to finish: "
    INPUT Name
END WHILE

OUTPUT "Do you want to print in reverse (y/n): "
INPUT Direction
IF TOLOWER(Direction) = "y" THEN
    FOR i <-- TotalItems TO 1 STEP -1
        OUTPUT Names[i]
    NEXT I
    //alternatively:
    // FOR i = 1 TO TotalItems
    //     OUTPUT Names[TotalItems - i - 1]
    //NEXT i
ELSE
    FOR i <-- 1 TO TotalItems
        OUTPUT Names[i]
    NEXT i
END IF

"""
