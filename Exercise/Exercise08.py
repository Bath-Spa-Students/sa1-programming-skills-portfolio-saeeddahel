# It keeps a sorted list of names that can be retrieved or changed at a later time
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# It saves a particular name for later use, like in a program for comparison or search
target_name = "Sam"

# This code prints a message indicating whether or not the value of target_name ("Sam") was found in the names list
if target_name in names:
    print(f"{target_name} found in the list!")
else:
    print(f"{target_name} not found in the list.")