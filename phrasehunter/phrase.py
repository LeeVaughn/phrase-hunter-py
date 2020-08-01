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

#* original comments below
# Create your Phrase class logic here.

# Phrase class will store attributes of phrase and methods to display phrase
