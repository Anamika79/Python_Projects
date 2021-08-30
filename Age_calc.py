from tkinter import*
from tkinter import messagebox

def clearall():
    Dayfield.delete(0, END)
    Monthfield.delete(0, END)
    Yearfield.delete(0, END)
    Givendayfield.delete(0, END)
    Givenmonthfield.delete(0, END)
    Givenyearfield.delete(0, END)
    Resultdays.delete(0, END)
    Resultmonths.delete(0, END)
    Resultyears.delete(0, END)

def checkerror():
    if (Dayfield.get() == "" or Monthfield.get() == "" or Yearfield.get() == "" or Givendayfield.get() == "" or Givenmonthfield.get() == ""
                or Givenyearfield.get() == ""):
        messagebox.showerror("Input error")
        clearall()
        return 0

def submit():

    value = checkerror()
    if value == 0:
        return
    else:
        birth_date = int(Dayfield.get())
        birth_month = int(Monthfield.get())
        birth_year = int(Yearfield.get())

        given_day = int(Givendayfield.get())
        given_month = int(Givenmonthfield.get())
        given_year = int(Givenyearfield.get())

        calculate_day =  given_day - birth_date;
        calculate_month = given_month - birth_month;
        calculate_year = given_year - birth_year;

        Resultdays.insert(10, str(calculate_day))
        Resultmonths.insert(10, str(calculate_month))
        Resultyears.insert(10, str(calculate_year))



if __name__=="__main__":
    root = Tk()
    root.title("Age Calculator")
    root.geometry("700x400")
    root.config(bg="light green")

    DOBlbl = Label(root, bg="blue", text="Date Of Birth")
    given_date = Label(root, bg="blue", text="Given Date")
    Day = Label(root, bg="light green", text="Day")
    Month = Label(root, bg="light green", text="Month")
    Year = Label(root, bg="light green", text="Year")
    Given_day = Label(root, bg="light green", text="Given Day")
    Given_month = Label(root, bg="light green", text="Given Month")
    Given_year = Label(root, bg="light green", text="Given Year")
    Resultant_Years = Label(root, bg="light green", text="Years")
    Resultant_Months = Label(root, bg="light green", text="Months")
    Resultant_Days = Label(root, bg="light green", text="Days")

    Dayfield = Entry(root)
    Monthfield = Entry(root)
    Yearfield = Entry(root)
    Givendayfield = Entry(root)
    Givenmonthfield = Entry(root)
    Givenyearfield = Entry(root)
    Resultyears = Entry(root)
    Resultmonths = Entry(root)
    Resultdays = Entry(root)

    submitbtn = Button(root, bg="white", text="Resultant Age", command=submit)
    Clear = Button(root, bg="white", text="Clear All", command=clearall)

    DOBlbl.grid(row=0, column=1)

    Day.grid(row=1, column=0)
    Dayfield.grid(row=1, column=1)

    Month.grid(row=2, column=0)
    Monthfield.grid(row=2, column=1)

    Year.grid(row=3, column=0)
    Yearfield.grid(row=3, column=1)

    given_date.grid(row=0, column=4)

    Given_day.grid(row=1, column=3)
    Givendayfield.grid(row=1, column=4)

    Given_month.grid(row=2, column=3)
    Givenmonthfield.grid(row=2, column=4)

    Given_year.grid(row=3, column=3)
    Givenyearfield.grid(row=3, column=4)

    submitbtn.grid(row=4, column=2)

    Resultant_Years.grid(row=5, column=2)
    Resultyears.grid(row=6, column=2)

    Resultant_Months.grid(row=7, column=2)
    Resultmonths.grid(row=8, column=2)

    Resultant_Days.grid(row=9, column=2)
    Resultdays.grid(row=10, column=2)

    Clear.grid(row=11, column=2)


    root.mainloop()