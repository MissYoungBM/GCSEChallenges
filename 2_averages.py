"""
Make a program that asks the user for a series of numbers until they either want to output the average or quit the
program.
"""

total = 0
count = 0
response = ""

while response.lower() != "q":
    response = input("Enter a number (or q to quit): ")
    if response.lower() != "q":
        if response.isnumeric():
            value = int(response)
            total += value
            count += 1
        else:
            print("You need to enter a whole number or q\n")
        # end if
    # end if
# end while

average = total / count
print("The average is " + str(average))
