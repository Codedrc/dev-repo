from tkinter import *

display = Tk() 
display.geometry("450x350")
display.title("Login Page")

title  = Label(display,text="login page",font=30,width=20,bg="red").pack(padx=20,pady=30)

username = Label(display,text="name - ",font=20).place(x=60,y= 80)
enter = Entry(display)
enter.place(x=170,y=80)

email = Label(display,text="email id - ",font= 20).place(x=60,y=120)
enter2 = Entry(display)
enter2.place(x=170,y=120)


password =Label(display,text="password -",font=20).place(x=60,y=160)
enter3 = Entry(display)
enter3.place(x=170,y=160)

Button(display,text="submit",font=20).place(x=150,y=200)
Button(display,text="forgot password",font=20).place(x=110,y=240)
Button(display,text="clear",font=20).place(x=375,y=310)


display.mainloop()