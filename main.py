from tkinter import *
import csv

window = Tk()
window.title("Library Inventory")
window.geometry('700x500')


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


def main():
    first_name_value = StringVar(window)
    last_name_value = StringVar(window)
    input_frame = LabelFrame(window, text="Book Search")
    input_frame.grid(row=0, column=0)
    first_name_label = Label(input_frame, text="Book Title")
    first_name_label.grid(row=0, column=0)
    first_name_entry = Entry(input_frame, textvariable=first_name_value)
    first_name_entry.grid(row=0, column=1)
    last_name_label = Label(input_frame, text="Author")
    last_name_label.grid(row=1, column=0)
    last_name_entry = Entry(input_frame, textvariable=last_name_value)
    last_name_entry.grid(row=1, column=1)
    submit_button = Button(input_frame, text='Checkout', command=write_data)
    submit_button.grid(row=3, column=1)
    show_button = Button(input_frame, text='Show Inventory', command=read_data)
    show_button.grid(row=3, column=0)


def customer():
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
    data_frame = LabelFrame(window, text="Currently Checked Out")
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
    input_frame = LabelFrame(window, text="Information")
    input_frame.grid(row=0, column=0)

    first_name_label = Label(input_frame, text="Username: ")
    first_name_label.grid(row=0, column=0)
    last_name_label = Label(input_frame, text="ID: ")
    last_name_label.grid(row=1, column=0)
    last_name_label = Label(input_frame, text="Total Items: " + str(item_count))
    last_name_label.grid(row=3, column=0)

    # late fees
    input_frame = LabelFrame(window, text="Late Fees")
    input_frame.grid(row=0, column=1)

    first_name_label = Label(input_frame, text="Fees Owed: $" + str(abs(late_fees)) + '0')
    first_name_label.grid(row=0, column=1)
    last_name_label = Label(input_frame, text="(Late books: $0.20/day")
    last_name_label.grid(row=1, column=1)
    last_name_label = Label(input_frame, text="(Late games: $0.30/day")
    last_name_label.grid(row=2, column=1)


customer()
mainloop()
