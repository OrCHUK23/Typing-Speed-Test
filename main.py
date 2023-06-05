from tkinter import *
import random

WINDOW_GEOMETRY = "500x500"
TITLE_FONT = ("Myriad Pro Black", 30, "bold")
START_FONT = ("Myriad Pro Black", 15, "bold")
TIMER_FONT = ("Myriad Pro Black", 25, "bold")


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


def draw_start_button(wnd):
    """
    Function draws the start button.
    :param wnd: Tkinter window object.
    :return: None
    """
    # Start button.
    start_button = Button(
        wnd,
        text="START",
        command=start_game,
        width=20,
        height=3,
        bg="green",
        fg="black",
        relief="flat",
        font=START_FONT
    )
    start_button.grid(row=1, column=1, pady=100)


def game_window_and_title():
    """
    Function creates the game window and title.
    :return: Tkinter window object.
    """
    # Create the window.
    wnd = Tk()
    wnd.title("Typing Speed Test")
    wnd.geometry(WINDOW_GEOMETRY)
    center_window(wnd)

    # Create timer oval.
    circle_canvas = Canvas(wnd, width=80, height=80)
    circle_canvas.grid(row=0, column=0, padx=10, pady=10)
    circle_canvas.create_oval(10, 10, 70, 70, fill="lightblue")
    # circle_canvas.pack(pady=10, anchor="w")
    timer = circle_canvas.create_text(40, 40, text="60", font=TIMER_FONT, fill="black")
    circle_canvas.grid(row=0, column=0)

    # Create the title label.
    title_label = Label(wnd, text="Typing Speed Test")
    title_label.config(font=TITLE_FONT)
    title_label.grid(row=0, column=1)
    return wnd


def start_game():
    """
    Function starts the game.
    :return: None
    """
    # Destroy the welcome window.
    start_window.destroy()

    # Create the game window.
    game_window = game_window_and_title()


# Create welcome window and start button.
start_window = game_window_and_title()
draw_start_button(start_window)

if __name__ == "__main__":
    start_window.mainloop()
