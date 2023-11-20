import random

def generate_random_word():
    word_list = ["Apple", "Orange", "Banana", "Grapes", "Mango", "Melon"]
    for fruit in word_list:
        print(fruit)
    word = random.choice(word_list)
    print("Selected random fruit:", word)
    return word

def check_guess(guess, word):
    """
    Checks if the guessed letter is in the secret word.

    Args:
        guess (str): The guessed letter.
        word (str): The secret word.

    Returns:
        bool: True if the guess is in the word, False otherwise.
    """
    # Step 2: Convert the guess into lower case.
    guess = guess.lower()

    # Step 3: Move the code that checks if the guess is in the word into this function block.
    if guess in word.lower():
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

def ask_for_input():
    """
    Takes user input for a single letter and checks if it is in the secret word.

    Returns:
        str: The user input (a single letter).
    """
    while True:
        # Step 2: Move the code that checks if the input is a valid guess into this function block.
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call the check_guess function to check if the guess is in the word.
            check_guess(guess, random_word)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    return guess

# Call the function to generate a random word.
random_word = generate_random_word()

# Call the function to ask for user input and check if the guess is in the word.
user_guess = ask_for_input()

# Print the user's valid guess.
print("User's valid guess:", user_guess)