from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image, ImageTk
from andmetöötleja import *
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle
kõik_andmed = []

def save():
    global fsavename
    global kõik_andmed
    if fsave == "":
        pass
    else:
        salvestaja(kõik_andmed, fsave)

def quit(): #Programmi kinni panemiseks
    root.destroy()

def browse_file(): #See funktsioon tagastab valitud faili path'i
    global fname
    global fpath
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
    messagebox.showinfo("Küsige julgelt", "Abi saamiseks helistage numbrile: 5454 1010")
    
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
    global kõik_andmed
    global fsavename
    global fpath
    loomade_algne_hulk = {'põhikarja uted': int(põhikarja_uted.get()), 'põhikarja jäärad': int(põhikarja_jäärad.get()), 'utikud': int(utikud.get()), 'jäärikud': int(jäärikud.get()), 'utt_talled': int(utt_talled.get()), 'jäär_talled': int(jäär_talled.get())}
    andmed = andmetöötleja(algus.get(), lõpp.get(), fpath, loomade_algne_hulk)
    e0.configure(text = andmed[7][1][0])
    e1.configure(text = andmed[7][1][1][0])
    e2.configure(text = andmed[7][1][1][1])
    e3.configure(text = andmed[7][1][1][2])
    e4.configure(text = andmed[7][1][1][3])
    e5.configure(text = andmed[7][2][0])
    e6.configure(text = andmed[7][2][1][0])
    e7.configure(text = andmed[7][2][1][1])
    e8.configure(text = andmed[7][2][1][2])
    e9.configure(text = andmed[7][2][1][3])
    kõik_andmed = andmed
    salvestaja(kõik_andmed, fsavename)

def only_numbers(char):
    return char.isdigit()

def numbers_dot(char):
    if char == ".":
        return True
    elif char == "dd.mm.yyyy":
        return True
    else:
        return char.isdigit()
    
def del_ins(event):
    if algus.get() == "dd.mm.yyyy":
        algus.delete(0, "end")
    elif lõpp.get() == "":
        lõpp.insert(0, "dd.mm.yyyy")
    return None

def del_ins2(event):
    if lõpp.get() == "dd.mm.yyyy":
        lõpp.delete(0, "end")
    elif algus.get() == "":
        algus.insert(0, "dd.mm.yyyy")
    return None

root = Tk()
root.wm_title("Andmetöötleja")
root_menu = Menu(root)
root.config(menu = root_menu)
root.resizable(0, 0)

style = ThemedStyle(root)
style.set_theme("plastik")

def function(): #Lihtsalt tühi funktsioon nuppudele määramiseks
    pass

file_menu = Menu(root_menu)
root_menu.add_cascade(label = "Info", menu = file_menu) 
file_menu.add_command(label = "Help", command = alert)
file_menu.add_command(label = "Info", command = info)

top_frame = ttk.Frame(root, borderwidth=0)
top_frame.pack(fill=BOTH, expand=False)
center_frame = ttk.Frame(root,relief=RAISED,borderwidth=1, padding = 10)
center_frame.pack(fill=BOTH, expand=True)
bottom_frame = ttk.Frame(root,relief=RAISED,borderwidth=1)
bottom_frame.pack(fill=BOTH, expand=False)

closeButton = ttk.Button(bottom_frame, text="Close", command = quit)
closeButton.pack(side=RIGHT, padx=5, pady=5)

okButton = ttk.Button(bottom_frame, text="OK", command = lambda:[andmeanalüüs(), save()])
okButton.pack(side=RIGHT, padx=5, pady=5)

riba = ttk.Label(top_frame, text = "Loomade andmete analüüsija", foreground = "white", background = "green", anchor="center")
riba.pack(fill = "x")

browseButton = ttk.Button(master = bottom_frame, text = 'Browse', width = 6, command = browse_file)
browseButton.pack(side=LEFT, padx = 2, pady=2)

var = StringVar()
tabel = ttk.Label(bottom_frame, textvariable=var, width=17, background="white", relief = SUNKEN)
tabel.pack(side=LEFT, padx = 2, pady = 2)

selectButton = ttk.Button(master = bottom_frame, text = 'Select', width = 6, command = select_file)
selectButton.pack(side=LEFT, padx = 2, pady=2)

loc = StringVar()
tabel2 = ttk.Label(bottom_frame, textvariable=loc, width=17, background="white", relief = SUNKEN)
tabel2.pack(side=LEFT, padx = 2, pady = 2)


center_frame.grid_columnconfigure(0, weight=1)
center_frame.grid_rowconfigure(0, weight=1)
center_frame.grid_columnconfigure(1, weight=1)
center_frame.grid_rowconfigure(1, weight=1)
center_frame.grid_columnconfigure(2, weight=1)
center_frame.grid_rowconfigure(2, weight=1)

ttk.Label(center_frame, text='Sisestage loomade\narvud kuu alguses', font=("Helvetica 12 bold")).grid(column = 0, columnspan = 2, row=0, padx=5, sticky = S)

validation = center_frame.register(only_numbers)
validation2 = center_frame.register(numbers_dot)

ttk.Label(center_frame, text='uted', font=("Helvetica 10 bold")).grid(column = 1, row=1, padx=5, sticky = S) 
põhikarja_uted = ttk.Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
põhikarja_uted.insert(0,0)
põhikarja_uted.grid(row=2, column = 1, padx=5, sticky = S)

ttk.Label(center_frame, text='jäärad', font=("Helvetica 10 bold")).grid(column = 0, row=1, padx=5, sticky = S) 
põhikarja_jäärad = ttk.Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
põhikarja_jäärad.insert(0,0)
põhikarja_jäärad.grid(row=2, padx=5, sticky = S)

ttk.Label(center_frame, text='utikud', font=("Helvetica 10 bold")).grid(column = 1, row=3, padx=5, sticky = S) 
utikud = ttk.Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
utikud.insert(0,0)
utikud.grid(row=4, column = 1, padx=5, sticky = S)

ttk.Label(center_frame, text='jäärikud', font=("Helvetica 10 bold")).grid(column = 0, row=3, padx=5, sticky = S) 
jäärikud = ttk.Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
jäärikud.insert(0,0)
jäärikud.grid(row=4, padx=5, sticky = S)

ttk.Label(center_frame, text='utt-talled', font=("Helvetica 10 bold")).grid(column = 1, row=5, padx=5, sticky = S) 
utt_talled = ttk.Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
utt_talled.insert(0,0)
utt_talled.grid(row=6, column = 1, padx=5, sticky = S)

ttk.Label(center_frame, text='jäär-talled', font=("Helvetica 10 bold")).grid(column = 0, row=5, padx=5, sticky = S) 
jäär_talled = ttk.Entry(center_frame, width = 4, validate="key", validatecommand=(validation, '%S'))
jäär_talled.insert(0,0)
jäär_talled.grid(row=6, padx=5, sticky = S)

ttk.Label(center_frame, text='Sisestage alguskuupäev', font=("Helvetica 10 bold")).grid(row=7, columnspan = 2, padx=5, sticky = S) 
algus = ttk.Entry(center_frame, validate="key", validatecommand=(validation2, '%S'))
algus.grid(row=8, padx=5, sticky = S, columnspan = 2)
algus.insert(0, "dd.mm.yyyy")
algus.bind("<Button-1>", del_ins)


ttk.Label(center_frame, text='Sisestage lõppkuupäev', font=("Helvetica 10 bold")).grid(row=9, columnspan = 2, padx=5, sticky = S) 
lõpp = ttk.Entry(center_frame, validate="key", validatecommand=(validation2, '%S'))
lõpp.grid(row=10, padx=5, sticky = S, columnspan = 2)
lõpp.insert(0, "dd.mm.yyyy")
lõpp.bind("<Button-1>", del_ins2)


lamb = Image.open("rehekivi.bmp")
resized = lamb.resize((150, 120),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
lambLabel = ttk.Label(top_frame, image = photo, background = "white", anchor="center")
lambLabel.image = photo
lambLabel.pack(fill = "x")


ttk.Label(center_frame, text='Sissetulek', font=("Helvetica 12 bold")).grid(row=0, column=2, padx=5, sticky = S)
ttk.Label(center_frame, text='Kokku').grid(row=1, column=2, padx=5, sticky = S)
ttk.Label(center_frame, text='Teisest rühmast').grid(row=3, column=2, padx=5, sticky = S)
ttk.Label(center_frame, text='Sünd').grid(row=5, column=2, padx=5, sticky = S)
ttk.Label(center_frame, text='Ostetud').grid(row=7, column=2, padx=5, sticky = S) 
ttk.Label(center_frame, text='Muu').grid(row=9, column=2, padx=5, sticky = S)
e0 = ttk.Label(center_frame, relief = SUNKEN, width=17, background="white")
e0.grid(row=2, column=2, padx=5, sticky = S)
e1 = ttk.Label(center_frame, relief = SUNKEN, width=17, background="white")
e1.grid(row=4, column=2, padx=5, sticky = S)
e2 = ttk.Label(center_frame, relief = SUNKEN, width=17, background="white")
e2.grid(row=6, column=2, padx=5, sticky = S)
e3 = ttk.Label(center_frame, relief = SUNKEN, width=17, background="white")
e3.grid(row=8, column=2, padx=5, sticky = S)
e4 = ttk.Label(center_frame, relief = SUNKEN, width=17, background="white")
e4.grid(row=10, column=2, padx=5, sticky = S)


ttk.Label(center_frame, text='Väljaminek', font=("Helvetica 12 bold")).grid(row=0, column=3, padx=5, sticky = S)
ttk.Label(center_frame, text='Kokku').grid(row=1, column=3, padx=5, sticky = S)
ttk.Label(center_frame, text='Teise rühma').grid(row=3, column=3, padx=5, sticky = S)
ttk.Label(center_frame, text='Hukkumine').grid(row=5, column=3, padx=5, sticky = S) 
ttk.Label(center_frame, text='Müük').grid(row=7, column=3, padx=5, sticky = S)
ttk.Label(center_frame, text='Lihaks').grid(row=9, column=3, padx=5, sticky = S)
e5 = ttk.Label(center_frame, relief = SUNKEN, width=17, background="white")
e5.grid(row=2, column=3, padx=5, sticky = S)
e6 = ttk.Label(center_frame, relief = SUNKEN, width=17, background="white")
e6.grid(row=4, column=3, padx=5, sticky = S)
e7 = ttk.Label(center_frame, relief = SUNKEN, width=17, background="white")
e7.grid(row=6, column=3, padx=5, sticky = S)
e8 = ttk.Label(center_frame, relief = SUNKEN, width=17, background="white")
e8.grid(row=8, column=3, padx=5, sticky = S)
e9 = ttk.Label(center_frame, relief = SUNKEN, width=17, background="white")
e9.grid(row=10, column=3, padx=5, sticky = S)



root.mainloop()
