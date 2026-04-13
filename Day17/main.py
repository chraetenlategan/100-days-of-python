# Main.py
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")


#quiz_brain.py

class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer =input(f"Q.{self.question_number}: {current_question.text} True/False")
        self.check_answer(user_answer, current_question.answer)
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score +=1
        else:
            print("You got it wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"You score is {self.score}/{self.question_number}")
        print("\n")



#question_model.py

class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer
    

#data.py

question_data = {
    "response_code": 0,
    "results": [
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Sports",
            "question": "ATP tennis hosted several tournaments on carpet court before being replaced to reduce injuries.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Sports",
            "question": "Formula E is an auto racing series that uses hybrid electric race cars.",
            "correct_answer": "False",
            "incorrect_answers": ["True"]
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Sports",
            "question": "During Wimbledon, spectators in the grounds can buy the tennis balls that have been used in matches.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Sports",
            "question": "In 2008, Usain Bolt set the world record for the 100 meters with one shoelace untied.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Sports",
            "question": "Wilt Chamberlain scored his infamous 100-point-game against the New York Knicks in 1962.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Sports",
            "question": "The Olympics tennis court is a giant green screen.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Sports",
            "question": "Skateboarding was included in the 2020 Summer Olympics in Tokyo.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Sports",
            "question": "The first episode of WWF Monday Night RAW aired on January 11, 1990.",
            "correct_answer": "False",
            "incorrect_answers": ["True"]
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Sports",
            "question": "Soccer player Cristiano Ronaldo opened a museum dedicated to himself.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Sports",
            "question": "Tennis was once known as Racquetball.",
            "correct_answer": "False",
            "incorrect_answers": ["True"]
        }
    ]
}
