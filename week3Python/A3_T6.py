print("Program starting.")
print("Welcome to the unit coverter program!")
print("Follow the menu instructions below.\n")
print("Option:",end="\n" + "1 - Length\n")
print("2 - Weight",end="\n" + "0 - Exit\n")
ans = int(input("Your choice: "))
if ans == 1:
    print("Length options: ",end="\n" + "1 - Meters to kilometers\n")
    print("2 - Kilometers to meters",end="\n" + "0 - Exit\n")
    ans1 = int(input("Your choices: "))
    if ans1 == 1:
        m = round(float(input("Insert meters: ")),1)
        km = m / 1000
        rkm = round(km,1)
        print(f"{m} m is {rkm} km")
        print("\nProgram ending.")
    elif ans1 == 2:
        km = round(float(input("Insert kilometers: ")),1)
        m = km * 1000 
        rm = round(m,1)
        print(f"{km} km is {rm} m")
        print("\nProgram ending.")
    elif ans1 == 0:
        print("Exiting...")
        print("\nProgram ending.")
    else:
        print("Unknown option.")
        print("\nProgram ending.")
elif ans == 2:
    print("Weight options: ",end="\n" + "1 - Grams to pounds\n")
    print("2 - Pounds to grams",end="\n" + "0 - Exit\n")
    ans1 = int(input("Your choices: "))
    if ans1 == 1:
        gr = round(float(input("Insert grams: ")),1)
        p = gr * 0.00220462
        rp = round(p,1)
        print(f"{gr} g is {rp} lb")
        print("\nProgram ending.")
    elif ans1 == 2:
        p = round(float(input("Insert pounds: ")),1)
        gr = p / 0.00220462 
        rgr = round(gr,1)
        print(f"{p} lb is {rgr} g")
        print("\nProgram ending.")
    elif ans1 == 0:
        print("Exiting...")
        print("\nProgram ending.")
    else:
        print("Unknown option.")
        print("\nProgram ending.")
elif ans == 0:
    print("\nExiting...")
    print("\nProgram ending.")
else:
    print("Unknown option.")
    print("\nProgram ending.")




 




