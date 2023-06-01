from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.minsize(width=350,height=300)

        self.score_label = Label(text='Score: 0 ',fg='white',bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg='white')
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.question_text = self.canvas.create_text(150,125,width=250,font=('Arial',12,'italic'),text='Default',fill=THEME_COLOR)
        
        self.right_image = PhotoImage(file='./images/true.png')
        self.wrong_image = PhotoImage(file='./images/false.png')
        self.false = Button(image=self.wrong_image,highlightthickness=0,command=self.true_clicked)
        self.false.grid(row=2,column=1,padx=50)
        self.true = Button(image=self.right_image,highlightthickness=0,command=self.false_clicked)
        self.true.grid(row=2, column=0,padx=50)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text= f"You've reached the end of the quiz. \nScore: {self.quiz.score}/10")
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def true_clicked(self):
        check =self.quiz.check_answer('true')
        self.get_next_question()
        self.score_label.config(text=f'Score: {self.quiz.score}')
        self.feedback_check(check)


    def false_clicked(self):
        check = self.quiz.check_answer('false')
        self.get_next_question()
        self.score_label.config(text=f'Score: {self.quiz.score}')
        self.feedback_check(check)

    def feedback_check(self,is_right):

        if is_right:
            self.canvas.config(bg='green')
            # self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
            # self.canvas.config(bg='red')

        self.window.after(1000,self.get_next_question)




