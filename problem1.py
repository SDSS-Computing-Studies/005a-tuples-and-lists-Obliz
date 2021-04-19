#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
print("\n======")

myList = ["Alain","Brian","Chris","Justin","Angela","Rick"]
print(myList)

word = str(input("Choose a person from the list to replace: ").strip())
replace = str(input("Enter the replacement: "))

dIndex = myList.index(word)
myList.remove(word)
myList.insert(dIndex, str(replace))

print(myList)