import random
from copy import deepcopy

CASES = [
    {
        "title": "Manor Murder",
        "description": "A wealthy collector was killed in his manor. The suspects are all connected to the estate and each hides a dangerous secret.",
        "location": "Silverwood Manor",
        "suspects": [
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
        ],
    },
    {
        "title": "Lakeside Betrayal",
        "description": "A rising politician was found dead during a retreat at a lakeside cottage. The suspects are colleagues, friends, and a jealous rival.",
        "location": "Cedar Lake Cottage",
        "suspects": [
            {
                "name": "Mia",
                "age": 34,
                "occupation": "campaign manager",
                "personality": "focused and intense",
                "alibi": "I was making calls in the study when the scream happened.",
                "clue": "I heard someone running toward the dock, and there was water on the floor.",
                "motive": "Mia feared the victim would take all the credit and ruin her career.",
                "is_murderer": False,
            },
            {
                "name": "Noah",
                "age": 40,
                "occupation": "rival politician",
                "personality": "confident and demanding",
                "alibi": "I was outside pacing by the lake. I didn't see anyone else.",
                "clue": "I found a torn speech note near the boat house.",
                "motive": "Noah wanted to eliminate his opponent before the election.",
                "is_murderer": False,
            },
            {
                "name": "Olivia",
                "age": 29,
                "occupation": "journalist",
                "personality": "curious and bold",
                "alibi": "I stepped away to take photos of the sunset.",
                "clue": "My camera was knocked over near the victim's room.",
                "motive": "Olivia was hiding a story that would ruin the politician's reputation.",
                "is_murderer": False,
            },
            {
                "name": "Parker",
                "age": 52,
                "occupation": "family friend",
                "personality": "smooth and protective",
                "alibi": "I was in the kitchen preparing snacks for everyone.",
                "clue": "The kitchen knife block was disturbed and one knife was missing.",
                "motive": "Parker wanted to keep the family legacy intact at any cost.",
                "is_murderer": False,
            },
        ],
    },
    {
        "title": "Gallery Night Murder",
        "description": "An avant-garde artist was murdered during a gallery opening. The suspects are fellow creatives, critics, and a jealous collector.",
        "location": "Urban Gallery",
        "suspects": [
            {
                "name": "Riley",
                "age": 26,
                "occupation": "artist",
                "personality": "fiery and passionate",
                "alibi": "I was discussing a commission with a collector in the west wing.",
                "clue": "I noticed a staff badge on the floor near the scene.",
                "motive": "Riley wanted the gallery's attention on their own work instead.",
                "is_murderer": False,
            },
            {
                "name": "Sydney",
                "age": 33,
                "occupation": "collector",
                "personality": "refined and secretive",
                "alibi": "I was examining a sculpture in the front room.",
                "clue": "I heard a glass display case slam shut near the back.",
                "motive": "Sydney feared the artist would expose their illicit purchases.",
                "is_murderer": False,
            },
            {
                "name": "Taylor",
                "age": 30,
                "occupation": "gallery curator",
                "personality": "organized and anxious",
                "alibi": "I was checking the guest list at the entrance.",
                "clue": "One of the gallery lights was turned off before the murder.",
                "motive": "Taylor was desperate to keep the gallery's reputation safe.",
                "is_murderer": False,
            },
            {
                "name": "Jordan",
                "age": 42,
                "occupation": "critic",
                "personality": "cynical and cutting",
                "alibi": "I was writing notes in my journal near the portraits.",
                "clue": "The artist's latest review had its last page torn out.",
                "motive": "Jordan wanted to silence a critic who would expose a scandal.",
                "is_murderer": False,
            },
        ],
    },
    {
        "title": "Midnight Express",
        "description": "A passenger is murdered aboard a luxury overnight train. Investigate the crew and travelers before the journey ends.",
        "location": "Northbound Express",
        "suspects": [
            {
                "name": "Elena",
                "age": 28,
                "occupation": "playwright",
                "personality": "dramatic and perceptive",
                "alibi": "I was in the observation car writing when the scream happened.",
                "clue": "A transport schedule was found with a missing departure time.",
                "motive": "Elena believed the victim stole her story idea.",
                "is_murderer": False,
            },
            {
                "name": "Frank",
                "age": 52,
                "occupation": "conductor",
                "personality": "efficient and secretive",
                "alibi": "I was checking passenger tickets in the sleeper car.",
                "clue": "A carriage door was unlocked when it should have been secured.",
                "motive": "Frank needed to cover up a hidden shipment on the train.",
                "is_murderer": False,
            },
            {
                "name": "Maya",
                "age": 22,
                "occupation": "student",
                "personality": "curious and anxious",
                "alibi": "I was asleep in my cabin and woke when I heard the scream.",
                "clue": "A torn notebook page mentioned the victim by name.",
                "motive": "Maya wanted to prevent the victim from revealing her secret project.",
                "is_murderer": False,
            },
            {
                "name": "Nathan",
                "age": 39,
                "occupation": "chef",
                "personality": "brusque but loyal",
                "alibi": "I was cooking dinner in the dining car.",
                "clue": "A key to the victim's cabin was found in the kitchen drawer.",
                "motive": "Nathan discovered the victim was blackmailing the crew.",
                "is_murderer": False,
            },
        ],
    },
    {
        "title": "Harbor Secrets",
        "description": "A shipyard owner is found dead beside the docks. The suspects are workers, traders, and a mysterious importer.",
        "location": "Blackwater Harbor",
        "suspects": [
            {
                "name": "Ari",
                "age": 36,
                "occupation": "shipwright",
                "personality": "stubborn and honest",
                "alibi": "I was repairing a hull in the dry dock.",
                "clue": "A crate label showed the wrong cargo manifest.",
                "motive": "Ari feared the victim would ruin his family business with false charges.",
                "is_murderer": False,
            },
            {
                "name": "Bella",
                "age": 29,
                "occupation": "export broker",
                "personality": "sharp and charming",
                "alibi": "I was negotiating a shipping contract at the warehouse.",
                "clue": "A forged customs stamp was found on a shipment.",
                "motive": "Bella wanted to silence the victim before he exposed her smuggling ring.",
                "is_murderer": False,
            },
            {
                "name": "Colin",
                "age": 47,
                "occupation": "harbor master",
                "personality": "gruff and controlling",
                "alibi": "I was reviewing dock assignments in my office.",
                "clue": "The victim's logbook contained a note about missing cargo.",
                "motive": "Colin needed to hide the fact that he illegally redirected ships.",
                "is_murderer": False,
            },
            {
                "name": "Diana",
                "age": 33,
                "occupation": "importer",
                "personality": "mysterious and strategic",
                "alibi": "I was unloading a crate from the freighter.",
                "clue": "A shipment record showed a falsified delivery time.",
                "motive": "Diana stood to lose everything if the victim exposed her operation.",
                "is_murderer": False,
            },
        ],
    },
]


def create_game(case_index=0):
    case_data = deepcopy(CASES[case_index])
    suspects = case_data["suspects"]
    hidden = random.choice(suspects)
    hidden["is_murderer"] = True
    for suspect in suspects:
        suspect["interrogated"] = False
    return {
        "case_title": case_data["title"],
        "case_description": case_data["description"],
        "case_location": case_data["location"],
        "case_index": case_index,
        "suspects": suspects,
        "game_over": False,
        "remaining_accusations": 3,
        "evidence": [],
        "log": [],
        "message": "",
        "case_solved": False,
    }


def case_list():
    return [
        {
            "title": case["title"],
            "description": case["description"],
            "location": case["location"],
        }
        for case in CASES
    ]


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


def list_suspects(case_index=0):
    return [
        f"{index + 1}. {suspect['name']} - {suspect['occupation']}"
        for index, suspect in enumerate(CASES[case_index]["suspects"])
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
    if game["game_over"]:
        return False

    if game["remaining_accusations"] <= 0:
        game["game_over"] = True
        murderer = next(item for item in game["suspects"] if item["is_murderer"])
        game["message"] = (
            f"You have no accusations left. The real murderer was {murderer['name']}.")
        return False

    suspect = game["suspects"][index]
    if suspect["is_murderer"]:
        game["game_over"] = True
        game["case_solved"] = True
        game["message"] = f"You accused {suspect['name']}. Congratulations! You found the murderer!"
        game["log"].append(f"Accused {suspect['name']} and solved the case.")
        return True

    game["remaining_accusations"] -= 1
    if game["remaining_accusations"] < 0:
        game["remaining_accusations"] = 0

    game["log"].append(f"Accused {suspect['name']} and was wrong.")
    if game["remaining_accusations"] <= 0:
        game["game_over"] = True
        murderer = next(item for item in game["suspects"] if item["is_murderer"])
        game["message"] = (
            f"You accused {suspect['name']}, but they were innocent. "
            f"The real murderer was {murderer['name']}."
        )
    else:
        game["message"] = (
            f"You accused {suspect['name']}, but they were innocent. "
            f"You have {game['remaining_accusations']} accusations left.")
    return False


def list_suspects(case_index=0):
    return [
        f"{index + 1}. {suspect['name']} - {suspect['occupation']}"
        for index, suspect in enumerate(CASES[case_index]["suspects"])
    ]


def print_intro():
    print("Welcome to the Murder Mystery game!")
    print("A crime has been committed, and your job is to solve the case.")
    print("Interrogate suspects, collect clues, and accuse the correct person before your chances run out.\n")


def game_loop():
    print_intro()
    print("Choose a case to investigate:")
    for index, case in enumerate(CASES, start=1):
        print(f"  {index}. {case['title']} - {case['description']}")

    case_choice = input("Enter the case number: ").strip()
    if not case_choice.isdigit() or not (1 <= int(case_choice) <= len(CASES)):
        print("That is not a valid case number. Starting the default case.\n")
        case_index = 0
    else:
        case_index = int(case_choice) - 1

    game = create_game(case_index)
    print(f"\nStarting case: {game['case_title']} at {game['case_location']}\n")
    print(f"Case summary: {game['case_description']}\n")

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
