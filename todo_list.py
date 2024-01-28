todos = []
while True:
    user_action = input("Enter add, edit, complete, show or exit: ").strip()
    match user_action:
        case 'add':
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(input("Enter a todo: ").strip() + "\n")

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        case 'show' | 'display':

            with open("files/todos.txt", "r") as file:
                todos = [item.strip("\n") for item in file.readlines()]
                # file.close()

            print([(idx, item) for idx, item in enumerate(todos)])

            for n, item in enumerate(todos):
                print(f"{n + 1} - {item}")
            # print("last index, item:", n, item)
        case 'edit':
            item_number = int(input("Enter a number of the todo to edit: ").strip()) - 1
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos[item_number] = input("Enter a new todo: ").strip() + "\n"

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case 'complete':
            item_number = int(input("Enter a number of the todo to complete: ").strip()) - 1
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            removed_todo = todos.pop(item_number)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

            print(f"Todo {removed_todo} was removed from the list")
        case 'exit':
            break
        case stupid_param:
            print("add-hoc param is", stupid_param)
