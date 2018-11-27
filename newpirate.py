from tkinter import*
def addnew():
    x=0
    #create a new instance of pirate class
    #get values out of boxes
    #load into pirate
    #clear boxes
    #generate dict
    #create new instance of file manager class
    #generate random id
    #use file manager to save the pirate dict into our pirate database
myfont="Arial 14 bold"
root = Tk()
root.title("Add a Pirate!")

#generating...
title = Label(root, text="New Pirate", font="Arial 20 bold")
nameLabel =Label(root, text="Name", font=myfont)
shipLabel =Label(root, text="Ship", font=myfont)
fictLabel =Label(root, text="Fictional", font=myfont)
nBox= Entry(root, font=myfont)
sBox= Entry(root, font=myfont)
btn= Button(root, text ="Save", font="Arial 20 bold", bg="#eeddff", command = addnew)

#dropdown...
optionstring= StringVar(root)
optionstring.set("true")
fictdrop = OptionMenu(root, optionstring, "true", "false")
fictdrop.config(font=myfont)
fictdrop.nametowidget(fictdrop.menuname).config(font=myfont)

#adding...
title.grid(row=0,column=0,columnspan=2)
nameLabel.grid(row=1,column=0)
shipLabel.grid(row=2,column=0)
fictLabel.grid(row=3,column=0)
nBox.grid(row=1, column=1)
sBox.grid(row=2, column=1)
btn.grid(row=4,column=0, columnspan=2, sticky = "E")
fictdrop.grid(row=3,column=1, sticky="W") 

root.mainloop()

