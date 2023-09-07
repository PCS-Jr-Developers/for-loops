# Initialize a flag to control the loop
valid_input = False

# Keep asking for input until a valid positive number is entered
while not valid_input:
    # Ask the user for input
    user_input = input("Please enter a positive number: ")
    
    # Check if the input consists of digits only
    if user_input.isdigit():
        # Convert the input to an integer
        number = int(user_input)
        
        # Check if the number is positive
        if number > 0:
            valid_input = True  # Set the flag to exit the loop
            print("Thank you!")  # Positive number entered
        else:
            print("That's not a positive number. Try again.")
    else:
        print("That's not a valid number. Try again.")
