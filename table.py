from tkinter import Entry, END, Toplevel, DISABLED, ttk, Scrollbar, RIGHT, BOTH, LEFT, Listbox, BOTTOM


def openNewWindowWithTable(window, lst):
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Tabulka")

    # sets the geometry of toplevel
    newWindow.geometry("1250x700")

    Table(newWindow, lst)


# třída Table, která vygenerovává tabulku v konstruktoru
class Table:

    def __init__(self, root, list_of_data):

        # Create a horizontal scrollbar
        scrollbar = ttk.Scrollbar(root, orient='vertical')
        scrollbar.pack(side=RIGHT, fill=BOTH)
        scrollbarH = ttk.Scrollbar(root, orient='horizontal')
        scrollbarH.pack(side=BOTTOM, fill=BOTH)

        # Add a Listbox Widget
        listbox = Listbox(root, width=350, font='Helvetica 15 bold')
        listbox.pack(side=LEFT, fill=BOTH)

        # Add values to the Listbox
        for values in list_of_data:
            listbox.insert(END, values)

        listbox.config(yscrollcommand=scrollbar.set)
        listbox.config(xscrollcommand=scrollbarH.set)

        # Configure the scrollbar
        scrollbar.config(command=listbox.yview)
        scrollbarH.config(command=listbox.xview)
        # total_rows = len(listOfData)
        # total_columns = len(listOfData[0])
        # scrollbar = Scrollbar(orient="horizontal")
        # for i in range(total_rows):
        #     for j in range(total_columns):
        #         self.e = Entry(root, width=20, fg='grey',
        #                        font=('Arial', 16, 'bold'), xscrollcommand=scrollbar.set)
        #
        #         self.e.grid(row=i, column=j)
        #         self.e.insert(END, listOfData[i][j])
        #         self.e.config(state=DISABLED)
        #         scrollbar.pack(fill="x")
        #         scrollbar.config(command=self.e.xview)
