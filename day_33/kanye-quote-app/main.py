from tkinter import *

import requests


def get_quote():
    request = requests.get("https://api.kanye.rest")
    request.raise_for_status()

    return request.json()["quote"]


def show_quote():
    canvas.itemconfig(canvas_quote, text=get_quote())


root = Tk()
root.title("Kanye Says...")
root.config(padx=50, pady=50, bg="white")
bg_image = PhotoImage(file="background.png")
canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)
canvas.create_image(150, 207, image=bg_image)
canvas_quote = canvas.create_text(150, 200, text=f"{get_quote()}", width=125, fill="white", font=("Arial", 8, "bold"))
canvas.pack()

kanye_image = PhotoImage(file="kanye.png")
button = Button(image=kanye_image, command=show_quote, highlightthickness=0, bg="white")
button.pack()

root.mainloop()
