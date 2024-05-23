from question_model import Question
from data import question_data
from quiz_game import QuizBrain

#TODO 1 : write a loop to iterate over the question_data.
# create a Question object from eacch entry in question_data.
# append each Question object to the question_ba
question_bank =[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
   
quiz =   QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")
print("/n")
    

