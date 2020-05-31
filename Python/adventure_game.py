import time
import random


def print_pause(text):
    print(text)
    time.sleep(2)


def intro():
    global cave_visited
    cave_visited = False
    global weapon
    weapon = False
    print_pause("You find yourself standing in a village in twilight hours, " +
                "the sky is filled with shining stars.")
    print_pause("Rumor has it that the villagers have been experiencing " +
                "very strange activities lately.")
    global monster
    monster = random.choice(['Vampire', 'Dragon', 'Wearwolf', 'Gorgon',
                            'Dracula', 'Cannibal'])
    print_pause("Villagers are really terrified because of recent " +
                "missing persons who dissapeard mysteriously")
    print_pause("Witnesses have spoken about sightings of a " +
                monster + "!!!")
    print()
    print_pause("You have a very strange looking house infront of you " +
                "a cave to the left")


def house():
    print_pause("You have knocked the door")
    print_pause("There is no response")
    print_pause("Suddenly the door opens and a " + monster + " attacks you")
    print()
    if weapon:
        print_pause("You move backward and encouters his attack")
        print_pause("You take out your " + armament + ' and attack it back')
        print_pause("You won!")
        print()
        play_again()
    else:
        print_pause("You try it save your life and run")
        print_pause("Unfortunately, you wasnt able to outrun it")
        print_pause("You lose")
        print()
        play_again()


def run():
    print_pause("You turn around and walk towards your car")
    print_pause("You see something coming towards you from the jungle !!!")
    print_pause("You start running !")
    print_pause("You were too slow\nA " + monster +
                " attacks you and you are defeated")
    print()
    play_again()


def cave():
    global cave_visited
    global weapon
    if cave_visited:
        print_pause("You have already checked the cave")
        print_pause("There is nothing new here")
        print_pause("You come out of the cave")
        print()
        home()
    else:
        print_pause("You carefully enter into the cave")
        print_pause("The cave is filled with darkness")
        print_pause("Fortuntely, you have a torch")
        global armament
        armament = random.choice(['shotgun', 'ballista', "silver sowrd"])
        print_pause("When you turn on your torch, you see there is a " +
                    armament+" available")
        print_pause("You picked it up for your defense")
        print_pause("You come out of the cave")
        print()
        weapon = True
        cave_visited = True
        home()


def home():
    print_pause("Enter 1 to knock on the door of house")
    print_pause("Enter 2 to check the cave")
    print_pause("Enter 3 to go back to your home")
    print_pause("What would you like to do?")
    choice = 0
    while choice != '1' and choice != '2' and choice != '3':
        choice = input()
    if choice == '1':
        house()
    elif choice == '2':
        cave()
    else:
        run()


def play_again():
    option = input("Do you want to play again? (y/n)").lower()
    if option == 'y':
        print_pause("Great, Restarting your Game!")
        play_game()
    elif option == 'n':
        print("Goodbye!")


def play_game():
    intro()
    home()


play_game()
