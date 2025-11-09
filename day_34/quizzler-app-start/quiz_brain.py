class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        return {
            "number": self.question_number,
            "text": question.text,
        }

    def check_answer(self, answer):
        if answer.lower() == self.question_list[self.question_number - 1].answer.lower():
            self.score += 1
            return True
        else:
            return False

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def get_question_count(self):
        return len(self.question_list)