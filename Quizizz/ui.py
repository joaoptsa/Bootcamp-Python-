THEME_COLOR="#375362"
from tkinter import *
from quizBrain import QuizBrain

class QuizInterface:

    def pressed_True(self):
        if self.quiz.still_has_question() == False:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"Your result {self.quiz.score}/10")
        else:
            self.quiz.check_answer("True")
            self.get_next_question()



    def pressed_False(self):
        if self.quiz.still_has_question() == False:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"Your result {self.quiz.score}/10")
        else:
            self.quiz.check_answer("False")
            self.get_next_question()



    def get_next_question(self):
        self.canvas.config(bg="white")
        if  self.quiz.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)






    def __init__(self, quizBrain: QuizBrain):
        self.quiz=quizBrain
        self.window=Tk()
        self.window.title("Game")
        self.window.config(padx=30,pady=30,bg=THEME_COLOR)
        self.score_label=Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=0,columnspan=2)

        self.canvas=Canvas(width=400,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,text="",fill=THEME_COLOR,width=280)
        self.canvas.grid(row=2,column=0,columnspan=2)

        self.true_button=Button(text="True",highlightthickness=5,fg="black",command=self.pressed_True)
        self.true_button.grid(row=5,column=4,columnspan=6,ipadx=3)

        self.false_button = Button(text="False", highlightthickness=5, fg="black",command=self.pressed_False)
        self.false_button.grid(row=3, column=2,columnspan=4)

        self.get_next_question()
      
        self.window.mainloop()














