from phrasehunter.phrase import Phrase
import random

# will contain the Game class and manage the game functionality
# will contain methods to show the game, handle interactions, and check when the game is over
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("My precious"),
            Phrase("All righty then"),
            Phrase("Show me the money"),
            Phrase("I see dead people"),
            Phrase("That escalated quickly")
            ]
        self.active_phrase = None
        self.guesses = " "

    def get_random_phrase(self):
        return random.choice(self.phrases)

#* original comments below
# Create your Game class logic in here.

# game class will manage things like starting the game, handling interactions, getting random phrase, checking win/loss and removing lives

# at the beginning of the the player will see the number of words and letters in the phrase represented by underscores
# players will input a guess
# once a correct letter is guessed it cannot be guessed again
# if letter is in the phrase the _ will be replaced in all positions by the letter
# if letter is not in the phrase the player will lose a life
# play continues until the player has guessed all of the letters or run out of lives
