# will contain the Phrase class and manage individual phrases
class Phrase:
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
            print("True")
            return True
        else:
            print("False")
            return False

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                print("False")
                return False
        print("True")
        return True


#* original comments below
# Create your Phrase class logic here.

# Phrase class will store attributes of phrase and methods to display phrase
