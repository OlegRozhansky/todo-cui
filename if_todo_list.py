from modules import functions
from modules.some_script_file import some_function

import time
now = time.strftime("%Y-%B-%d %H:%M:%S")
print(now)

some_function()

print(f"it was invoked from {__name__}")
while True:
    user_action = input("Enter add, edit, complete, show or exit: ").strip()
    if user_action.startswith('add '):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(p_todos=todos)
    elif user_action == 'show' or user_action == 'display':

        todos = [item.strip("\n") for item in functions.get_todos()]

        print([(idx, item) for idx, item in enumerate(todos)])

        for n, item in enumerate(todos):
            print(f"{n + 1} - {item}")
        # print("last index, item:", n, item)
    elif user_action.startswith('edit '):
        try:
            item_number = int(user_action[5:]) - 1

            todos = functions.get_todos()

            todos[item_number] = input("Enter a new todo: ").strip() + "\n"

            functions.write_todos(p_todos=todos)
        except ValueError:
            print("Your command is invalid")
            continue

    elif user_action.startswith('complete '):
        try:
            item_number = int(user_action[9:]) - 1

            todos = functions.get_todos()

            removed_todo = todos.pop(item_number)

            functions.write_todos(p_todos=todos)

            print(f"Todo {removed_todo} was removed from the list")

        except IndexError:
            print("There is no item with specified index")
            continue

    elif user_action == 'exit':
        break
