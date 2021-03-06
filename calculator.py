from tkinter import *

root = Tk()
root.title("Calculator")

screen = Entry(root, width=35, borderwidth=5)
screen.grid(row=0, column=0, columnspan=4,
            pady=10, ipady=5)


def button_click(number):
    currentNum = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(currentNum) + str(number))


def button_clear():
    screen.delete(0, END)


def button_symbol(symbol):
    global symbol_used
    symbol_used = symbol
    num1 = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(num1) + symbol)


def button_solve():
    nums = screen.get()
    if symbol_used == "+":
        num1, num2 = nums.split("+")
        answer = int(num1) + int(num2)
    elif symbol_used == "-":
        num1, num2 = nums.split("-")
        answer = int(num1) - int(num2)
    elif symbol_used == "*":
        num1, num2 = nums.split("*")
        answer = int(num1) * int(num2)
    elif symbol_used == "/":
        num1, num2 = nums.split("/")
        answer = int(num1) / int(num2)
        answer = int(answer)

    screen.delete(0, END)
    screen.insert(0, answer)


button_1 = Button(root, text="1", padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,
                  command=lambda: button_click(0))
button_addition = Button(root, text="+", padx=40,
                         pady=20, width=1, command=lambda: button_symbol("+"))
button_subtraction = Button(root, text="-", padx=40,
                            pady=20, width=1, command=lambda: button_symbol("-"))
button_multiplication = Button(root, text="*", padx=40,
                               pady=20, width=1, command=lambda: button_symbol("*"))
button_division = Button(root, text="/", padx=40,
                         pady=20, width=1, command=lambda: button_symbol("/"))
button_equal = Button(root, text="=", padx=40, pady=20, command=button_solve)
button_clear = Button(root, text="Clear", padx=40,
                      pady=20, width=1, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_addition.grid(row=1, column=3)
button_subtraction.grid(row=2, column=3)
button_multiplication.grid(row=3, column=3)
button_division.grid(row=4, column=3)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

root.mainloop()
