# will contain the main logic for the app
# from /phrasehunter import game
# from /phrasehunter import phrase
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase

if __name__ == '__main__':
    # # tests step 2
    # newPhrase = Phrase()
    # newGame = Game()

    # # tests step 3
    # phrase = Phrase("Life is like a box of chocolates")
    # print(phrase.phrase)

    # # tests step 4
    # game = Game()
    # for phrase in game.phrases:
    #     print(phrase.phrase)

    # # tests step 5
    # def print_phrase(phrase_object):
    #     print(f"the phrase is: {phrase_object.phrase}")

    # game = Game()
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())

    # # tests step 6
    # game = Game()
    # print(game.active_phrase)
    # print(game.active_phrase.phrase)
    
    # # tests step 7
    # game = Game()
    # print(game.active_phrase.phrase)
    # game.active_phrase.display(game.guesses)

    # # tests step 8
    # game = Game()
    # game.welcome()

    # # tests step 9 and beyond
    # game = Game()
    # print(game.active_phrase.phrase)
    # game.start()

    # tests step 10 and beyond
        # tests step 9 and beyond
    game = Game()
    game.start()


#* original comments below
# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
