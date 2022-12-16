import tkinter
from tkinter import Entry, END, Toplevel, DISABLED, ttk, Scrollbar, RIGHT, BOTH, LEFT, Listbox, BOTTOM


def openNewWindowWithTable(window, lst):
    print(lst)
    if len(lst) == 0:
        answer = tkinter.messagebox.askokcancel(title="Kde nic, tu nic", message="Žádná data se neshodují se vstupem! "
                                                                                 "\nPokud chcete i přesto pokračovat,"
                                                                                 " dejte OK")
        if not answer:
            return

    new_window = Toplevel(window)

    new_window.title("Tabulka")

    new_window.geometry("1250x700")

    Table(new_window, lst)


# třída Table, která vygenerovává tabulku v konstruktoru
class Table:

    def __init__(self, root, list_of_data):
        scrollbar = ttk.Scrollbar(root, orient='vertical')
        scrollbar.pack(side=RIGHT, fill=BOTH)
        scrollbarH = ttk.Scrollbar(root, orient='horizontal')
        scrollbarH.pack(side=BOTTOM, fill=BOTH)

        listbox = Listbox(root, width=350, font='Helvetica 15 bold')
        listbox.pack(side=LEFT, fill=BOTH)

        for values in list_of_data:
            listbox.insert(END, values)

        listbox.config(yscrollcommand=scrollbar.set)
        listbox.config(xscrollcommand=scrollbarH.set)

        scrollbar.config(command=listbox.yview)
        scrollbarH.config(command=listbox.xview)

