def take_user_input():
    """
    Takes user input for a single letter.

    Returns:
        str: The user input (a single letter).
    """
    while True:
        # Step 2: Ask the user to guess a letter and assign this to a variable called guess.
        guess = input("Enter a single letter: ")

        # Step 3: Check that the guess is a single alphabetical character.
        if len(guess) == 1 and guess.isalpha():
            # Step 4: If the guess passes the checks, break out of the loop.
            break
        else:
            # Step 5: If the guess does not pass the checks, print an error message.
            print("Invalid letter. Please, enter a single alphabetical character.")

    return guess

# Call the function to take user input.
user_guess = take_user_input()

# Print the user's valid guess.
print("User's valid guess:", user_guess)