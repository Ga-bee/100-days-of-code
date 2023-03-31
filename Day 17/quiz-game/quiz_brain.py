class QuizBrain:
    def __init__(self,question_list) -> None:
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0

    def still_has_questions(self):
        #chek if it til has questions
        return self.question_number < len(self.questions_list)
        
        #if yes return true
        #if it dont return false

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False):')
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,u_answer,c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong.") 
        print(f"The right answer is {c_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        
