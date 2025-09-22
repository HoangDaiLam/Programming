print("Program starting.")
name = input("WHat is your name: ")
num = float(input("Enter a floating point number: "))
num1 = float(input("Enter second flaoting point number: "))
print(f"{name} you gave numbers {num} and {num1}")
result = num * num1
result1 = round(result,2) 
print(f"Multiplying first and second number will result in product {result1}",end='\n' + "Program ending.")
