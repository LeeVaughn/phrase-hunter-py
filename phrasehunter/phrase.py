class Phrase:
    """
    initializes instance attribute and contains methods to display phrase and check guesses

    initializes phrase attribute
    display method prints the phrase
    check_guess method returns True if phrase contains guess or False if it doesn't
    check_complete method returns True or False based on if all letters in the phrase have been guessed
    """
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end = " ")
            else:
                print("_ ", end = " ")

    def check_guess(self, guess):
        if guess.lower() in self.phrase:
            print("Success!")
            return True
        else:
            print("Sorry, that letter is not in the phrase.")
            return False

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
