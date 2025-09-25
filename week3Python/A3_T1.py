print("Program starting.")
print("Insert two intergers" )
x = int(input("Insert first interger: "))
y = int(input("Insert second integer: "))
if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is equal to {y}")
print("Adding intergers together.")
sum = x + y
print(f"{x} + {y} = {sum}")
print("Checking the parity of the sum...")
if sum % 2 == 0:
    print(f"{sum} is even")
elif sum % 2 !=0:
    print(f"{sum} is odd")
print("Program ending.")



 
    
    
