
from tkinter import *
import csv

# base window
window = Tk()
window.title("Start Menu")
window.geometry('200x200')
password = StringVar(window)
id = StringVar(window)

# modes
def customer_screen():
    window.minsize(width=500, height=500)
    customer_frame = Frame(window, width=500, height=500, bg="yellow")
    customer_frame.grid(row=0, column=0)

def employee_screen():
    window.minsize(width=500, height=500)
    employee_frame = Frame(window, width=500, height=500, bg="red")
    employee_frame.grid(row=0, column=0)

def sign_in_menu():
    # initial frame
    sign_in_frame = Frame(window, width=200, height=200, name="sign in")
    sign_in_frame.grid(row=0, column=0)

    # id label and entry
    id_label = Label(sign_in_frame, text="ID")
    id_label.grid(row=0, column=0)
    id_entry = Entry(sign_in_frame, textvariable=id)
    id_entry.grid(row=0, column=1)

    # password label and entry
    password_label = Label(sign_in_frame, text="Password")
    password_label.grid(row=1, column=0)
    password_entry = Entry(sign_in_frame, textvariable=password)
    password_entry.grid(row=1, column=1)

    # valid entry label
    global invalid_label
    invalid_label = Label(sign_in_frame)
    invalid_label.grid(row=2, column=1)

    # sign in button
    sign_in_button = Button(sign_in_frame, text="Sign in", command=validate_entry)
    sign_in_button.grid(row=3, column=1)

# helper functions
def validate_entry():
    curr_user_id = None
    curr_user_pass = None
    curr_user_status = None
    if not id.get().isnumeric():
        print("Invalid ID")
        invalid_label.config(text="Invalid ID")
        return
    with open("Users.csv", "r") as users:
        users.readline()
        accounts = users.readlines()
        for a in accounts:
            a = a.split(',')
            if a[0] == id.get():
                curr_user_id = a[0].strip()
                if a[1] == password.get():
                    curr_user_pass = a[1].strip()
                    curr_user_status = a[2].strip()
                    if curr_user_status == "employee":
                        employee_screen()
                        return
                    elif curr_user_status == "customer":
                        customer_screen()
                        return
                    else:
                        invalid_label.config(text="Invalid user status,\nupdate users file")
                        print("Invalid user status, update users file")
                    return
                else:
                    if password.get() == "":
                        print("Invalid password")
                        invalid_label.config(text="Invalid password")
                    else:
                        print("Incorrect password")
                        invalid_label.config(text="Incorrect password")
                    break
    if curr_user_id is None:
        print("No user found, ask an employee to create one")
        invalid_label.config(text="No user found,\nask an employee to\ncreate one")

sign_in_menu()
window.mainloop()
