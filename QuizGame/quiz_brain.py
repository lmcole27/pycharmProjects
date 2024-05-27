class Quizbrain:

    def __init__(self, question_list):
        self.question_no = 0
        self.questions = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.questions)

    def check_answer(self, answer):
        print(f"The correct answer is {self.questions[self.question_no].answer}")
        if answer == self.questions[self.question_no].answer:
            self.score += 1
            print(f"You got it right.")
        else:
            print(f"That's not right.")
        self.question_no += 1
        print(f"Your score is {self.score} / {self.question_no}")

    def ask_question(self):
        current_question = self.questions[self.question_no].question

        answer = input(f"Q.{self.question_no +1}: {current_question} Answer 'True' or 'False': ")
        print(f"Your answer was {answer}")
        return answer