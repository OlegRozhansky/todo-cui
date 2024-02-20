FILE_PATH = "files/todos.txt"


def get_todos(filepath=FILE_PATH):
    with open(filepath, "r") as file:
        return file.readlines()


def write_todos(p_todos, filepath=FILE_PATH):
    with open(filepath, "w") as file:
        file.writelines(p_todos)


if __name__ == '__main__':
    print("hello from functions")
else:
    print(f"hello from {__name__}")
