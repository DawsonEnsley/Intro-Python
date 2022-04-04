# class Dog:
#     scientific_name = "Canis lupus familiaris"
#
#     def __init__(self, name):
#         self.name = name
#         self.bark = 0
#
#     def speak(self):
#         print("Woof!")
#
#     # def learn_name(self, name):
#     #     self.name = name
#
#     def hear(self, words):
#         if self.name in words:
#             self.speak()
#
#     def count(self):
#         self.bark += 1
#         for count in range(self.bark):
#             self.speak()
#         # self.count += 1
#         # if self.count < 1:
#         #     print("Woof!")
#         # elif self.count > 1:
#         #     print("Woof!") * int(self.count)
#
#     def eat(self, food):
#         if food == "treat":
#             print("Yummy!")
#         else:
#             print("That's not a treat!")
#
#
# class Husky(Dog):
#     origin = "Siberia"
#
#     def speak(self):
#         print("Awoooo!")
#
#
# class Chihuahua(Dog):
#     origin = "Mexico"
#
#     def speak(self):
#         print("Yip!")
#
#
# class Collie(Dog):
#     origin = "Scotland"
#
#     def speak(self):
#         print("Bark")
#
#
# class DogPark:
#     def __init__(self, dogs):
#         self.dogs = dogs
#
#     def roll_call(self):
#         print("Dogs in the Park:")
#         for dog in self.dogs:
#             print(f"    {dog.name}")
#         print()
#
#     def shout(self, words):
#         for dog in self.dogs:
#             dog.hear(words)
#
#     def converse(self):
#         self.roll_call()
#         while True:
#             words = input("Talk to doggos! ('quit' to quit) > ")
#             if "quit" in words:
#                 print("Bye")
#                 break
#             else:
#                 # The shout method is used here.
#                 self.shout(words)
#
#
# if __name__ == "__main__":
#     dogs = [main.Husky(f"{self.name}"),
#             main.Chihuahua(f"{self.name}"),
#             main.Collie(f"{self.name}")]
#     park = DogPark(dogs)
#     park.converse()
# class Cat:
#
#     def __init__(self):
#         self.mood = "Neutral"
#
#     def speak(self):
#         if self.mood == "happy":
#             print("Purrr")
#         elif self.mood == "angry":
#             print("Hiss!")
#         else:
#             print("Meow!")
# class BigOrangeTurtle(turtle.Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("orange")
#         self.width(10)

import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    player_score = 0
    computer_score = 0

    def __init__(self):
        self.p1_move = None
        self.p2_move = None

    def learn(self, p1_move, p2_move):
        self.p1_move = p1_move
        self.p2_move = p2_move

    # def move(self):
    #     return 'rock'


class AlwaysRockPlayer(Player):
    def move(self):
        return "rock"


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.opponents = "Human"

    def move(self):
        while True:
            throw = input("CHOOSE YOUR WEAPON: "
                          "(Rock / Paper / Scissors\n").lower()
            if throw in moves:
                return throw
            else:
                print("I'm Sorry. I didn't quite catch that.")


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        if self.p2_move is None:
            return random.choice(moves)
        else:
            return self.p2_move


class CyclePlayer(Player):
    def move(self):
        if self.p1_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.p1_move) + 1
            if index == len(moves):
                index = 0
            return moves[index]


def p1_beats(move1, move2):
    return ((move1 == 'rock' and move2 == 'scissors') or
            (move1 == 'scissors' and move2 == 'paper') or
            (move1 == 'paper' and move2 == 'rock'))


def p2_beats(move1, move2):
    return ((move1 == 'rock' and move2 == 'paper') or
            (move1 == 'paper' and move2 == 'scissors') or
            (move1 == 'scissors' and move2 == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player_score = 0
        self.computer_score = 0

    # def p1_beats(self, move1, move2):
    #     return ((move1 == 'Rock' and move2 == 'Scissors') or
    #             (move1 == 'Scissors' and move2 == 'Paper') or
    #             (move1 == 'Paper' and move2 == 'Rock'))
    #
    # def p2_beats(self, move1, move2):
    #     return ((move1 == 'Rock' and move2 == 'Paper') or
    #             (move1 == 'Paper' and move2 == 'Scissors') or
    #             (move1 == 'Scissors' and move2 == 'Rock'))
    def match_results(self):
        print(" Who is the Winner? \n")
        if self.player_score > self.computer_score:
            print(" Player 1 has won the match!")
        elif self.player_score < self.computer_score:
            print(" Player 2 has won the match!")
        else:
            print(" Neither Player won. Try Again.")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if p1_beats(move1, move2):
            self.player_score += 1
            print(" You Win this Round! \n")
        elif p2_beats(move1, move2):
            self.computer_score += 1
            print(" You Lose this Round! \n")
        else:
            print(" It's a Tie. Try Again. \n")
            self.computer_score += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Player 1: {self.player_score} | "
              f"Player 2: {self.computer_score}")
        # print(" What's the Score? \n")
        # print(f"Player 1: {score1} | Player 2: {score2}")

    def play_game(self):
        print("Ready Your Weapon!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        self.match_results()
        print("GAME OVER!\n")

    def p1_beats(self, move1, move2):
        pass

    def p2_beats(self, move1, move2):
        pass


if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']
    opponents = {
        "repeat": AlwaysRockPlayer(),
        "human": HumanPlayer(),
        "reflect": ReflectPlayer(),
        "random": RandomPlayer(),
        "cycle": CyclePlayer()
    }

    while True:
        print("Let's Play Rock, Paper, Scissors!\n")
        print("The rules are as follows:"
              "Rock breaks Scissors. "
              "Paper covers Rock. "
              "Scissors cuts Paper")
        choice = input(
            "Who will you be playing against?\n"
            "(Repeat / Human / Reflect / Random / Cycle)").lower()
        if choice in opponents:
            game = Game(opponents["human"], opponents[choice])
            game.play_game()
        else:
            print("I'm Sorry. I didn't quite catch that.")
