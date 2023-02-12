# Importing modules
from tkinter import *
from items_config import Items

BACKGROUND_COLOR = "#343434"

# Object creation
item = Items()

# Window creation
window = Tk()
window.title("Shopping list")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

# textbox creation
item_text_list = Text(height=15, width=25, padx=20, pady=20)
item_text_list.grid(row=1, column=2, rowspan=2)


def add_to_food_entry(food):
    item_text_list.insert(END, f"\n{food}".title())


def listbox_food_used(event):
    add_to_food_entry(food_l_box.get(food_l_box.curselection()))


def listbox_drink_used(event):
    add_to_food_entry(drink_l_box.get(drink_l_box.curselection()))


def listbox_sauce_used(event):
    add_to_food_entry(sauce_l_box.get(sauce_l_box.curselection()))


# Label creation
food_label = Label(text="Food")
food_label.grid(column=0, row=0)
drink_label = Label(text="Drink")
drink_label.grid(column=0, row=2)
sauce_label = Label(text="Sauce")
sauce_label.grid(column=0, row=4)

# Listbox creation
food_choice = StringVar(value=item.items_food_list)
food_l_box = Listbox(listvariable=food_choice, selectmode="extended")
food_l_box.bind("<<ListboxSelect>>", listbox_food_used)
food_l_box.grid(column=0, row=1)

drink_choice = StringVar(value=item.items_drink_list)
drink_l_box = Listbox(listvariable=drink_choice, selectmode="extended")
drink_l_box.bind("<<ListboxSelect>>", listbox_drink_used)
drink_l_box.grid(column=0, row=3)

sauce_choice = StringVar(value=item.items_sauce_list)
sauce_l_box = Listbox(listvariable=sauce_choice, selectmode="extended")
sauce_l_box.bind("<<ListboxSelect>>", listbox_sauce_used)
sauce_l_box.grid(column=0, row=5)

window.mainloop()
