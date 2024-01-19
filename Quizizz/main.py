from question import Question
from quizBrain import QuizBrain
from ui import QuizInterface
import requests


parameters={
    "amount":10,
    "category":12,
    "type":"boolean"}

response=requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data=response.json()
question_data=data["results"]
question_bank=[]


for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quizz = QuizBrain(question_bank)
ui=QuizInterface(quizz)





