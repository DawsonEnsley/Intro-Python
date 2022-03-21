import time
import random
items = []
# option1 = ["1", 1, "yes", "y"]
# option2 = ["2", 2, "no", "n"]
beasts = ["Griffin", "Dragon", "Wyvern", "Basilisk"]
monster = random.choice(beasts)


def print_sleep(print_pause):
    print(print_pause)
    time.sleep(1)


def intro(items):
    print_sleep("After a long journey through the countryside, \n"
                "you find some shade underneath a great oak where "
                "you take a short rest.")
    print_sleep("You awake to gather your things, and you can't help but "
                "notice the faint scent of lilac and gooseberries.")
    print_sleep(f"Rumor has it that a terrible {monster} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_sleep("In front of you is an abandoned church.")
    print_sleep("To your right is a murky lake.")
    print_sleep("In your hand you wield an old rusty sword")
    items.append("rusty")


def fight_or_flight(items):
    if "rusty" in items:
        print_sleep("You feel a bit under-prepared for this, while"
                    " only carrying a rusty sword.")
    pick = valid_inputstr("Would you like to (1) fight or (2) run away?",
                          "1", "2")
    if pick == "1":
        fight(items)
    if pick == "2":
        flight(items)


def church(items):
    print_sleep("You carefully approach the church's front door.")
    print_sleep(f"You are just about to knock when it flies open instead "
                f"and out steps a {monster}.")
    print_sleep(f"This church must have the {monster}'s nest inside!")
    print_sleep(f"The {monster} takes a swipe at you!")
    fight_or_flight(items)


def lake(items):
    print_sleep("You cautiously step to the edge of the embankment.")
    if "rusty" in items:
        print_sleep("It appears to quite faint, but there is something "
                    "in the center, between the thick of the fog.")
        print_sleep("Your eye catches a glint of metal in the middle of a"
                    " pool of water.")
        print_sleep("You have found Aerondight! A sword of Legend!")
        items.append("silver")
        items.remove("rusty")
        print_sleep("You discard your rusty old sword and take the "
                    "surprisingly shiny new one with you.\n")
    if "silver" in items:
        print_sleep("There is nothing more to do here.")
    print_sleep("You head back to the oak tree.")
    decision(items)


def valid_inputstr(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_sleep("Sorry, I don't understand.")
    return response

# def valid_inputint(prompt, option1, option2):
#     while True:
#         response = input(prompt)
#         try:
#             if int(response) == 1:
#                 break
#             elif int(response) == 2:
#                 break
#             else:
#                 print_sleep("Enter either 1 or 2:")
#         except:
#             print_sleep("Sorry, I don't understand. Try again.")


def decision(items):
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to make your way to the lake.")
    print_sleep("What would you like to do?")
    choice = valid_inputstr("(Please enter 1 or 2.)", "1", "2")
    if choice == "1":
        church(items)
    if choice == "2":
        lake(items)


def fight(items):
    if "rusty" in items:
        print_sleep("You do your best...")
        print_sleep(f"but your rusty sword is no match for a {monster}.")
        print_sleep("You have been defeated!")
        play_again()
    elif "silver" in items:
        print_sleep(f"As the {monster} comes back for another attack,")
        print_sleep("You unsheathe Aerondight, your new sword.")
        print_sleep(f"The {monster} quickly swoops down for it's attack,")
        print_sleep("it has remarkable speed... but you are faster.")
        print_sleep(f"In a flash just as bright as the sun,")
        print_sleep("the mighty {monster} falls to the ground.")
        print_sleep("You victoriously stand over the felled beast unharmed.")
        print_sleep(f"You have rid the nearby town of the {monster}.")
        play_again()


def flight(items):
    print_sleep("You quickly run back to the oak tree.")
    print_sleep("Luckily, you don't seem to have been pursued.")
    decision(items)


def play_game():
    items = []
    intro(items)
    # options()
    decision(items)


def play_again():
    print_sleep("Would you like to play again?")
    play = valid_inputstr("(Y/N)", "y", "n")
    if "y" in play:
        play_game()
    if "n" in play:
        print_sleep("Thanks for playing! See you next time!")


play_game()
