Num1 = 47
Num2 = 102
Sum = int(Num1) + int(Num2)
Diff = int(Num2) - int(Num1)
format = "{0} + {1} = {2}".format(Num1, Num2, Sum)
print(format)
format1 = "{0} - {1} = {2}".format(Num2, Num1, Diff)
print(format1)
product = int(Sum) * int(Diff)
format2 = "(({0}+{1}) * ({1}-{0}) = {2} ".format(Num1, Num2, product)
print(format2)

