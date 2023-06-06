import math
from tkinter import Tk, Canvas, Button, PhotoImage, Entry
import tkinter.font as tkfont
import random
from PIL import Image, ImageTk, ImageDraw

WINDOW_GEOMETRY = "500x500"
BACKGROUND_COLOR = "#D3D3D3"
TITLE_COLOR = "#009bff"
TITLE_FONT = ("Myriad Pro Black", 30, "bold")
START_FONT = ("Myriad Pro Black", 15, "bold")
TIMER_FONT = ("Courier", 25, "bold")
WORDS_FONT = ("Myriad Pro Black", 10, "bold")

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

STARTING_X_POS = 100
STARTING_Y_POS = 150

GAME_TIME = 2  # Game time in seconds


def center_window(wnd):
    """
    Function centers the tkinter window.
    :param wnd: Tkinter.
    :return: None
    """
    wnd.update_idletasks()
    width = wnd.winfo_width()
    height = wnd.winfo_height()
    x = (wnd.winfo_screenwidth() // 2) - (width // 2)
    y = (wnd.winfo_screenheight() // 2) - (height // 2)
    wnd.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def start_button_clicked():
    """
    Function destroys the start button and starts the game.
    :return: None
    """
    start_button.destroy()
    start_game()


def generate_random_word():
    """
    Function generates random word from the .txt file
    :return: String
    """
    with open("data/words.txt", "r") as file:
        words_list = [word.strip() for word in file.readlines()]
    return random.choice(words_list)


def end_game():
    """
    Function handles the ending of the game after time's up.
    :return: None
    """
    global user_entry
    user_entry.delete(0, "end")
    user_entry.config(state="disabled")
    for text_object_id, _ in text_objects:
        canvas.delete(text_object_id)
    # TODO: Show final score.
    # TODO: add start over button.


def count_down(count):
    """
    Function handles the timer start
    :param count: Int.
    :return: None.
    """
    canvas.itemconfig(timer_text, text=f"{count}")

    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        end_game()
        canvas.itemconfig(timer_text, text=f"")  # Make timer disappear.
        print("DONE")


def start_game():
    """
    Function handles the game.
    :return: None
    """

    def get_user_input(event):
        """
        Function to handle the user's input.
        :return: None
        """
        user_input = ""
        if event.keysym == "Return":
            user_input = user_entry.get()
            print(user_input)
            user_entry.delete(0, "end")
        else:
            user_input += event.char  # Add the entered character to the user input

    # Get current x and y cords.
    current_x = STARTING_X_POS
    current_y = STARTING_Y_POS
    # Manage words creation.
    for _ in range(20):
        word = generate_random_word()  # Generate random word
        text_object = canvas.create_text(current_x, current_y, text=word, fill="black", font=WORDS_FONT)
        text_objects.append((text_object, word))  # Add each object to a list.
        bounds = canvas.bbox(text_object)  # returns a tuple like (x1, y1, x2, y2).
        width = bounds[2] - bounds[0]  # Calc word width.
        x_coor = bounds[2]
        offset = 5  # Spacing between words.
        current_x = width + x_coor
        if current_x + offset >= WINDOW_WIDTH:  # Check if we've reached the window width.
            current_x = 100  # Reset the x_coor to the starting position.
            current_y += 50
        # TODO: Check height collision.

    # Create the user input rectangle.
    global user_entry
    user_entry = Entry(canvas,
                       font=("Myriad Pro Black", 14),
                       width=15,
                       bd=2,
                       relief="groove",
                       fg="black",
                       bg="lightgray")
    user_entry.place(x=170, y=400)
    user_entry.focus_set()

    # Bind the <Key> event to the user input rectangle.
    user_entry.bind("<Key>", get_user_input)

    # Create user input label.
    canvas.create_text(270, 390, text="Write words here. ENTER for new word.")

    # Start time countdown.
    count_down(GAME_TIME)


# Create window.
window = Tk()
window.title("Typing Speed Test")

# Create canvas.
canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.grid(row=0, column=0)

# Create start button
start_button_image = PhotoImage(file="images/start_button.png")
start_button = Button(canvas, highlightthickness=0, bd=0, image=start_button_image, command=start_button_clicked)
start_button.place(x=180, y=250)

# Create title text.
title_label = canvas.create_text(260, 40, text="Typing Speed Test", font=TITLE_FONT, fill=TITLE_COLOR)

# Words objects list.
text_objects = []

# Create user input object.
user_entry = None

# Timer creation
timer_text = canvas.create_text(45, 40, text="", fill="black", font=(TIMER_FONT, 35, "bold"))
my_timer = None

# Make the window to be in the center.
center_window(window)

if __name__ == "__main__":
    window.mainloop()
