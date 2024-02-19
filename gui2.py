import PySimpleGUI as sg
from modules import functions

label = sg.Text('Type in a to-do')
input_box = sg.InputText()
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

# Create the Window
window = sg.Window('To Do App',
                   layout=[[label, input_box, add_button], [exit_button]],
                   font=('Helvetica', 20))
# Event Loop to process "events" and get the "values" of the inputs
window.read()
print("Hello")
window.close()