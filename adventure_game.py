import time
import random


def printAndPause(message):
    print(message)
    time.sleep(2)


def intro(item, option):
    printAndPause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    printAndPause("Rumor has it that a " + option + " is somewhere around "
                "here, and has been terrifying the nearby village. ")
    printAndPause("In front of you is a house. ")
    printAndPause("To your right is a dark cave.")
    printAndPause("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")


def cave(item, option):
    if "sward" in item:
        printAndPause(" You peer cautiously into the cave.")
        printAndPause(" You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        printAndPause(" You walk back to the field. ")
    else:
        printAndPause(" You peer cautiously into the cave.")
        printAndPause(" It turns out to be only a very small cave.")
        printAndPause(" Your eye catches a glint of metal behind a "
                    "rock.")
        printAndPause(" You have found the magical Sword of Ogoroth!")
        printAndPause(" You discard your silly old dagger and take "
                    "the sword with you.")
        printAndPause(" You walk back out to the field. ")
        item.append("sward")
    field(item, option)


def house(item, option):
    printAndPause(" You approach the door of the house.")
    printAndPause(" You are about to knock when the door "
                "opens and out steps a " + option + ".")
    printAndPause(" Eep! This is the " + option + "'s house!")
    printAndPause(" The " + option + " attacks you! ")
    if "sward" not in item:
        printAndPause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger. ")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "sward" in item:
                printAndPause(" As the " + option + " moves to attack, "
                            "you unsheath your new sword.")
                printAndPause(" The Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                printAndPause(" But the " + option + "takes one look at "
                            "your shiny new toy and runs away!")
                printAndPause(" You have rid the town of the " + option +
                            ". You are victorious! ")
            else:
                printAndPause(" You do your best...")
                printAndPause("but your dagger is no match for the "
                            + option + ".")
                printAndPause(" You have been defeated! ")
            play_again()
            break
        if choice2 == "2":
            printAndPause(" You run back into the field. "
                        " Luckily, you don't seem to have been "
                        "followed. ")
            field(item, option)
            break


def field(item, option):
    printAndPause("Enter 1 to knock on the door of the house.")
    printAndPause("Enter 2 to peer into the cave.")
    printAndPause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n \n ")
        if choice1 == "1":
            house(item, option)
            break
        elif choice1 == "2":
            cave(item, option)
            break


def play_again():
    again = input("Would you like to play again? (y/n)\n").lower()
    if again == "y":
        printAndPause("Excellent! Restarting the game ...   ")
        play_game()
    elif again == "n":
        printAndPause("Thanks for playing! See you next time.   ")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                            "gorgon"])
    intro(item, option)
    field(item, option)


play_game()