"""
This file consist functions used by main program.

"""
import os
import PySimpleGUI as Sg


def save_file(dirr, name, login, pwd):
    """
    This function purpose is to save file with login and password plain string, and before it check if file with the
    same name didn't exist.
    :param dirr: directory where file will be saved
    :param name: name of the file
    :param login: login
    :param pwd: password
    :return: if file exist return true to raise exception in main file
    """
    check_if_exits = os.path.exists(dirr + name)
    if check_if_exits:
        return check_if_exits

    os.chdir(dirr)
    plain_string = login + ' ' + pwd

    # Create and save file
    x = open(name, 'wt')
    x.write(plain_string)
    x.close()


def open_file():
    """
    Purpose of this function is to open existing file consisting the pair login - password and show it to the user in
    simple popup window.
    :return: no specified return for this function
    """
    # Open file
    file_path = Sg.popup_get_file('Select password file')
    try:
        x = open(file_path, 'r')
        log_pwd = x.readline().split()

        # Create popup with login and password
        Sg.popup(f"Your login is: {log_pwd[0]} \nand password is: {log_pwd[1]}", title="Open file", line_width=300)

    except (TypeError, FileNotFoundError):
        pass



