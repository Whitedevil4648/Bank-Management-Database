from cgitb import text
from glob import glob
from pydoc import classname
from queue import Empty
import tkinter as tk
global bg
def saving():
    found = False
    empty = False
    nf = open("data.txt","r")
    for line in nf:
        txt = line.split()[0]
        if(user.get()==txt):
            found  = True
            label=tk.Label(signupwin,text="Account with this username already exist.Kindly use another Username.")
            l1 = canvas2.create_window( 50, 210, anchor = "nw",window = label)
        elif user.get()+ passw.get() == "":
            empty = True
            label=tk.Label(signupwin,text="Please enter your User name and Password")
            l1 = canvas2.create_window( 50, 210, anchor = "nw",window = label)
    
        
        
    
    nf.close()
    if(not(found or empty)):
         file = open("data.txt","a")
         file.write(user.get()+" "+passw.get()+"\n")
         file.close()
         label=tk.Label(signupwin,text="Your Account is Successfully created close this window now")
         l1 = canvas2.create_window( 50, 210, anchor = "nw",window = label)
def check():
    found = False
    empty =False
    nf = open("data.txt","r")
    for line in nf:
        if(suser.get()+" "+spassw.get()==line.strip()):
            found  = True
            label=tk.Label(signinwin,text="Successfully Logged In")
            l1 = canvas3.create_window( 50, 210, anchor = "nw",window = label)
            #new win function
        elif suser.get()+ spassw.get() == "":
            empty = True
            label=tk.Label(signinwin,text="Please enter your User name and Password")
            l1 = canvas3.create_window( 50, 210, anchor = "nw",window = label)
    
    if(not(found or empty)):
        label=tk.Label(signinwin,text="Either \nYour Account doesnot exists please create one.\nor You have entered wrong username or password")
        l1 = canvas3.create_window( 50, 210, anchor = "nw",window = label)

        
    
    nf.close()

def signin():
    global signinwin
    signinwin = tk.Toplevel(win)
    signinwin.geometry("642x635")
    global canvas3
    canvas3 = tk.Canvas(signinwin, width = 635,height = 642)
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, image = bg,anchor = "nw")
    global suser
    suser =tk.Entry(signinwin,width=15)
    global spassw
    spassw = tk.Entry(signinwin,width=15)
    e1 = canvas3.create_window( 200, 120, anchor = "nw",window = suser)
    e2 = canvas3.create_window( 200, 160, anchor = "nw",window = spassw)
    uword=tk.Label(signinwin,text="Enter your Username")
    pword=tk.Label(signinwin,text="Enter your Password")
    t1 = canvas3.create_window( 50, 120, anchor = "nw",window = uword)
    t2 = canvas3.create_window( 50, 160, anchor = "nw",window = pword)
    dsi = tk.Button(signinwin,text = "Sign In",command=check)
    bd = canvas3.create_window(50,260,anchor="nw",window=dsi)
    signinwin.mainloop()  
       
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
si = tk.Button(win,text="Sign In",command=signin)
su = tk.Button(win,text="Create new Account",command= signupwindow )

# packing
b1 = canvas1.create_window( 100, 120, anchor = "nw",window = si)
b2 = canvas1.create_window( 100, 160, anchor = "nw",window = su)

win.mainloop()