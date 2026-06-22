import random

suspects = [
    {
        "name": "Ava",
        "age": 31,
        "occupation": "baker",
        "alibi": "I was baking pastries in the kitchen when the murder happened.",
        "clue": "I saw someone with flour on their shoes near the garden.",
        "is_murderer": False,
    },
    {
        "name": "Ben",
        "age": 38,
        "occupation": "gardener",
        "alibi": "I was trimming the hedges outside. I heard a scream and ran inside.",
        "clue": "The rope in the shed was cut recently.",
        "is_murderer": False,
    },
    {
        "name": "Claire",
        "age": 27,
        "occupation": "artist",
        "alibi": "I was painting in my studio all afternoon.",
        "clue": "My paintbrushes were moved while I was away from the studio.",
        "is_murderer": False,
    },
]


def create_game():
    game_suspects = [suspect.copy() for suspect in suspects]
    hidden = random.choice(game_suspects)
    hidden["is_murderer"] = True
    return {"suspects": game_suspects, "game_over": False}


def suspect_list(game_suspects):
    return game_suspects


def interrogate_suspect(game_suspects, index):
    return game_suspects[index]


def accuse_suspect(game_suspects, index):
    suspect = game_suspects[index]
    return suspect["is_murderer"]


def print_intro():
    print("Welcome to the Murder Mystery game!")
    print("A crime has been committed, and your job is to find the hidden murderer.")
    print("You can interrogate suspects, collect clues, and then accuse the person you think did it.\n")


def list_suspects():
    print("Suspects:")
    for index, person in enumerate(suspects, start=1):
        print(f"  {index}. {person['name']} - {person['occupation']}")
    print()


def interrogate():
    list_suspects()
    choice = input("Enter the number of the suspect you want to interrogate: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(suspects)):
        print("That is not a valid suspect number. Try again.\n")
        return

    suspect = suspects[int(choice) - 1]
    print(f"\nInterrogating {suspect['name']}...")
    print(f"Alibi: {suspect['alibi']}")
    print(f"Clue: {suspect['clue']}\n")


def accuse():
    list_suspects()
    choice = input("Enter the number of the suspect you want to accuse: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(suspects)):
        print("That is not a valid suspect number. Try again.\n")
        return False

    suspect = suspects[int(choice) - 1]
    if suspect["is_murderer"]:
        print(f"\nYou accused {suspect['name']}. Congratulations! You found the murderer!")
        print("Case closed. Well done, detective!\n")
        return True

    print(f"\nYou accused {suspect['name']}, but they are innocent.")
    print("The real murderer got away this time. Try again later.\n")
    return True


def game_loop():
    print_intro()
    while True:
        print("What would you like to do?")
        print("  1. Interrogate a suspect")
        print("  2. Accuse a suspect")
        print("  3. Quit")
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            interrogate()
        elif choice == "2":
            game_over = accuse()
            if game_over:
                break
        elif choice == "3":
            print("Goodbye, detective. Come back when you are ready to solve the case.")
            break
        else:
            print("Please type 1, 2, or 3.\n")


if __name__ == "__main__":
    game_loop()
