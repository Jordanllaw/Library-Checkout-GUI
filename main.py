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
    customer_frame = Frame(window, width=500, height=500)
    customer_frame.grid(row=0, column=0)

    # user inventory
    inventory = []
    late_fees = 0
    item_count = 0
    with open('Customer Inventory Template.csv', mode='r') as file:
        first_line = file.readline()
        categories = ''
        temp_array = []

        # adding : to the end of each category
        for i in range(len(first_line)):
            if first_line[i] == ',' or i == len(first_line) - 1:
                categories += ':'
                temp_array.append(categories)
                categories = ''
            else:
                categories += first_line[i]

        # adding the first line to the inventory array
        inventory.append(temp_array)

        # adding the rest of the lines to the inventory array
        csv_file = csv.reader(file)
        for line in csv_file:
            if int(line[1]) < 0 and line[2] == "Book":
                late_fees += 0.2 * int(line[1])
            if int(line[1]) < 0 and line[2] == "Game":
                late_fees += 0.3 * int(line[1])
            inventory.append(line)
            item_count += 1
    file.close()

    # Initialize the data frame
    data_frame = LabelFrame(customer_frame, text="Currently Checked Out")
    data_frame.grid(row=6, column=1)

    for widget in data_frame.winfo_children():
        widget.destroy()
    # Now table is the csv file in nested-list form
    for r in range(len(inventory)):
        for c in range(len(inventory[r])):
            cell_value = inventory[r][c]
            cell_label = Label(data_frame, text=cell_value)
            cell_label.grid(row=r, column=c)

    # main checked out items
    input_frame = LabelFrame(customer_frame, text="Information")
    input_frame.grid(row=0, column=0)

    # first_name_label = Label(input_frame, text="Username: " + str(id))
    # first_name_label.grid(row=0, column=0)
    last_name_label = Label(input_frame, text="ID: " + id.get())
    last_name_label.grid(row=0, column=0)
    last_name_label = Label(input_frame, text="Total Items: " + str(item_count))
    last_name_label.grid(row=3, column=0)

    # late fees
    input_frame = LabelFrame(customer_frame, text="Late Fees")
    input_frame.grid(row=0, column=1)

    first_name_label = Label(input_frame, text="Fees Owed: $" + str(abs(late_fees)) + '0')
    first_name_label.grid(row=0, column=1)
    last_name_label = Label(input_frame, text="(Late books: $0.20/day)")
    last_name_label.grid(row=1, column=1)
    last_name_label = Label(input_frame, text="(Late games: $0.30/day)")
    last_name_label.grid(row=2, column=1)

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

def read_data():
    table = []
    with open('Library Inventory.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            table.append(line)
    file.close()

    # Initialize the data frame
    data_frame = LabelFrame(window, text="Books in our Library")
    data_frame.grid(row=6, column=0)

    for widget in data_frame.winfo_children():
        widget.destroy()
    # Now table is the csv file in nested-list form
    for row_num in range(len(table)):
        for column_num in range(len(table[row_num])):
            cell_value = table[row_num][column_num]
            cell_label = Label(data_frame, text=cell_value)
            cell_label.grid(row=row_num, column=column_num)


def write_data():
    table = []
    with open('Library Inventory.csv', mode ='r', newline='') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            table.append(line)
    file.close()

    # Now table is the csv file in nested-list form
    # Update the table and do the write
    # table.append([first_name_value.get(), last_name_value.get()])
    # with open('Library Inventory.csv', mode ='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(table)
    # file.close()

sign_in_menu()
window.mainloop()
