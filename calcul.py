import tkinter as tk

def get_values():
    num1 = int(number_entry1.get())
    num2 = int(number_entry2.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, "end")
    answer_entry.insert(0, value)




def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def divede():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)








window = tk.Tk()
window.title('calculator')
window.geometry("350x350")
window.resizable(False, False)

button_add = tk.Button(window, text ="+", width=3, height=2, command=add)
button_minus = tk.Button(window, text="-", width=3, height=2, command=sub)
button_multiplication = tk.Button(window, text="x", width=3, height=2, command=mul)
button_divide = tk.Button(window, text="/", width=3, height=2, command=divede)

button_multiplication.place(x=10, y=290) ##
button_minus.place(x=50, y=240) #
button_divide.place(x=50, y=290) ##
button_add.place(x=10, y=240,) #

number_entry1 = tk.Entry(window, width= 35)
number_entry1.place(x=90, y=70)
number_entry2 = tk.Entry(window, width= 35)
number_entry2.place(x=90, y=100)
answer_entry = tk.Entry(window, width= 35)
answer_entry.place(x=90, y=130)

welcome = tk.Label(window,text="Calculator")
welcome.place(x=150, y=20)

first_number = tk.Label(window, text="first value:")
second_number = tk.Label(window, text="second value:")
answer = tk.Label(window, text="answer:")

first_number.place(x=10, y=67)
second_number.place(x=10, y=97)
answer.place(x=10, y=127)

window.mainloop()