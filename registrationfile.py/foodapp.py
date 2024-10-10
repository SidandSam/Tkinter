import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
top=tk.Tk()
top.geometry("500x500")
top.title("food_app")
menu={"pizza":8.99,
      "burger":5.99,
      "salad":4.99,
      "soda":2.99
}

selected_items=[]

def dark_mode():
    if dark_mode_var.get():
        top.config(bg="black")
        for widget in top.winfo_children():
            widget.config(bg="black",fg="white")
    else:
        top.config(bg="white")
        for widget in top.winfo_children():
            widget.config(bg="white",fg="black")

def update_total():
    total=sum(menu[item]*qty for item,qty in selected_items)
    total_label.config(text=f"Total:${total:.2f}")

def add_item(item,quantity_entry):
    try:
        qty=int(quantity_entry.get())
        if qty>0:
            selected_items.append((item,qty))
            update_total()
            update_selection_list()

    except IndexError:
        pass

def clear_selection():
    selected_items.clear()
    update_total()
    update_selection_list()

def update_selection_list():
    selection_list.delete(0,END)
    for item,qty in selected_items:
        selection_list.insert(END,f"{item}x{qty}") 
def submit_order():
    if not selected_items:
        messagebox.showinfo("order submission","no item is selected.")
        return
    total=sum(menu[item]*qty for item,qty in selected_items)
    messagebox.showinfo("order Submission",f"Order Submitted!\nTotal:${total:.2f}")
    clear_selection()

def remove_order():
    try:
        selected=selection_list.curselection()
        if selected:
            index=selected[0]
            del selected_items[index]
            update_total()
            update_selection_list()
    except IndexError:
        pass

pizza_image=PhotoImage(file="pizza.png").subsample(20,20)  
burger_image=PhotoImage(file="burger.png").subsample(20,20) 
salad_image=PhotoImage(file="salad.png").subsample(20,20) 
soda_image=PhotoImage(file="soda.png").subsample(20,20) 

images={
    "pizza":pizza_image,
    "burger":burger_image,
    "soda":soda_image,
    "salad":salad_image
}




row=0
for item,price in menu.items():
    
    img_label=Label(top,image=images[item])
    img_label.grid(row=row,column=0)
    label1=Label(top,text=f"{item}-${price:.2f}")
    label1.grid(row=row,column=1)
    quantity_entry=Entry(top)
    quantity_entry.grid(row=row,column=2)
    add_btn=Button(top,text="ADD",command=lambda item=item,entry=quantity_entry:add_item(item,entry))
    add_btn.grid(row=row,column=3)
    row+=1
selected_label=Label(top,text="selected items:")
selected_label.grid(row=0,column=4)
selection_list=Listbox(top)
selection_list.grid(row=1,column=4,rowspan=5)

remove_button=Button(top,text="remove selected item",command=remove_order)
remove_button.grid(row=6,column=4)
clear_button=Button(top,text="clear selected item",command=clear_selection)
clear_button.grid(row=7,column=4)
submit_button=Button(top,text="submit selected item",command=submit_order)
submit_button.grid(row=8,column=4)
total_label=Label(top,text="total:$0.00")
total_label.grid(row=9,column=4)

dark_mode_var=tk.BooleanVar()
dark_mode_checkbox=Checkbutton(top,text="Dark mode",variable=dark_mode_var,command=dark_mode)

dark_mode_checkbox.grid(row=10,column=1)










top.mainloop()