from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz_brain = quiz_brain

        self.root = Tk()

        self.root.title("Quizzler")
        self.root.config(pady=20, padx=20, bg=THEME_COLOR)

        self.question_number = Label(bg=THEME_COLOR, fg="white", text="Question N: 0", font=("Arial", 6, "normal"))
        self.question_number.grid(row=0, column=0)
        self.score = Label(bg=THEME_COLOR, fg="white", text="Score: 0", font=("Arial", 6, "normal"))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, fill=THEME_COLOR, width=280, text="lorem ipsum dolor",
                                                     font=("Arial", 10, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.root.mainloop()

    def answer_true(self):
        result = self.quiz_brain.check_answer("true")
        self.give_feedback(result)

    def answer_false(self):
        result = self.quiz_brain.check_answer("false")
        self.give_feedback(result)

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, text="Correct")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, text="Incorrect")
        self.root.after(500, self.get_next_question)

    def reset_canvas_bg(self):
        self.canvas.config(bg="white")

    def get_next_question(self):
        self.reset_canvas_bg()
        self.score.config(text=f"Score: {self.quiz_brain.score}")
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.question_number.config(text=f"Question N: {question["number"]}")
            self.canvas.itemconfig(self.question_text, text=question["text"])
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="You've completed the quiz.\nFinal score: "
                                        f"{self.quiz_brain.score}/{self.quiz_brain.get_question_count()}")
            self.true_button.grid_remove()
            self.false_button.grid_remove()
