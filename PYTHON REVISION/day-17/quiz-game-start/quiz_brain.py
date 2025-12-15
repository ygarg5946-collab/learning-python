current_score=0
class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        my_answer=input(f"Question {self.question_number}: {current_question.text} (True/False)")
        if my_answer==current_question.answer:
            print("You got it right")
            print(f"The correct answer is {current_question.answer}")
            global current_score
            current_score+=1
            print(f"Your current score is {current_score}/{self.question_number}")
        else:
            print("You got it wrong")
            print(f"The current score is {current_question.answer}/{current_score}/{self.question_number}")

    def still_has_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False
