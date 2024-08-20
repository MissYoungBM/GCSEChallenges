# coin_values = [100, 50, 20, 10, 5]
# cost = int(input("Enter the cost in cents: "))
# tendered = int(input("Enter the amount tendered in cents: "))
# total_change = tendered - cost
# print("The total change is " + str(total_change))
# change = total_change
# i = 0
# while change > 0:
#     coin_value = coin_values[i]
#     total_of_coins = change // coin_value
#     if total_of_coins  != 0:
#          print(str(coin_value) + " x " + str(total_of_coins))
#     #end if
#     change = change % coin_value
#     i = i + 1
# #end while

def HEX(val):
    return "A"

number = int(input("Enter a number between 0 and 255"))
while number >= 0 and number <= 255:
    print("Invalid number, try again: Enter a number between 0 an 255: ")
    number = int(input("Enter a number between 0 and 255"))
#end while
total_16s = number // 16
total_1s = number % 16
if total_16s > 9:
    digit1 = HEX(total_16s)
else:
    digit1 = str(total_16s)
#end if
if total_1s > 9:
    digit2 = HEX(total_1s)
else:
    digit2 = str(total_1s)
#end if
hex_number = digit1 + digit2