# Function to determine if a number is even or odd
def check_even_odd(number):
    # Using the modulus operator, the Python code determines whether a given number is even or odd and outputs the result in a laid out string
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main function
def main():
    # After asking the user to enter a number, this code transforms it into an integer and saves it in the variable `num`
    num = int(input("Enter a number: "))
    
    # With the variable {num` as input, this code invokes the function `check_even_odd`. The result, which is probably a string indicating whether the number is even or odd, is stored in the variable `result`
    result = check_even_odd(num)
    
    # Print the result returned by the function
    print(result)

# Call the main function to run the program
if __name__ == "__main__":
    main()
