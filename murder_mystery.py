import random
from copy import deepcopy

SUSPECT_TEMPLATES = [
    {
        "name": "Ava",
        "age": 31,
        "occupation": "baker",
        "personality": "warm and observant",
        "alibi": "I was baking pastries in the kitchen when the murder happened.",
        "clue": "I saw someone with flour on their shoes near the garden.",
        "motive": "Ava worried the victim would expose her bakery's ingredient shortcuts.",
        "is_murderer": False,
    },
    {
        "name": "Ben",
        "age": 38,
        "occupation": "gardener",
        "personality": "quiet and meticulous",
        "alibi": "I was trimming the hedges outside. I heard a scream and ran inside.",
        "clue": "The rope in the shed was cut recently.",
        "motive": "Ben believed the victim was going to sell the estate and leave him without work.",
        "is_murderer": False,
    },
    {
        "name": "Claire",
        "age": 27,
        "occupation": "artist",
        "personality": "creative and emotional",
        "alibi": "I was painting in my studio all afternoon.",
        "clue": "My paintbrushes were moved while I was away from the studio.",
        "motive": "Claire felt the victim was plagiarizing her artwork and wanted revenge.",
        "is_murderer": False,
    },
    {
        "name": "Daniel",
        "age": 45,
        "occupation": "antique dealer",
        "personality": "charming and secretive",
        "alibi": "I was cataloging rare pieces in the parlor. I didn't leave the room.",
        "clue": "A broken vase was found near the body, and it belonged to me.",
        "motive": "Daniel needed money quickly and feared the victim would ruin his business.",
        "is_murderer": False,
    },
]


def create_game():
    suspects = deepcopy(SUSPECT_TEMPLATES)
    hidden = random.choice(suspects)
    hidden["is_murderer"] = True
    for suspect in suspects:
        suspect["interrogated"] = False
    return {
        "suspects": suspects,
        "game_over": False,
        "remaining_accusations": 3,
        "evidence": [],
        "log": [],
        "message": "",
        "case_solved": False,
    }


def suspect_list(game_suspects):
    return [
        {
            "name": suspect["name"],
            "occupation": suspect["occupation"],
            "age": suspect["age"],
            "interrogated": suspect.get("interrogated", False),
        }
        for suspect in game_suspects
    ]


def interrogate_suspect(game, index):
    suspect = game["suspects"][index]
    if not suspect["interrogated"]:
        suspect["interrogated"] = True
        evidence = {
            "name": suspect["name"],
            "occupation": suspect["occupation"],
            "clue": suspect["clue"],
            "motive": suspect["motive"],
        }
        game["evidence"].append(evidence)
        game["log"].append(
            f"Interrogated {suspect['name']}: {suspect['alibi']}" 
            f" | Clue: {suspect['clue']}"
        )

    return {
        "name": suspect["name"],
        "age": suspect["age"],
        "occupation": suspect["occupation"],
        "personality": suspect["personality"],
        "alibi": suspect["alibi"],
        "clue": suspect["clue"],
        "motive": suspect["motive"],
        "interrogated": suspect["interrogated"],
    }


def accuse_suspect(game, index):
    suspect = game["suspects"][index]
    if suspect["is_murderer"]:
        game["game_over"] = True
        game["case_solved"] = True
        game["message"] = f"You accused {suspect['name']}. Congratulations! You found the murderer!"
        game["log"].append(f"Accused {suspect['name']} and solved the case.")
        return True

    game["remaining_accusations"] -= 1
    game["log"].append(f"Accused {suspect['name']} and was wrong.")
    if game["remaining_accusations"] <= 0:
        game["game_over"] = True
        murderer = next(item for item in game["suspects"] if item["is_murderer"])
        game["message"] = (
            f"You accused {suspect['name']}, but they were innocent. "
            f"The real murderer was {murderer['name']}.")
    else:
        game["message"] = (
            f"You accused {suspect['name']}, but they were innocent. "
            f"You have {game['remaining_accusations']} accusations left.")
    return False


def list_suspects():
    return [
        f"{index + 1}. {suspect['name']} - {suspect['occupation']}"
        for index, suspect in enumerate(SUSPECT_TEMPLATES)
    ]


def print_intro():
    print("Welcome to the Murder Mystery game!")
    print("A crime has been committed, and your job is to solve the case.")
    print("Interrogate suspects, collect clues, and accuse the correct person before your chances run out.\n")


def game_loop():
    game = create_game()
    print_intro()

    while not game["game_over"]:
        print("What would you like to do?")
        print("  1. Interrogate a suspect")
        print("  2. Accuse a suspect")
        print("  3. Review evidence")
        print("  4. Quit")
        choice = input("Enter 1, 2, 3, or 4: ").strip()

        if choice == "1":
            print("\nSuspects:")
            for index, suspect in enumerate(game["suspects"], start=1):
                status = "(questioned)" if suspect["interrogated"] else "(not questioned)"
                print(f"  {index}. {suspect['name']} - {suspect['occupation']} {status}")
            suspect_choice = input("Enter the number of the suspect you want to interrogate: ").strip()
            if not suspect_choice.isdigit() or not (1 <= int(suspect_choice) <= len(game["suspects"])):
                print("That is not a valid suspect number. Try again.\n")
                continue
            interrogation = interrogate_suspect(game, int(suspect_choice) - 1)
            print(f"\nInterrogating {interrogation['name']}...")
            print(f"Alibi: {interrogation['alibi']}")
            print(f"Clue: {interrogation['clue']}")
            print(f"Motive: {interrogation['motive']}\n")
        elif choice == "2":
            print("\nSuspects:")
            for index, suspect in enumerate(game["suspects"], start=1):
                print(f"  {index}. {suspect['name']} - {suspect['occupation']}")
            suspect_choice = input("Enter the number of the suspect you want to accuse: ").strip()
            if not suspect_choice.isdigit() or not (1 <= int(suspect_choice) <= len(game["suspects"])):
                print("That is not a valid suspect number. Try again.\n")
                continue
            accuse_suspect(game, int(suspect_choice) - 1)
            print(f"\n{game['message']}\n")
        elif choice == "3":
            if not game["evidence"]:
                print("\nYou haven't collected any evidence yet. Interrogate a suspect first.\n")
            else:
                print("\nEvidence collected:")
                for evidence in game["evidence"]:
                    print(f"- {evidence['name']}: {evidence['clue']}")
                print(f"Remaining accusations: {game['remaining_accusations']}\n")
        elif choice == "4":
            print("Goodbye, detective. Come back when you are ready to solve the case.")
            break
        else:
            print("Please type 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    game_loop()
