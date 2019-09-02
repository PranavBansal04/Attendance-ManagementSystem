#DIGITAL ATTENDANCE MANAGEMENT SYSTEM     

from tkinter import*
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import csv
import time
import datetime
import os
from decimal import Decimal
###if you are changing the path of any file used below, remember to replace its path in the whole program
#specify a path where you want to store the student_data.csv file
if os.path.isfile('G:/student_data.csv')==True:
    pass
else:
    with open('G:/student_data.csv','w',newline='') as f:
        f.close()
#specify a path where you want to store the Physics_Attendance.csv file
if os.path.isfile('G:/Physics_Attendance.csv')==True:
    pass
else:
    with open('G:/Physics_Attendance.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerow(['']*365)
        f.close()
#specify a path where you want to store the Pentry_no.csv file
if os.path.isfile('G:/Pentry_no.csv')==True:
    pass
else:
    with open('G:/Pentry_no.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerow('1')
        f.close()
#specify a path where you want to store the Chemistry_Attendance.csv file
if os.path.isfile('G:/Chemistry_Attendance.csv')==True:
    pass
else:
    with open('G:/Chemistry_Attendance.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerow(['']*365)
        f.close()
#specify a path where you want to store the Centry_no.csv file
if os.path.isfile('G:/Centry_no.csv')==True:
    pass
else:
    with open('G:/Centry_no.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerow('1')
        f.close()
#specify a path where you want to store the Maths_Attendance.csv file
if os.path.isfile('G:/Maths_Attendance.csv')==True:
    pass
else:
    with open('G:/Maths_Attendance.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerow(['']*365)
        f.close()
#specify a path where you want to store the Mentry_no.csv file
if os.path.isfile('G:/Mentry_no.csv')==True:
    pass
else:
    with open('G:/Mentry_no.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerow('1')
        f.close()                
server=smtplib.SMTP('mail.smtp2go.com',2525)
#create your account with your mail id on smpt2go
#fill in your email and password in the below variables
myemail=""
mypass=""
server.login(myemail,mypass)
root=Tk()
root.title('STUDENT LOGIN')

#specify the path for background pic to be used
bgpic = PhotoImage(file="C:/Users/PRANAV BANSAL/Downloads/bg image.png")
bglabel = Label(root,image=bgpic)
bglabel.pack(fill=Y)

w1=Label(root,text='Enrollment No :',fg='red',bg='white',font=('Comic Sans MS',13,'bold')).place(relx=0.35,rely=0.36,anchor=CENTER)
e1=Entry(root,bg="white",fg="black",relief=SUNKEN)
e1.place(relx=0.48,rely=0.36,anchor=CENTER)
w2=Label(root,text='      Password :',fg='red',bg='white',font=('Comic Sans MS',13,'bold')).place(relx=0.35,rely=0.45,anchor=CENTER)
e2=Entry(root,bg='white',fg='black',show='*',relief=SUNKEN)
e2.place(relx=0.48,rely=0.45,anchor=CENTER)


def get_input():
    a=[]
    c=[]
    d=[]
    with open('G:/student_data.csv','r',newline='') as f:
        r=csv.reader(f)
        for i in r:
            a.append(i[0].strip())
            c.append(i[2].strip())
            d.append(i[4].strip())
        if e1.get()!='' and e2.get()!='':
            if e1.get() in c:
                m=c.index(e1.get())
                if e2.get()==d[m]:
                    e1.delete(0,END)
                    e2.delete(0,END)
                    profile=Tk()
                    profile.configure(background='white')
                    profile.title('Student Profile')
                    with open('G:/Mentry_no.csv','r',newline='') as f:
                        r=csv.reader(f)
                        y=list(r)
                        f.close()
                    k=int(y[0][0])
                    l=Label(profile,text='WELCOME'+'  '+a[m].upper()+' !',fg='blue',bg='white',font=('Comic Sans MS',8,'bold')).grid(row=0,column=2)
                    list_date=Listbox(profile,height=k)
                    list_P=Listbox(profile,width=20,height=k)
                    list_C=Listbox(profile,height=k)
                    list_M=Listbox(profile,height=k)
                    list_P.insert(1,'PHYSICS')
                    list_P.itemconfig(0,{'fg':'orange'})
                    list_C.insert(1,'CHEMISTRY')
                    list_C.itemconfig(0,{'fg':'orange'})
                    list_M.insert(1,'MATHS')
                    list_M.itemconfig(0,{'fg':'orange'})
                    
                    with open('G:/Physics_Attendance.csv','r',newline='') as f:
                        r1=csv.reader(f)
                        templist=list(r1)
                        f.close()   
                    for j1 in range(0,k):
                        list_date.insert(j1+1,templist[0][j1])
                        list_date.itemconfig(j1,{'fg':'blue'})
                    with open('G:/Physics_Attendance.csv','r',newline='') as f:
                        r2=csv.reader(f)
                        Q=list(r2)
                        f.close()
                    pa1=[]
                    for j2 in range(0,k-1):
                        list_P.insert(j2+1,Q[m+1][j2+1])
                        pa1.append(Q[m+1][j2+1])
                        if Q[m+1][j2+1]=='P':
                            list_P.itemconfig(j2+1,{'fg':'green'})
                        elif Q[m+1][j2+1]=='A':
                            list_P.itemconfig(j2+1,{'fg':'red'})
                    with open('G:/Chemistry_Attendance.csv','r',newline='') as f:
                        r3=csv.reader(f)
                        W=list(r3)
                        f.close()
                    pa2=[]    
                    for j3 in range(0,k-1):
                        list_C.insert(j3+1,W[m+1][j3+1])
                        pa2.append(W[m+1][j3+1])
                        if W[m+1][j3+1]=='P':
                            list_C.itemconfig(j3+1,{'fg':'green'})
                        elif W[m+1][j3+1]=='A':
                            list_C.itemconfig(j3+1,{'fg':'red'})
                    with open('G:/Maths_Attendance.csv','r',newline='') as f:
                        r4=csv.reader(f)
                        U=list(r4)
                        f.close()
                    pa3=[]    
                    for j4 in range(0,k-1):
                        list_M.insert(j4+1,U[m+1][j4+1])
                        pa3.append(U[m+1][j4+1])
                        if U[m+1][j4+1]=='P':
                            list_M.itemconfig(j4+1,{'fg':'green'})
                        elif U[m+1][j4+1]=='A':
                            list_M.itemconfig(j4+1,{'fg':'red'})

                    
                    list_date.grid(row=1,column=1)  
                    list_P.grid(row=1,column=2) 
                    list_C.grid(row=1,column=3)
                    list_M.grid(row=1,column=4)

                    p1=str(pa1.count('P'))
                    p2=str(pa2.count('P'))
                    p3=str(pa3.count('P'))
                    a1=str(pa1.count('A'))
                    a2=str(pa2.count('A'))
                    a3=str(pa3.count('A'))
                    
                    atdPt=Decimal((int(p1)/(int(p1)+int(a1)))*100)
                    atdCt=Decimal((int(p2)/(int(p2)+int(a2)))*100)
                    atdMt=Decimal((int(p3)/(int(p3)+int(a3)))*100)
                    atdP=str(round(atdPt,2))
                    atdC=str(round(atdCt,2))
                    atdM=str(round(atdMt,2))
                    
                    Label(profile,text='TRY NOT TO',fg='red',bg='white',width=18).grid(row=2,column=1)
                    Label(profile,text='MISS LECTURES.',fg='red',bg='white',width=18).grid(row=3,column=1)
                    Button(profile,bg='white',fg='navy blue',text='LOG OUT',font=('helventica',8,'bold'),width=18,command=profile.destroy).grid(row=4,column=1)
                    Label(profile,text='Total P='+p1,bg='white',width=18,fg='magenta').grid(row=2,column=2)
                    Label(profile,text='Total A='+a1,bg='white',width=18,fg='purple').grid(row=3,column=2)
                    Label(profile,text='Total P='+p2,bg='white',width=18,fg='magenta').grid(row=2,column=3)
                    Label(profile,text='Total A='+a2,bg='white',width=18,fg='purple').grid(row=3,column=3)
                    Label(profile,text='Total P='+p3,bg='white',width=18,fg='magenta').grid(row=2,column=4)
                    Label(profile,text='Total A='+a3,bg='white',width=18,fg='purple').grid(row=3,column=4)
                    Label(profile,text='Attendance='+atdP+'%',bg='black',width=18,fg='white').grid(row=4,column=2)
                    Label(profile,text='Attendance='+atdC+'%',bg='black',width=18,fg='white').grid(row=4,column=3)
                    Label(profile,text='Attendance='+atdM+'%',bg='black',width=18,fg='white').grid(row=4,column=4)
                       
                    profile.mainloop()
                elif e1.get()in c and e2.get()not in d:
                    e2.delete(0,END)
                    wrong=Tk()
                    wrong.configure(background='white')
                    l=Label(wrong,text='WRONG PASSWORD ENTERED!!!\nENTER PASSWORD AGAIN.',fg='red',bg='white',font='times,5').pack()
                    k=Button(wrong,text='Okay',fg='blue',bg='white',command=wrong.destroy).pack()
                    wrong.mainloop()
                elif e1.get()in c and e2.get() in d:
                    e1.delete(0,END)
                    e2.delete(0,END)
                    r=Tk()
                    r.configure(background='white')
                    Label(r,text='INVALID ENROL NO. OR PASSWORD !',fg='red',bg='white').pack()
                    Button(r,text='Okay',bg='white',command=r.destroy).pack()
                    r.mainloop()
            else:
                e1.delete(0,END)
                e2.delete(0,END)
                r=Tk()
                r.configure(background='white')
                Label(r,text='INVALID ENROL NO. OR PASSWORD !',fg='red',bg='white').pack()
                Button(r,text='Okay',bg='white',command=r.destroy).pack()
                r.mainloop()
        else:
            r=Tk()
            r.configure(background='white')
            Label(r,text='ENTER DATA!',fg='red',bg='white').pack(fill=X)
            Button(r,text='Okay',fg='blue',bg='white',command=r.destroy).pack(fill=X)
            r.mainloop()
            
             
b1=Button(root,text='LOGIN',font=('MS Sans serif',11,'bold'),fg='navy blue',bg='white',command=get_input,relief=RAISED).place(relx=0.43,rely=0.53,anchor=CENTER)
def quitroot():
    qroot=Tk()
    qroot.configure(background='white')
    Label(qroot,text='Are You Sure You Want To Exit ?',fg='red',bg='white',font=('Times',12,'bold')).pack(side=TOP)
    Button(qroot,text='NO',fg='blue',bg='white',command=qroot.destroy).pack(side=BOTTOM)
    def destroyall():
        qroot.destroy()
        root.destroy()
    Button(qroot,text='YES',fg='blue',bg='white',command=destroyall).pack(side=BOTTOM)
    qroot.mainloop()
    
b2=Button(root,text='Exit',font=('verdana',11,'bold'),fg='red',bg='white',command=quitroot).place(relx=0.53,rely=0.7,anchor=CENTER)
def new_entry():
    new=Tk()
    new.configure(background='white')
    new.title('NEW ENTRY')
    l1=Label(new,text=' NAME :',fg='blue',bg='white',font=('Comic Sans MS',10)).place(relx=0.3,rely=0.2,anchor=CENTER)
    n1=Entry(new)
    n1.place(relx=0.6,rely=0.2,anchor=CENTER)
    l2=Label(new,text='ENROLMENT NO :',fg='blue',bg='white',font=('Comic Sans MS',10)).place(relx=0.25,rely=0.37,anchor=CENTER)
    n2=Entry(new)
    n2.place(relx=0.6,rely=0.37,anchor=CENTER)
    l3=Label(new,text='        PASSWORD :',fg='blue',bg='white',font=('Comic Sans MS',10)).place(relx=0.25,rely=0.55,anchor=CENTER)
    n3=Entry(new,show='*')
    n3.place(relx=0.6,rely=0.55,anchor=CENTER)
    l4=Label(new,text='CONFIRM PASSWORD :',fg='blue',bg='white',font=('Comic Sans MS',10)).place(relx=0.220,rely=0.7,anchor=CENTER)
    n4=Entry(new,show='*')
    n4.place(relx=0.6,rely=0.7,anchor=CENTER)
    new.geometry('400x400')
    def n_save():
        server=smtplib.SMTP('mail.smtp2go.com',2525)
        server.login('pranavbansal04@gmail.com','Lt1xseaRlpLy')
        import csv
        with open('G:/student_data.csv','r',newline='') as f:
            r=csv.reader(f)
            list1=[]
            for i in r:
                list1.append(i)
            if n1.get()=='' or n2.get()=='' or n3.get()=='' or n4.get()=='':
                v=Tk()
                v.configure(background='white')
                n=Label(v,text='ENTER DATA!',fg='red',bg='white',font='times,4').pack()
                d=Button(v,text='OKAY',fg='blue',bg='white',command=v.destroy).pack()
                v.mainloop()
            elif any((n1.get()) in s for s in list1):
                def re_data():
                    q.destroy()
                    n1.delete(0,END)
                    n2.delete(0,END)
                    n3.delete(0,END)
                    n4.delete(0,END)
                q=Tk()
                q.configure(background='white')
                l=Label(q,text='Data Already Exists!',fg='red',font='times,6').pack()
                but=Button(q,text='Okay',fg='blue',bg='white',command=re_data).pack()
                q.mainloop()
            else:
                server=smtplib.SMTP('mail.smtp2go.com',2525)
                if (n3.get())==(n4.get()):
                    server.login('pranavbansal04@gmail.com','Lt1xseaRlpLy')
                    m=random.randint(100000,999999)
                    y=str(m)
                    msg = MIMEMultipart()
                    msg['Subject'] = "OTP FOR BENNETT ATTENDANCE MANAGEMENT SYSTEM"
                    body = 'Your OTP for Bennett Attendance Management System is:\n'+y+'\nDo not share this OTP with anyone.\nThankYou!\nDeveloper:Pranav Bansal\n\tRishabh Yadav'
                    msg.attach(MIMEText(body, 'plain'))
                    text = msg.as_string()
                    h=Tk()
                    h.configure(background='white')
                    l=Label(h,text='Enter Your Email ID',bg='white').pack()
                    e=Entry(h)
                    e.pack()
                    
                    
                    def send():
                        global o
                        o=str(e.get())
                        with open('G:/student_data.csv','r',newline='') as f:
                            r=csv.reader(f)
                            elist=list(r)
                            f.close()
                        if e.get()=='':
                            l=Tk()
                            l.configure(background='white')
                            Label(l,text='ENTER YOUR EMAIL ID',fg='red',bg='white').pack()
                            Button(l,text='OKAY',bg='white',command=l.destroy).pack()
                            l.mainloop()
                            
                        elif any(o in s for s in elist):
                            e.delete(0,END)
                            temp=Tk()
                            temp.cnfigure(background='white')
                            Label(temp,text='''SORRY! THIS EMAIL ID ALREADY EXISTS!\nENTER A NEW EMAIL ID.''',fg='red',bg='white',font='times,3').pack()
                            Button(temp,text='OKAY',fg='dark green',bg='white',command=temp.destroy).pack()
                            temp.mainloop()
                        else:
                            try:
                                server.sendmail('pranavbansal04@gmail.com',[o],text)
                                h.destroy()
                                t=Tk()
                                t.configure(background='white')
                                l=Label(t,text='Enter passcode :',bg='white').pack()
                                z=Entry(t)
                                z.pack()
                                def codematch():
                                    if y==z.get():
                                        t.destroy()
                                        try:
                                            with open('G:/student_data.csv','a',newline='') as f:
                                                w=csv.writer(f)
                                                w.writerow([(n1.get()),'',n2.get(),'',n3.get(),o])
                                                n1.delete(0,END)
                                                n2.delete(0,END)
                                                n3.delete(0,END)
                                                n4.delete(0,END)
                                                new.destroy()
                                                q=Tk()
                                                q.configure(background='white')
                                                L=Label(q,text='Entry Saved',fg='green',bg='white',font='helventica,5').pack()
                                                B=Button(q,text='Okay',fg='blue',bg='white',font='times,3',command=q.destroy).pack()
                                                q.mainloop()
                                                f.close()
                                        except Exception:
                                            with open('G:/student_data.csv','w',newline='') as f:
                                                w=csv.writer(f)
                                                w.writerow([(n1.get()),'',n2.get(),'',n3.get()])
                                                n1.delete(0,END)
                                                n2.delete(0,END)
                                                n3.delete(0,END)
                                                n4.delete(0,END)
                                                q=Tk()
                                                q.configure(background='white')
                                                L=Label(q,text='Entry Saved',fg='green',bg='white',font='helventica,5').pack()
                                                B=Button(q,text='Okay',fg='blue',bg='white',font='times,3',command=q.destroy).pack()
                                                q.mainloop()
                                                f.close()
                                    else:
                                        u=Tk()
                                        u.configure(background='white')
                                        l=Label(u,text='WRONG PASSCODE',fg='red',bg='white').pack()
                                        b3=Button(u,text='Okay',fg='blue',bg='white',command=u.destroy).pack()
                                        u.mainloop()
                                       
                                b2=Button(t,text='Proceed',command=codematch).pack()
                                t.mainloop()
                            except Exception:
                                e.delete(0,END)
                                f=Tk()
                                f.configure(background='white')
                                p=Label(f,text='ENTER EMAIL AGAIN !',fg='red',bg='white',font='times,4').pack()
                                c=Button(f,text='Okay',fg='blue',bg='white',command=f.destroy).pack()
                                f.mainloop()
                                       
                                    
                    b=Button(h,text='DONE',fg='blue',bg='white',command=send).pack() 
                    h.mainloop()
                    
                else:
                    n3.delete(0,END)
                    n4.delete(0,END)
                    t=Tk()
                    t.configure(background='white')
                    l=Label(t,text='Enter Password Again!',fg='red',bg='white',font='times,4').pack()
                    b=Button(t,text='Okay',fg='blue',bg='white',command=t.destroy).pack()
                    t.mainloop()
                                 
    b1=Button(new,text='SAVE',command=n_save,fg='red',bg='white',font=('Helventica',8)).place(relx=0.5,rely=0.85,anchor=CENTER)        
    new.mainloop()

p=[]
with open('G:/student_data.csv','r',newline='') as f:
    r1=csv.reader(f)
    for i in r1:
        p.append(i[2])
    f.close()    
q=[]        
with open('G:/Physics_Attendance.csv','r',newline='') as g:
    r2=csv.reader(g)
    for j in r2:
        q.append(j[0])
    g.close()    
del(q[0])     
pq=[]    
if len(p)==len(q):
    pass
else:
    for h in range(len(q),len(p)):
        pq.append(p[h])    
    with open('G:/Pentry_no.csv','r') as f:
        r=csv.reader(f)
        t1=list(r)
        t11=int(t1[0][0])-1
        f.close()
    for i in pq:
        with open('G:/Physics_Attendance.csv','a',newline='') as g:
            w1=csv.writer(g)
            w1.writerow([i]+['N']*t11+['']*330)
            g.close()         

            
p=[]
with open('G:/student_data.csv','r',newline='') as f:
    r1=csv.reader(f)
    for i in r1:
        p.append(i[2])
    f.close()   
q=[]        
with open('G:/Chemistry_Attendance.csv','r',newline='') as g:
    r2=csv.reader(g)
    for j in r2:
        q.append(j[0])
    g.close()
del(q[0])     
pq=[]    
if len(p)==len(q):
    pass
else:
    for h in range(len(q),len(p)):
        pq.append(p[h])
    with open('G:/Centry_no.csv','r') as f:
        r=csv.reader(f)
        t2=list(r)
        t22=int(t2[0][0])-1
        f.close()
    for i in pq:
        with open('G:/Chemistry_Attendance.csv','a',newline='') as g:
            w1=csv.writer(g)
            w1.writerow([i]+['N']*t22+['']*340)
            g.close()      


p=[]
with open('G:/student_data.csv','r',newline='') as f:
    r1=csv.reader(f)
    for i in r1:
        p.append(i[2])
    f.close()   
q=[]        
with open('G:/Maths_Attendance.csv','r',newline='') as g:
    r2=csv.reader(g)
    for j in r2:
        q.append(j[0])
    g.close()
del(q[0])     
pq=[]    
if len(p)==len(q):
    pass
else:
    for h in range(len(q),len(p)):
        pq.append(p[h])
    with open('G:/Pentry_no.csv','r') as f:
        r=csv.reader(f)
        t3=list(r)
        t33=int(t3[0][0])-1
        f.close()
    for i in pq:
        with open('G:/Maths_Attendance.csv','a',newline='') as g:
            w1=csv.writer(g)
            w1.writerow([i]+['N']*t33+['']*340)
            g.close()            
def am():
    def td():
        if k.get()=='L6QNL38WGT':
            ad.destroy()
            a=Tk()
            a.configure(background='white')
            a.title('ADMIN')
            Label(a,text='CHOOSE LECTURE :',fg='purple',bg='white',font=('Times New Roman',25)).pack(fill=X)
            
            def phy_atd():
                check=datetime.date.today().strftime("%d|%m|%y")
                with open('G:/Physics_Attendance.csv','r',newline='') as f:
                    r=csv.reader(f)
                    checkdata=list(r)
                    f.close()
                if any(check in s for s in checkdata):
                    temp=Tk()
                    temp.configure(background='white')
                    Label(temp,text='''TODAY'S ATTENDANCE ALREADY FILLED!''',fg='red',bg='white',font='times,4').pack()
                    Button(temp,text='OKAY',fg='blue',bg='white',command=temp.destroy).pack()
                else:
                    with open('G:/student_data.csv','r',newline='') as f:
                        r=csv.reader(f)
                        a=[]
                        for i in r:
                            a.append(i[0].strip())
                        phy=Tk()
                        phy.title('PHYSICS')
                        phy.configure(background='white')
                        lb1=Listbox(phy,width=2,font='times,1',height=len(a))
                        lb1.pack(side=LEFT)
                        lb2=Listbox(phy,fg='blue',selectmode=EXTENDED,width=16,font='times,1',height=len(a))
                        lb2.pack(side=LEFT)
                        i=0
                        for name in a:
                            i+=1
                            lb1.insert(i,str(i)+'.')
                            lb2.insert(i,name)
                        Label(phy,text='P/A',bg='white',font='times,0.1').pack(side=TOP)
                        entries=[]
                        for i in range(len(a)):
                            e=Entry(phy,width=3)
                            e.pack(side=TOP)
                            entries.append(e)    
                        def update_data():
                            sa=[]    
                            for k in entries:
                                sa.append(k.get())
                            def echeck():
                                for n in sa:
                                    if n=='P' or n=='A':
                                        ec=0
                                        continue
                                    else:
                                        ec=1
                                        break
                                return(ec)    
                            if '' in sa:
                                    temp=Tk()
                                    temp.configure(background='white')
                                    Label(temp,text='Please fill all the entries !',fg='red',bg='white',font='times,4').pack()
                                    Button(temp,text='Okay',bg='white',command=temp.destroy).pack()
                                    temp.mainloop()
                            elif echeck()==1:
                                    wrong_entry=Tk()
                                    wrong_entry.configure(background='white')
                                    Label(wrong_entry,text='Fill either P or A',fg='blue',bg='white').pack()
                                    Button(wrong_entry,text='Okay',fg='red',bg='white',command=wrong_entry.destroy).pack()
                                    wrong_entry.mainloop()        
                            else:
                                psure=Tk()
                                psure.configure(background='white')
                                Label(psure,text='ARE YOU SURE ?\nDID YOU CHECK ALL THE ENTRIES ?',fg='red',bg='white').pack()
                                Button(psure,text='NO',fg='blue',bg='white',command=psure.destroy).pack()

                                def p_sure():
                                    psure.destroy()   
                                    with open('G:/Pentry_no.csv','r',newline='') as o:
                                        read=csv.reader(o)
                                        h=list(read)
                                        entryno=int(h[0][0])
                                        o.close()
                                    with open('G:/Pentry_no.csv','w',newline='') as o:
                                        w=csv.writer(o)
                                        w.writerow([str(entryno+1)])
                                    
                                    date=datetime.date.today().strftime("%d|%m|%y")
                                    with open('G:/Physics_Attendance.csv','r',newline='') as f:
                                        r=csv.reader(f)
                                        wholedata=list(r)
                                        f.close()
                                        wholedata[0][entryno]=date
                                        
                                        i=0
                                        for k in entries:
                                            i+=1
                                            wholedata[i][entryno]=k.get()
                                        with open('G:/Physics_Attendance.csv','w',newline='') as z:
                                            w=csv.writer(z)
                                            w.writerows(wholedata)
                                            z.close()
                                        phy.destroy()
                                Button(psure,text='YES',fg='blue',bg='white',command=p_sure).pack()
                                psure.mainloop()               
                                
                        Button(phy,text='UPDATE DATA',fg='red',bg='white',command=update_data).pack()
                        phy.mainloop()
                        
                        
            b1=Button(a,text='PHYSICS',fg='orange',bg='white',font=('Verdana',16,'bold'),height=5,width=8,command=phy_atd)
            b1.pack(fill=X)

            
            def chem_atd():
                check=datetime.date.today().strftime("%d|%m|%y")
                with open('G:/Chemistry_Attendance.csv','r',newline='') as f:
                    r=csv.reader(f)
                    checkdata=list(r)
                    f.close()
                if any(check in s for s in checkdata):
                    temp=Tk()
                    temp.configure(background='white')
                    Label(temp,text='''TODAY'S ATTENDANCE ALREADY FILLED!''',fg='red',bg='white',font='times,4').pack()
                    Button(temp,text='OKAY',fg='blue',bg='white',command=temp.destroy).pack()
                else:
                    with open('G:/student_data.csv','r',newline='') as f:
                        r=csv.reader(f)
                        a=[]
                        for i in r:
                            a.append(i[0].strip())
                        chm=Tk()
                        chm.title('CHEMISTRY')
                        chm.configure(background='white')
                        lb1=Listbox(chm,width=2,font='times,1',height=len(a))
                        lb1.pack(side=LEFT)
                        lb2=Listbox(chm,fg='blue',selectmode=EXTENDED,width=16,font='times,1',height=len(a))
                        lb2.pack(side=LEFT)
                        i=0
                        for name in a:
                            i+=1
                            lb1.insert(i,str(i)+'.')
                            lb2.insert(i,name)
                        Label(chm,text='P/A',bg='white',font='times,0.1').pack(side=TOP)
                        entries=[]
                        for i in range(len(a)):
                            e=Entry(chm,width=3)
                            e.pack(side=TOP)
                            entries.append(e)    
                        def update_data():
                            sa=[] 
                            for k in entries:
                                    sa.append(k.get())        
                            def echeck():
                                for n in sa:
                                    if n=='P' or n=='A':
                                        ec=0
                                        continue
                                    else:
                                        ec=1
                                        break
                                return(ec)
                            if '' in sa:
                                temp=Tk()
                                temp.configure(background='white')
                                Label(temp,text='Please fill all the entries !',fg='red',bg='white',font='times,4').pack()
                                Button(temp,text='Okay',bg='white',command=temp.destroy).pack()
                                temp.mainloop()
                            elif echeck()==1:
                                    wrong_entry=Tk()
                                    wrong_entry.configure(background='white')
                                    Label(wrong_entry,text='Fill either P or A',fg='blue',bg='white').pack()
                                    Button(wrong_entry,text='Okay',fg='red',bg='white',command=wrong_entry.destroy).pack()
                                    wrong_entry.mainloop()
                                    
                            else:
                                csure=Tk()
                                csure.configure(background='white')
                                Label(csure,text='ARE YOU SURE ?\nDID YOU CHECK ALL THE ENTRIES ?',fg='red',bg='white').pack()
                                Button(csure,text='NO',fg='blue',bg='white',command=csure.destroy).pack()

                                def c_sure():
                                    csure.destroy()
                                    with open('G:/Centry_no.csv','r',newline='') as o:
                                        read=csv.reader(o)
                                        h=list(read)
                                        entryno=int(h[0][0])
                                        o.close()
                                    with open('G:/Centry_no.csv','w',newline='') as o:
                                        w=csv.writer(o)
                                        w.writerow([str(entryno+1)])
                                    
                                    date=datetime.date.today().strftime("%d|%m|%y")
                                    with open('G:/Chemistry_Attendance.csv','r',newline='') as f:
                                        r=csv.reader(f)
                                        wholedata=list(r)
                                        f.close()
                                        wholedata[0][entryno]=date
                                       
                                        i=0
                                        for k in entries:
                                            i+=1
                                            wholedata[i][entryno]=k.get()
                                        with open('G:/Chemistry_Attendance.csv','w',newline='') as z:
                                            w=csv.writer(z)
                                            w.writerows(wholedata)
                                            z.close()
                                        chm.destroy()
                                Button(csure,text='YES',fg='blue',bg='white',command=c_sure).pack()
                                csure.mainloop()                
                            
                        Button(chm,text='UPDATE DATA',fg='red',bg='white',command=update_data).pack()
                        chm.mainloop()
            b2=Button(a,text='CHEMISRY',fg='orange',bg='white',font=('Verdana',16,'bold'),height=5,width=8,command=chem_atd)
            b2.pack(fill=X)


            def mat_atd():
                check=datetime.date.today().strftime("%d|%m|%y")
                with open('G:/Maths_Attendance.csv','r',newline='') as f:
                    r=csv.reader(f)
                    checkdata=list(r)
                    f.close()
                if any(check in s for s in checkdata):
                    temp=Tk()
                    temp.configure(background='white')
                    Label(temp,text='''TODAY'S ATTENDANCE ALREADY FILLED!''',fg='red',bg='white',font='times,4').pack()
                    Button(temp,text='OKAY',fg='blue',bg='white',command=temp.destroy).pack()
                else:
                    with open('G:/student_data.csv','r',newline='') as f:
                        r=csv.reader(f)
                        a=[]
                        for i in r:
                            a.append(i[0].strip())
                        mat=Tk()
                        mat.title('MATHS')
                        mat.configure(background='white')
                        lb1=Listbox(mat,width=2,font='times,1',height=len(a))
                        lb1.pack(side=LEFT)
                        lb2=Listbox(mat,fg='blue',selectmode=EXTENDED,width=16,font='times,1',height=len(a))
                        lb2.pack(side=LEFT)
                        i=0
                        for name in a:
                            i+=1
                            lb1.insert(i,str(i)+'.')
                            lb2.insert(i,name)
                        Label(mat,text='P/A',bg='white',font='times,0.1').pack(side=TOP)
                        entries=[]
                        for i in range(len(a)):
                            e=Entry(mat,width=3)
                            e.pack(side=TOP)
                            entries.append(e)    
                        def update_data():
                            sa=[]    
                            for k in entries:
                                sa.append(k.get())
                            def echeck():
                                for n in sa:
                                    if n=='P' or n=='A':
                                        ec=0
                                        continue
                                    else:
                                        ec=1
                                        break
                                return(ec)        
                            if '' in sa:
                                temp=Tk()
                                temp.configure(background='white')
                                Label(temp,text='Please fill all the entries !',fg='red',bg='white',font='times,4').pack()
                                Button(temp,text='Okay',bg='white',command=temp.destroy).pack()
                                temp.mainloop()
                            elif echeck()==1:
                                    wrong_entry=Tk()
                                    wrong_entry.configure(background='white')
                                    Label(wrong_entry,text='Fill either P or A',fg='blue',bg='white').pack()
                                    Button(wrong_entry,text='Okay',fg='red',bg='white',command=wrong_entry.destroy).pack()
                                    wrong_entry.mainloop()    
                            else:
                                msure=Tk()
                                msure.configure(background='white')
                                Label(msure,text='ARE YOU SURE ?\nDID YOU CHECK ALL THE ENTRIES ?',fg='red',bg='white').pack()
                                Button(msure,text='NO',fg='blue',bg='white',command=msure.destroy).pack()

                                def m_sure():
                                    msure.destroy()   
                                    with open('G:/Mentry_no.csv','r',newline='') as o:
                                        read=csv.reader(o)
                                        h=list(read)
                                        entryno=int(h[0][0])
                                        o.close()
                                    with open('G:/Mentry_no.csv','w',newline='') as o:
                                        w=csv.writer(o)
                                        w.writerow([str(entryno+1)])
                                    
                                    date=datetime.date.today().strftime("%d|%m|%y")
                                    with open('G:/Maths_Attendance.csv','r',newline='') as f:
                                        r=csv.reader(f)
                                        wholedata=list(r)
                                        f.close()
                                        wholedata[0][entryno]=date
                                        
                                        i=0
                                        for k in entries:
                                            i+=1
                                            wholedata[i][entryno]=k.get()
                                        with open('G:/Maths_Attendance.csv','w',newline='') as z:
                                            w=csv.writer(z)
                                            w.writerows(wholedata)
                                            z.close()
                                        mat.destroy()
                                Button(msure,text='YES',fg='blue',bg='white',command=m_sure).pack()
                                msure.mainloop()
                                
                        Button(mat,text='UPDATE DATA',fg='red',bg='white',command=update_data).pack()
                        mat.mainloop()
            b3=Button(a,text='MATHS',fg='orange',bg='white',font=('Verdana',16,'bold'),height=5,width=8,command=mat_atd)
            b3.pack(fill=X)

            def see_atd():
                see=Tk()
                see.configure(background='white')
                see.title('ATTENDANCE DATA')
                Label(see,text='PHY',fg='blue',bg='white',font=('Comic',12,'bold')).grid(row=0,column=1)
                Label(see,text='CHEM',fg='blue',bg='white',font=('Comic',12,'bold')).grid(row=2,column=1)
                Label(see,text='MATHS',fg='blue',bg='white',font=('Comic',12,'bold')).grid(row=4,column=1)
                names1=Listbox(see)
                names1.insert(1,'NAMES')
                names1.itemconfig(0,{'fg':'red'})
                enrol1=Listbox(see,width=10)
                enrol1.insert(1,'ENROL NO.')
                enrol1.itemconfig(0,{'fg':'Purple'})
                attendance1=Listbox(see,width=187)
                
                names2=Listbox(see)
                names2.insert(1,'NAMES')
                names2.itemconfig(0,{'fg':'red'})
                enrol2=Listbox(see,width=10)
                enrol2.insert(1,'ENROL NO.')
                enrol2.itemconfig(0,{'fg':'Purple'})
                attendance2=Listbox(see,width=187)
                
                names3=Listbox(see)
                names3.insert(1,'NAMES')
                names3.itemconfig(0,{'fg':'red'})
                enrol3=Listbox(see,width=10)
                enrol3.insert(1,'ENROL NO.')
                enrol3.itemconfig(0,{'fg':'Purple'})
                attendance3=Listbox(see,width=187)
                
                with open('G:/student_data.csv','r',newline='') as f:
                    r11=csv.reader(f)
                    datalist=list(r11)
                    f.close()
                initial=0   
                for i in datalist:
                    initial+=1
                    names1.insert(initial+1,i[0])
                    enrol1.insert(initial+1,i[2])
                    names2.insert(initial+1,i[0])
                    enrol2.insert(initial+1,i[2])
                    names3.insert(initial+1,i[0])
                    enrol3.insert(initial+1,i[2])
                    names1.itemconfig(initial,{'fg':'navy blue'})
                    names2.itemconfig(initial,{'fg':'navy blue'})
                    names3.itemconfig(initial,{'fg':'navy blue'})
                    enrol1.itemconfig(initial,{'fg':'Orange'})
                    enrol2.itemconfig(initial,{'fg':'Orange'})
                    enrol3.itemconfig(initial,{'fg':'Orange'})
                with open('G:/Physics_Attendance.csv','r',newline='') as f:
                    r12=csv.reader(f)
                    phylist=list(r12)
                    f.close()
                dates=phylist[0]
                del(dates[0])
                dp=[]
                dp.append(dates[0])
                itemp=0
                while dates[itemp]!='':
                    itemp+=1
                    dp.append(dates[itemp])
                del(dp[-1])       
                attendance1.insert(1,dp)
                attendance2.insert(1,dp)
                attendance3.insert(1,dp)

                for i in range(1,initial+1):
                    templist1=phylist[i]
                    del(templist1[0])
                    ix=0
                    pab1=[]
                    pab1.append('_____'+templist1[0])
                    while templist1[ix]!='':
                        ix+=1
                        pab1.append('______'+templist1[ix]+'_')
                    del(pab1[-1])
                    attendance1.insert(i+1,pab1)
                    attendance1.itemconfig(i,{'fg':'Blue'})
                with open('G:/Chemistry_Attendance.csv','r',newline='') as f:
                    r13=csv.reader(f)
                    chemlist=list(r13)
                    f.close()
                for i in range(1,initial+1):
                    templist2=chemlist[i]
                    del(templist2[0])
                    iy=0
                    pab2=[]
                    pab2.append('_____'+templist2[0])
                    while templist2[iy]!='':
                        iy+=1
                        pab2.append('______'+templist2[iy]+'_')
                    del(pab2[-1])
                    attendance2.insert(i+1,pab2)
                    attendance2.itemconfig(i,{'fg':'Blue'})
    
                with open('G:/Maths_Attendance.csv','r',newline='') as f:
                    r14=csv.reader(f)
                    matlist=list(r14)
                    f.close()
                for i in range(1,initial+1):
                    templist3=matlist[i]
                    del(templist3[0])
                    iz=0
                    pab3=[]
                    pab3.append('_____'+templist3[0])
                    while templist3[iz]!='':
                        iz+=1
                        pab3.append('______'+templist3[iz]+'_')
                    del(pab3[-1])
                    attendance3.insert(i+1,pab3)
                    attendance3.itemconfig(i,{'fg':'Blue'})
     
                names1.grid(row=1,column=0)
                enrol1.grid(row=1,column=1)
                attendance1.grid(row=1,column=2)
                names2.grid(row=3,column=0)
                enrol2.grid(row=3,column=1)
                attendance2.grid(row=3,column=2)
                names3.grid(row=5,column=0)
                enrol3.grid(row=5,column=1)
                attendance3.grid(row=5,column=2)
                def logout():
                    see.destroy()
                    a.destroy()
                Button(see,text='LOG OUT',fg='blue',bg='white',font=('Helventica',10,'bold'),command=logout).grid(row=6,column=1)
                Button(see,text='CLOSE',fg='red',bg='white',font=('Helventica',10,'bold'),command=see.destroy).grid(row=6,column=0)
                Label(see,text='N = NOT AVAILABLE',fg='red').grid(row=6,column=2)
                see.mainloop()
                    
            b4=Button(a,text='SEE ATTENDANCE',fg='blue',bg='white',font=('times',16,'bold'),height=5,width=8,command=see_atd)
            b4.pack(fill=X)
            a.mainloop()
        else:
            k.delete(0,END)
            d=Tk()
            d.configure(background='white')
            Label(d,text='Wrong Password!',fg='red',bg='white',font=('Times',12,'bold')).pack(fill=X)
            Button(d,text='Okay',bg='white',command=d.destroy).pack(fill=X)
             
    ad=Tk()
    ad.configure(background='white')
    Label(ad,text='ENTER PASSWORD :',fg='purple',bg='white',font=('Comic Sans MS',13,'bold italic')).pack()
    k=Entry(ad,show='*',fg='magenta')
    k.pack()
    Button(ad,text='LOGIN',fg='blue',bg='white',command=td).pack()
    ad.mainloop()
    
b3=Button(root,text='SIGN UP',font=('helventica',10,'bold'),fg='red',bg='white',command=new_entry).place(relx=0.36,rely=0.7,anchor=CENTER)
Button(root,text='Admin Login',fg='cyan',bg='blue',command=am).place(relx=0.89,rely=0.36,anchor=CENTER)
Label(root,bg='white',height=7).pack(side=BOTTOM,fill=X)
root.mainloop()
