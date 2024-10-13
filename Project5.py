import random
import json
import time

# Definition to get questions from our json file
def load_question():
    with open("questions.json", "r") as f:
        questions = json.load(f)["questions"]
    return questions

# Definition to generate random questions
def get_random_questions(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)
    # Randomly select the specified number of unique questions
    random_questions = random.sample(questions, num_questions)
    return random_questions

# Definition to select and show the question on the screen automatically
def ask_question(question):  # Changed to accept a single question
    print(question["question"])  # Access the question text properly
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")  # Improved string formatting

    number = int(input("Select the correct number: "))
    if number < 1 or number > len(question["options"]):
        print("Invalid choice, defaulting to wrong answer.")
        return False

    correct = question["options"][number - 1] == question["answer"]
    return correct

# Main Function
if __name__ == "__main__":  # Added a main guard
    questions = load_question()
    total_questions = int(input("Enter the number of questions: "))
    random_questions = get_random_questions(questions, total_questions)
    correct = 0
    start_time = time.time()

    for question in random_questions:
        is_correct = ask_question(question)
        if is_correct:
            correct += 1
        print("-----------------")

    completed_time = time.time() - start_time
    print("Summary")
    print("Total Questions:", total_questions)
    print("Correct Answers:", correct)
    print("Score:", f"{round((correct / total_questions) * 100, 2)}%")  # Improved string formatting
    print("Time:", round(completed_time, 2), "seconds")
