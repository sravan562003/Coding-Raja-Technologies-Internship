from tkinter import *
window=Tk()
window.title("Budget Tracker")

data_dict={}
import json

def add():
    cashflow = cashflowtype_variable.get()
    category = category_entry.get()
    amount = amount_entry.get()

    # Check if the cashflow type already exists in the dictionary
    if cashflow in data_dict:
        data_dict[cashflow].append({"Category": category, "Amount": amount})
    else:
        data_dict[cashflow] = [{"Category": category, "Amount": amount}]

    with open("budget-tracker-data.txt", "w") as file:
        json.dump(data_dict, file)



def Income():

    # Check if 'Income' key exists in data_dict
    if 'Income' in data_dict:
        income_list = data_dict['Income']
        total_income = sum(float(item['Amount']) for item in income_list)
        # Clear previous items in the listbox
        display_listbox.delete(0, END)
        # Insert the total income into the listbox
        display_listbox.insert(END, f'Total Income: ${total_income:.2f}')
    else:
        # If 'Income' key doesn't exist, display a message
        display_listbox.delete(0, END)
        display_listbox.insert(END, 'No Income data found.')










def Expenses():
    # Check if 'Expenses' key exists in data_dict
    if 'Expenses' in data_dict:
        expenses_list = data_dict['Expenses']
        total_expenses = sum(float(item['Amount']) for item in expenses_list)
        # Clear previous items in the listbox
        display_listbox.delete(0, END)
        # Insert the total expenses into the listbox
        display_listbox.insert(END, f'Total Expenses: ${total_expenses:.2f}')
    else:
        # If 'Expenses' key doesn't exist, display a message
        display_listbox.delete(0, END)
        display_listbox.insert(END, 'No Expenses data found.')










def Budget():
    # Check if both 'Income' and 'Expenses' keys exist in data_dict
    if 'Income' in data_dict and 'Expenses' in data_dict:
        income_list = data_dict['Income']
        expenses_list = data_dict['Expenses']

        # Calculate total income and expenses
        total_income = sum(float(item['Amount']) for item in income_list)
        total_expenses = sum(float(item['Amount']) for item in expenses_list)

        # Calculate the difference (budget) between total income and expenses
        budget_difference = total_income - total_expenses

        # Clear previous items in the listbox
        display_listbox.delete(0, END)
        # Insert the budget difference into the listbox
        display_listbox.insert(END, f'Budget Difference: ${budget_difference:.2f}')
    else:
        # If either 'Income' or 'Expenses' key doesn't exist, display a message
        display_listbox.delete(0, END)
        display_listbox.insert(END, 'Insufficient data to calculate budget difference.')





def Display():
    # Clear previous items in the listbox
    display_listbox.delete(0, END)

    # Display Income details
    if 'Income' in data_dict:
        display_listbox.insert(END, 'Income Details:')
        for item in data_dict['Income']:
            display_listbox.insert(END, f"Category: {item['Category']}, Amount: {item['Amount']}")
        display_listbox.insert(END, '')  # Add an empty line for separation

    # Display Expenses details
    if 'Expenses' in data_dict:
        display_listbox.insert(END, 'Expenses Details:')
        for item in data_dict['Expenses']:
            display_listbox.insert(END, f"Category: {item['Category']}, Amount: {item['Amount']}")











center_label=Label(window,text="Budget Tracker",width=20,bg="#6666FF",fg="#FFFFFF",font=("Times New Roman",40,"bold"))
center_label.place(x=480,y=20)

cashflowlabel=Label(window, text="Cash Flow Type: ", font=(20))
cashflowlabel.place(x=40,y=120)

cashflowtype=["Income","Expenses"]
cashflowtype_variable=StringVar()
cashflowtype_variable.set(cashflowtype[0])

cashflowmenu=OptionMenu(window,cashflowtype_variable,*cashflowtype)
cashflowmenu.place(x=40,y=160)
cashflowmenu.config(width=53,height=2)

category_entry_label=Label(window,text="Category: ",font=(20))
category_entry_label.place(x=40,y=240)
category_entry=Entry(window,width=20,font=("Arial",25))
category_entry.place(x=40,y=280)

amount_label=Label(window,text="Enter the amount: ",font=(20))
amount_label.place(x=40,y=360)

amount_entry=Entry(window,width=20,font=("Arial",25))
amount_entry.place(x=40,y=400)

add_button=Button(window,text="ADD",bg="#CC9933",width=10,font=("bold"),command=add)
add_button.place(x=280,y=480)

display_button=Button(window,text="DISPLAY",bg="#CC9933",width=10,font=("bold"),command=Display)
display_button.place(x=40,y=480)


display_label=Label(window,text="Display Budget:",font=(20))
display_label.place(x=520,y=120)

display_listbox=Listbox(window,height=6,width=20,font=("Raleway",30))
display_listbox.place(x=520,y=150)

income_button=Button(window,text="INCOME",bg="#CC9933",width=10,font=("bold"),command=Income)
income_button.place(x=520,y=480)

expenses_button=Button(window,text="EXPENSES",bg="#CC9933",width=10,font=("bold"),command=Expenses)
expenses_button.place(x=680,y=480)

budget_button=Button(window,text="BUDGET",bg="#CC9933",width=10,font=("bold"),command=Budget)
budget_button.place(x=840,y=480)









































































































window.mainloop()