"""
Allow a user to select from a menu of three conversion types:
km to miles - 1km = 0.621 miles (approximately)
deg C to deg F - F = (9/5)C + 32
kg to lbs - 1kg = 2.204lb (approximately)

When the user has selected the conversion type, ask them to enter the value to convert and display the conversion

eg. user selects km to miles:

Enter the value to convert? 5
5 km is 3.1 miles
"""

print("Menu")
print("1. Convert km to miles")
print("2. Convert deg C to deg F")
print("3. Convert kg to lbs")

choice = input("Select the conversion type (1,2,3): ")
value_string = input("Enter the value to convert: ")
initial_value = int(value_string)

converted_value = 0.0
output_string = ""

if choice == "1":
    converted_value = initial_value * 0.621
    output_string = str(converted_value) + " miles"
elif choice == "2":
    converted_value = ((9/5) * initial_value) + 32
    converted_value = round(converted_value, 2)
    output_string = str(converted_value) + " deg F"
elif choice == "3":
    converted_value = initial_value * 2.204
    output_string = str(converted_value) + " lbs"
else:
    print("Invalid choice")
#end if

if output_string != "":
    print(output_string)
#end if
