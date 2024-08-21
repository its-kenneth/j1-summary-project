from moves import Move
# option text
option_stack = ["Exercise", "Eat", "Sleep", "Display Stats", "Display Moves", "Go to Pokemon Gym"]

# choice text
choice_stack = ["You exercise", "You eat", "You slept! Your hp and move pp have been restored to full!", "Stats:\n", "Moves:\n", "You enter the Pokemon Gym..."]

# final msgs
final_win = "You won!"
final_lose = "You lost!"

moves = [
    {"name": "Kick", "multiplier": 1.2, "power_limit": 10},
    {"name": "Throw", "multiplier": 1.5, "power_limit": 7},
    {"name": "Slash", "multiplier": 2.0, "power_limit": 5},
    {"name": "Shot", "multiplier": 2.5, "power_limit": 3}
]

creatures = [
    {"name": "Toss Boss", "hp": 200, "attack": 10, "move_dropped": "Throw"},
    {"name": "Silver Knight", "hp": 450, "attack": 25, "move_dropped": "Slash"},
    {"name": "Captain Gun", "hp": 800, "attack": 45, "move_dropped": "Shot"}
]

monster = {"name": "Monster", "hp": 1000, "attack": 65}

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
    