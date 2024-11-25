from tkinter import *
import csv

# base window
window = Tk()
window.title("Start Menu")
window.geometry('200x200')

# variables
password = StringVar(window)
id = StringVar(window)

add_password = StringVar(window) 
add_id = StringVar(window)

book_name = StringVar(window)
author_last_name = StringVar(window)
author_first_name = StringVar(window)
total_copies = StringVar(window)

# modes
def customer_screen():
    window.minsize(width=500, height=500)
    customer_frame = Frame(window, width=500, height=500)
    customer_frame.grid(row=0, column=0)

    # user inventory
    inventory = []
    late_fees = 0
    item_count = 0
    with open(str(id.get()) + ' Customer Inventory.csv', mode='r') as file:
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

    # book name label and entry
    book_name_label = Label(customer_frame, text="Book Name")
    book_name_label.grid(row=3, column=0)
    book_name_entry = Entry(customer_frame, textvariable=book_name)
    book_name_entry.grid(row=4, column=0)

    # check out button
    check_out_button = Button(customer_frame, text="Check Out", command=check_out_book)
    check_out_button.grid(row=5, column=0)

    # return button
    return_button = Button(customer_frame, text="Return", command=return_book)
    return_button.grid(row=6, column=0)

    # checkout and return entry labels
    global checkout_and_return_label
    checkout_and_return_label = Label(customer_frame)
    checkout_and_return_label.grid(row=7, column=0)

def employee_screen():
    window.minsize(width=500, height=500)
    employee_frame = Frame(window, width=500, height=500, bg="red")
    employee_frame.grid(row=0, column=0)

        # book details label and entry
    book_name_label = Label(employee_frame, text="Book Name")
    book_name_label.grid(row=0, column=0)
    book_name_entry = Entry(employee_frame, textvariable=book_name)
    book_name_entry.grid(row=0, column=1)

    author_last_name_label = Label(employee_frame, text="Author Last Name")
    author_last_name_label.grid(row=1, column=0)
    author_last_name_entry = Entry(employee_frame, textvariable=author_last_name)
    author_last_name_entry.grid(row=1, column=1)

    author_first_name_label = Label(employee_frame, text="Author First Name")
    author_first_name_label.grid(row=2, column=0)
    author_first_name_entry = Entry(employee_frame, textvariable=author_first_name)
    author_first_name_entry.grid(row=2, column=1)

    total_copies_label = Label(employee_frame, text="Total Copies")
    total_copies_label.grid(row=3, column=0)
    total_copies_entry = Entry(employee_frame, textvariable=total_copies)
    total_copies_entry.grid(row=3, column=1)

    # add book button
    add_book_button = Button(employee_frame, text="Add book to stock", command=add_book)
    add_book_button.grid(row=4, column=1)

    # employee details label and entry
    id_label = Label(employee_frame, text="ID")
    id_label.grid(row=5, column=0)
    id_entry = Entry(employee_frame, textvariable=add_id)
    id_entry.grid(row=5, column=1)
    
    password_label = Label(employee_frame, text="Password")
    password_label.grid(row=6, column=0)
    password_entry = Entry(employee_frame, textvariable=add_password)
    password_entry.grid(row=6, column=1)

    # add employee button
    add_employee_button = Button(employee_frame, text="Add employee to database", command=add_employee)
    add_employee_button.grid(row=7, column=1)

    # add book and employee entry labels
    global add_book_and_employee_label
    add_book_and_employee_label = Label(employee_frame)
    add_book_and_employee_label.grid(row=8, column=1)

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

def check_out_book():
    inventory = []
    with open("Library Inventory.csv", mode="r", newline='') as books:
        stock = csv.reader(books)
        for line in stock:
            inventory.append(line)
    books.close()

    users_inventory = []
    with open("Customer Inventory.csv", mode="r", newline='') as books:
        stock = csv.reader(books)
        for line in stock:
            users_inventory.append(line)
    books.close()

    for row in users_inventory:
        if row[0] == book_name.get() and row[1] == id.get():
            print("You already have this book checked out")
            checkout_and_return_label.config(text="You already have this book checked out")
            return

    for row in inventory:
        if row[0] == book_name.get():
            if int(row[4]) > 0:
                row[4] = str(int(row[4]) - 1)
                row[5] = str(int(row[5]) + 1)
                print("Book checked out successfully")
                checkout_and_return_label.config(text="Book checked out successfully")
                break
            else:
                print("No copies available for checkout")
                checkout_and_return_label.config(text="No copies available for checkout")
                return

    with open("Library Inventory.csv", mode="w", newline='') as books:
        stock = csv.writer(books)
        stock.writerows(inventory)
    books.close()

def return_book():
    inventory = []
    with open("Library Inventory.csv", mode="r", newline='') as books:
        stock = csv.reader(books)
        for line in stock:
            inventory.append(line)
    books.close()

    for row in inventory:
        if row[0] == book_name.get():
            if int(row[5]) > 0:
                row[4] = str(int(row[4]) + 1)
                row[5] = str(int(row[5]) - 1)
                print("Book returned successfully")
                checkout_and_return_label.config(text="Book returned successfully")
                break
            else:
                print("No copies of this book are currently checked out")
                checkout_and_return_label.config(text="No copies of this book are currently checked out")
                return

    with open("Library Inventory.csv", mode="w", newline='') as books:
        stock = csv.writer(books)
        stock.writerows(inventory)
    books.close()

def add_book():
    inventory = []
    with open("Library Inventory.csv", mode="r", newline='') as books:
        stock = csv.reader(books)
        for line in stock:
            inventory.append(line)
    books.close()

    inventory.append([book_name.get(), author_last_name.get(), author_first_name.get(), total_copies.get(), total_copies.get(), 0])
    print("Book added")
    add_book_and_employee_label.config(text="Book added")

    with open("Library Inventory.csv", mode="w", newline='') as books:
        stock = csv.writer(books)
        stock.writerows(inventory)
    books.close()

def add_employee():
    table = []
    with open("Users.csv", mode="r", newline='') as users:
        accounts = csv.reader(users)
        for line in accounts:
            table.append(line)
    users.close()

    table.append([id.get(), password.get(), "employee"])
    print("Employee added")
    add_book_and_employee_label.config(text="Employee added")

    with open("Users.csv", mode="w", newline='') as users:
        accounts = csv.writer(users)
        accounts.writerows(table)
    users.close()

sign_in_menu()
window.mainloop()
