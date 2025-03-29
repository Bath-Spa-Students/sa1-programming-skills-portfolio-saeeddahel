# The valid password and the maximum number of permitted login attempts are represented by the constants `CORRECT_PASSWORD` (set to `"12345"`) and `MAX_ATTEMPTS` (set to `5`), respectively, defined in this Python code
CORRECT_PASSWORD = "12345"
MAX_ATTEMPTS = 5  

# The variable `attempts`, which is commonly used to track or count the number of tries in a loop or condition, is initialized with the value `0` by this code
attempts = 0

# As long as the value of `attempts` is less than `MAX_ATTEMPTS`, the `while` loop that this code initiates will keep running
while attempts < MAX_ATTEMPTS:
    # This code asks the user for their password and saves it in the `enter_password` variable
    enter_password = input("Enter the password: ")
    
    # If `enter_password` matches `CORRECT_PASSWORD`, this code grants access and ends the loop; if not, it moves on to the next iteration (assuming this is inside a loop like `while`) 

    if enter_password == CORRECT_PASSWORD:
        print("Access granted. Welcome!")
        break  
    else:
        # This code, which is usually used in a loop to track login attempts before locking access, increases the attempts counter by 1 and determines the number of attempts left by subtracting attempts from MAX_ATTEMPTS

        attempts += 1
        remaining_attempts = MAX_ATTEMPTS - attempts
        
        # This code determines how many login attempts are left and, if none are left, either indicates that authorities have been notified or shows the number of tries that are left
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts remaining.")
        else:
            print("Too many failed attempts. Authorities have been alerted!")
