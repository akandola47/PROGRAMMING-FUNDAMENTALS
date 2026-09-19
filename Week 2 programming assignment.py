# Author: Arsh Kandola
# Date: September 13, 2026
# Description: Test Grading Calculator
# Tier Level: Base

print("Test Grading Calculator!")
Student_name = input("Enter student's name: ").strip().title()

# 5 quiz scores
score1 = int(input("Enter quiz score 1: "))
score2 = int(input("Enter quiz score 2: "))
score3 = int(input("Enter quiz score 3: "))
score4 = int(input("Enter quiz score 4: "))
score5 = int(input("Enter quiz score 5: "))

# Store scores in a list
quiz_scores = [score1, score2, score3, score4, score5]

# Calculate the average
average = sum(quiz_scores) / len(quiz_scores)

# Store letter grades in a tuple
grade_letters = ("A", "B", "C", "D", "F")

# Determine the letter grade and personalized message
if average >= 90:
    grade = grade_letters[0]
    message = "Excellent work!"
elif average >= 80:
    grade = grade_letters[1]
    message = "Great job! Keep it up!"
elif average >= 70:
    grade = grade_letters[2]
    message = "Good effort! Keep working hard."
elif average >= 60:
    grade = grade_letters[3]
    message = "Consider visiting office hours."
else:
    grade = grade_letters[4]
    message = "Consider visiting office hours and getting extra help."

# Display the report
print("\n--- Student Grade Report ---")
print(f"Student Name: {Student_name}")
print(f"Quiz Scores: {quiz_scores}")
print(f"Average: {average:.1f}")
print(f"Letter Grade: {grade}")
print(f"Message: {message}")