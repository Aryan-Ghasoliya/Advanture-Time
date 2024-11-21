def start_game():
    print("\nWelcome to the Adventure Game!")
    print("You find yourself in a dark forest. There's a path ahead.")
    print("What will you do?")
    print("1. Follow the path.")
    print("2. Explore the forest.")
    print("3. Climb a tree to look around.")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        follow_path()
    elif choice == "2":
        explore_forest()
    elif choice == "3":
        climb_tree()
    else:
        print("Invalid choice. Try again.")
        start_game()

def follow_path():
    print("\nYou follow the path and come across an old man sitting by the road.")
    print("He offers you a riddle: 'What has roots as nobody sees, is taller than trees, up, up it goes, and yet it never grows?'")
    print("What will you do?")
    print("1. Try to answer the riddle.")
    print("2. Ignore the old man and continue walking.")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        answer_riddle()
    elif choice == "2":
        print("\nYou ignore the old man and continue down the path.")
        print("Unfortunately, you fall into a trap set by bandits! Game over.")
    else:
        print("Invalid choice. Try again.")
        follow_path()

def answer_riddle():
    print("\nWhat is your answer?")
    answer = input("Enter your answer: ").strip().lower()

    if answer == "mountain":
        print("\nThe old man smiles and says, 'Correct!'")
        print("He gives you a magical amulet and points you to a hidden treasure. You win!")
    else:
        print("\nThe old man frowns and says, 'Wrong answer.'")
        print("A trapdoor opens beneath you, and you fall into a pit. Game over.")

def explore_forest():
    print("\nYou wander into the forest and hear a growl.")
    print("A wild wolf appears!")
    print("What will you do?")
    print("1. Fight the wolf.")
    print("2. Run away.")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        fight_wolf()
    elif choice == "2":
        print("\nYou run away safely, but you get lost and can't find your way back. Game over.")
    else:
        print("Invalid choice. Try again.")
        explore_forest()

def fight_wolf():
    print("\nYou decide to fight the wolf.")
    print("Do you:")
    print("1. Use a stick as a weapon.")
    print("2. Try to scare it away by shouting.")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("\nYou bravely fend off the wolf with the stick and manage to escape the forest. You win!")
    elif choice == "2":
        print("\nYour shouting only angers the wolf. It attacks, and you lose. Game over.")
    else:
        print("Invalid choice. Try again.")
        fight_wolf()

def climb_tree():
    print("\nYou climb a tree and see a cabin in the distance.")
    print("What will you do?")
    print("1. Climb down and head to the cabin.")
    print("2. Stay in the tree and wait for help.")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        cabin_scenario()
    elif choice == "2":
        print("\nYou stay in the tree for hours. Eventually, you fall asleep and fall out. Game over.")
    else:
        print("Invalid choice. Try again.")
        climb_tree()

def cabin_scenario():
    print("\nYou arrive at the cabin and knock on the door.")
    print("An old woman answers and offers you shelter.")
    print("Do you:")
    print("1. Accept her offer.")
    print("2. Decline and continue exploring.")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("\nThe old woman turns out to be a witch!")
        print("She traps you in her cabin. Game over.")
    elif choice == "2":
        print("\nYou continue exploring and find your way out of the forest. You win!")
    else:
        print("Invalid choice. Try again.")
        cabin_scenario()

# Start the game
start_game()
