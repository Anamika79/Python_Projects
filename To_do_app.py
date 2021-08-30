from tkinter import*
from tkinter import messagebox

counter = 1
task_list = []

def inputerror():
    if entry.get() == "":
        messagebox.showerror("Input Error")
        return 0
    return 1

def clear_taskNumberField():
    taskNumberField.delete(0.0, END)

def clear_entry():
    entry.delete(0, END)

def insertTask():
    global counter
    value = inputerror()
    if value == 0:
        return

    content = entry.get() + "\n"
    task_list.append(content)
    TextArea.insert('end -1 chars', "["+str(counter)+"]"+content)
    counter += 1
    clear_entry()


def delete():
    global counter

    if len(task_list) == 0:
        messagebox.showerror("No task")
        return

    number = taskNumberField.get(1.0, END)

    if number == "\n":
        messagebox.showerror("input error")
        return

    else:
        task_no = int(number)

    clear_taskNumberField()

    task_list.pop(task_no - 1)

    counter -= 1

    TextArea.delete(1.0, END)

    for i in range(len(task_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + task_list[i])



if __name__ == "__main__":
    root = Tk()
    root.title("ToDoApp")
    root.geometry("250x300")
    root.config(bg="light green")

    task = Label(root, text="Enter Your Task", bg="light green")
    entry = Entry(root)
    submit = Button(root, text="Submit", bg="red", command=insertTask)
    TextArea = Text(root, height=5, width=25, font="lucida 13")
    deletelbl = Label(root, text="Delete Tack Number", bg="blue")
    taskNumberField = Text(root, height=1, width=2, font="lucida 13")
    delete1 = Button(root, text="Delete", bg="red", command=delete)
    exitbtn = Button(root, text="Exit", bg="red", command=exit)

    task.grid(row=0, column=2)
    entry.grid(row=1, column=2, columnspan=6, ipadx=50)
    submit.grid(row=2, column=2)
    TextArea.grid(row=3, column=2, padx=10)
    deletelbl.grid(row=4, column=2, pady=5)
    taskNumberField.grid(row=5, column=2)
    delete1.grid(row=6, column=2, pady=5)
    exitbtn.grid(row=7, column=2)

    root.mainloop()

