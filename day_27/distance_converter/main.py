from tkinter import *

def convert_miles_to_km():
    miles = float(input_miles.get())
    km = miles * 1.609
    km_value_label.config(text=km)

window = Tk()
window.minsize(320, 240)
window.config(padx=20, pady=20, background="white")

input_miles = Entry(width=10)
input_miles.insert(END, string="0")
input_miles.grid(row=0, column=1)

miles_label = Label(text="Miles", background="white", pady=10, padx=10)
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to", background="white", pady=10, padx=10)
is_equal_label.grid(row=1, column=0)

km_value_label = Label(text="0", background="white", pady=10, padx=10)
km_value_label.grid(row=1, column=1)

km_label = Label(text="Km", background="white", pady=10, padx=10)
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=convert_miles_to_km)
button.grid(row=2, column=1)

window.mainloop()