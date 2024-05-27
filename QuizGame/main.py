#from data import question_data

from qdata import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

#print(question_bank[11].question)

quiz_brain = Quizbrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.check_answer(quiz_brain.ask_question())

print("You have completed the quiz.")
print(f"Your final score is {quiz_brain.score} out of {quiz_brain.question_no}")