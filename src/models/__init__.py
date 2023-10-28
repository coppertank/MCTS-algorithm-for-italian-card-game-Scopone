# Menu

# Menu Buttons
NEW_GAME = 'New Game'
SIMULATE_GAME = 'Simulate Game'
EXIT = 'Exit'

# Menu options
PLAY = 'Play'
SIMULATE = 'Simulate'
MODE = 'Mode'
MODE_REVERSE = 'Mode Reverse'
PARTNER = 'Partner'
DIFFICULTY = 'Difficulty'
TEAM1 = 'Team 1'
TEAM2 = 'Team 2'
WATCH = 'Watch'

# Team options
GREEN = 'Green'
YELLOW = 'Yellow'
ORANGE = 'Orange'
RED = 'Red'

# Difficulty options
EASY = 'Easy'
MEDIUM = 'Medium'
HARD = 'Hard'
EXTREME = 'Extreme'

# Watch options
YES = 'Yes'
NO = 'No'

menu_options = {
    MODE: ([(PLAY, 1), (SIMULATE, 2)]),
    MODE_REVERSE: ([(SIMULATE, 2), (PLAY, 1)]),
    PARTNER: ([(GREEN, 1), (YELLOW, 2), (ORANGE, 3), (RED, 4)]),
    DIFFICULTY: ([(EASY, 1), (MEDIUM, 2), (HARD, 3), (EXTREME, 4)]),
    TEAM1: ([(GREEN, 1), (YELLOW, 2), (ORANGE, 3), (RED, 4)]),
    TEAM2: ([(GREEN, 1), (YELLOW, 2), (ORANGE, 3), (RED, 4)]),
    WATCH: [(YES, 1), (NO, 0)]
}
