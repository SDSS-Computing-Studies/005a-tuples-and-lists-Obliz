#!python3

"""
Create a LIST that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

inputs:
integer number

outputs:
string animal

example:
Enter the index for an animal:2
The animal at that index is Dog
"""



<<<<<<< HEAD
animals =["Mouse","Frog","Dog","Cow","Chicken"]


index = input("Enter the index for an animal:")

if int(index) == 0:
    print("The animal at that index is ", animals[0])

elif int(index) == 1:
    print("The animal at that index is ", animals[1])

elif int(index) == 2:
    print("The animal at that index is ", animals[2])

elif int(index) == 3:
    print("The animal at that index is ", animals[3])

else:
    print("The animal at that index is ", animals[4])


