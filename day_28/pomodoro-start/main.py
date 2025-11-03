from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

work_sessions = 0
time = WORK_MIN
is_time_to_work = True
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global work_sessions
    global is_time_to_work
    global time
    work_sessions = 0
    time = WORK_MIN
    is_time_to_work = True
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", foreground=GREEN)
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global work_sessions
    global is_time_to_work
    global time
    if is_time_to_work:
        work_sessions += 1
        title_label.config(text="Work", foreground=GREEN)
        time = WORK_MIN
        is_time_to_work = False
    else:
        is_time_to_work = True
        if work_sessions < 4:
            title_label.config(text="Break", foreground=PINK)
            time = SHORT_BREAK_MIN
        else:
            title_label.config(text="Break", foreground=RED)
            time = LONG_BREAK_MIN
            work_sessions = 0

    countdown(time * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    canvas.itemconfig(timer_text, text=f"{int(count / 60):02}:{count % 60:02}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        check_marks.config(text="✓" * work_sessions)
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, bd=0)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
title_label.grid(row=0, column=1)

check_marks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
check_marks.grid(row=3, column=1)

start_button = Button(text="Start", command=start_timer, bg="white", padx=0, pady=0, font=("Arial", 6, "bold"))
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset_timer, bg="white", padx=0, pady=0, font=("Arial", 6, "bold"))
reset_button.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 133, text="00:00", fill="white", font=(FONT_NAME, 14, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
