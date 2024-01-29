import modules.functions
import PySimpleGUI as sg
from modules import functions

label = sg.Text('Type in a to-do')
input_box = sg.InputText()
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

todos = [item.strip("\n") for item in functions.get_todos()]
listbox = sg.Listbox(values=todos, size=(20, 12), key='-LIST-', enable_events=True)

# Create the Window
window = sg.Window('To Do App', layout=[ [label, input_box, add_button], [listbox], [exit_button]])
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    print('You entered ', values)
    if event == 'Add':
        todos = functions.get_todos()
        todos.append(values[0])
        functions.write_todos(p_todos=todos)

window.close()