import PySimpleGUI as sg
from modules import functions
import time
import os

if not os.path.exists(functions.FILE_PATH):
    with open(functions.FILE_PATH, "w"):
        pass

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key="todo", size=46)
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

# Create the Window
window = sg.Window('To Do App',
                   layout=[[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
                   font=('Helvetica', 20))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(time.strftime("%Y-%B-%d %H:%M:%S"))
    print(event, values)
    match event:
        case 'Exit' | None:
            break
        case 'Add':
            new_item = values['todo']
            if len(new_item) > 0:
                todos = functions.get_todos()
                todos.append(new_item if '\n' in new_item else new_item + '\n')
                functions.write_todos(p_todos=todos)
                # window['todos'].update(todos)
                list_box.update(todos)
            else:
                sg.popup("You cannot add an empty todo!", font=('Helvetica', 20))
        case 'todos':
            window['todo'].update(values['todos'][0])
        case 'Edit':
            new_item = values['todo']
            if (len(new_item) > 0) and (len(values['todos']) != 0):
                old_item = values['todos'][0]
                todos = functions.get_todos()
                index_to_replace = todos.index(old_item)
                todos[index_to_replace] = new_item if '\n' in new_item else new_item + '\n'
                functions.write_todos(p_todos=todos)
                #window['todos'].update(todos)
                list_box.update(todos)
            else:
                sg.popup("This is a wrong state", font=('Helvetica', 20))
        case 'Complete':
            if len(values['todos']) != 0:
                todos = functions.get_todos()
                todos.remove(values['todos'][0])
                functions.write_todos(p_todos=todos)
                list_box.update(todos)
                window['todo'].update('')
            else:
                sg.popup("You should select an item!", font=('Helvetica', 20))

window.close()