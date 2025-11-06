from random import choice
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

root = Tk()
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
root.title("Flashy")

current_word = None
root_after = None


def flip_card():
    global current_word
    canvas.itemconfig(card_image, image=card_back)

    canvas.itemconfig(language_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=current_word["English"])


def cancel_flip():
    if root_after:
        root.after_cancel(root_after)


def change_word():
    global current_word, root_after
    cancel_flip()
    canvas.itemconfig(card_image, image=card_front)
    if len(words_list) > 0:
        current_word = choice(words_list)
        canvas.itemconfig(language_text, fill="black", text="French")
        canvas.itemconfig(word_text, fill="black", text=current_word["French"])
        root_after = root.after(3000, func=flip_card)


def change_known_word():
    global current_word
    if len(words_list) > 0:
        words_list.remove(current_word)
    data_frame = pandas.DataFrame(words_list)
    data_frame.to_csv("data/words_to_learn.csv", index=False)
    change_word()


try:
    words_list = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except pandas.errors.EmptyDataError:
    words_list = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 268, image=card_front)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 16, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 24, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=change_known_word)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=change_word)
wrong_button.grid(row=1, column=1)

change_word()

root.mainloop()
