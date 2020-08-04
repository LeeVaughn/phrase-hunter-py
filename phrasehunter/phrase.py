class Phrase:
    """Initializes instance attribute and contains methods to display phrase and check guesses."""

    def __init__(self, phrase):
        """Initializes the instance attribute."""
        self.phrase = phrase.lower()

    def display(self, guesses):
        """Prints the phrase"""
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end = " ")
            else:
                print("_ ", end = " ")

    def check_guess(self, guess):
        """Returns True if phrase contains guess or False if it doesn't."""
        if guess.lower() in self.phrase:
            print("Success!")
            return True
        else:
            print("Sorry, that letter is not in the phrase.")
            return False

    def check_complete(self, guesses):
        """Returns True or False based on if all letters in the phrase have been guessed."""
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
