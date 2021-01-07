

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "Which of the following cannot be checked in a switch-case statement??\n(a) Float\n(b)Integer",
     "Which of the following is not logical operator??\n(a) &&\n(b)&",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("Your score is", score, "out of", len(questions))
     (print(" Great Success, Happy Learning @yearahul"))

run_quiz(questions)
