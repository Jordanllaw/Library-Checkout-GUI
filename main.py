
from tkinter import *
import tkinter as tk
import csv

# helper functions
def check_empty(s: StringVar):
    if s.get() == "":
        return True
    return False

# def read_data():
#     table = []
#     with open('Library Inventory.csv', mode ='r')as file:
#         csvFile = csv.reader(file)
#         for line in csvFile:
#             table.append(line)
#     file.close()
#     # Initialize the data frame
#     for widget in data_frame.winfo_children():
#         widget.destroy()
#     # Now table is the csv file in nested-list form
#     for row_num in range(len(table)):
#         for column_num in range(len(table[row_num])):
#             cell_value = table[row_num][column_num]
#             cell_label = Label(data_frame, text=cell_value)
#             cell_label.grid(row=row_num, column=column_num)

# def write_data():
#     table = []
#     with open('Library Inventory.csv', mode ='r', newline='') as file:
#         csvFile = csv.reader(file)
#         for line in csvFile:
#             table.append(line)
#     file.close()
#     # Now table is the csv file in nested-list form
#     # Update the table and do the write
#     table.append([first_name_value.get(), last_name_value.get(),
#     student_number_value.get()])
#     with open('Library Inventory.csv', mode ='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(table)
#     file.close()

########## SCREEN ##########

# base window
window = Tk()
window.title("Start Menu")
window.geometry('200x200')
password = StringVar(window)
id = StringVar(window)

# fonts
# style1 = font.Font(size=25)
# style2 = font.Font(size=12)

# modes
def mode_chooser():
    with open("Users.csv", "r") as users:
        curr_user_id = None
        curr_user_pass = None
        curr_user_status = None
        users.readline()
        accounts = users.readlines()
        print(accounts)
        for a in accounts:
            a = a.split(',')
            if a[0] == id:
                curr_user_id = a[0]
                if a[1] == password:
                    curr_user_pass = a[1]
                    curr_user_status = a[2]
                    break
                else:
                    print("incorrect password")
                    break
    if curr_user_id is None:
        print("No user found, ask an employee to create one")


def sign_in_menu():
    window.title("Sign In")

    # initial frame
    input_frame = LabelFrame(window, text="Sign in")
    input_frame.grid(row=0, column=0)

    # id label and entry
    id_label = Label(input_frame, text="ID")
    id_label.grid(row=0, column=0)
    id_entry = Entry(input_frame, textvariable=id)
    id_entry.grid(row=0, column=1)

    # password label and entry
    password_label = Label(input_frame, text="Password")
    password_label.grid(row=1, column=0)
    password_entry = Entry(input_frame, textvariable=password)
    password_entry.grid(row=1, column=1)

    # valid entry label
    valid_label = Label(input_frame)

    # sign in button
    sign_in_button = Button(input_frame, text="Sign in", command=mode_chooser)
    sign_in_button["state"] = "disabled"
    sign_in_button.grid(row=2, column=1)
    tk.update_idletasks()
    tk.update()
    if not(check_empty(password)) and not(check_empty(id)):
        sign_in_button["state"] = "enabled"

# first_name_value = StringVar(window)
# last_name_value = StringVar(window)
# student_number_value = StringVar(window)
# data_frame = LabelFrame(window, text="Books in our Library")
# data_frame.grid(row=6, column=0)
# input_frame = LabelFrame(window, text="Book Search")
# input_frame.grid(row=0, column=0)
# first_name_label = Label(input_frame, text="Book Title")
# first_name_label.grid(row=0, column=0)
# first_name_entry = Entry(input_frame, textvariable=first_name_value)
# first_name_entry.grid(row=0, column=1)
# last_name_label = Label(input_frame, text="Author")
# last_name_label.grid(row=1, column=0)
# last_name_entry = Entry(input_frame, textvariable=last_name_value)
# last_name_entry.grid(row=1, column=1)
# submit_button = Button(input_frame, text='Checkout', command=write_data)
# submit_button.grid(row=3, column=1)
# show_button = Button(input_frame, text='Show Inventory', command=read_data)
# show_button.grid(row=3, column=0) 
sign_in_menu()
mainloop()
