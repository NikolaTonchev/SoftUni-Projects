from json import loads, dump, load

from buying_page import display_products
from helpers import clean_screen
from canvas import *


def get_all_users_data():
    info_data = []
    with open('./db/users_information.json', 'r') as users_file:
        for line in users_file:
            info_data.append(loads(line))  # For appending string load for others????CHECK IT
    return info_data


def render_entry():
    with open("./db/products_data.json", 'r') as stock:  #
        info = load(stock)
    for item_key, item_value in info.items():  # THIS IS MY ADDITION
        info[item_key]['quantity'] = 20

    with open("./db/products_data.json", 'w') as stock:  #
        dump(info, stock)

    register_button = Button(
        root,
        text="Register",
        bg='green',
        fg='white',
        width=20,
        height=3,
        command=register
    )  # This Creates the button and modifies it but does not show it on the program

    log_in_button = Button(
        root,
        text='Login',
        bg='Blue',
        fg='white',
        width=20,
        height=3,
        command=login
    )  # This Creates the button and modifies it but does not show it on the program

    frame.create_window(350, 260, window=register_button)
    # This puts the Button in the program so you can see it and interact with it
    frame.create_window(350, 320, window=log_in_button)


def login():
    clean_screen()
    frame.create_text(100, 110, text='Username:')
    frame.create_text(100, 140, text='Password:')

    frame.create_window(200, 110, window=username_box)
    frame.create_window(200, 140, window=password_box)

    login_button = Button(
        root,
        text="Login",
        bg='blue',
        fg='white',
        width=10,
        height=2,
        command=logging
    )

    frame.create_window(220, 180, window=login_button)


def logging():
    if check_login():
        display_products()
    else:
        frame.create_text(175, 230, text="Invalid username or password!", fill='red')


def check_login():
    info_data = get_all_users_data()

    for i in range(len(info_data)):
        username = info_data[i]['username']
        password = info_data[i]['password']

        if username == username_box.get() and password == password_box.get():
            return True

    return False


def register():
    clean_screen()  # Clears everything
    frame.create_text(100, 50, text='First name:')
    frame.create_text(100, 80, text='Last name:')
    frame.create_text(100, 110, text='Username:')
    frame.create_text(100, 140, text='Password:')

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 80, window=last_name_box)
    frame.create_window(200, 110, window=username_box)
    frame.create_window(200, 140, window=password_box)

    registration_button = Button(
        root,
        text="Register",
        bg='green',
        fg='white',
        width=10,
        height=2,
        command=registration
    )

    frame.create_window(220, 180, window=registration_button)


def registration():
    info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": password_box.get(),
        'products': []
    }  # This takes what is inside the space where you type stuff
    if check_registration(info_dict):
        with open("./db/users_information.json", 'a') as users_file:
            users_file.write("\n")
            dump(info_dict, users_file)  # Storing dictionaries in other files!!!CHECK IT
            login()


def check_registration(info):
    for el in info.values():
        if el == '':
            frame.create_text(
                300,
                300,
                text='We are missing some information, please check your fields',
                fill='red',
                tag='error'
            )
            return False
    frame.delete('error')

    info_data = get_all_users_data()

    for i in range(len(info_data)):
        if info_data[i]['username'] == info['username']:
            frame.create_text(
                300,
                300,
                text='Username already exists!',
                fill='red',
                tag='error',
            )
            return False
    frame.delete('error')
    return True


first_name_box = Entry(root, bd=0)  # Creates a space to type like in USERNAME or PASSWORD
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0)
