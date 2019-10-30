from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()

frame = Frame(root, height=300,width=600)
frame.pack()

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

def browse_file():
    fname = filedialog.askopenfilename(filetypes = (("CSV failid", "*.csv"), ("All files", "*")))
    var.set(fname)
    label.pack(side=LEFT)
    label.config(text = fname)

root.wm_title("Browser")
broButton = Button(master = root, text = 'Browse', width = 6, command=browse_file)
broButton.pack(side=LEFT, padx = 2, pady=2)

#text = Text(frame)
#text.insert(INSERT, "Sisestage analüüsitav fail")
#text.pack()


#text.insert(END, "Bye Bye.....")
#def helloCallBack():
    #messagebox.showinfo( "Hello Python", "Hello World")
#B = Button(root, text ="Hello", command = helloCallBack)




#B.pack(side = LEFT)
#dirname = filedialog.askdirectory(parent=root, initialdir="/",title='Please select a directory')
root.mainloop()
