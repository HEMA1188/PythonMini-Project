#9.create option button using tkinter GUI in python

from tkinter import*
def sel():
   selection = "You are selected the Programming Language is  " + str(var.get())
   label.config(text = selection)

master = Tk()
var = StringVar()
lbl = Label(text = "Favourite programming language:")  
lbl.pack()  
R1 = Radiobutton(master, text="Python", variable=var, value='Python',
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(master, text="C++", variable=var, value="C++",
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(master, text="Java", variable=var, value="Java",
                  command=sel)
R3.pack( anchor = W)

label = Label(master)
label.pack()
master.mainloop()