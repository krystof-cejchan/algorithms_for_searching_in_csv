from tkinter import *
from tkinter.filedialog import askopenfile

from table import openNewWindowWithTable

window = Tk(className='Algoritmy pro vyhledávání v CSV')
# set window size
window.geometry("600x400")
window.resizable(False, False)
window.iconphoto(False, PhotoImage(file="media/icon.png"))

csv_text = ""
filepath = "-"

MODES = [
    ("Linear Search", "1"),
    ("Binary Search", "2"),
    ("Jump Search", "3"),
    ("Interpolation Search", "4"),
    ("Exponential Search", "5"),
]

v = StringVar()
v.set("1")
labelText = StringVar()
labelText.set("Soubor nebyl prozatím vybrán")
Label(window,
      textvariable=labelText).place(x=240,
                                    y=60)

for text, mode in MODES:
    b = Radiobutton(window, text=text,
                    variable=v, value=mode)
    b.pack(anchor=W)


def open_file():
    file = askopenfile(mode='r', filetypes=[('csv soubory', '*.csv')])
    if file is not None:
        csv_text = file.read()
        labelText.set('Cesta k vybranému souboru je\n' + file.name)
        openNewWindowWithTable(window, use_data(csv_text))
        # id,first_name,last_name,email,gender,phone


def use_data(csv):
    lines = csv.splitlines()
    data = []
    for f in lines:
        data.append(f.split(','))
        print(f.split(','))
    return data

    # for i in range(len(f.split(','))):
    #     if i == 0:
    #         print("\n")
    #     print(f.split(',')[i])
    # create an object of person which will hold the data from the csv file
    # --objects may not be possible as user can open any file
    # then work with these objects


btn = Button(window, fg='black', bg='yellow', text='Vybrat CSV soubor', command=lambda: open_file())
btn.pack(side=TOP, pady=10)

mainloop()
