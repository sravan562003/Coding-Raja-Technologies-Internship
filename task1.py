from tkinter import *

window = Tk()
window.title("To-do-List")

data_dict = {}
import json

def add():
    task_name = task_entry.get()
    task_details = {
        "Priority": priority_variable.get(),
        "DueDate": duedate_entry.get(),
        "Status": status_variable.get()
    }
    data_dict[task_name] = task_details

    with open("to-do-list-data.txt", "w") as file:
        json.dump(data_dict, file)

    display_listbox.insert(END, task_name)

def delete():
    curselection_variable = display_listbox.curselection()
    if curselection_variable:
        index = curselection_variable[0]
        task_name = display_listbox.get(index)
        display_listbox.delete(index)
        data_dict.pop(task_name)  # Remove task from the dictionary

        with open("to-do-list-data.txt", "w") as file:
            json.dump(data_dict, file)

def display_selected_task(event):
    display_taskinfo_listbox.delete(0, END)  # Clear previous values
    selected_index = display_listbox.curselection()
    if selected_index:
        selected_task = display_listbox.get(selected_index)
        task_details = data_dict.get(selected_task)
        if task_details:
            for detail_name, detail_value in task_details.items():
                display_taskinfo_listbox.insert(END, f"{detail_name}: {detail_value}")

center_label = Label(window, text="To-do-List-Application", width=20, bg='#6666FF', fg='#FFFFFF', font=("Times New roman", 40, "bold"))
center_label.place(x=480, y=20)

task_entry = Entry(window, width=20, font=("Arial", 25))
task_entry.place(x=40, y=150)

task_label = Label(window, text="Task: ", font=(20))
task_label.place(x=40, y=120)

priority_options = ["High", "Medium", "Low"]
priority_variable = StringVar()
priority_variable.set(priority_options[0])

priority_option = OptionMenu(window, priority_variable, *priority_options)
priority_option.place(x=40, y=250)
priority_option.config(width=53, height=2)

priority_label = Label(window, text="Priority: ", font=(20))
priority_label.place(x=40, y=220)

duedate_entry = Entry(window, width=20, font=("Arial", 25))
duedate_entry.place(x=40, y=350)

duedate_label = Label(window, text="Due Date: ", font=(20))
duedate_label.place(x=40, y=320)

status_options = ["Incomplete", "Complete"]
status_variable = StringVar()
status_variable.set(status_options[0])

complete_option = OptionMenu(window, status_variable, *status_options)
complete_option.place(x=40, y=450)
complete_option.config(width=53, height=2)

status_label = Label(window, text="Status: ", font=(20))
status_label.place(x=40, y=420)

add_button = Button(window, text="ADD", bg="#CC9933", width=10, font=("bold"), command=add)
add_button.place(x=40, y=550)

delete_button = Button(window, text="Delete", bg="#CC9933", width=10, font=("bold"), command=delete)
delete_button.place(x=230, y=550)

label_6 = Label(window, text="To-do Tasks: ", font=(20))
label_6.place(x=520, y=120)

display_listbox = Listbox(window, height=8, width=20, font=("Raleway", 30))
display_listbox.place(x=520, y=150)
display_listbox.bind("<<ListboxSelect>>", display_selected_task)  # Bind the selection event

label_7 = Label(window, text="Task Info:", font=(20))
label_7.place(x=1040, y=120)

display_taskinfo_listbox = Listbox(window, height=8, width=20, font=("Raleway", 30))
display_taskinfo_listbox.place(x=1040, y=150)

window.mainloop()