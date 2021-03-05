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
people=['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']
print(people)
person1=(input("Choose a person from the list to replace: ").strip())
person2=(input("Enter the replacement: ").strip())
ind=people.index(person1)
people.insert(ind.person2)
print(people)