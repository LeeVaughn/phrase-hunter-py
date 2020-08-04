from phrasehunter.phrase import Phrase
import random


class Game:
    """Initializes instance attributes and contains methods for gameplay."""

    def __init__(self):
        """Initializes the instance attributes."""
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = " "

    def start(self):
        """Calls welcome method and continues gameplay until phrase is guessed or player is out of tries."""
        self.welcome()

        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) is False:
            print(f"\nNumber of misses: {self.missed}")
            print(f"You have {5 - self.missed} misses remaining\n")

            self.active_phrase.display(self.guesses)

            print("\n")

            user_guess = self.get_guess()

            # validates player's guess and returns exception if it is not a single letter
            try:
                if len(user_guess) is 1 and user_guess.isalpha():
                    self.guesses = self.guesses + user_guess

                    if not self.active_phrase.check_guess(user_guess):
                        self.missed += 1
                else:
                    raise ValueError()

            except ValueError:
                print("Whoops! That guess is not a valid letter. Please try again...\n")

        self.game_over()
        self.play_again()

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
        """Prompts player for guess and returns it."""
        current_guess = str(input("Guess a letter: "))

        return current_guess

    def game_over(self):
        if self.missed is 5:
            print("\nUh oh! You have run out of guesses. Better luck next time!")
        else:
            print("\nCongratulations! You have guessed all of the letters in the phrase!")

    def play_again(self):
        """Gives the player the option to play again, ends game after three invalid input."""
        attempts = 0

        while attempts < 3:
            try:
                play_again = input("\nWould you like to play again? (Y/N): ")

                if play_again.lower() == "y":
                    game = Game()
                    game.start()
                elif play_again.lower() == "n":
                    print("\nThanks for playing!")
                elif attempts == 2:
                    raise ValueError("Invalid input limit exceeded.")
                else:
                    raise ValueError("Invalid input. Please enter Y or N.")
            except ValueError as err:
                attempts += 1
                print("{}".format(err))
