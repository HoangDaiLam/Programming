print("Program starting.")
print("String comparisons")
wordfirst = input("Insert first word: ").strip()
character = input("insert a character: ")
if character in wordfirst:
    print(f"Word \"{wordfirst}\" contains character \"{character}\".")
else:
    print(f"Character not being contained by {wordfirst}.")
wordsecond = input("Insert second word: ")
if (wordfirst > wordsecond):
    print(f"The first word \"{wordfirst}\" is before the first word \"{wordsecond}\" alphabetically.")
elif (wordsecond > wordfirst):
    print(f"The first word \"{wordsecond}\" is before the first word \"{wordfirst}\" alphabetically.\n")

print("Program ending.")