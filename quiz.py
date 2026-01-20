questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['London', 'Paris', 'Berlin', 'Madrid'],
        'answer': '2'
    },
    {
        'question': 'Which Python data structure uses key-value pairs?',
        'options': ['List', 'Tuple', 'Dictionary', 'Set'],
        'answer': '3'
    },
    {
        'question': 'What is the result of 3 + 2 * 2 in Python?',
        'options': ['10', '7', '8', '9'],
        'answer': '2'
    },
    {
        'question': 'Which keyword is used to define a function in Python?',
        'options': ['func', 'define', 'def', 'function'],
        'answer': '3'
    },
    {
        'question': 'Which loop is used to iterate over a sequence?',
        'options': ['for loop', 'while loop', 'loop', 'repeat loop'],
        'answer': '1'
    }
]

score = 0
question_number = 1

print("Welcome to the Holton College Python Quiz!")
print("Answer with 1, 2, 3, or 4\n")

for question in questions:
    print(f"Question {question_number}: {question['question']}")

    for i in range(4):
        print(f"{i + 1}. {question['options'][i]}")

    user_answer = input("Your answer: ")

    if user_answer == question['answer']:
        print("Correct!\n")
        score = score + 1
    else:
        print(f"Incorrect! The correct answer was {question['answer']}.\n")

    question_number = question_number + 1

print(f"Quiz Complete!")
print(f"You scored {score} out of {len(questions)} correct.")
print("Thank you for playing!")