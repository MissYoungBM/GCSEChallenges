
print("1. Convert km to miles")
print("2. Convert deg C to deg F")
print("3. Convert kg to lbs")

choice = input("Enter an option: 1, 2 or 3: ")

if choice == "1":
    distance_km: float = float(input("Enter the distance in km: "))
    distance_miles: float = distance_km * 0.621
    print(str(distance_km) + "km is equal to " + str(distance_miles) + " miles")

elif choice == "2":
    degC: int = int(input("Enter temp in degrees C: "))
    degF: float = ((9/5) * degC) + 32
    print(str(degC) + " degrees C is equal to " + str(degF) + " degrees F"
                                                             "")
elif choice == "3":
    weight_kg: int = int(input("Enter the weight in kg: "))
    weight_lbs: float = weight_kg * 2.204

    print(str(weight_kg) + "kg is equal to " + str(weight_lbs) + " lbs")
else:
    print("Invalid option")