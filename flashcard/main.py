from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}
# --------------------------- OPEN DATA FILE ----------------------------------------

try:
    current_data = pd.read_csv("data/words_to_learn.csv")
    to_learn = current_data.to_dict(orient="records")
    print(to_learn)


except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")



# --------------------------- DEFINE FUNCTIONS --------------------------------------


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.grid(row=0, column=0, columnspan=2)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.grid(row=0, column=0, columnspan=2)
    # window.after(3000, func=next_card)


def remove_card():
    global current_card
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame.from_dict(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# --------------------------- CREATE GUI NEW LANGUAGE --------------------------------------------

window = Tk()
window.title("Flashcard")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_image = canvas.create_image(410, 263, image=card_front)
title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 273, text="french_word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

incorrect_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=next_card)
incorrect_button.grid(row=1, column=0)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=remove_card)
correct_button.grid(row=1, column=1)

# --------------------------- CREATE GUI KNOWN LANGUAGE --------------------------------------------

next_card()
mainloop()
