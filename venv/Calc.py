import tkinter
from tkinter import *
expression=""
def press(num):
    global expression
    expression = expression+ str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""

def clear():
    global expression
    equation.set("")
    expression = ""


if __name__ == "__main__":
    window = Tk()
    window.geometry("265x150")
    window.resizable(1,1)
    window.title("Simple Calculator")

    equation= StringVar()

    entry = Entry(window, textvariable= equation)
    entry.grid(columnspan=4, ipadx=70)

    clear = Button(window, text=' Clear ', bg='black', fg='white', height=1, width=7, command = clear)
    clear.grid(row=1, column=0)
    percent = Button(window, text=' % ', bg='black', fg='white', height=1, width=7, command=lambda: press("%"))
    percent.grid(row=1, column=1)
    divide = Button(window, text=' / ', bg='black', fg='white', height=1, width=7, command=lambda: press("/"))
    divide.grid(row=1, column=3)
    multiply = Button(window, text=' * ', bg='black', fg='white', height=1, width=7, command=lambda: press("*"))
    multiply.grid(row=2, column=3)
    minus = Button(window, text=' - ', bg='black', fg='white', height=1, width=7, command=lambda: press("-"))
    minus.grid(row=3, column=3)
    plus = Button(window, text=' + ', bg='black', fg='white', height=1, width=7, command=lambda: press("+"))
    plus.grid(row=4, column=3)
    decimal = Button(window, text=' . ', bg='black', fg='white', height=1, width=7, command=lambda: press("."))
    decimal.grid(row=5, column=2)
    equal = Button(window, text=' = ', bg='black', fg='white', height=1, width=7, command=equalpress)
    equal.grid(row=5, column=3)
    button1 = Button(window, text=' 1 ', bg='black', fg='white', height=1, width=7, command=lambda: press(1))
    button1.grid(row=4, column=0)
    button2 = Button(window, text=' 2 ', bg='black', fg='white', height=1, width=7, command=lambda: press(2))
    button2.grid(row=4, column=1)
    button3 = Button(window, text=' 3 ', bg='black', fg='white', height=1, width=7, command=lambda: press(3))
    button3.grid(row=4, column=2)
    button4 = Button(window, text=' 4 ', bg='black', fg='white', height=1, width=7, command=lambda: press(4))
    button4.grid(row=3, column=2)
    button5 = Button(window, text=' 5 ', bg='black', fg='white', height=1, width=7, command=lambda: press(5))
    button5.grid(row=3, column=1)
    button6 = Button(window, text=' 6 ', bg='black', fg='white', height=1, width=7, command=lambda: press(6))
    button6.grid(row=3, column=0)
    button7 = Button(window, text=' 7 ', fg='white', bg='black', height=1, width=7, command=lambda: press(7))
    button7.grid(row=2, column=0)
    button8 = Button(window, text=' 8 ', bg='black', fg='white', height=1, width=7, command=lambda: press(8))
    button8.grid(row=2, column=1)
    button9 = Button(window, text=' 9 ', bg='black', fg='white', height=1, width=7, command=lambda: press(9))
    button9.grid(row=2, column=2)
    button00 = Button(window, text=' 00 ', bg='black', fg='white', height=1, width=7, command=lambda: press(00))
    button00.grid(row=5, column=0)
    button0 = Button(window, text=' 0 ', bg='black', fg='white', height=1, width=7, command=lambda: press(0))
    button0.grid(row=5, column=1)

    window.mainloop()


