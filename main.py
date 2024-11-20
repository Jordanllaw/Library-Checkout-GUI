
from tkinter import *
import csv

def read_data():
    table = []
    with open('Library Inventory.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            table.append(line)
    file.close()
    # Initialize the data frame
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
    table.append([first_name_value.get(), last_name_value.get(),
    student_number_value.get()])
    # with open('Library Inventory.csv', mode ='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(table)
    # file.close()

window = Tk()
window.title("Library Inventory")
window.geometry('700x500')
first_name_value = StringVar(window)
last_name_value = StringVar(window)
student_number_value = StringVar(window)
data_frame = LabelFrame(window, text="Books in our Library")
data_frame.grid(row=6, column=0)
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
mainloop()
