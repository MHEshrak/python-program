questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
correct_answers = ("C", "D", "A", "A", "B")
question_num = 0
score = 0
user_answers = []

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    user_answers.append(user_answer)
    if user_answer == correct_answers[question_num]:
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT")
        print(f"Correct answers is {correct_answers[question_num]}")
    question_num += 1

print("--------------------")
print("       RESULT       ")
print("--------------------")

print("user_answers: ")
for user_answer in user_answers:
    print(user_answer, end=" ")
print()

print("correct_answers: ")
for correct_answer in correct_answers:
    print(correct_answer, end=" ")
print()

score = (score / len(questions) * 100)
print(f"Your Marks {score}%")
