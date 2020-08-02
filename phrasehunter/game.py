from phrasehunter.phrase import Phrase
import random

# will contain the Game class and manage the game functionality
# will contain methods to show the game, handle interactions, and check when the game is over
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = " "

    def start(self):
        self.welcome()

        print(f"\nNumber of misses: {self.missed}\n")

        self.active_phrase.display(self.guesses)

        print("\n")

        user_guess = self.get_guess()
        self.guesses = self.guesses + user_guess
    
    def welcome(self):
        # print("\n=======================================")
        # print("\n       Welcome to Phrase Hunter!")
        # print("\n   Guess all of the letters and win.")
        # print("\n              Good luck!")
        # print("\n=======================================")
        print("""
        =======================================

               Welcome to Phrase Hunter!

           Guess all of the letters and win.

                      Good luck!

        =======================================
        """)
    
    def create_phrases(self):
        return [
            Phrase("My precious"),
            Phrase("All righty then"),
            Phrase("Show me the money"),
            Phrase("I see dead people"),
            Phrase("That escalated quickly")
            ]

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def get_guess(self):
        try:
            current_guess = str(input("Guess a letter: "))
        except ValueError:
            print("Sorry! That guess is not a valid letter. Please try again...\n")

        return current_guess

#* original comments below
# Create your Game class logic in here.

# game class will manage things like starting the game, handling interactions, getting random phrase, checking win/loss and removing lives

# at the beginning of the the player will see the number of words and letters in the phrase represented by underscores
# players will input a guess
# once a correct letter is guessed it cannot be guessed again
# if letter is in the phrase the _ will be replaced in all positions by the letter
# if letter is not in the phrase the player will lose a life
# play continues until the player has guessed all of the letters or run out of lives
