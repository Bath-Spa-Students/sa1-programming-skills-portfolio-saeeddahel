# The user gets asked to enter their name by this Python code, which then saves the input in the variable `name`
name = input("Write your name: ")

# The user gets asked to enter their age by this Python code, which then saves the result as a string in the variable `age`
age = input("Write your age: ")

# The user is prompted by this Python code to enter their hometown, which is then stored as a string in the variable `hometown`
hometown = input("Write your hometown: ")

# In order to store the corresponding values from the variables `name`, `age`, and `hometown`, this Python code generates a dictionary called `name_dictionary` with keys "name", "age", and "hometown"
name_dictionary = {"name": name, "age": age, "hometown": hometown}

# Print the dictionary containing the user's details
print(name_dictionary)
