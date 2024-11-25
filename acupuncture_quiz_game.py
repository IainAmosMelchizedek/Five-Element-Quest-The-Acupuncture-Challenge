import random

# Questions and answers
questions = [
    {
        "question": "Which acupuncture point is known as the 'Spirit Gate' and associated with the Earth element?",
        "options": ["HT-9", "HT-8", "HT-7", "HT-4"],
        "answer": "C"
    },
    {
        "question": "Which acupuncture point is located on the radial side of the pinky finger?",
        "options": ["HT-9", "HT-7", "HT-3", "HT-4"],
        "answer": "A"
    },
    {
        "question": "Which acupuncture point is associated with the Fire element?",
        "options": ["HT-3", "HT-4", "HT-8", "HT-9"],
        "answer": "C"
    },
    {
        "question": "Which acupuncture point is located on the wrist crease in line with the little finger?",
        "options": ["HT-3", "HT-7", "HT-9", "HT-4"],
        "answer": "B"
    },
    {
        "question": "Which acupuncture point is called the 'Lesser Sea' and associated with the Water element?",
        "options": ["HT-7", "HT-8", "HT-4", "HT-3"],
        "answer": "D"
    }
]

# Shuffle the questions for randomness
random.shuffle(questions)

# Introduction
print("Welcome to the Five Element Acupuncture Quiz Game!")
print("Answer the following questions by typing the letter corresponding to your choice (A, B, C, or D).")
print()

# Initialize score
score = 0

# Loop through the questions
for idx, q in enumerate(questions):
    print(f"Question {idx + 1}: {q['question']}")
    print("A) " + q["options"][0])
    print("B) " + q["options"][1])
    print("C) " + q["options"][2])
    print("D) " + q["options"][3])

    # Get the user's answer
    answer = input("Your Answer: ").strip().upper()

    # Check if the answer is correct
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. The correct answer was {q['answer']}.\n")

# Display final score
print(f"Your Final Score: {score}/{len(questions)}")
if score == len(questions):
    print("Excellent! You're an acupuncture master!")
elif score > len(questions) // 2:
    print("Good job! You know quite a bit about acupuncture.")
else:
    print("Keep studying, and you'll master the Five Elements soon!")
