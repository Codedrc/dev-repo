from tkinter import *
dev = Tk()
dev.geometry("450x600")
dev.title("login page ")

title = Label(dev,text="Registretion Form ",width=30,font=20,bg="blue").place(x=70,y=30)

name =Label(dev,text=" NAME ",font=40,fg="black",highlightcolor="yellow").place(x=90,y=90)
a1 = Entry(dev)
a1.place(x=90,y=110)

name1 = Label(dev,text=" AGE ",font=40,fg="black",highlightbackground="black").place(x=90,y= 140)
a2 = Entry(dev)
a2.place(x=90,y=160) 

name2 = Label(dev,text=" PHONE NO ",font=40,fg="black").place(x=90,y=190)
a3 = Entry(dev)
a3.place(x=90,y=210)

name3 = Label(dev,text= "EMAIL ID ",font=40,fg="black").place(x=90,y=240)
a4 = Entry(dev)
a4.place(x=90,y=260)

name6 = Label(dev,text="GENDER",font=40,fg="black").place(x=90,y=290)
name4 = IntVar()
name5 = Radiobutton(dev,text="male",variable=name4,value=1).place(x=90,y=330)
name8 = Radiobutton(dev,text="female",variable=name4,value=2).place(x=150,y=330)

name9 = Label(dev,text="PASSWORD",font=40,fg="BLACK").place(x=90,y=350)
A5 = Entry(dev)
A5.place(x=90,y=370)
Button(dev,text="SUBMITE",font=40,fg="black",bg="green").place(x=115,y=410)

Button(dev,text="already sign in ",font=40,fg="black",bg="green").place(x=300,y=560)

Button(dev,text="clear",font=40,fg="black",bg = "green").place(x= 10,y=560)


dev.mainloop()