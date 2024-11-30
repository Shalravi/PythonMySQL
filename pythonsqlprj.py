from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
def enroll():
    def insert():
        #To insert or update the fields in the database
        fname=e_fname.get()
        lname=e_lname.get()
        address=e_addr.get()
        email=e_email.get()
        tos=e_tos.get()
        age=e_age.get()
        phone=e_phone.get()
        courname=e_cname.get()
        tutname=e_tutname.get()
        fees=e_fee.get()
        regid=e_regid.get()
        nom=e_mon.get()
        # To check whether all the fields are given
        if(fname=="" or lname=="" or address=="" or email=="" or tos=="" or courname=="" or tutname=="" or fees=="" or regid=="" or nom=="" or age=="" or phone==""):
                       messagebox.showinfo("Insert Status", "All the Fields are required")
                       
        else:
             db=mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="#shalini30",
                 database="applica")
        mysql_cursor=db.cursor()
        # creating a table in database application
        mysql_cursor.execute("CREATE TABLE form9(fname VARCHAR(255), lname VARCHAR(255), address VARCHAR(255), email VARCHAR(255), tos VARCHAR(255), age INT, phone BIGINT, courname VARCHAR(255),tutname VARCHAR(255), fees BIGINT, regid BIGINT, nom INT)")
        #Inserting the fields into the table
        mysql_cursor.execute("insert into form1 values('"+ fname +"','"+ lname +"','"+ address +"','"+ email +"','"+ tos +"','"+ age +"','"+ phone +"','"+ courname +"','"+ tutname +"','"+ fees +"','"+ regid +"','"+ nom +"')")
        mysql_cursor.execute("commit")
        messagebox.showinfo("Insert Status","Inserted")
        db.close()
       # Creation of entrollment form using python tkinter module
    top=tkinter.Tk()
    top.geometry("800x400")
    top.title("Enrollment form")
    top.configure(bg="gray72")
    label_font=font.Font(weight="bold",font=("Times",20))
    label_font1=font.Font(weight="bold",font=("Times",10))
    label=Label(top,text="COURSE ENROLLMENT",font=label_font,bg="gray72")
    label.pack()
    labelframe1 = LabelFrame(top, text="STUDENT DETAILS",font=label_font,highlightthickness=2,bg="gray72")
    labelframe1.pack(fill="both",expand="yes")
    name=Label(labelframe1,text=" STUDENT NAME ",bg="gray72",font=label_font1).place(x=480,y=60)
    fname=Label(labelframe1,text=" FIRST NAME ",bg="gray72",font=label_font1).place(x=830,y=30)
    Lname=Label(labelframe1,text=" LAST NAME ",bg="gray72",font=label_font1).place(x=1120,y=30)
    e_fname=Entry(labelframe1,width=40)
    e_fname.place(x=750,y=60)
    e_lname=Entry(labelframe1,width=40)
    e_lname.place(x=1040,y=60)
    addr=Label(labelframe1,text=" ADDRESS ",bg="gray72",font=label_font1).place(x=480,y=100)
    e_addr=Entry(labelframe1)
    e_addr.place(x=750,y=100)
    email=Label(labelframe1,text=" EMAIL ID ",bg="gray72",font=label_font1).place(x=480,y=140)
    e_email=Entry(labelframe1,width=50)
    e_email.place(x=750,y=140)
    phone=Label(labelframe1,text=" PHONE NUMBER ",bg="gray72",font=label_font1).place(x=480,y=180)
    e_phone=Entry(labelframe1,width=50)
    e_phone.place(x=750,y=180)
    age=Label(labelframe1,text=" AGE ",bg="gray72",font=label_font1).place(x=480,y=220)
    e_age=Spinbox(labelframe1,from_=1,to=50)
    e_age.place(x=750,y=220)
    tos=Label(labelframe1,text=" TYPE OF STUDENT",bg="gray72",font=label_font1).place(x=480,y=260)
    e_tos=ttk.Combobox(labelframe1,values=["UNDER GRADUATE","GRADUATE"])
    e_tos.place(x=750,y=260)
    labelframe2 = LabelFrame(top, text="COURSE DETAILS",font=label_font,highlightthickness=2,bg="gray72")
    labelframe2.pack(fill="both",expand="yes")
    cname=Label(labelframe2,text=" COURSE ENROLLED ",bg="gray72",font=label_font1).place(x=480,y=60)
    e_cname=ttk.Combobox(labelframe2,values=["PYTHON","JAVA","AI","PHP","DATA SCIENCE","WEB DESIGN","C"])
    e_cname.place(x=750,y=60)
    regid=Label(labelframe2,text=" REGISTRATION ID ",bg="gray72",font=label_font1).place(x=480,y=100)
    e_regid=Entry(labelframe2,width=40)
    e_regid.place(x=750,y=100)
    tutname1=Label(labelframe2,text=" TUTOR NAME ",bg="gray72",font=label_font1).place(x=480,y=140)
    e_tutname=Entry(labelframe2,width=40)
    e_tutname.place(x=750,y=140)
    fee=Label(labelframe2,text=" FEES ",bg="gray72",font=label_font1).place(x=480,y=180)
    e_fee=Entry(labelframe2,width=40)
    e_fee.place(x=750,y=180)
    mon=Label(labelframe2,text=" NO OF MONTHS ",bg="gray72",font=label_font1).place(x=480,y=220)
    e_mon=Spinbox(labelframe2,from_=1,to=12)
    e_mon.place(x=750,y=220)
    btn = Button(labelframe2, text = 'submit',background="yellow", bd = '5',command=insert ).place(x=700,y=270)
    label1=Label(labelframe2,text="!!!!!! ONLY ONE RESPONSE WILL BE RECORDED!!!",bg="gray72")
    label1.place(x=600,y=320)
    top.mainloop()
# Login database 
def username():
     pas1= "Python#123"
     username=user_name.get()
     passw_ord=e_password.get()
     if(username=="" or passw_ord==""):
         messagebox.showinfo("Insert Status","All the Fields are required")
     else:
         if(passw_ord!=pas1):
             messagebox.showinfo("Insert Status","Password Incorrect")
         else:
                 db=mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="#shalini30",
                 database="applica")
mysql_cursor=db.cursor()
mysql_cursor.execute("insert into user_detail values('"+ username +"','"+ passw_ord +"')")
messagebox.showinfo("Insert Status","Signing In")
mysql_cursor.execute("commit")
enroll() # leading to the 2nd Enrollment form

# Login page
m=tkinter.Tk()
m.title("Login")
m.geometry("925x500")
m.configure(bg="#fff")
m.resizable(False,False)
img=PhotoImage(file="C:\Program Files (x86)Users\Dell\Downloads\login.PNG")
Label(m,image=img,bg='white').place(x=50,y=50)
frame=Frame(m,width=350,height=350,bg='white')
frame.place(x=480,y=70)
head=Label(frame,text="Sign In",fg='#57a1f8',bg='white',font=("Microsoft YaHei UI Light",23,'bold'))
head.place(x=100,y=5)
user_name=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user_name.place(x=30,y=80)
user_name.insert(0,'Username')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
e_password=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
e_password.place(x=30,y=150)
e_password.insert(0,'Password')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
butn=Button(frame,width=39,pady=7,text="Sign in",bg='#57a1f8',fg='white',border=0,command=username).place(x=35,y=204)
head1=Label(m,text="VELGROW",fg='#6B9E05',bg='white',font=("Microsoft YaHei UI Light",20,'bold'))
head1.place(x=80,y=250)
head2=Label(m,text="ACADEMY",fg='#9d00d4',bg='white',font=("Microsoft YaHei UI Light",20,'bold'))
head2.place(x=222,y=250)
m.mainloop()

















