from tkinter import Tk, Canvas, Button, PhotoImage, Entry
import random

# ---------------------------- CONSTANTS ------------------------------- #
# Fonts.
TITLE_FONT = ("Myriad Pro Black", 30, "bold")
START_FONT = ("Myriad Pro Black", 15, "bold")
WORD_FONT = ("Myriad Pro Black", 20, "bold")
SCORE_FONT = ("Myriad Pro Black", 20, "bold")
STARTING_FONT = ("Myriad Pro Black", 80, "bold")
TIMER_FONT = ("Courier", 25, "bold")

# Colors.
BACKGROUND_COLOR = "#D3D3D3"
WINDOW_GEOMETRY = "500x500"
TITLE_COLOR = "#009bff"

# Sizes and positions.
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

GAME_TIMER = 3  # Game time in seconds.


class TypingSpeedTest:
    def __init__(self):
        # Create the window.
        self.window = Tk()
        self.window.title("Typing Speed Test")

        # Create the Canvas on the window.
        self.canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.grid(row=0, column=0)

        # Starting timer text and counter.
        self.start_timer_text = self.canvas.create_text(WINDOW_WIDTH // 2, 200, text="", font=STARTING_FONT)
        self.start_timer_counter = 1
        self.starting_timer = None

        # Create the start image and button objects.
        self.start_button_image = PhotoImage(file="images/start_button.png")
        self.start_button = Button(self.canvas, highlightthickness=0, bd=0, image=self.start_button_image,
                                   command=lambda: self.start_countdown(self.start_timer_counter))
        self.start_button.place(x=180, y=250)

        # Main game title.
        self.title_label = self.canvas.create_text(260, 40, text="Typing Speed Test", font=TITLE_FONT,
                                                   fill=TITLE_COLOR)

        # Game timer.
        self.timer_text = self.canvas.create_text(45, 40, text="", fill="black",
                                                  font=TIMER_FONT)
        self.game_timer = None

        # Create words following variables.
        self.correct = self.canvas.create_text(50, WINDOW_HEIGHT / 4.5, text="", font=SCORE_FONT, fill="green")
        self.incorrect = self.canvas.create_text(WINDOW_WIDTH - 50, WINDOW_HEIGHT / 4.5, text="", font=SCORE_FONT,
                                                 fill="red")
        self.correct_counter = 0
        self.incorrect_counter = 0

        # Current word and user Entry object.
        self.current_word = self.canvas.create_text(250, 250, text="", font=WORD_FONT)
        self.user_entry = None
        self.write_here = None

        # Center the window.
        self.__center_window()

        # Create random words list.
        with open("data/words.txt", "r") as file:
            self.words_list = random.sample([word.strip() for word in file.readlines()], 500)

    def __center_window(self):
        """
        Function centers the window object.
        :return: None.
        """
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # 3 2 1 At the beginning.
    def start_countdown(self, count):
        """
        Function handles the first screen countdown.
        :param count: int
        :return: None.
        """
        # Handle starting button clicked again.
        if self.starting_timer is not None:
            self.window.after_cancel(self.starting_timer)

        self.canvas.itemconfig(self.start_timer_text, text=self.start_timer_counter)

        if count > 0:
            self.canvas.itemconfig(self.start_timer_text, text=str(count))
            self.starting_timer = self.window.after(1000, self.start_countdown, count - 1)
        else:
            self.canvas.itemconfig(self.start_timer_text, text="")
            self.start_game()

    def timer_count_down(self, count):
        """
        Function handles the main timer countdown.
        :param count: Int.
        :return: None
        """
        self.canvas.itemconfig(self.timer_text, text=count)

        if count > 0:
            self.game_timer = self.window.after(1000, self.timer_count_down, count - 1)
        else:
            self.end_game()

    def start_game(self):
        """
        Function handles game started.
        :return: None
        """
        # Destroy start button and reset answers counter.
        self.start_button.destroy()
        self.canvas.itemconfig(self.correct, text="0")
        self.canvas.itemconfig(self.incorrect, text="0")

        # Start game timer, user input graphics and get first word to show.
        self.timer_count_down(GAME_TIMER)
        self.create_user_input()
        self.get_next_word()

    def create_user_input(self):
        """
        Function handles the user input graphics.
        :return: None.
        """
        self.user_entry = Entry(self.canvas, font=WORD_FONT, width=15, bd=2, relief="groove",
                                fg="black", bg="lightgray")
        self.user_entry.place(x=170, y=400)
        self.user_entry.focus_set()
        self.write_here = self.canvas.create_text(250, 390, text="Write words here. ENTER for new word.",
                                                  font=("Courier", 10, "bold"),
                                                  fill="purple")

        # Bind users key to check input.
        self.user_entry.bind("<Key>", self.check_user_input)

    def check_user_input(self, event):
        """
        Function checks user input and handles it accordingly.
        :param event: Tkinter Event object.
        :return: None.
        """
        # Check if "ENTER" key was pressed.
        if event.keysym == "Return":
            if self.user_entry.get() == self.canvas.itemcget(self.current_word, "text"):
                self.correct_counter += 1
                self.canvas.itemconfig(self.correct, text=self.correct_counter)
            else:
                self.incorrect_counter += 1
                self.canvas.itemconfig(self.incorrect, text=self.incorrect_counter)
            self.user_entry.delete(0, "end")  # Empty user input.
            self.get_next_word()

    def get_next_word(self):
        """
        Function handles the next word.
        :return: None.
        """
        next_word = random.choice(self.words_list)
        self.canvas.itemconfig(self.current_word, text=next_word)

    def end_game(self):
        """
        Function handles the end of the game, gives score and offers a new game.
        :return: None
        """
        self.user_entry.destroy()

        self.canvas.itemconfig(self.correct, text="")
        self.canvas.itemconfig(self.incorrect, text="")

        self.canvas.itemconfig(self.timer_text, text="")

        self.canvas.itemconfig(self.current_word, text="")
        self.canvas.itemconfig(self.write_here, text="")

        self.canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 50,
                                text=f"Time's UP!\n",
                                fill="black",
                                font=SCORE_FONT)
        self.canvas.create_text(WINDOW_WIDTH / 2 - 100,
                                WINDOW_HEIGHT / 2,
                                text=f"Correct words:\n{self.correct_counter}",
                                fill="green",
                                font=SCORE_FONT)
        self.canvas.create_text(WINDOW_WIDTH / 2 + 100,
                                WINDOW_HEIGHT / 2,
                                text=f"Incorrect words:\n{self.incorrect_counter}",
                                fill="red",
                                font=SCORE_FONT)


if __name__ == "__main__":
    game = TypingSpeedTest()
    game.window.mainloop()
