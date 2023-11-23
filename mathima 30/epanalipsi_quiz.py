class Quiz:
    def __init__(self):
        self.questions = {}

    def add_question(self, question, correct_answer):
        self.questions[question] = correct_answer
        print(f"Question added: {question}")

    def take_quiz(self):
        score = 0
        for question, correct_answer in self.questions.items():
            user_answer = input(f"{question} (Enter your answer: ")
            if user_answer.lower() == correct_answer.lower():
                print("Correct!")
                score = 1
            else:
                print(f"Incorrect! The correct answer is{correct_answer}")

        print(f"You scored {score}/ {len(self.questions)} in the quiz")

    def display_question(self):
        if self.questions:
            print("Quiz Questions:")
            for question in self.questions:
                print(f" {question}")
            else:
                print("No question added to the quiz yet")


quiz = Quiz
quiz.add_question("What is the capital of France?", "Paris")
quiz.add_question("What is 2+2", "4")
quiz.add_question("Who wrote 'Romeo and Juliet?", "Shakespeare")

quiz.display_question()
quiz.take_quiz()
