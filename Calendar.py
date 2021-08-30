from tkinter import*
import calendar

def showCal() :
    window = Tk()
    window.title("CALENDAR")
    window.geometry("550x600")
    window.config(bg="white")

    getyear = int(year_field.get())
    cal_content = calendar.calendar(getyear)
    cal_year = Label(window, text=cal_content, font="Consoles 10 bold")
    cal_year.grid(row=5, column=1, padx=20)

    window.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.title('Calendar')
    root.geometry("250x140")
    root.config(bg="white")

    cal = Label(root, text="CALENDAR", bg="dark gray", font=("times", 28, 'bold'))
    year = Label(root, text="Enter Year", bg="light green")
    year_field = Entry(root)
    Show = Button(root, text="Show Calendar", bg="red", command=showCal)
    Exit = Button(root, text="Exit", bg="red", command=exit)

    cal.grid(row=1, column=1)
    year.grid(row=2,column=1)
    year_field.grid(row=3, column=1)
    Show.grid(row=4, column=1)
    Exit.grid(row=6, column=1)

    root.mainloop()


