import streamlit as st
from modules import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo']
    if (new_todo is not None) and (len(new_todo) > 0):
        todos.append(new_todo + "\n")
        functions.write_todos(todos)


def remove_item():
    for item in todos:
        if st.session_state[item]:
            todos.remove(item)
            functions.write_todos(todos)
            st.session_state.pop(item)
            break


st.title("My todo app")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(label=todo, on_change=remove_item, key=todo)

st.text_input(label="todo", on_change=add_todo, key='new_todo')

st.session_state
