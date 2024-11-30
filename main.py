from tkinter import *
import csv
from tkinter import font

# base window
window = Tk()
window.title("Start Menu")
window.geometry('300x200')

# initial log in window --------------------------------------------------------

# variables
password = StringVar(window)
id = StringVar(window)
default_font = font.nametofont('TkTextFont')  # default font for tkinter -> this is a dict

# text inputs
add_password = StringVar(window) 
add_id = StringVar(window)
add_item_name = StringVar(window)
add_item_creator = StringVar(window)
add_total_copies = StringVar(window)

item_name = StringVar(window)
add_item_and_user_text = ''
checkout_and_return_text = ''


# frames
customer_frame = Frame(window, width=1400, height=700)
employee_frame = Frame(window, width=1400, height=700)

# customer screen --------------------------------------------------------------
def customer_screen():
    window.minsize(width=1370, height=620)
    global customer_frame
    customer_frame = Frame(window, width=1400, height=700)
    customer_frame.grid(row=0, column=0, padx=10, pady=10)

    # user inventory -----------------------------------------------------------
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

    # Initialize the data frame ------------------------------------------------
    data_frame = LabelFrame(customer_frame, text="Currently Checked Out", font=(default_font["family"],default_font["size"] + 6))
    data_frame.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

    for widget in data_frame.winfo_children():
        widget.destroy()
    # Now table is the csv file in nested-list form
    for r in range(len(inventory)):
        for c in range(len(inventory[r])):
            cell_value = inventory[r][c]
            if r == 0:
                cell_label = Label(data_frame, text=cell_value, font=(default_font["family"],default_font["size"] + 2, "underline"))
            else:
                cell_label = Label(data_frame, text=cell_value)
            cell_label.grid(row=r, column=c, padx=5, pady=5)

    # library inventory --------------------------------------------------------
    library_inventory = []
    with open("Library Inventory.csv", mode="r") as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            library_inventory.append(line)

    data_frame2 = LabelFrame(customer_frame, text="Current Library Inventory", font=(default_font["family"],default_font["size"] + 6))
    data_frame2.grid(row=0, column=2, rowspan=10, columnspan=10)

    for widget in data_frame2.winfo_children():
        widget.destroy()
    for r in range(len(library_inventory)):
        for c in range(len(library_inventory[r])):
            cell_value = library_inventory[r][c]
            if r == 0:
                cell_label = Label(data_frame2, text=cell_value, font=(default_font["family"],default_font["size"] + 2, "underline"))
            else:
                cell_label = Label(data_frame2, text=cell_value)
            cell_label.grid(row=r, column=c)

    # welcome text -------------------------------------------------------------
    input_frame = Frame(customer_frame, width=300, height=300)
    input_frame.grid(row=0, column=0, padx=10, pady=10)
    Label(input_frame, text="Welcome Back Customer " + str(id.get()) + "!", font=(default_font["family"],default_font["size"] + 10)).grid(row=0, column=0, columnspan=2, pady=20)

    Label(input_frame, text="Total Items: " + str(item_count), font=(default_font["family"],default_font["size"] + 2)).grid(row=1, column=0, padx=15)

    # late fees ----------------------------------------------------------------
    # input_frame = Frame(customer_frame).grid(row=1, column=1)

    first_name_label = Label(input_frame, text="Fees Owed: $" + str(abs(late_fees)) + '0', padx=60, font=(default_font["family"],default_font["size"] + 2))
    first_name_label.grid(row=2, column=0)
    last_name_label = Label(input_frame, text="(Late books: $0.20/day)", padx=15)
    last_name_label.grid(row=3, column=0)
    last_name_label = Label(input_frame, text="(Late games: $0.30/day)")
    last_name_label.grid(row=4, column=0)

    # book name label and entry ------------------------------------------------

    Label(input_frame, text="Item Name").grid(row=1, column=1, padx=15)
    Entry(input_frame, textvariable=item_name).grid(row=2, column=1, padx=15)

    # check out button
    Button(input_frame, text="Check Out", command=check_out_book).grid(row=3, column=1, padx=15)

    # return button
    Button(input_frame, text="Return", command=return_item).grid(row=4, column=1, padx=15)

    # checkout and return entry labels -----------------------------------------
    global checkout_and_return_label
    global checkout_and_return_text
    checkout_and_return_label = Label(customer_frame, text=checkout_and_return_text)
    checkout_and_return_label.grid(row=7, column=0)

# employee screen ---------------------------------------------------------------
def employee_screen():
    window.minsize(width=1370, height=620)
    global employee_frame
    employee_frame = Frame(window, width=1400, height=700)
    employee_frame.grid(row=0, column=0, padx=10, pady=10)

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
        if late_fees == 0:
            late_fees = 0.0

    # library inventory
    library_inventory = []
    with open("Library Inventory.csv", mode="r") as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            library_inventory.append(line)

    data_frame2 = LabelFrame(employee_frame, text="Current Library Inventory", font=(default_font["family"],default_font["size"] + 6))
    data_frame2.grid(row=0, column=2, rowspan=10, columnspan=10)

    for widget in data_frame2.winfo_children():
        widget.destroy()
    for r in range(len(library_inventory)):
        for c in range(len(library_inventory[r])):
            cell_value = library_inventory[r][c]
            if r == 0:
                cell_label = Label(data_frame2, text=cell_value, font=(
                default_font["family"], default_font["size"] + 2, "underline"))
            else:
                cell_label = Label(data_frame2, text=cell_value)
            cell_label.grid(row=r, column=c)

    input_frame = Frame(employee_frame, width=300, height=300)
    input_frame.grid(row=0, column=0, padx=10, pady=10)
    Label(input_frame, text="Welcome Back Employee " + str(id.get()) + "!",
          font=(default_font["family"], default_font["size"] + 10)).grid(row=0, column=0, columnspan=4, pady=20)

    Label(input_frame, text="Total Items: " + str(item_count),
          font=(default_font["family"], default_font["size"] + 2)).grid(row=1,column=0, columnspan=2)

    # late fees
    first_name_label = Label(input_frame,
                             text="Fees Owed: $" + str(abs(late_fees)) + '0',
                             font=(
        default_font["family"], default_font["size"] + 2))
    first_name_label.grid(row=2, column=0, columnspan=2)
    last_name_label = Label(input_frame, text="(Late books: $0.20/day)")
    last_name_label.grid(row=3, column=0, columnspan=2)
    last_name_label = Label(input_frame, text="(Late games: $0.30/day)")
    last_name_label.grid(row=4, column=0, columnspan=2)

    # book name label and entry ------------------------------------------------

    Label(input_frame, text="Item Name").grid(row=1, column=2, padx=15, columnspan=2)
    Entry(input_frame, textvariable=item_name).grid(row=2, column=2, padx=15, columnspan=2)

    # check out button
    Button(input_frame, text="Check Out", command=check_out_book).grid(row=3,
                                                                       column=2,
                                                                       padx=15, columnspan=2)

    # return button
    Button(input_frame, text="Return", command=return_item).grid(row=4,
                                                                 column=2,
                                                                 padx=15, columnspan=2)

    # checkout and return entry labels
    global checkout_and_return_label
    global checkout_and_return_text
    checkout_and_return_label = Label(input_frame, text=checkout_and_return_text)
    checkout_and_return_label.grid(row=7, column=0)

    # spacer
    Label(input_frame, text='').grid(row=8, column=0, columnspan=4)

    # book details label and entry
    book_name_label = Label(input_frame, text="Item Name:")
    book_name_label.grid(row=9, column=0)
    book_name_entry = Entry(input_frame, textvariable=add_item_name)
    book_name_entry.grid(row=9, column=1, columnspan=2)

    author_last_name_label = Label(input_frame, text="Item Creator:")
    author_last_name_label.grid(row=10, column=0)
    author_last_name_entry = Entry(input_frame, textvariable=add_item_creator)
    author_last_name_entry.grid(row=10, column=1, columnspan=2)

    total_copies_label = Label(input_frame, text="Total Copies:")
    total_copies_label.grid(row=11, column=0)
    total_copies_entry = Entry(input_frame, textvariable=add_total_copies)
    total_copies_entry.grid(row=11, column=1, columnspan=2)

    # add book button
    add_book_button = Button(input_frame, text="Add book", command=add_book)
    add_book_button.grid(row=10, column=3)

    # add game button
    add_game_button = Button(input_frame, text="Add game", command=add_game)
    add_game_button.grid(row=11, column=3)

    # spacer
    Label(input_frame, text='').grid(row=12, column=0, columnspan=4)

    # employee details label and entry
    id_label = Label(input_frame, text="ID")
    id_label.grid(row=13, column=0)
    id_entry = Entry(input_frame, textvariable=add_id)
    id_entry.grid(row=13, column=1, columnspan=2)

    password_label = Label(input_frame, text="Password")
    password_label.grid(row=14, column=0)
    password_entry = Entry(input_frame, textvariable=add_password)
    password_entry.grid(row=14, column=1, columnspan=2)

    # add employee button
    add_employee_button = Button(input_frame, text="Add employee", command=add_employee)
    add_employee_button.grid(row=13, column=3)

    add_customer_button = Button(input_frame, text="Add customer",  command=add_customer)
    add_customer_button.grid(row=14, column=3)

    # add book and employee entry labels
    global add_item_and_user_label
    global add_item_and_user_text
    add_item_and_user_label = Label(input_frame, text=add_item_and_user_text)
    add_item_and_user_label.grid(row=17, column=1)

    Label(input_frame, text='').grid(row=18, column=0, columnspan=4)

    # Initialize the data frame
    data_frame = LabelFrame(input_frame, text="Currently Checked Out", font=(
        default_font["family"], default_font["size"] + 6))
    data_frame.grid(row=19, column=0, padx=10, pady=10, columnspan=4)

    for widget in data_frame.winfo_children():
        widget.destroy()

    # Now table is the csv file in nested-list form
    for r in range(len(inventory)):
        for c in range(len(inventory[r])):
            cell_value = inventory[r][c]
            if r == 0:
                cell_label = Label(data_frame, text=cell_value, font=(
                    default_font["family"], default_font["size"] + 2,
                    "underline"))
            else:
                cell_label = Label(data_frame, text=cell_value)
            cell_label.grid(row=r, column=c)


def sign_in_menu():
    # initial frame
    sign_in_frame = Frame(window, width=400, height=200, name="sign in")
    sign_in_frame.grid(row=0, column=0, padx=10, pady=10)

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
    global curr_user_status
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

def check_out_book():
    global checkout_and_return_text
    inventory = []
    with open("Library Inventory.csv", mode="r", newline='') as items:
        stock = csv.reader(items)
        for line in stock:
            inventory.append(line)

    users_inventory = []
    with open(f"{id.get()} Customer Inventory.csv", mode="r", newline='') as items:
        stock = csv.reader(items)
        for line in stock:
            users_inventory.append(line)

    for row in users_inventory:
        if row[0] == item_name.get():
            print("You already have this book checked out")
            checkout_and_return_text = "You already have this book checked out"
            return
        
    if item_name.get() != "": 
        found = False
        for row in inventory:
            if row[0] == item_name.get():
                found = True
                if int(row[3]) > 0:
                    row[3] = str(int(row[3]) - 1)
                    row[4] = str(int(row[4]) + 1)
                    users_inventory.append([item_name.get(), '14', row[5]])
                    print("Item checked out successfully")
                    checkout_and_return_text = "Item checked out successfully"
                    break
                else:
                    print("No copies available for checkout")
                    checkout_and_return_text = "No copies available for checkout"
                    return
        if not found:
            print("Invalid input! Please enter an item from the inventory")
            checkout_and_return_text = "Invalid input! Please enter an item from inventory"
            return
    else: 
        print("Please enter the name of an item")
        checkout_and_return_text = "Please enter the name of an item"
        return

    with open("Library Inventory.csv", mode="w", newline='') as items:
        stock = csv.writer(items)
        stock.writerows(inventory)

    with open(f"{id.get()} Customer Inventory.csv", mode='w', newline='') as items:
        stock = csv.writer(items)
        stock.writerows(users_inventory)

    global employee_frame
    global customer_frame
    global curr_user_status
    if curr_user_status == 'employee':
        employee_frame.destroy()
        employee_screen()
    elif curr_user_status == 'customer':
        customer_frame.destroy()
        customer_screen()

def return_item():
    global checkout_and_return_text
    inventory = []
    with open("Library Inventory.csv", mode="r", newline='') as items:
        stock = csv.reader(items)
        for line in stock:
            inventory.append(line)

    customer_inventory = []
    customer_items = []
    with open(f"{id.get()} Customer Inventory.csv", mode='r', newline='') as items:
        stock = csv.reader(items)
        for line in stock:
            customer_inventory.append(line)
            customer_items.append(line[0])

    if item_name.get() != "":
        found = False
        for row in inventory: 
            if row[0] == item_name.get(): 
                found = True
                if row[0] in customer_items:
                    if int(row[4]) > 0:
                        row[3] = str(int(row[3]) + 1)
                        row[4] = str(int(row[4]) - 1)
                        print("Item returned successfully")
                        checkout_and_return_text = "Item return successfully"
                        i = customer_items.index(row[0])
                        customer_inventory.pop(i)
                        break
                else: 
                    print("No copies to be returned")
                    checkout_and_return_text = "No copies to be returned"
                    return
        if not found:
            print("Invalid input! Please enter an item from the inventory")
            checkout_and_return_text = "Invalid input! Please enter an item from the inventory"
    else: 
        print("Please enter the name of an item")
        checkout_and_return_text = "Please enter the name of an item"
        return
    
    with open("Library Inventory.csv", mode="w", newline='') as items:
        stock = csv.writer(items)
        stock.writerows(inventory)

    with open(f"{id.get()} Customer Inventory.csv", mode='w', newline='') as items:
        stock = csv.writer(items)
        stock.writerows(customer_inventory)

    global employee_frame
    global customer_frame
    global curr_user_status
    if curr_user_status == 'employee':
        employee_frame.destroy()
        employee_screen()
    elif curr_user_status == 'customer':
        customer_frame.destroy()
        customer_screen()

def add_book():
    global add_item_and_user_text
    inventory = []
    with open("Library Inventory.csv", mode="r", newline='') as items:
        stock = csv.reader(items)
        for line in stock:
            inventory.append(line)

    if add_item_name.get() and add_item_creator.get() and add_total_copies.get() != "":
        if add_total_copies.get().isnumeric() and int(add_total_copies.get()) > 0: 
            item_exists = False
            for row in inventory:
                if row[0] == add_item_name.get() and row[1] == add_item_creator.get():
                    row[2] = str(int(row[2]) + int(add_total_copies.get()))
                    row[3] = str(int(row[3]) + int(add_total_copies.get()))
                    item_exists = True
                    print("Updated the number of copies")
                    add_item_and_user_text = "Updated the number of copies"
                    break
            if not item_exists: 
                inventory.append([add_item_name.get(), add_item_creator.get(), add_total_copies.get(), add_total_copies.get(), 0, 'Book'])
                print("Book added")
                add_item_and_user_text = "Book added"
        else: 
            print("Invalid number of copies")
            add_item_and_user_text = "Invalid number of copies"
    else:
        print("Please fill in the missing information")
        add_item_and_user_text = "Please fill in the missing information"

    with open("Library Inventory.csv", mode="w", newline='') as items:
        stock = csv.writer(items)
        stock.writerows(inventory)
    
    global employee_frame
    global customer_frame
    global curr_user_status
    employee_frame.destroy()
    employee_screen()

def add_game():
    global add_item_and_user_text
    inventory = []
    with open("Library Inventory.csv", mode="r", newline='') as items:
        stock = csv.reader(items)
        for line in stock:
            inventory.append(line)

    if add_item_name.get() and add_item_creator.get() and add_total_copies.get() != "":
        if add_total_copies.get().isnumeric() and int(add_total_copies.get()) > 0: 
            item_exists = False
            for row in inventory:
                if row[0] == add_item_name.get() and row[1] == add_item_creator.get():
                    row[2] = str(int(row[2]) + int(add_total_copies.get()))
                    item_exists = True
                    print("Updated the number of copies")
                    add_item_and_user_text = "Updated the number of copies"
                    break
            if not item_exists:
                inventory.append([add_item_name.get(), add_item_creator.get(), add_total_copies.get(), add_total_copies.get(), 0, 'Game'])
                print("Game added")
                add_item_and_user_text = "Game added"
        else: 
            print("Invalid number of copies")
            add_item_and_user_text = "Invalid number of copies"
    else:
        print("Please fill in the missing information")
        add_item_and_user_text = "Please fill in the missing information"

    with open("Library Inventory.csv", mode="w", newline='') as items:
        stock = csv.writer(items)
        stock.writerows(inventory)
    
    global employee_frame
    global customer_frame
    global curr_user_status
    employee_frame.destroy()
    employee_screen()

def add_employee():
    global add_item_and_user_text
    table = []
    with open("Users.csv", mode="r", newline='') as users:
        accounts = csv.reader(users)
        for line in accounts:
            table.append(line)

    if add_id.get() and add_password.get() != "":
        if add_id.get().isnumeric():
            id_taken = False
            for row in table: 
                if row[0] == add_id.get(): 
                    id_taken = True
                    break
            if not id_taken: 
                table.append([add_id.get(), add_password.get(), "employee"])
                print("Employee added")
                add_item_and_user_text = "Employee Added"
            else:
                print("ID already taken")
                add_item_and_user_text = "ID already taken"
        else: 
            print("Invalid ID. Please enter a number ID")
            add_item_and_user_text = "Invalid ID. Please enter a number ID"
    else:
        print("Please fill in the missing information")
        add_item_and_user_text = "Please fill in the missing information"

    with open("Users.csv", mode="w", newline='') as users:
        accounts = csv.writer(users)
        accounts.writerows(table)

    with open(f"{add_id.get()} Customer Inventory.csv", mode='w', newline='') as inventory:
        inventory.write("Item Name,Days Until Due,Type")

    global employee_frame
    global customer_frame
    global curr_user_status
    employee_frame.destroy()
    employee_screen()

def add_customer():
    global add_item_and_user_text
    table = []
    with open("Users.csv", mode="r", newline='') as users:
        accounts = csv.reader(users)
        for line in accounts:
            table.append(line)
    
    if add_id.get() and add_password.get() != "":
        if add_id.get().isnumeric():
            id_taken = False
            for row in table: 
                if row[0] == add_id.get():
                    id_taken = True
                    break
            if not id_taken:
                table.append([add_id.get(), add_password.get(), "customer"])
                print("Customer added")
                add_item_and_user_text = "Customer added"
            else:
                print("ID already taken")
                add_item_and_user_text = "ID already taken"
        else: 
            print("Invalid ID. Please enter a number ID")
            add_item_and_user_text = "Invalid ID. Please enter a number ID"
    else:
        print("Please fill in the missing information")
        add_item_and_user_text = "Please fill in the missing information"

    with open("Users.csv", mode="w", newline='') as users:
        accounts = csv.writer(users)
        accounts.writerows(table)

    with open(f"{add_id.get()} Customer Inventory.csv", mode='w', newline='') as inventory:
        inventory.write("Item Name,Days Until Due,Type")

    global employee_frame
    global customer_frame
    global curr_user_status
    employee_frame.destroy()
    employee_screen()

sign_in_menu()
window.mainloop()