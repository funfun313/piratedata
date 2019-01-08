from tkinter import *

window1 = Tk()

#frame1
frame1= Frame(window1)
title =Label(frame1,text="Pirate Database", font="Arial 20")
title.pack()

#frame2
frame2= Frame(window1)
searchbox = Entry(frame2, font="Arial 20")
searchbox.pack()

#frame3
frame3= Frame(window1)
name =Label(frame3, text="Name", font="Arial 20")
name.grid(row=0,column=1)
arrow1 =Button(frame3, text="<", font="Arial 20")
arrow1.grid(row=1,column=0)
pic =Label(frame3, text="picture", font="Arial 16")
pic.grid(row=1,column=1)
arrow2 =Button(frame3, text=">", font="Arial 20")
arrow2.grid(row=1,column=2)
ship =Label(frame3, text="Ship", font="Arial 16")
ship.grid(row=2,column=1)
fict =Label(frame3, text="Fictional", font="Arial 16")
fict.grid(row=3,column=1)
#frame4
frame4= Frame(window1)
listbox = Listbox(frame4, font="Arial 20")
listbox.grid(row=0,column=0)
    #dictionary of sample items
d= {1:"Annie", 2:"Anna", 3: "Ani"}
for item in d:
    listbox.insert(END, d[item])
new =Button(frame4, text="New", font="Arial 20")
new.grid(row=1,column=0)
quitme =Button(frame4, text="Quit", font="Arial 20")
quitme.grid(row=1,column=1)
    
#grid the frames into the window
frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)

window1.mainloop()
