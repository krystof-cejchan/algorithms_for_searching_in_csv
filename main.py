from tkinter import *
from tkinter.filedialog import askopenfile

window = Tk()
csv_text = ""

MODES = [
    ("Linear Search", "1"),
    ("Binary Search", "2"),
    ("Jump Search", "3"),
    ("Interpolation Search", "4"),
    ("Exponential Search", "5"),
]

v = StringVar()
v.set("1")

for text, mode in MODES:
    b = Radiobutton(window, text=text,
                    variable=v, value=mode)
    b.pack(anchor=W)


def open_file():
    file = askopenfile(mode='r', filetypes=[('csv soubory', '*.csv')])
    if file is not None:
        csv_text = file.read()
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


btn = Button(window, text='otevři', command=lambda: open_file())
btn.pack(side=TOP, pady=10)

mainloop()
