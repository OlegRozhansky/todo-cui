prompt = "Enter a title:"
todos = []
while True:
    user_input = input(prompt)
    if user_input == 'exit':
        break
    todos.append(user_input)
print(todos)
