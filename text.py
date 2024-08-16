from moves import Move

options = "What would you like to do? \n 1. Exercise \n 2. Eat \n 3. Sleep"

# choices
choice_exercise = "you exercised"
choice_eat = "you eat"
choice_sleep = "you slept"
choice_invalid = "invalid choice"

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