from tkinter import Entry, END, Toplevel, DISABLED


def openNewWindowWithTable(window, total_rows, total_columns, lst):
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Tabulka")

    # sets the geometry of toplevel
    newWindow.geometry("1200x200")

    Table(newWindow, total_rows, total_columns, lst)


# třída Table, která vygenerovává tabulku v konstruktoru
class Table:

    def __init__(self, root, total_rows, total_columns, listOfData):

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='grey',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, listOfData[i][j])
                self.e.config(state=DISABLED)
