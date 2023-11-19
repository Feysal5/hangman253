# milestone_2.py

import random

def generate_random_word():
    """
    Generates a random word from the given word_list.

    Returns:
        str: A randomly chosen word from the word_list.
    """
    # Step 1: Create a list containing the names of your 5 favorite fruits.
    word_list = ["Apple", "Orange", "Banana", "Grapes", "Mango", "Melon"]

    # Step 2: use for loop to print list of items in word_list.
    for fruit in word_list:
        print(fruit)

    # Step 3: Use random.choice to get a random word.
    word = random.choice(word_list)

    # Step 4: Print out the selected random fruit.
    print("Selected random fruit:", word)

    return word


def take_user_input():
    """
    Takes user input for a single letter.

    Returns:
        str: The user input (a single letter).
    """
    # Step 1: Using the input function, ask the user to enter a single letter.
    guess = input("Enter a single letter: ")

    # Step 2: Validate the input.
    if len(guess) == 1 and guess.isalpha():
        # Step 3: Print a message for a valid input.
        print("Good guess!")
    else:
        # Step 4: Print a message for an invalid input.
        print("Oops! That is not a valid input.")

    # Return the user input regardless of validation.
    return guess

# Call the function to generate a random word.
random_word = generate_random_word()

# Call the function to take user input.
user_guess = take_user_input()

# Print the user's guess.
print("User's guess:", user_guess)