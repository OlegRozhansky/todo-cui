import modules.functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText()
add_button = sg.Button("Add")
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout=[ [label], [input_box, add_button] ])
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values)

window.close()