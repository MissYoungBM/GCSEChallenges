"""
Make a program that asks the user for a series of numbers until they either want to output the average or quit the
program.
"""

total: int = 0
count: int = 0

response: str = input("Enter a number (or q to quit or a to print average): ")
while response.lower() != "q" and response.lower() != "a":
    # assume valid number input
    value = int(response)
    total += value
    count += 1
    response = input("Enter a number (or q to quit or a to print average): ")
# end while

if response.lower() == "a":
    average = total / count
    print("The average is " + str(average))
#end if
