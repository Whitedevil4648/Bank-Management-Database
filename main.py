from cgitb import text
from glob import glob
from pydoc import classname
import tkinter as tk
global bg
def saving():
    if user.get()+ passw.get() == "":
        label=tk.Label(signupwin,text="Please enter your User name and Password")
        l1 = canvas2.create_window( 50, 100, anchor = "nw",window = label)
    else:
         file = open("data.txt","a")
         file.write(user.get()+" "+passw.get()+"\n")
         file.close()
def signupwindow():
    global signupwin
    signupwin = tk.Toplevel(win)
    signupwin.geometry("642x635")
    global canvas2
    canvas2 = tk.Canvas(signupwin, width = 635,height = 642)
    canvas2.pack(fill = "both", expand = True)
    canvas2.create_image( 0, 0, image = bg,anchor = "nw")   
    global user
    user =tk.Entry(signupwin,width=15)
    global passw
    passw = tk.Entry(signupwin,width=15)
    e1 = canvas2.create_window( 200, 120, anchor = "nw",window = user)
    e2 = canvas2.create_window( 200, 160, anchor = "nw",window = passw)
    uword=tk.Label(signupwin,text="Enter your Username")
    pword=tk.Label(signupwin,text="Enter your Password")
    t1 = canvas2.create_window( 50, 120, anchor = "nw",window = uword)
    t2 = canvas2.create_window( 50, 160, anchor = "nw",window = pword)
    dsu = tk.Button(signupwin,text = "Create your Account",command=saving)
    bd = canvas2.create_window(50,260,anchor="nw",window=dsu)
    signupwin.mainloop()




win = tk.Tk(className=" AID Bank")

win.geometry("642x635")

bg = tk.PhotoImage(file = "1.png") 


 
canvas1 = tk.Canvas(win, width = 635,height = 642)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")

# main screen button
si = tk.Button(win,text="Sign In",)
su = tk.Button(win,text="Create new Account",command= signupwindow )

# packing
b1 = canvas1.create_window( 100, 120, anchor = "nw",window = si)
b2 = canvas1.create_window( 100, 160, anchor = "nw",window = su)

win.mainloop()