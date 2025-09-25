print("Program starting.\n")
print("Option: ", end="\n" + "1 - Celsius to Fahrenheit\n")
print("2 - Fahrenheit to Celcius",end="\n" + "0 - Exit\n")
ans = int(input("Your choice: "))
if ans == 1:
    cel = round(float(input("Insert the amount of Celsius: ")),1)
    result = (cel * 1.8) + 32
    rresult = round(result,1)
    print(f"{cel} °C equals to {rresult} °F")
elif ans == 2:
    fah = round(float(input("Insert the amout of Fahrenheit: ")),1)
    result = (fah - 32)/1.8
    rresult = round(result,1)
    print(f"{fah} °F equals to {rresult} °C ")
elif ans == 0:
    print("Exiting...")
    print("\nProgram ending.")
else:
    print("Unknown option.")
    

    