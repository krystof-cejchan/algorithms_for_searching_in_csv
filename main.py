from tkinter import *
from tkinter.filedialog import askopenfile

from table import Table, openNewWindowWithTable

window = Tk(className='Algoritmy pro vyhledávání v CSV')
# set window size
window.geometry("600x400")
window.resizable(False, False)
window.iconphoto(False, PhotoImage(file="media/icon.png"))

csv_text = ""
filepath = "-"
lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]
total_rows = len(lst)
total_columns = len(lst[0])

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
        openNewWindowWithTable(window, total_rows, total_columns, lst)
        # id,first_name,last_name,email,gender,phone
        use_data(csv_text)


def use_data(csv):
    lines = csv.splitlines()
    for f in lines[1:]:
        for i in range(len(f.split(','))):
            if i == 0:
                print("\n")
            print(f.split(',')[i])
            # create an object of person which will hold the data from the csv file
            # --objects may not be possible as user can open any file
            # then work with these objects


btn = Button(window, fg='black', bg='yellow', text='Vybrat CSV soubor', command=lambda: open_file())
btn.pack(side=TOP, pady=10)

mainloop()
