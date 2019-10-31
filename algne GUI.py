from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

def quit(): #Programmi kinni panemiseks
    root.destroy()

def browse_file(): #See funktsioon tagastab valitud faili path'i
    global fname
    fpath = filedialog.askopenfilename(filetypes = (("CSV failid", "*.csv"), ("All files", "*")))
    fname = os.path.split(fpath)[1]
    if fpath == "":
        pass
    else:
        var.set(fname)
        tabel.pack(side=LEFT, padx = 2, pady = 2)
        tabel.config(text = fname)
    return fpath

def alert(): # Popup window esile kutsumine
    messagebox.showinfo("Nice huh?","Nüüd peaks analüüsimine toimuma.")
    
def info():
    root2 = Tk()
    root2.minsize(200,100)
    root2.wm_title("Info")

    rida1 = Label(root2, text = "GUI: Allan Loo").pack()
    rida2 = Label(root2, text = "Backend: Tiit Vaino").pack()
    rida3 = Label(root2, text = "COPYRIGHT © 2019 Tiit Vaino, Allan Loo").pack()
    rida4 = Label(root2, text = "All right reserved").pack()

    root2.mainloop()
    
root = Tk()
root.wm_title("Andmetöötleja")
root.minsize(500,300)
root_menu = Menu(root)
root.config(menu = root_menu)

def function(): #Lihtsalt tühi funktsioon nuppudele määramiseks
    pass

file_menu = Menu(root_menu)
root_menu.add_cascade(label = "Info", menu = file_menu) 
file_menu.add_command(label = "Help", command = function())
file_menu.add_command(label = "Info", command = info)

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
tabel = Label(bottom_frame, textvariable=var, fg="black", bg="white", relief = SUNKEN)

broButton = Button(master = bottom_frame, text = 'Browse', width = 6, command = browse_file)
broButton.pack(side=LEFT, padx = 2, pady=2)

root.mainloop()
