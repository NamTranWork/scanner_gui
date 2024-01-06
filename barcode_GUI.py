from datetime import datetime
import tkinter as tk
import pickle
import os

window = tk.Tk()
window.title('Barcode GUI')
label_text = "Select a Function"
add_text = ""
filename = "barcode_record.pkl"
func_indicator = 0

if os.path.exists(filename):
    with open(filename,'rb') as f:
        database = pickle.load(f)
else:
    database = {}

input_frame = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5, bg="black")
fRow1 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
fRow2 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
fRow3 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
fRow4 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
fRow5 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
fRow6 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
fRow7 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
log_frame = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5, bg="black")

scrollbar = tk.Scrollbar(master=log_frame)
log = tk.Listbox(master=log_frame, yscrollcommand=scrollbar.set, font='Georgia 14',bg='black', fg="white")

label = tk.Label(master=input_frame, relief = tk.GROOVE, text=label_text, fg="black", bg="white", font=("Arial",20), anchor="w")
input_text = tk.Entry(master=input_frame, relief = tk.GROOVE, fg="blue", bg="gray", font=("Arial",20))

def query():
    global label_text
    global func_indicator
    global input_text
    global log
    
    if (func_indicator == 0):
        label_text = "What do you want to query?"
        label.config(text=label_text)
        func_indicator = 1
        input_text.delete(0,tk.END)
        log.insert(0, "{}  [Query Item]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
        log.itemconfig(0, {'fg':'yellow'})
        log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
        log.itemconfig(0, {'fg':'white'})
        
def add_to_db():
    global label_text
    global func_indicator
    global input_text
    global log
    
    if (func_indicator == 0):
        label_text = "What do you want to add to database?"
        label.config(text=label_text)
        func_indicator = 2
        input_text.delete(0,tk.END)
        log.insert(0, "{}  [Add Item]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
        log.itemconfig(0, {'fg':'yellow'})
        log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
        log.itemconfig(0, {'fg':'white'})
        
def sub_from_db():
    global label_text
    global func_indicator
    global input_text
    global log
    
    if (func_indicator == 0):
        label_text = "What do you want to delete from database?"
        label.config(text=label_text)
        func_indicator = 3
        input_text.delete(0,tk.END)
        log.insert(0, "{}  [Delete Item]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
        log.itemconfig(0, {'fg':'yellow'})
        log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
        log.itemconfig(0, {'fg':'white'})
        
def edit_from_db():
    global label_text
    global func_indicator
    global input_text
    global log
    
    if (func_indicator == 0):
        label_text = "What do you want to edit from database?"
        label.config(text=label_text)
        func_indicator = 4
        input_text.delete(0,tk.END)
        log.insert(0, "{}  [Edit Item]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
        log.itemconfig(0, {'fg':'yellow'})
        log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
        log.itemconfig(0, {'fg':'white'})
        
def cancel():
    global input_text
    global func_indicator
    global log
    label_text = "Select a Function"
    label.config(text=label_text)
    func_indicator = 0
    input_text.delete(0,tk.END)
    log.insert(0, "{}  [Cancel]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
    log.itemconfig(0, {'fg':'yellow'})
    log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
    log.itemconfig(0, {'fg':'white'})
    
def save_to_database():
    global filename
    global database
    global label_text
    global input_text
    with open(filename,'wb') as f:
        pickle.dump(database,f)
    
    log.insert(0, "{}  [Save Database]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
    log.itemconfig(0, {'fg':'yellow'})
    if label_text == "Function doesn't exist. Choose another":
        label_text = "Select a Function"
        label.config(text=label_text)
        input_text.delete(0,tk.END)
        log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
        log.itemconfig(0, {'fg':'white'})
        
def reset():
    global input_text
    global log
    input_text.delete(0,tk.END)
    log.insert(0, "{}  [Reset]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
    log.itemconfig(0, {'fg':'yellow'})
    
def exit_window():
    window.destroy()
    
def show_database():
    global label_text
    global log
    print(database)
    
    log.insert(0, "{}  [Show Database]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
    log.itemconfig(0, {'fg':'yellow'})
    if label_text == "Function doesn't exist. Choose another":
        label_text = "Select a Function"
        label.config(text=label_text)
        input_text.delete(0,tk.END)
        log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
        log.itemconfig(0, {'fg':'white'})
        
def check_valid_command():
    global label_text
    global func_indicator
    global input_text
    global log
    match input_text.get():
        case "Query Item":
            label_text = "What do you want to query?"
            label.config(text=label_text)
            func_indicator = 1
            input_text.delete(0,tk.END)
            log.insert(0, "{}  [Query Item]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
            log.itemconfig(0, {'fg':'yellow'})
        case "Add Item":
            label_text = "What do you want to add to database?"
            label.config(text=label_text)
            func_indicator = 2
            input_text.delete(0,tk.END)
            log.insert(0, "{}  [Add Item]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
            log.itemconfig(0, {'fg':'yellow'})
        case "Delete Item":
            label_text = "What do you want to delete from database?"
            label.config(text=label_text)
            func_indicator = 3
            input_text.delete(0,tk.END)
            log.insert(0, "{}  [Delete Item]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
            log.itemconfig(0, {'fg':'yellow'})
        case "Edit Item":
            label_text = "What do you want to edit from database?"
            label.config(text=label_text)
            func_indicator = 4
            input_text.delete(0,tk.END)
            log.insert(0, "{}  [Edit Item]".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y")))
            log.itemconfig(0, {'fg':'yellow'})
        case "Cancel":
            cancel()
        case "Reset":
            reset()
        case "Show Database":
            show_database()
            input_text.delete(0,tk.END)
        case "Save Database":
            save_to_database()
        case "Exit Window":
            exit_window()
        case default:
            label_text = "Function doesn't exist. Choose another"
            label.config(text=label_text)
            input_text.delete(0,tk.END)
            func_indicator = 0
    log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
    if label_text == "Function doesn't exist. Choose another":
        log.itemconfig(0, {'fg':'red'})
    else:
        log.itemconfig(0, {'fg':'white'})
    
def query_function():
    global label_text
    global input_text
    global func_indicator
    global database
    label_text = "Result: "
    red = False
    
    if (input_text.get() in database):
        label_text += database[input_text.get()]
    else:
        label_text += "Data not in database"
        red = True
    func_indicator = 0
    label.config(text=label_text)
    input_text.delete(0,tk.END)
    log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
    
    if red == True:
        log.itemconfig(0, {'fg':'red'})
    else:
        log.itemconfig(0, {'fg':'white'})
    
def add_function():
    global label_text
    global input_text
    global add_text
    global func_indicator
    global database
    red = False
    
    if (input_text.get() in database):
        label_text = "Result: Data already in database"
        func_indicator = 0
        red = True
    elif (label_text == "Insert value to database"):
        database[add_text] = input_text.get()
        label_text = "Result: Data added in database"
        func_indicator = 0
    else:
        add_text = input_text.get()
        label_text = "Insert value to database"
        
    label.config(text=label_text)
    input_text.delete(0,tk.END)
    log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
    
    if red == True:
        log.itemconfig(0, {'fg':'red'})
    else:
        log.itemconfig(0, {'fg':'white'})
    
def delete_function():
    global label_text
    global input_text
    global func_indicator
    global database
    label_text = "Result: "
    red = False
    
    if (input_text.get() in database):
        del database[input_text.get()]
        label_text += "Data successfully deleted"
    else:
        label_text += "Data not in database"
        red = True
        
    func_indicator = 0
    label.config(text=label_text)
    input_text.delete(0,tk.END)
    log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
    
    if red == True:
        log.itemconfig(0, {'fg':'red'})
    else:
        log.itemconfig(0, {'fg':'white'})
    
def edit_function():
    global label_text
    global input_text
    global add_text
    global func_indicator
    global database
    
    red = False
    if (add_text in database and label_text == "Modify value of selected data"):
        database[add_text] = input_text.get()
        label_text = "Result: Data successfully modified"
        func_indicator = 0
    elif (input_text.get() in database):
    	add_text = input_text.get()
    	label_text = "Modify value of selected data"
    else:
        label_text = "Result: Data not in database"
        func_indicator = 0
        red = True
        
    label.config(text=label_text)
    input_text.delete(0,tk.END)
    log.insert(0, "{}  {}".format(datetime.now().strftime("%H:%M:%S %m/%d/%Y"),label_text))
    
    if red == True:
        log.itemconfig(0, {'fg':'red'})
    else:
        log.itemconfig(0, {'fg':'white'})
        
def output():
    global input_text
    global func_indicator
    if (len(input_text.get()) > 0 and input_text.get() != "Cancel"):
        match func_indicator:
            case 0: check_valid_command()
            case 1: query_function()
            case 2: add_function()
            case 3: delete_function()
            case 4: edit_function()
            case default: pass 
    elif input_text.get() == "Cancel":
        cancel()
            
def scan_entry(event):
    output()
            
window.bind('<Return>',scan_entry)

font_type_and_size = ("Arial",18)
f1 = tk.Button(master=fRow1, fg="white", bg="blue", text="Query Item", font=font_type_and_size, command=query)
f2 = tk.Button(master=fRow1, fg="white", bg="blue", text="Add Item", font=font_type_and_size, command=add_to_db)
f3 = tk.Button(master=fRow1, fg="white", bg="blue", text="Delete Item", font=font_type_and_size, command=sub_from_db)
f4 = tk.Button(master=fRow1, fg="white", bg="blue", text="Edit Item", font=font_type_and_size, command=edit_from_db)
f5 = tk.Button(master=fRow2, fg="white", bg="blue", text="Cancel", font=font_type_and_size, command=cancel)
f6 = tk.Button(master=fRow2, fg="white", bg="blue", text="Reset", font=font_type_and_size, command=reset)
f7 = tk.Button(master=fRow2, fg="white", bg="blue", text="Output", font=font_type_and_size, command=output)
f8 = tk.Button(master=fRow2, fg="white", bg="blue", text="Exit Window", font=font_type_and_size, command=exit_window)
f9 = tk.Button(master=fRow3, fg="white", bg="green", text="Clean Bottle", font=font_type_and_size)
f10 = tk.Button(master=fRow3, fg="white", bg="green", text="Empty Container", font=font_type_and_size)
f11 = tk.Button(master=fRow3, fg="white", bg="green", text="Fill Bottles", font=font_type_and_size)
f12 = tk.Button(master=fRow3, fg="white", bg="green", text="New Bottles", font=font_type_and_size)
f13 = tk.Button(master=fRow4, fg="white", bg="green", text="New Drum", font=font_type_and_size)
f14 = tk.Button(master=fRow4, fg="white", bg="green", text="Qualify Drum", font=font_type_and_size)
f15 = tk.Button(master=fRow4, fg="white", bg="green", text="Query Container", font=font_type_and_size)
f16 = tk.Button(master=fRow5, fg="white", bg="red", text="Make Premix", font=font_type_and_size)
f17 = tk.Button(master=fRow5, fg="white", bg="red", text="New Lubelot", font=font_type_and_size)
f18 = tk.Button(master=fRow5, fg="white", bg="red", text="Qualify Libebottle", font=font_type_and_size)
f19 = tk.Button(master=fRow6, fg="white", bg="red", text="Qualify Premix", font=font_type_and_size)
f20 = tk.Button(master=fRow6, fg="white", bg="red", text="Query Lubebottle", font=font_type_and_size)
f21 = tk.Button(master=fRow6, fg="white", bg="red", text="Transfer Premix", font=font_type_and_size)
f22 = tk.Button(master=fRow7, fg="white", bg="orange", text="Show Database", font=font_type_and_size, command=show_database)
f23 = tk.Button(master=fRow7, fg="white", bg="orange", text="Save Database", font=font_type_and_size, command=save_to_database)

label.pack(fill=tk.X)
input_text.pack(fill=tk.X)

f1.pack(fill=tk.X , expand=True, side=tk.LEFT)
f2.pack(fill=tk.X , expand=True, side=tk.LEFT)
f3.pack(fill=tk.X , expand=True, side=tk.LEFT)
f4.pack(fill=tk.X, expand=True, side=tk.LEFT)
f5.pack(fill=tk.X , expand=True, side=tk.LEFT)
f6.pack(fill=tk.X , expand=True, side=tk.LEFT)
f7.pack(fill=tk.X , expand=True, side=tk.LEFT)
f8.pack(fill=tk.X, expand=True, side=tk.LEFT)
f9.pack(fill=tk.X , expand=True, side=tk.LEFT)
f10.pack(fill=tk.X , expand=True, side=tk.LEFT)
f11.pack(fill=tk.X , expand=True, side=tk.LEFT)
f12.pack(fill=tk.X, expand=True, side=tk.LEFT)
f13.pack(fill=tk.X , expand=True, side=tk.LEFT)
f14.pack(fill=tk.X , expand=True, side=tk.LEFT)
f15.pack(fill=tk.X, expand=True, side=tk.LEFT)
f16.pack(fill=tk.X , expand=True, side=tk.LEFT)
f17.pack(fill=tk.X , expand=True, side=tk.LEFT)
f18.pack(fill=tk.X, expand=True, side=tk.LEFT)
f19.pack(fill=tk.X , expand=True, side=tk.LEFT)
f20.pack(fill=tk.X , expand=True, side=tk.LEFT)
f21.pack(fill=tk.X, expand=True, side=tk.LEFT)
f22.pack(fill=tk.X , expand=True, side=tk.LEFT)
f23.pack(fill=tk.X, expand=True, side=tk.LEFT)

input_frame.pack(fill=tk.X)
fRow1.pack(fill=tk.X)
fRow2.pack(fill=tk.X)
fRow3.pack(fill=tk.X)
fRow4.pack(fill=tk.X)
fRow5.pack(fill=tk.X)
fRow6.pack(fill=tk.X)
fRow7.pack(fill=tk.X)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
log_frame.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=log.yview)


window.mainloop()
