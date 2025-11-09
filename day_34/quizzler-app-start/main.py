import html

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = [Question(html.unescape(data["question"]), data["correct_answer"]) for data in question_data]

quiz_brain = QuizBrain(question_bank)

ui = QuizInterface(quiz_brain)
