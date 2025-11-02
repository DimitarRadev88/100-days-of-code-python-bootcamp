from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=640, height=480)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

my_label["text"] = "New Text"
my_label.config(text="New New Text")

def button_clicked():
    my_label.config(text=my_input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)
button.config(padx=100, pady=200)

my_input = Entry()
my_input.grid(row=2, column=3)

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)

window.mainloop()

