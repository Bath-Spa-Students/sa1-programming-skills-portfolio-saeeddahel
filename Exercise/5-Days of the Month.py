#The function get_days_in_month() is defined by this Python code
def get_days_in_month():
    # The `month_days` dictionary is created by this Python code, with each key representing a month number (1–12) and the number of days in that month (accounting for non-leap years) as its corresponding value
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Before exiting, this code asks the user to enter a month number (1–12), determines whether it falls outside of that range, and prints an error message (though return will only work if this code is inside a function)
    try:
        month = int(input("Enter the month number (1-12): "))
        if month < 1 or month > 12:
            print("Invalid month number. Please enter a number between 1 and 12.")
            return
        
        # In order to determine leap year status (printing 28 or 29 days), this code first determines whether the entered month is February (2). If not, it handles non-numeric input errors and displays the days for other months from a predefined list
        if month == 2:
            year = int(input("Enter the year: "))
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print("February in a leap year has 29 days.")
            else:
                print("February has 28 days.")
        else:
            print(f"The month has {month_days[month]} days.")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Run the function
get_days_in_month()
