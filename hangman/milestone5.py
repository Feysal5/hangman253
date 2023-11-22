'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}
        word_index = random.randint(0, len(word_list)-1)
        self.word = word_list[word_index]
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = []

        print(f"The mystery word has {len(self.word)} characters")
        print(f"{self.word_guessed}")

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        
        #convert letter inputted and original word into lower case
        letter = str.lower(letter)
        word_lower = str.lower(self.word)
        letter_count = word_lower.count(letter)

        #replace the '_' in word_guessed list with the letter, use index() method from string class
        if letter_count == 1:
            letter_index = word_lower.index(letter)
            self.word_guessed[letter_index] = letter
            
            #reduce number of unique letters num_letters by one
            self.num_letters -= 1

            #print updates
            print(f'Nice! {letter} is in the word!')
            print(f'{self.word_guessed}')
        
        elif letter_count > 1:   
            letter_indices = []

            #find first occurance of letter
            letter_index = word_lower.index(letter)
            letter_indices.append(letter_index)
            count = 1

            while count < letter_count:
                letter_index = word_lower.index(letter, letter_indices[-1]+1)
                letter_indices.append(letter_index)
                count += 1

            for i in letter_indices:
                self.word_guessed[i] = letter
            
            #reduce number of unique letters num_letters by one
            self.num_letters -= 1

            #print updates
            print(f'Nice! {letter} is in the word!')
            print(f'{self.word_guessed}')

        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word.')
            print(f'You have {self.num_lives} lives left.')


    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method
        
        while True:
            letter = input("Please enter a letter: ")
            if len(letter) != 1:
                print("Please, enter just one character")
                continue
            elif letter in self.list_letters:
                print(f"{letter} was already tried")
                continue
            self.list_letters.append(str.lower(letter))
            self.check_letter(letter)
            break

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    # TODO 1: To test this task, you can call the ask_letter method

    #game.ask_letter()

    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # this has been tested and is acting as expected.
    
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    #game.ask_letter()

    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations! You won!"
    # If the user runs out of lives, print "You lost! The word was {word}" *discrepency with test wanting "You ran out of lives"

    while game.num_lives > 0 and game.word_guessed.count('_') > 0:
        game.ask_letter()
    
    if game.num_lives == 0:
        print(f"You ran out of lives. The word was {game.word}")

    if game.word_guessed.count('_') == 0:
        print("Congratulations, you won!")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
