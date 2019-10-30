from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import ImageTk, Image

def quit(): #Programmi kinni panemiseks
    root.destroy()

def browse_file(): #See funktsioon tagastab valitud faili path'i
    fpath = filedialog.askopenfilename(filetypes = (("CSV failid", "*.csv"), ("All files", "*")))
    fname = os.path.split(fpath)[1]
    if fpath == "":
        pass
    else:
        var.set(fname)
        label.pack(side=LEFT, padx = 2, pady = 2)
        label.config(text = fname)
    return fpath

def alert(): # Popup window esile kutsumine
    messagebox.showinfo("Nice huh?","Nüüd peaks analüüsimine toimuma.")

root = Tk()
root.wm_title("Andmetöötleja")
root.minsize(500,300)

top_frame = Frame(root,relief=RAISED,borderwidth=1)
top_frame.pack(fill=BOTH, expand=True)
bottom_frame = Frame(root,relief=RAISED,borderwidth=1)
bottom_frame.pack(fill=BOTH, expand=False)

closeButton = Button(bottom_frame, text="Close", command = quit)
closeButton.pack(side=RIGHT, padx=5, pady=5)

okButton = Button(bottom_frame, text="OK", command = alert)
okButton.pack(side=RIGHT, padx=5, pady=5)


riba = Label(top_frame, text = "Loomade andmete analüüsija", fg = "white", bg = "green")
riba.pack(fill = "x")

var = StringVar()
label = Label(bottom_frame, textvariable=var, relief=RAISED)

broButton = Button(master = bottom_frame, text = 'Browse', width = 6, command = browse_file)
broButton.pack(side=LEFT, padx = 2, pady=2)

root.mainloop()
