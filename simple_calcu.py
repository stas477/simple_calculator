from tkinter import *

root = Tk()

root.title('Simple Calculator 2000')

#Create input field
entry_field = Entry(root, width=40, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#addition

def click_handler(event=None):
    assert type(event) == int
    current = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(current) + str(event))

tmp = None

def clear_event():
    entry_field.delete(0, END)
    
def sum_event():
    global tmp
    if not tmp:
        tmp = entry_field.get()
        entry_field.delete(0, END)
    else:
        current = entry_field.get()
        entry_field.delete(0, END)
        entry_field.insert(0, int(current) + int(tmp))
        tmp = None


def equal_event():
    global tmp
    if tmp:
        current = entry_field.get()
        entry_field.delete(0, END)
        entry_field.insert(0, int(current) + int(tmp))
        tmp = None

def button_one():
    return 1

def button_two():
    return 2


#Define buttons

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: click_handler(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: click_handler(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: click_handler(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: click_handler(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: click_handler(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: click_handler(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: click_handler(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: click_handler(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: click_handler(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: click_handler(0))

button_add = Button(root, text='+', padx=40, pady=20, command=sum_event)

button_sub = Button(root, text='-', padx=40, pady=20, command=equal_event)
button_mul = Button(root, text='*', padx=40, pady=20, command=equal_event)
button_div = Button(root, text='/', padx=40, pady=20, command=equal_event)
button_equal = Button(root, text='=', padx=19, pady=20, command=equal_event)

button_clear = Button(root, text='Clear', padx=40, pady=20, command=clear_event)

#Put buttons on screen
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1, sticky="we")
button_sub.grid(row=4, column=2, sticky="we")
button_mul.grid(row=5, column=1, sticky="we")
button_div.grid(row=5, column=2, sticky="we")
button_equal.grid(row=5, column=0, sticky="we")
button_clear.grid(row=6, column=0, columnspan=3, sticky="we")

root.mainloop()