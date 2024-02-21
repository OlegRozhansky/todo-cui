import streamlit as st
from modules import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo']
    if (new_todo is not None) and (len(new_todo) > 0):
        todos.append(new_todo + "\n")
        functions.write_todos(todos)


st.title("My todo app")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="todo", on_change=add_todo, key='new_todo')

st.session_state
