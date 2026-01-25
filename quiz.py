def get_questions():
    """
    Returns a list of quiz questions.
    Each question is stored as a dictionary with question text, options, and correct answer.
    """
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['London', 'Paris', 'Berlin', 'Madrid'],
            'answer': 2
        },
        {
            'question': 'Which data structure uses key-value pairs?',
            'options': ['List', 'Tuple', 'Dictionary', 'Set'],
            'answer': 3
        },
        {
            'question': 'What does CPU stand for?',
            'options': ['Central Processing Unit', 'Computer Personal Unit', 'Central Program Utility', 'Core Processing Unit'],
            'answer': 1
        },
        {
            'question': 'Which of these is a Python loop?',
            'options': ['repeat', 'for', 'loop', 'iterate'],
            'answer': 2
        },
        {
            'question': 'What symbol is used for comments in Python?',
            'options': ['//', '/*', '#', '--'],
            'answer': 3
        }
    ]
    return questions


def display_question(question_num, question_data):
    """
    Displays a single question with its options to the user.
    
    Parameters:
    question_num - the question number to display
    question_data - dictionary containing the question information
    """
    print(f"\nQuestion {question_num}: {question_data['question']}")
    
    # Display each option with its number
    for i in range(len(question_data['options'])):
        print(f"{i + 1}. {question_data['options'][i]}")


def get_user_answer():
    """
    Gets and validates the user's answer.
    Keeps asking until a valid input (1-4) is received.
    
    Returns:
    The user's answer as an integer
    """
    while True:
        try:
            user_input = input("Your answer: ")
            answer = int(user_input)
            
            # Check if answer is in valid range
            if answer >= 1 and answer <= 4:
                return answer
            else:
                print("Please enter a valid number between 1 and 4.")
        except ValueError:
            # This runs if the input cannot be converted to an integer
            print("Please enter a valid number between 1 and 4.")


def check_answer(user_answer, correct_answer):
    """
    Checks if the user's answer is correct.
    
    Parameters:
    user_answer - the number entered by the user
    correct_answer - the correct answer number
    
    Returns:
    True if correct, False if incorrect
    """
    if user_answer == correct_answer:
        return True
    else:
        return False


def run_quiz():
    """
    Main function that runs the entire quiz.
    Controls the flow of the program.
    """
    # Display welcome message
    print("Welcome to the Holton College Quiz!")
    print("Please answer with the number (1, 2, 3, or 4) of your choice\n")
    
    # Get the list of questions
    questions = get_questions()
    
    # Variable to keep track of the score
    score = 0
    total_questions = len(questions)
    
    # Loop through each question
    for i in range(total_questions):
        # Display the current question
        display_question(i + 1, questions[i])
        
        # Get the user's answer
        user_answer = get_user_answer()
        
        # Check if the answer is correct
        is_correct = check_answer(user_answer, questions[i]['answer'])
        
        # Give feedback and update score
        if is_correct:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect")
    
    # Display final results
    print("\nQuiz Complete!")
    print(f"You scored {score} out of {total_questions} correct.")
    print("Thank you for playing!")


# Run the quiz when the program starts
if __name__ == "__main__":
    run_quiz()
print("Thank you for playing!")
