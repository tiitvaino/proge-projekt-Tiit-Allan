from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image, ImageTk
from andmetöötleja import *

def save():
    if fsave == "":
        pass
    else:
        f = open(fsave+".csv", "w")
        f.close()

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

def select_file():
    global fsave
    global fsavename
    fsave = filedialog.asksaveasfilename(initialfile="Andmed", title="Valige faili salvestamise kaust ja nimi", filetypes = (("CSV failid", "*.csv"), ("All files", "*")))
    fsavename = os.path.split(fsave)[1]
    if fsave == "":
        pass
    else:
        fsavename = (fsavename+".csv")
        loc.set(fsavename)
        tabel2.pack(side=LEFT, padx = 2, pady = 2)
        tabel2.config(text = fsavename)

def alert(): # Popup window esile kutsumine
    messagebox.showinfo("Nice huh?","Nüüd peaks analüüsimine toimuma.")
    
def info():
    root2 = Tk()
    root2.wm_title("Info")
    root.resizable(0, 0)

    rida1 = Label(root2, text = "GUI: Allan Loo").pack()
    rida2 = Label(root2, text = "Backend: Tiit Vaino").pack()
    rida3 = Label(root2, text = "COPYRIGHT © 2019 Tiit Vaino, Allan Loo").pack()
    rida4 = Label(root2, text = "All rights reserved").pack()

    root2.mainloop()

def andmeanalüüs():
    loomade_algne_hulk = {'põhikarja uted': int(põhikarja_uted.get()), 'põhikarja jäärad': int(põhikarja_jäärad.get()), 'utikud': int(utikud.get()), 'jäärikud': int(jäärikud.get()), 'utt_talled': int(utt_talled.get()), 'jäär_talled': int(jäär_talled.get())}
    andmed = andmetöötleja(algus.get(), lõpp.get(), fname, loomade_algne_hulk)
    e0.configure(text = andmed[1][1][0])
    e1.configure(text = andmed[1][1][1][0])
    e2.configure(text = andmed[1][1][1][1])
    e3.configure(text = andmed[1][1][1][2])
    e4.configure(text = andmed[1][1][1][3])
    e5.configure(text = andmed[1][2][0])
    e6.configure(text = andmed[1][2][1][0])
    e7.configure(text = andmed[1][2][1][1])
    e8.configure(text = andmed[1][2][1][2])
    e9.configure(text = andmed[1][2][1][3])

def only_numbers(char):
    return char.isdigit()

def numbers_dot(char):
    if char == ".":
        return True
    else:
        return char.isdigit()


root = Tk()
root.wm_title("Andmetöötleja")
root.minsize(500,300)
root_menu = Menu(root)
root.config(menu = root_menu)
root.resizable(0, 0)


def function(): #Lihtsalt tühi funktsioon nuppudele määramiseks
    pass

file_menu = Menu(root_menu)
root_menu.add_cascade(label = "Info", menu = file_menu) 
file_menu.add_command(label = "Help", command = function())
file_menu.add_command(label = "Info", command = info)

top_frame = Frame(root, borderwidth=1)
top_frame.pack(fill=BOTH, expand=False)
center_frame = Frame(root,relief=RAISED,borderwidth=1)
center_frame.pack(fill=BOTH, expand=True)
bottom_frame = Frame(root,relief=RAISED,borderwidth=1)
bottom_frame.pack(fill=BOTH, expand=False)

closeButton = Button(bottom_frame, text="Close", command = quit)
closeButton.pack(side=RIGHT, padx=5, pady=5)

okButton = Button(bottom_frame, text="OK", command = lambda:[andmeanalüüs(),save()])
okButton.pack(side=RIGHT, padx=5, pady=5)

riba = Label(top_frame, text = "Loomade andmete analüüsija", fg = "white", bg = "green")
riba.pack(fill = "x")

browseButton = Button(master = bottom_frame, text = 'Browse', width = 6, command = browse_file)
browseButton.pack(side=LEFT, padx = 2, pady=2)

var = StringVar()
tabel = Label(bottom_frame, textvariable=var, width=17, bg="white", relief = SUNKEN)
tabel.pack(side=LEFT, padx = 2, pady = 2)

selectButton = Button(master = bottom_frame, text = 'Select', width = 6, command = select_file)
selectButton.pack(side=LEFT, padx = 2, pady=2)

loc = StringVar()
tabel2 = Label(bottom_frame, textvariable=loc, width=17, bg="white", relief = SUNKEN)
tabel2.pack(side=LEFT, padx = 2, pady = 2)


center_frame.grid_columnconfigure(0, weight=1)
center_frame.grid_rowconfigure(0, weight=1)
center_frame.grid_columnconfigure(1, weight=1)
center_frame.grid_rowconfigure(1, weight=1)
center_frame.grid_columnconfigure(2, weight=1)
center_frame.grid_rowconfigure(2, weight=1)

Label(center_frame, text='Sisestage loomade\narvud kuu alguses', font=("Helvetica 12 bold")).grid(column = 0, columnspan = 2, row=0, padx=5, sticky = S)

validation = center_frame.register(only_numbers)
validation2 = center_frame.register(numbers_dot)

Label(center_frame, text='uted', font=("Helvetica 10 bold")).grid(column = 1, row=1, padx=5, sticky = S) 
põhikarja_uted = Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
põhikarja_uted.grid(row=2, column = 1, padx=5, sticky = S)

Label(center_frame, text='jäärad', font=("Helvetica 10 bold")).grid(column = 0, row=1, padx=5, sticky = S) 
põhikarja_jäärad = Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
põhikarja_jäärad.grid(row=2, padx=5, sticky = S)

Label(center_frame, text='utikud', font=("Helvetica 10 bold")).grid(column = 1, row=3, padx=5, sticky = S) 
utikud = Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
utikud.grid(row=4, column = 1, padx=5, sticky = S)

Label(center_frame, text='jäärikud', font=("Helvetica 10 bold")).grid(column = 0, row=3, padx=5, sticky = S) 
jäärikud = Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
jäärikud.grid(row=4, padx=5, sticky = S)

Label(center_frame, text='utt-talled', font=("Helvetica 10 bold")).grid(column = 1, row=5, padx=5, sticky = S) 
utt_talled = Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
utt_talled.grid(row=6, column = 1, padx=5, sticky = S)

Label(center_frame, text='jäär-talled', font=("Helvetica 10 bold")).grid(column = 0, row=5, padx=5, sticky = S) 
jäär_talled = Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
jäär_talled.grid(row=6, padx=5, sticky = S)

Label(center_frame, text='Sisestage alguskuupäev', font=("Helvetica 10 bold")).grid(row=7, columnspan = 2, padx=5, sticky = S) 
algus = Entry(center_frame, validate="key", validatecommand=(validation2, '%S'))
algus.grid(row=8, padx=5, sticky = S, columnspan = 2)

Label(center_frame, text='Sisestage lõppkuupäev', font=("Helvetica 10 bold")).grid(row=9, columnspan = 2, padx=5, sticky = S) 
lõpp = Entry(center_frame, validate="key", validatecommand=(validation2, '%S'))
lõpp.grid(row=10, padx=5, sticky = S, columnspan = 2)


lamb = Image.open("lamb.png")
resized = lamb.resize((150, 120),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
lambLabel = Label(top_frame, image = photo, bg = "white")
lambLabel.image = photo
lambLabel.pack(fill = "x")


Label(center_frame, text='Sissetulek', font=("Helvetica 12 bold")).grid(row=0, column=2, padx=5, sticky = S)
Label(center_frame, text='Kokku').grid(row=1, column=2, padx=5, sticky = S)
Label(center_frame, text='Teisest rühmast').grid(row=3, column=2, padx=5, sticky = S)
Label(center_frame, text='Sünd').grid(row=5, column=2, padx=5, sticky = S)
Label(center_frame, text='Ostetud').grid(row=7, column=2, padx=5, sticky = S) 
Label(center_frame, text='Muu').grid(row=9, column=2, padx=5, sticky = S)
e0 = Label(center_frame, relief = SUNKEN, width=17, bg="white")
e0.grid(row=2, column=2, padx=5, sticky = S)
e1 = Label(center_frame, relief = SUNKEN, width=17, bg="white")
e1.grid(row=4, column=2, padx=5, sticky = S)
e2 = Label(center_frame, relief = SUNKEN, width=17, bg="white")
e2.grid(row=6, column=2, padx=5, sticky = S)
e3 = Label(center_frame, relief = SUNKEN, width=17, bg="white")
e3.grid(row=8, column=2, padx=5, sticky = S)
e4 = Label(center_frame, relief = SUNKEN, width=17, bg="white")
e4.grid(row=10, column=2, padx=5, sticky = S)


Label(center_frame, text='Väljaminek', font=("Helvetica 12 bold")).grid(row=0, column=3, padx=5, sticky = S)
Label(center_frame, text='Kokku').grid(row=1, column=3, padx=5, sticky = S)
Label(center_frame, text='Teise rühma').grid(row=3, column=3, padx=5, sticky = S)
Label(center_frame, text='Hukkumine').grid(row=5, column=3, padx=5, sticky = S) 
Label(center_frame, text='Müük').grid(row=7, column=3, padx=5, sticky = S)
Label(center_frame, text='Lihaks').grid(row=9, column=3, padx=5, sticky = S)
e5 = Label(center_frame, relief = SUNKEN, width=17, bg="white")
e5.grid(row=2, column=3, padx=5, sticky = S)
e6 = Label(center_frame, relief = SUNKEN, width=17, bg="white")
e6.grid(row=4, column=3, padx=5, sticky = S)
e7 = Label(center_frame, relief = SUNKEN, width=17, bg="white")
e7.grid(row=6, column=3, padx=5, sticky = S)
e8 = Label(center_frame, relief = SUNKEN, width=17, bg="white")
e8.grid(row=8, column=3, padx=5, sticky = S)
e9 = Label(center_frame, relief = SUNKEN, width=17, bg="white")
e9.grid(row=10, column=3, padx=5, sticky = S)


root.mainloop()
