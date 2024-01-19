import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question=None


    def next_question(self):

        self.current_question = self.question_list[self.question_number]
        cur=html.unescape(self.current_question.text)
        self.question_number += 1
        return cur

    def still_has_question(self):

        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self,user_answer):
        
        value=self.question_list[self.question_number]
        value=value.answer
        if user_answer.lower() == value.lower():
            self.score += 1
            return True
            
        else:
            return False
            




