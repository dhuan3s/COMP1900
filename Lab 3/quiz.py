score = int(input("Enter your quiz score: "))

if score <= 59:
    feedback = "failing"
elif 59 < score < 80:
    feedback = "passing"
elif 79 < score < 90:
    feedback = "good"
elif score >= 90:
    feedback = "excellent"


if (score >= 90) or (79 < score < 90):
    print(f"That score is {feedback}!")
elif (score <= 59) or (59 < score < 80):
    print(f"That score is {feedback}.")