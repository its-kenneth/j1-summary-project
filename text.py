"""text.py

Contains data for text used in the game
"""

class Choice:
    """Encapsulates player choices

    Attributes:
    - label: str
      A label for the choice
    - text: str
      The text to display when the choice is selected
    - turns_used: int
      The number of turns the choice uses up
    """
    def __init__(
            self,
            label: str,
            text: str,
            turns_used: int = 0
    ):
        self.label = label
        self.text = text
        self.turns_used = turns_used


# option text
option_stack = [
    "Exercise", "Eat", "Sleep", "Display Stats", "Display Moves",
    "Go to Pokemon Gym"
]

# choice text
choice_stack = [
    "You exercise", "You eat",
    "You slept! Your hp and move pp have been restored to full!", "Stats:\n",
    "Moves:\n", "You enter the Pokemon Gym..."
]

choices = {
    "Exercise": Choice("Exercise", "You exercise", 1),
    "Eat": Choice("Eat", "You eat", 1),
    "Sleep": Choice("Sleep", "You slept! Your hp and move pp have been restored to full!", 1),
    "Display Stats": Choice("Display Stats", "Stats:\n", 0),
    "Display Moves": Choice("Display Moves", "Moves:\n", 0),
    "Go to Pokemon Gym": Choice("Go to Pokemon Gym", "You enter the Pokemon Gym...", 0)
}


# final msgs
final_win = "You won!"
final_lose = "You lost!"

moves = [{
    "name": "Kick",
    "multiplier": 1.2,
    "power_limit": 10
}, {
    "name": "Throw",
    "multiplier": 1.5,
    "power_limit": 7
}, {
    "name": "Slash",
    "multiplier": 2.0,
    "power_limit": 5
}, {
    "name": "Shot",
    "multiplier": 2.5,
    "power_limit": 3
}, {
    "name": "Harass",
    "multiplier": 3.5,
    "power_limit": 3
}, {
    "name": "Cry",
    "multiplier": 2,
    "power_limit": 6
}]

creatures = [
    {
        "name": "Toss Boss",
        "hp": 200,
        "attack": 10,
        "move_dropped": "Throw"
    },
    {
        "name": "Silver Knight",
        "hp": 450,
        "attack": 25,
        "move_dropped": "Slash"
    },
    {
        "name": "Little Boy",
        "hp": 300,
        "attack": 55,
        "move_dropped": "Cry"
    },
    {
        "name": "Captain Gun",
        "hp": 800,
        "attack": 45,
        "move_dropped": "Shot"
    },
    {
        "name": "Manuel",
        "hp": 600,
        "attack": 60,
        "move_dropped": "Harass"
    },
]

monster = {"name": "Monster", "hp": 2000, "attack": 65}


def intro():
    print("""hi welcome to mango tree
    """)

    faq_choice = input("backstory (y/n): ")

    if faq_choice.lower() == 'y':
        print("""
ok basically you got 30 turns before monster arrives to kill you

go do whatever you want to prepare

exercise increases attack
eat increases HP
sleep restores HP to full and Moves PP to full

fight monsters in gym to collect limited edition moves to have stronger attacks
        """)
    else:
        print("ok bye bye go start the game")


def prompt_valid_choice(options: list[str], preamble: str, prompt: str):
    print(preamble)
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    choice = input(prompt)
    while not choice.isdecimal() and (int(choice) - 1) not in range(
            0, len(options)):
        print("Invalid choice, pick a number from 1 to", len(options))
        choice = input(prompt)
    return int(choice) - 1

def attack_report(name: str, move: str, damage: int) -> str:
    return f"{name} used {move}! It dealt {damage} damage!"

def monster_attack_report(name: str, damage: int) -> str:
    return f"{name} lashed out! It dealt {damage} damage!"

def creature_report(name: str, hp: int, attack: int) -> str:
    return f"{name} has {hp} HP left and {attack} attack."

def player_report(name: str, hp: int) -> str:
    return f"{name} {"have" if name == "You" else "has"} {hp} HP left."

def flee_report(name: str, fatal: bool = False) -> str:
    if fatal:
        return f"Coward! The monster struck a fatal blow as {name.lower()} fled, causing {name.lower()} to bleed to death."
    else:
        return f"{name} {"flee" if name == "You" else "flees"} from the battle..."

def battle_report(victor: str, loser: str, loot: str) -> str:
    return f"{victor} won! {loser} dropped {loot}."

def win_report(name: str) -> str:
    return f"{name} won! Thank you for playing!"

def final_battle_report(name: str) -> str:
    return f"{name} {"have" if name == "You" else "has"} entered the final battle!"

def leave_gym_report(name: str) -> str:
    return f"{name} left the gym..."