"""
Class configures constants for the game.
"""


class Config:
    # Fonts
    TITLE_FONT = ("Myriad Pro Black", 30, "bold")
    STARTING_TIMER_FONT = ("Myriad Pro Black", 80, "bold")
    GAME_TIMER_FONT = ("Courier", 25, "bold")
    WORD_FONT = ("Arial", 20, "bold")
    ENTRY_FONT = ("Arial", 15)
    RESULTS_SCORE = ("Myriad Pro Black", 20, "bold")

    # Colors
    BACKGROUND_COLOR = "#D3D3D3"
    TITLE_COLOR = "#009bff"

    # Sizes and positions
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    WINDOW_GEOMETRY = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"

    # Game timer
    GAME_TIMER = 60  # Game time in seconds
