class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(answer)

    def check_answer(self, answer):
        if answer.lower() == self.question_list[self.question_number - 1].answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {self.question_list[self.question_number - 1].answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
