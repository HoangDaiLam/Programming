print("Program starting.")
fullword = input()
lastword = fullword[-1]
reversedword = fullword[::-1]
print(f"The word you inserted is \'{fullword}\'",end="")
print(f" and in reverse it is \'{reversedword}\'.")
print("The inserted word length is", len(fullword))
print(f"Last character is \'{lastword}\'")
print('Take substring from the inserted word by inserting...')
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
sliced = fullword[start:end:step]
print(f"The word \'{fullword}\' sliced to the defined substring is \'{sliced}\'. ")
print("Program ending.")
