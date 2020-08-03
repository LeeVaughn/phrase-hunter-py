from phrasehunter.phrase import Phrase
import random


class Game:
    """
    initializes the instance attributes and contains methods for gameplay

    initializes the instance attributes
    start method calls welcome method and continues gameplay until phrase is guessed or player is out of tries
    welcome method prints welcome message
    create_phrases method returns five Phrase objects
    get_random_phrase method returns a random Phrase object
    get_guess method prompts player to guess a letter
    game_over method prints a win or loss message based on number of misses
    """
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = " "

    def start(self):
        self.welcome()

        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) is False:
            print(f"\nNumber of misses: {self.missed}")
            print(f"You have {5 - self.missed} misses remaining\n")

            self.active_phrase.display(self.guesses)

            print("\n")

            user_guess = self.get_guess()
            self.guesses = self.guesses + user_guess

            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1

        self.game_over()

    def welcome(self):
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

    def game_over(self):
        if self.missed is 5:
            print("Sorry, you have run out of guesses. Better luck next time!")
        else:
            print("Congratulations! You have guessed all of the letters in the phrase!")
