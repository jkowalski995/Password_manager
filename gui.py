"""
This is the main program which initialize the main window and catch events.

"""
import PySimpleGUI as Sg
from functions import save_file, open_file

DEFAULT_PATH = "passwords/"

layout = [
    [Sg.Text("Key name", size=(40, 1)), Sg.InputText(key="-name-")],
    [Sg.Text("Login", size=(40, 1)), Sg.InputText(key="-login-")],
    [Sg.Text("Password", size=(40, 1)), Sg.InputText(key="-password-")],
    [Sg.Button("Save"), Sg.Button("Open")],
    [Sg.Exit()]
]

if __name__ == '__main__':

    window = Sg.Window(title="Password manager", layout=layout, margins=(100, 50))

    while True:
        event, values = window.read()
        print(event, values)

        # Exit the program
        if event == Sg.WINDOW_CLOSED or event == 'Exit':
            break

        key_name = values["-name-"]
        login = values["-login-"]
        pwd = values["-password-"]

        # Saving the password
        if event == "Save":

            # Check the values if any is empty
            if key_name == '' or login == '' or pwd == '':
                Sg.popup("Every field must be filled with proper value", title="Empty field!", line_width=300)
                continue

            # Save the file
            if save_file(DEFAULT_PATH, key_name, login, pwd):
                Sg.popup(f"The file with name {key_name} already exists! \nTry another name.", title="Name!",
                         line_width=300)
                continue

        # Opening the file with password
        if event == "Open":
            open_file()

    window.close()
