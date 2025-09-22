print("Calculate fuel consumtion")
Feed = float(input("Enter travel distance(kilometers): "))
Distance = round(Feed)
Feed1 = float(input("Enter fuel usage(liters): "))
FuelUsage = round(Feed1)
Consumption = (FuelUsage/Distance) * 100
Consumption1 = round(Consumption)
print(f"Fuel comsumption is {Consumption} per 100km")