import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile

import full_algorithms
from table import openNewWindowWithTable
import time


window = Tk(className='Algoritmy pro vyhledávání v CSV')
# set window size
window.geometry("600x130")
window.resizable(False, False)
window.iconphoto(False, PhotoImage(file="./media/icon.png"))


btn = Button(window, fg='black', bg='yellow', text='Vybrat CSV soubor', command=lambda: open_file())
btn.place(x=240, y=10)

btn = Button(window, fg='black', bg='pink', text='Vyhledat', command=lambda: find_data())
btn.place(x=370, y=77)

bv = BooleanVar()
c = Checkbutton(window, text="Musí se shodovat?", variable=bv, onvalue=True, offvalue=False)
c.place(x=430, y=77)

csv_text = ""
filepath = "-"
file_data = []

MODES = [
    ("Linear Search", "1"),
    ("Rabin-Karp", "2"),
    ("Boyer Moore", "3")
]

v = StringVar()
v.set("1")
labelText = StringVar()
labelText.set("Soubor nebyl prozatím vybrán")
Label(window,
      textvariable=labelText).place(x=240,
                                    y=35)

inputtxt = Entry(window)
inputtxt.place(x=240, y=80)


def check_box_visibility():
    match int(v.get()):
        case 1:
            c['state'] = "active"
        case 2:
            c['state'] = "disabled"
        case 3:
            bv.set(True)
            c['state'] = "disabled"


for text, mode in MODES:
    b = Radiobutton(window, text=text,
                    variable=v, value=mode, command=check_box_visibility)
    b.pack(anchor=W)


def open_file():
    file = askopenfile(mode='r', filetypes=[('csv soubory', '*.csv')])
    if file is not None:
        fd = file.read().splitlines()
        file_data.clear()
        file_data.extend(fd)
        print(file_data)
        labelText.set('Cesta k vybranému souboru je\n' + file.name)
        # openNewWindowWithTable(window, use_data(csv_text))
        # id,first_name,last_name,email,gender,phone


def find_data():
    # žádná data ze souboru ještě nebyly vybrány
    if not file_data:
        tkinter.messagebox.showerror(title="Chybějící data", message="Vyberte nejdříve CSV soubor")

    # data byly vybrány
    else:
        start = round(time.time() * 1000)
        match int(v.get()):
            case 1:
                openNewWindowWithTable(window, full_algorithms.full_linear_search(file_data, inputtxt.get(), bv.get()))
            case 2:
                openNewWindowWithTable(window, full_algorithms.full_rabin_karp(inputtxt.get(), file_data, 13))
            case 3:
                openNewWindowWithTable(window, full_algorithms.full_boyer_moore(inputtxt.get(), file_data))
        end = round(time.time() * 1000)
        tkinter.messagebox.showinfo(title="Čas", message=(str(end - start)+" ms"))


mainloop()
