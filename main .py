from cgitb import text
from glob import glob
from pydoc import classname
from queue import Empty
import tkinter as tk
global bg
def update():
    
    empty = False
    if (userna.get() ==""):
        empty = True
        label=tk.Label(chngprowin,text="Please fill username")
        l1 = canvas6.create_window( 50, 750, anchor = "nw",window = label)
    elif (passwo.get() == ""):
        empty = True
        label=tk.Label(chngprowin,text="Please fill Password")
        l1 = canvas6.create_window( 50, 750, anchor = "nw",window = label)
    elif (dobi.get()==""):
        empty = True
        label=tk.Label(chngprowin,text="Please fill Date of Birth")
        l1 = canvas6.create_window( 50, 750, anchor = "nw",window = label)
    elif (gend.get()==""):
        empty = True
        label=tk.Label(chngprowin,text="Please fill your Gender")
        l1 = canvas6.create_window( 50, 750, anchor = "nw",window = label)
    elif (addr.get("1.0",'end-1c')==""):
        empty = True
        label=tk.Label(chngprowin,text="Please fill your address")
        l1 = canvas6.create_window( 50, 750, anchor = "nw",window = label)
        
        
    
    if(not(empty)):
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
                ind = lstnew.index(line)
        lstnew[ind] = userna.get()+" "+ str(oldanobal)
        print(userna.get(),lstnew)
        file = open("balance.txt","w")
        for li in lstnew:
            file.write(li)
        file.close()   
        labe1=tk.Label(chngprowin,text="Update successfully applied!!")
        lab1 = canvas6.create_window( 50, 750, anchor = "nw",window = labe1) 


    
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
    canvas5 = tk.Canvas(prowin, width = win.winfo_screenwidth(),height = win.winfo_screenheight() )
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
    n = len(prolst)
    addres = ''
    for i in range(4,n):
        addres = addres +prolst[i]+' ' 
    la1=tk.Label(prowin,text="Username"+" - "+usern,height = 1,width=31,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    lap1 = canvas5.create_window( 50, 250, anchor = "nw",window = la1)
    la2=tk.Label(prowin,text="Date fo Birth"+" - "+date,height = 1,width=31,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    lap2 = canvas5.create_window( 50, 320, anchor = "nw",window = la2)
    la3=tk.Label(prowin,text="Gender"+" - "+gen,height = 1,width=31,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    lap3 = canvas5.create_window( 50, 390, anchor = "nw",window = la3)
    la4=tk.Label(prowin,text="Address"+" - "+addres,height = 1,width=31,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    lap4 = canvas5.create_window( 50, 460, anchor = "nw",window = la4)
    exitb = tk.Button(mainwin,text="Exit",command=exit,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    lap5 = canvas5.create_window( 50, 530, anchor = "nw",window = exitb)
    prowin.mainloop()
def chgpro():
    mainwin.destroy()
    global chngprowin
    chngprowin = tk.Toplevel(win)
    global canvas6
    canvas6 = tk.Canvas(chngprowin, width = win.winfo_screenwidth(),height = win.winfo_screenheight())
    canvas6.pack(fill = "both", expand = True)
    canvas6.create_image( 0, 0, image = bg,anchor = "nw")
    global userna,passwo,dobi,gend,addr
    userna =tk.Entry(chngprowin,width=15,font="CascadiaCode 15")
    passwo = tk.Entry(chngprowin,width=15,font="CascadiaCode 15")
    dobi = tk.Entry(chngprowin,width=15,font="CascadiaCode 15")
    gend = tk.Entry(chngprowin,width=5,font="CascadiaCode 15")
    addr = tk.Text(chngprowin,width=20,height=5,font="CascadiaCode 15")
    e1 = canvas6.create_window( 500, 250, anchor = "nw",window = userna,height=50,width=200)
    e2 = canvas6.create_window( 500, 320, anchor = "nw",window = passwo,height=50,width=200)
    e3 = canvas6.create_window( 580, 390, anchor = "nw",window = dobi,height=50,width=200)
    e4 = canvas6.create_window( 500, 460, anchor = "nw",window = gend,height=50,width=200)
    e5 = canvas6.create_window( 500, 530, anchor = "nw",window = addr)
    uword=tk.Label(chngprowin,text="Enter your Username",height=1,width=20,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    pword=tk.Label(chngprowin,text="Enter your Password",height = 1,width=20,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    dobword=tk.Label(chngprowin,text="Enter your Date of Birth(DD/MM/YYYY)",height = 1,width=31,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    gword=tk.Label(chngprowin,text="Enter your Gender(M/F)",height = 1,width=20,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    aword=tk.Label(chngprowin,text="Enter your Address",height = 1,width=20,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    t1 = canvas6.create_window( 50, 250, anchor = "nw",window = uword)
    t2 = canvas6.create_window( 50, 320, anchor = "nw",window = pword)
    t3 = canvas6.create_window( 50, 390, anchor = "nw",window = dobword)
    t4 = canvas6.create_window( 50, 460, anchor = "nw",window = gword)
    t5 = canvas6.create_window( 50, 530, anchor = "nw",window = aword)
    dsu = tk.Button(chngprowin,text = "Update your Info",command=update,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    bd = canvas6.create_window(50,600,anchor="nw",window=dsu)
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
    canvas7 = tk.Canvas(deacwin, width = win.winfo_screenwidth(),height = win.winfo_screenheight())
    canvas7.pack(fill = "both", expand = True)
    canvas7.create_image( 0, 0, image = bg,anchor = "nw")
    label1=tk.Label(deacwin,text="Please confirm if you really want to deactivate ?",height = 1,width=50,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    lp1 = canvas7.create_window( 50, 250, anchor = "nw",window = label1)
    dsu = tk.Button(deacwin,text = "Confirm Now",command=deactivate,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    bd = canvas7.create_window(50,400,anchor="nw",window=dsu)
    deacwin.mainloop()
    
def deposit():
    mainwin.destroy()
    global depwin
    depwin = tk.Toplevel(win)
    global canvas8
    canvas8 = tk.Canvas(depwin, width = win.winfo_screenwidth(),height = win.winfo_screenheight())
    canvas8.pack(fill = "both", expand = True)
    canvas8.create_image( 0, 0, image = bg,anchor = "nw")
    global dep
    dep =tk.Entry(depwin,width=15,font="CascadiaCode 15")
    
    aword=tk.Label(depwin,text="Enter amount you want to deposit",height = 1,width=50,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    dept1 = canvas8.create_window( 1000, 250, anchor = "nw",window = dep,height=50,width=200)
    dept2 = canvas8.create_window( 50, 250, anchor = "nw",window = aword)
    dsu = tk.Button(depwin,text = "Deposit Now",command=depositing,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    bd = canvas8.create_window(50,350,anchor="nw",window=dsu)



    depwin.mainloop()
def withdraw():
    mainwin.destroy()
    global witwin
    witwin = tk.Toplevel(win)
    global canvas9
    canvas9 = tk.Canvas(witwin, width = win.winfo_screenwidth(),height = win.winfo_screenheight())
    canvas9.pack(fill = "both", expand = True)
    canvas9.create_image( 0, 0, image = bg,anchor = "nw")
    global withd
    withd =tk.Entry(witwin,width=15,font="CascadiaCode 15")
    
    aword=tk.Label(witwin,text="Enter amount you want to withdraw",height = 1,width=50,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    dept1 = canvas9.create_window( 1000, 250, anchor = "nw",window = withd,height=50,width=200)
    dept2 = canvas9.create_window( 50, 250, anchor = "nw",window = aword)
    dsu = tk.Button(witwin,text = "Withdraw Now",command=withdrawing,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    bd = canvas9.create_window(50,350,anchor="nw",window=dsu)
    witwin.mainloop()
def mainwindow():

    global mainwin
    mainwin = tk.Toplevel(win)
    mainwin.geometry(str(win.winfo_screenwidth())+"x"+str(win.winfo_screenheight()))
    global canvas4
    canvas4 = tk.Canvas(mainwin, width = win.winfo_screenwidth(),height = win.winfo_screenheight())
    canvas4.pack(fill = "both", expand = True)
    canvas4.create_image( 0, 0, image = bg,anchor = "nw")
    b1 = tk.Button(mainwin,text="Profile",command=profile,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    b2 = tk.Button(mainwin,text="Change Profile",command=chgpro,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    b3 = tk.Button(mainwin,text="Exit",command=exit,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    b4 = tk.Button(mainwin,text="Deactivate",command=deac,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    b5 = tk.Button(mainwin,text="Deposit",command=deposit,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    b6 = tk.Button(mainwin,text="Withdraw",command=withdraw,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    balance = tk.Label(mainwin,text="Balance",height = 1,width=20,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    file = open("balance.txt","r")
    lstline = file.readlines()

    file.close()
    for line in lstline:
        if line.split()[0] == suser.get():
            inde = lstline.index(line)
    
    anolst = lstline[inde].split()
    
    balen = anolst[1]
    
    bal1 = tk.Label(mainwin,text="₹ "+balen,height = 1,width=20,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    bal = canvas4.create_window( 600, 300, anchor = "nw",window = balance)
    bale = canvas4.create_window( 600, 400, anchor = "nw",window = bal1)
    cb1 = canvas4.create_window( 100, 300, anchor = "nw",window = b1)
    cb2 = canvas4.create_window( 100, 450, anchor = "nw",window = b2)
    cb3 = canvas4.create_window( 100,600, anchor = "nw", window = b3)
    cb4 = canvas4.create_window( 1100, 300, anchor = "nw",window = b4)
    cb5 = canvas4.create_window( 1100, 450, anchor = "nw",window = b5)
    cb6 = canvas4.create_window( 1100, 600, anchor = "nw",window = b6)
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
            l1 = canvas2.create_window( 50, 750, anchor = "nw",window = label)
        elif (user.get() ==""):
            empty = True
            label=tk.Label(signupwin,text="Please fill username")
            l1 = canvas2.create_window( 50, 750, anchor = "nw",window = label)
        elif (passw.get() == ""):
            empty = True
            label=tk.Label(signupwin,text="Please fill Password")
            l1 = canvas2.create_window( 50, 750, anchor = "nw",window = label)
        elif (dob.get()==""):
            empty = True
            label=tk.Label(signupwin,text="Please fill Date of Birth")
            l1 = canvas2.create_window( 50, 750, anchor = "nw",window = label)
        elif (gender.get()==""):
            empty = True
            label=tk.Label(signupwin,text="Please fill your Gender")
            l1 = canvas2.create_window( 50, 750, anchor = "nw",window = label)
        elif (address.get("1.0",'end-1c')==""):
            empty = True
            label=tk.Label(signupwin,text="Please fill your address")
            l1 = canvas2.create_window( 50, 750, anchor = "nw",window = label)
        
        
    
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
            l1 = canvas3.create_window( 50, 550, anchor = "nw",window = label)
            mainwindow()
        elif suser.get()+ spassw.get() == "":
            empty = True
            label=tk.Label(signinwin,text="Please enter your User name and Password")
            l1 = canvas3.create_window( 50, 550, anchor = "nw",window = label)
    
    if(not(found or empty)):
        label=tk.Label(signinwin,text="Either \nYour Account doesnot exists please create one.\nor You have entered wrong username or password")
        l1 = canvas3.create_window( 50, 550, anchor = "nw",window = label)

        
    
    nf.close()
def signin():
    global signinwin
    signinwin = tk.Toplevel(win)
    signinwin.geometry(str(win.winfo_screenwidth())+"x"+str(win.winfo_screenheight()))
    global canvas3
    canvas3 = tk.Canvas(signinwin, width = win.winfo_screenwidth(),height = win.winfo_screenheight())
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, image = bg,anchor = "nw")
    global suser
    suser =tk.Entry(signinwin,width=15,font="CascadiaCode 15")
    global spassw
    spassw = tk.Entry(signinwin,width=15,font="CascadiaCode 15")
    e1 = canvas3.create_window( 600, 250, anchor = "nw",window = suser,height=50,width=200)
    e2 = canvas3.create_window( 600, 320, anchor = "nw",window = spassw,height=50,width=200)
    uword=tk.Label(signinwin,text="Enter your Username",height = 1,width=31,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    pword=tk.Label(signinwin,text="Enter your Password",height = 1,width=31,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    t1 = canvas3.create_window( 50, 250, anchor = "nw",window = uword)
    t2 = canvas3.create_window( 50, 320, anchor = "nw",window = pword)
    dsi = tk.Button(signinwin,text = "Sign In",command=check,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    bd = canvas3.create_window(50,400,anchor="nw",window=dsi)
    signinwin.mainloop()  
def signupwindow():
    global signupwin
    signupwin = tk.Toplevel(win)
    signupwin.geometry(str(win.winfo_screenwidth())+"x"+str(win.winfo_screenheight()))
    global canvas2
    canvas2 = tk.Canvas(signupwin, width = win.winfo_screenwidth(),height = win.winfo_screenheight())
    canvas2.pack(fill = "both", expand = True)
    canvas2.create_image( 0, 0, image = bg,anchor = "nw")   
    global user,passw,dob,gender,address
    user =tk.Entry(signupwin,width=15,font="CascadiaCode 15")
    passw = tk.Entry(signupwin,width=15,font="CascadiaCode 15")
    dob = tk.Entry(signupwin,width=15,font="CascadiaCode 15")
    gender = tk.Entry(signupwin,width=5,font="CascadiaCode 15")
    address = tk.Text(signupwin,width=20,height=5,font="CascadiaCode 15")
    e1 = canvas2.create_window( 500, 250, anchor = "nw",window = user,height=50,width=200)
    e2 = canvas2.create_window( 500, 320, anchor = "nw",window = passw,height=50,width=200)
    e3 = canvas2.create_window( 580, 390, anchor = "nw",window = dob,height=50,width=200)
    e4 = canvas2.create_window( 500, 460, anchor = "nw",window = gender,height=50,width=200)
    e5 = canvas2.create_window( 500, 530, anchor = "nw",window = address)
    uword=tk.Label(signupwin,text="Enter your Username",height=1,width=20,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    pword=tk.Label(signupwin,text="Enter your Password",height = 1,width=20,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    dobword=tk.Label(signupwin,text="Enter your Date of Birth(DD/MM/YYYY)",height = 1,width=31,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    gword=tk.Label(signupwin,text="Enter your Gender(M/F)",height = 1,width=20,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    aword=tk.Label(signupwin,text="Enter your Address",height = 1,width=20,relief="groove",bg="#f2f2f2",fg="#555",font="CascadiaCode 20",padx =5,pady=3)
    t1 = canvas2.create_window( 50, 250, anchor = "nw",window = uword)
    t2 = canvas2.create_window( 50, 320, anchor = "nw",window = pword)
    t3 = canvas2.create_window( 50, 390, anchor = "nw",window = dobword)
    t4 = canvas2.create_window( 50, 460, anchor = "nw",window = gword)
    t5 = canvas2.create_window( 50, 530, anchor = "nw",window = aword)
    dsu = tk.Button(signupwin,text = "Create your Account",command=saving,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
    bd = canvas2.create_window(50,600,anchor="nw",window=dsu)
    signupwin.mainloop()




win = tk.Tk(className=" AID Bank")

win.geometry(str(win.winfo_screenwidth())+"x"+str(win.winfo_screenheight()))

bg = tk.PhotoImage(file = "1.png") 


 
canvas1 = tk.Canvas(win, width = win.winfo_screenwidth(),height = win.winfo_screenheight())
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")


si = tk.Button(win,text="Sign In",command=signin,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10)
su = tk.Button(win,text="Create new Account",command= signupwindow,width=20,height=2,relief='groove',bg="#3598e8",fg="#f6f794",font="CascadiaCode 20",activeforeground="#b6bd39",activebackground="#394fbd",padx=10,pady=10 )

b1 = canvas1.create_window( 100, 250, anchor = "nw",window = si)
b2 = canvas1.create_window( 100, 500, anchor = "nw",window = su)

win.mainloop()