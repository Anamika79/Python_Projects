from tkinter import *

class Table:
    def __init__(self, root):
         for i in range(rowno):
             for j in range(columnno):
                 self.e = Entry(root, width=20, fg="black", bg="white", font=('Arial', 16, 'bold'))
                 self.e.grid(row=i, column=j)
                 self.e.insert(END, lst[i][j])


# data
lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Shona', 'Pune', 18),
       (3, 'Rahul', 'Mumbai', 20),
       (4, 'Anamika', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]

rowno = len(lst)
columnno = len(lst[0])


# root window
root = Tk()
t = Table(root)
root.title("Table")
root.mainloop()



