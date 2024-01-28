import json

with open("questions.json", "r") as file:
    content = file.read()
    data = json.loads(content)
statistics = []
score = 0
for (item_no, item) in enumerate(data):
    print(item["questionText"])
    for (i, option) in enumerate(item["alternatives"]):
        print(f"{i + 1} - {option}")
    user_answer = int(input("Enter your answer: "))
    item["user_choice"] = user_answer
    if item["user_choice"] == item["correctAnswer"]:
        score += 1

for (item_no, item) in enumerate(data):
    state = "Correct Answer" if item["user_choice"] == item["correctAnswer"] else "Incorrect Answer"
    print(f'{item_no + 1} {state}, "User Answer": {item["user_choice"]}, "Correct Answer": {item["correctAnswer"]}')

print(f"Score: {score}/{len(data)}")
