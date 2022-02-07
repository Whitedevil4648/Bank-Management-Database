from cgitb import text
from glob import glob
from pydoc import classname
from queue import Empty
import tkinter as tk
global bg
def update():
    file = open("data.txt","r")
    lst = file.readlines()
    file.close()
    for line in lst:
        if line.split()[0] == suser.get():
            
            ind = lst.index(line)
    lst[ind] = userna.get()+" "+passwo.get()+" "+dobi.get()+" "+gend.get()+" "+addr.get("1.0",'end-1c')+"\n"
    file = open("data.txt","w")
    for li in lst:
        file.write(li)
            
    file.close()
    file = open("balance.txt","r")
    lstnew = file.readlines()
    file.close()
    for line in lstnew:
        if line.split()[0] == suser.get():
            oldanobal = line.split()[1]
            ind = lst.index(line)
    lstnew[ind] = userna.get()+" "+ str(oldanobal)
    file = open("balance.txt","w")
    for li in lstnew:
        file.write(li)
    file.close()
    
def withdrawing():
    file = open("balance.txt","r")
    lst = file.readlines()
    file.close()
    

    for line in lst:
        if line.split()[0] == suser.get():
            oldbal = line.split()[1]
            ind = lst.index(line)
            
    lst[ind]=suser.get() + " " + str(int(oldbal) - int(withd.get()))+"\n"
    
    file = open("balance.txt","w")
    for li in lst:
        file.write(li)
            
    file.close()
    donewit=tk.Label(witwin,text="Successfull Withdrawn Money!!")
    withw = canvas9.create_window( 400, 160, anchor = "nw",window = donewit)
    witwin.destroy()
def depositing():
    file = open("balance.txt","r")
    lst = file.readlines()
    file.close()
    

    for line in lst:
        if line.split()[0] == suser.get():
            oldbal = line.split()[1]
            ind = lst.index(line)
            
    lst[ind]=suser.get() + " " + str(int(oldbal) + int(dep.get()))+"\n"
    print(lst)
    file = open("balance.txt","w")
    for li in lst:
        file.write(li)
            
    file.close()
    donedep=tk.Label(depwin,text="Successfull Deposited Money!!")
    depw = canvas8.create_window( 400, 160, anchor = "nw",window = donedep)
    depwin.destroy()
def profile():
    mainwin.destroy()
    global prowin
    prowin = tk.Toplevel(win)
    canvas5 = tk.Canvas(prowin, width = 635,height = 642)
    canvas5.pack(fill = "both", expand = True)
    canvas5.create_image( 0, 0, image = bg,anchor = "nw")
    file = open("data.txt","r")
    lst = file.readlines()
    file.close()
    for line in lst:
        if line.split()[0] == suser.get():
            
            ind = lst.index(line)
    prolst = lst[ind].split()
    usern = prolst[0]
    date = prolst[2]
    gen = prolst[3]
    addres = prolst[4]
    la1=tk.Label(prowin,text="Username"+" - "+usern)
    lap1 = canvas5.create_window( 50, 120, anchor = "nw",window = la1)
    la2=tk.Label(prowin,text="Date fo Birth"+" - "+date)
    lap2 = canvas5.create_window( 50, 160, anchor = "nw",window = la2)
    la3=tk.Label(prowin,text="Gender"+" - "+gen)
    lap3 = canvas5.create_window( 50, 200, anchor = "nw",window = la3)
    la4=tk.Label(prowin,text="Address"+" - "+addres)
    lap4 = canvas5.create_window( 50, 240, anchor = "nw",window = la4)
    exitb = tk.Button(mainwin,text="Exit",command=exit)
    lap5 = canvas5.create_window( 50, 280, anchor = "nw",window = exitb)
    prowin.mainloop()
def chgpro():
    mainwin.destroy()
    global chngprowin
    chngprowin = tk.Toplevel(win)
    canvas6 = tk.Canvas(chngprowin, width = 635,height = 642)
    canvas6.pack(fill = "both", expand = True)
    canvas6.create_image( 0, 0, image = bg,anchor = "nw")
    global userna,passwo,dobi,gend,addr
    userna =tk.Entry(chngprowin,width=15)
    passwo = tk.Entry(chngprowin,width=15)
    dobi = tk.Entry(chngprowin,width=15)
    gend = tk.Entry(chngprowin,width=5)
    addr = tk.Text(chngprowin,width=20,height=5)
    e1 = canvas6.create_window( 200, 120, anchor = "nw",window = userna)
    e2 = canvas6.create_window( 200, 160, anchor = "nw",window = passwo)
    e3 = canvas6.create_window( 280, 200, anchor = "nw",window = dobi)
    e4 = canvas6.create_window( 200, 240, anchor = "nw",window = gend)
    e5 = canvas6.create_window( 200, 280, anchor = "nw",window = addr)
    uword=tk.Label(chngprowin,text="Enter your (new) Username")
    pword=tk.Label(chngprowin,text="Enter your (new) Password")
    dobword=tk.Label(chngprowin,text="Enter your (new) Date of Birth(DD/MM/YYYY)")
    gword=tk.Label(chngprowin,text="Enter your (new) Gender(M/F)")
    aword=tk.Label(chngprowin,text="Enter your (new) Address")
    t1 = canvas6.create_window( 50, 120, anchor = "nw",window = uword)
    t2 = canvas6.create_window( 50, 160, anchor = "nw",window = pword)
    t3 = canvas6.create_window( 50, 200, anchor = "nw",window = dobword)
    t4 = canvas6.create_window( 50, 240, anchor = "nw",window = gword)
    t5 = canvas6.create_window( 50, 280, anchor = "nw",window = aword)
    dsu = tk.Button(chngprowin,text = "Update your Info",command=update)
    bd = canvas6.create_window(50,380,anchor="nw",window=dsu)
    chngprowin.mainloop()
def exit():
    mainwin.destroy()
def deactivate():
    file = open("balance.txt","r")
    lst = file.readlines()
    file.close()
    file = open("balance.txt","w")
    for line in lst:
        if line.split()[0] != suser.get():  
            file.write(line) 
    file.close()
    file = open("data.txt","r")
    lst = file.readlines()
    file.close()
    file = open("data.txt","w")
    for line in lst:
        if line.split()[0] != suser.get():  
            file.write(line) 
    file.close()  
    deacwin.destroy()        

def deac():
    mainwin.destroy()
    global deacwin
    deacwin = tk.Toplevel(win)
    canvas7 = tk.Canvas(deacwin, width = 635,height = 642)
    canvas7.pack(fill = "both", expand = True)
    canvas7.create_image( 0, 0, image = bg,anchor = "nw")
    label1=tk.Label(deacwin,text="Please confirm if you really want to deactivate ?")
    lp1 = canvas7.create_window( 50, 120, anchor = "nw",window = label1)
    dsu = tk.Button(deacwin,text = "Confirm Now",command=deactivate)
    bd = canvas7.create_window(50,200,anchor="nw",window=dsu)
    deacwin.mainloop()
    
def deposit():
    mainwin.destroy()
    global depwin
    depwin = tk.Toplevel(win)
    global canvas8
    canvas8 = tk.Canvas(depwin, width = 635,height = 642)
    canvas8.pack(fill = "both", expand = True)
    canvas8.create_image( 0, 0, image = bg,anchor = "nw")
    global dep
    dep =tk.Entry(depwin,width=15)
    
    aword=tk.Label(depwin,text="Enter amount you want to deposit")
    dept1 = canvas8.create_window( 400, 120, anchor = "nw",window = dep)
    dept2 = canvas8.create_window( 50, 120, anchor = "nw",window = aword)
    dsu = tk.Button(depwin,text = "Deposit Now",command=depositing)
    bd = canvas8.create_window(50,200,anchor="nw",window=dsu)



    depwin.mainloop()
def withdraw():
    mainwin.destroy()
    global witwin
    witwin = tk.Toplevel(win)
    global canvas9
    canvas9 = tk.Canvas(witwin, width = 635,height = 642)
    canvas9.pack(fill = "both", expand = True)
    canvas9.create_image( 0, 0, image = bg,anchor = "nw")
    global withd
    withd =tk.Entry(witwin,width=15)
    
    aword=tk.Label(witwin,text="Enter amount you want to withdraw")
    dept1 = canvas9.create_window( 400, 120, anchor = "nw",window = withd)
    dept2 = canvas9.create_window( 50, 120, anchor = "nw",window = aword)
    dsu = tk.Button(witwin,text = "Withdraw Now",command=withdrawing)
    bd = canvas9.create_window(50,200,anchor="nw",window=dsu)
    witwin.mainloop()
def mainwindow():

    global mainwin
    mainwin = tk.Toplevel(win)
    mainwin.geometry("642x635")
    global canvas4
    canvas4 = tk.Canvas(mainwin, width = 635,height = 642)
    canvas4.pack(fill = "both", expand = True)
    canvas4.create_image( 0, 0, image = bg,anchor = "nw")
    b1 = tk.Button(mainwin,text="Profile",command=profile)
    b2 = tk.Button(mainwin,text="Change Profile",command=chgpro)
    b3 = tk.Button(mainwin,text="Exit",command=exit)
    b4 = tk.Button(mainwin,text="Deactivate",command=deac)
    b5 = tk.Button(mainwin,text="Deposit",command=deposit)
    b6 = tk.Button(mainwin,text="Withdraw",command=withdraw)
    balance = tk.Label(mainwin,text="Balance")
    file = open("balance.txt","r")
    lstline = file.readlines()

    file.close()
    for line in lstline:
        if line.split()[0] == suser.get():
            inde = lstline.index(line)
    
    anolst = lstline[inde].split()
    
    balen = anolst[1]
    
    bal1 = tk.Label(mainwin,text=""+balen)
    bal = canvas4.create_window( 250, 120, anchor = "nw",window = balance)
    bale = canvas4.create_window( 250, 160, anchor = "nw",window = bal1)
    cb1 = canvas4.create_window( 100, 120, anchor = "nw",window = b1)
    cb2 = canvas4.create_window( 100, 160, anchor = "nw",window = b2)
    cb3 = canvas4.create_window( 100,200, anchor = "nw", window = b3)
    cb4 = canvas4.create_window( 400, 120, anchor = "nw",window = b4)
    cb5 = canvas4.create_window( 400, 160, anchor = "nw",window = b5)
    cb6 = canvas4.create_window( 400, 200, anchor = "nw",window = b6)
    mainwin.mainloop()

def saving():
    found = False
    empty = False
    nf = open("data.txt","r")
    for line in nf:
        txt = line.split()[0]
        if(user.get()==txt):
            found  = True
            label=tk.Label(signupwin,text="Account with this username already exist.Kindly use another Username.")
            l1 = canvas2.create_window( 50, 420, anchor = "nw",window = label)
        elif (user.get() ==""):
            empty = True
            label=tk.Label(signupwin,text="Please fill username")
            l1 = canvas2.create_window( 50, 420, anchor = "nw",window = label)
        elif (passw.get() == ""):
            empty = True
            label=tk.Label(signupwin,text="Please fill Password")
            l1 = canvas2.create_window( 50, 420, anchor = "nw",window = label)
        elif (dob.get()==""):
            empty = True
            label=tk.Label(signupwin,text="Please fill Date of Birth")
            l1 = canvas2.create_window( 50, 420, anchor = "nw",window = label)
        elif (gender.get()==""):
            empty = True
            label=tk.Label(signupwin,text="Please fill your Gender")
            l1 = canvas2.create_window( 50, 420, anchor = "nw",window = label)
        elif (address.get("1.0",'end-1c')==""):
            empty = True
            label=tk.Label(signupwin,text="Please fill your address")
            l1 = canvas2.create_window( 50, 420, anchor = "nw",window = label)
        
        
    
    nf.close()
    if(not(found or empty)):
         file = open("data.txt","a")
         file.write(user.get()+" "+passw.get()+" "+dob.get()+" "+gender.get()+" "+address.get("1.0",'end-1c')+"\n")
         file.close()
         label=tk.Label(signupwin,text="Your Account is Successfully created close this window now")
         l1 = canvas2.create_window( 50, 420, anchor = "nw",window = label)
    balfile = open("balance.txt","a")
    file.write(user.get()+" "+"0")
    balfile.close()

def check():
    
    found = False
    empty =False
    nf = open("data.txt","r")
    for line in nf:
        if(suser.get()+" "+spassw.get()==line.split()[0]+" "+line.split()[1]):
            found  = True
            label=tk.Label(signinwin,text="Successfully Logged In")
            l1 = canvas3.create_window( 50, 210, anchor = "nw",window = label)
            mainwindow()
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
    global user,passw,dob,gender,address
    user =tk.Entry(signupwin,width=15)
    passw = tk.Entry(signupwin,width=15)
    dob = tk.Entry(signupwin,width=15)
    gender = tk.Entry(signupwin,width=5)
    address = tk.Text(signupwin,width=20,height=5)
    e1 = canvas2.create_window( 200, 120, anchor = "nw",window = user)
    e2 = canvas2.create_window( 200, 160, anchor = "nw",window = passw)
    e3 = canvas2.create_window( 280, 200, anchor = "nw",window = dob)
    e4 = canvas2.create_window( 200, 240, anchor = "nw",window = gender)
    e5 = canvas2.create_window( 200, 280, anchor = "nw",window = address)
    uword=tk.Label(signupwin,text="Enter your Username")
    pword=tk.Label(signupwin,text="Enter your Password")
    dobword=tk.Label(signupwin,text="Enter your Date of Birth(DD/MM/YYYY)")
    gword=tk.Label(signupwin,text="Enter your Gender(M/F)")
    aword=tk.Label(signupwin,text="Enter your Address")
    t1 = canvas2.create_window( 50, 120, anchor = "nw",window = uword)
    t2 = canvas2.create_window( 50, 160, anchor = "nw",window = pword)
    t3 = canvas2.create_window( 50, 200, anchor = "nw",window = dobword)
    t4 = canvas2.create_window( 50, 240, anchor = "nw",window = gword)
    t5 = canvas2.create_window( 50, 280, anchor = "nw",window = aword)
    dsu = tk.Button(signupwin,text = "Create your Account",command=saving)
    bd = canvas2.create_window(50,380,anchor="nw",window=dsu)
    signupwin.mainloop()




win = tk.Tk(className=" AID Bank")

win.geometry("642x635")

bg = tk.PhotoImage(file = "1.png") 


 
canvas1 = tk.Canvas(win, width = 635,height = 642)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")


si = tk.Button(win,text="Sign In",command=signin)
su = tk.Button(win,text="Create new Account",command= signupwindow )

b1 = canvas1.create_window( 100, 120, anchor = "nw",window = si)
b2 = canvas1.create_window( 100, 160, anchor = "nw",window = su)

win.mainloop()