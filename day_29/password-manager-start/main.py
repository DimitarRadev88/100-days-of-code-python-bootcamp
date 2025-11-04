from random import randint
from tkinter import *
from tkinter import messagebox

import pyperclip


def generate_password():
    clear_password()
    password_length = randint(15, 20)
    password = ""
    for _ in range(0, password_length):
        password += chr(randint(32, 128))

    password_input.insert(0, password)
    pyperclip.copy(password)


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showinfo("Warning", "Please don't leave empty fields")

    else:
        should_save = messagebox.askokcancel(title=website,
                                             message=f"Details to be saved:\n"
                                                     f"Email: {email} | Password: {password}\n"
                                                     f"OK to confirm, Cancel to edit")

        if should_save:
            with open("data.txt", mode="a") as password_data:
                password_data.write(f"{website} | {email} | {password}\n")
                clear_password()
                clear_website()
                messagebox.showinfo("Success", "Password saved!")


def clear_password():
    password_input.delete(0, END)


def clear_website():
    website_input.delete(0, END)


root = Tk()
root.title("Password Manager")
root.config(background="white", pady=66, padx=66)

canvas = Canvas(width=266, height=266, highlightthickness=0, bg="white")
logo_image = PhotoImage(file="logo.png")
canvas.create_image(133, 133, image=logo_image)
canvas.grid(row=0, column=1)

website_input_label = Label(text="Website:", bg="white", font=("Arial", 8, "bold"))
website_input_label.grid(row=1, column=0)
website_input = Entry(width=37, font=("Arial", 8, "bold"))
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)
email_input_label = Label(text="Email/Username:", bg="white", font=("Arial", 8, "bold"))
email_input_label.grid(row=2, column=0)
email_input = Entry(width=37, font=("Arial", 8, "bold"))
email_input.insert(0, "goshe@abv.bg")
email_input.grid(row=2, column=1, columnspan=2)
password_input_label = Label(text="Password:", bg="white", padx=0, font=("Arial", 8, "bold"))
password_input_label.grid(row=3, column=0)
password_input = Entry(width=26, font=("Arial", 8, "bold"))
password_input.grid(row=3, column=1)
generate_password_button = Button(text="Generate Password", command=generate_password, font=("Arial", 5, "bold"),
                                  pady=1, padx=1)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", command=save_password, bg="white", font=("Arial", 8, "bold"), width=34, pady=1)
add_button.grid(row=4, column=1, columnspan=2)

root.mainloop()
