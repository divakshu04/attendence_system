from tkinter import *
from datetime import date
from tkinter import ttk
from datetime import datetime
from datetime import timedelta
from PIL import Image,ImageTk
import mysql.connector
#-----------------------------------LOGIN PAGE---------------------------------------------------
root=Tk()
root.title("Login")
root.geometry("925x500")
root.config(bg="#fff")
root.resizable(False,False)
def add_image_to_frame(image_label,imagePath,w,h):
    img=Image.open(imagePath)
    img_update=img.resize((w,h))
    img_tk=ImageTk.PhotoImage(img_update)
    image_label.config(image=img_tk,width=w,height=h)
    image_label.image = img_tk 
frame=Frame(root,width=350,height=400,bg="white")
frame.place(x=550,y=50)
name_frame=Frame(root,width=350,height=50,bg="white")
name_frame.place(x=210,y=20)
imagelabel=Label(root,image='',bg="white",width=470,height=380)
imagelabel.place(x=50,y=90)
add_image_to_frame(imagelabel,"A:\\Python\\Projects\\Automated Attendence System\\Login-amico.png",470,380)
app_name=Label(name_frame,text="Attendence Tracker",fg="#00243D",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
app_name.place(x=20,y=3)
sign_in_heading=Label(frame,text="Sign in",fg="#005694",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
sign_in_heading.place(x=100,y=8)
def root_destroy():
    if root.winfo_exists():
        root.destroy()
#----------------------------DATABASE-------------------------------------------------------------------------
def account_database():
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds')
        cursor=mydb.cursor()
        cursor.execute(f"create database if not exists Attendence_System")
        mydb.commit()
        cursor.close()
        mydb.close()
    except mysql.connector.Error as e:
        print(f"Error:{e}")
#-------------------------------SIGNUP ACCOUNT-------------------------------------------------------------------
def sign_up_page():
    signup=Toplevel(root)
    signup.title('Sign Up')
    signup.geometry('525x500')
    signup.config(bg="#fff")
    signup.resizable(False,False)
    signup_frame=Frame(signup,width=450,height=400,bg="white")
    signup_frame.place(x=40,y=50)
    sign_up_heading=Label(signup_frame,text="Sign up",fg="#1FB8D0",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    sign_up_heading.place(x=150,y=0)
    #---------------------------------------------------
    slabel=Label(signup,image='',bg='white',width=27,height=12)
    slabel.place(x=270,y=90)
    add_image_to_frame(slabel,imagepath_signup,250,250)
    #-------username----------------
    def on_enter(e):
        signup_user.delete(0,'end')
    def on_leave(e):
        signup_name=signup_user.get()
        if signup_name =='':
            signup_user.insert(0,'Username')
    enter_user=Label(signup_frame,text='Enter the username:',fg='black',bg='white',border=0,font=("Microsoft YaHei UI Light",11,'bold'))
    enter_user.place(x=30,y=80)
    signup_user=Entry(signup_frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
    signup_user.place(x=30,y=110)
    signup_user.insert(0,'Username')
    Frame(signup_frame,width=185,height=2,bg='black').place(x=25,y=137)
    signup_user.bind('<FocusIn>',on_enter)
    signup_user.bind('<FocusOut>',on_leave)
    #-------password----------------------
    def on_enter(e):
        signup_pssw.delete(0,'end')
    def on_leave(e):
        signup_name=signup_pssw.get()
        if signup_name=='':
            signup_pssw.insert(0,'Password')
    enter_pssw=Label(signup_frame,text='Enter your password:',fg='black',bg='white',border=0,font=("Microsoft YaHei UI Light",11,'bold'))
    enter_pssw.place(x=30,y=180)
    signup_pssw=Entry(signup_frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
    signup_pssw.place(x=30,y=215)
    signup_pssw.insert(0,'Password')
    Frame(signup_frame,width=185,height=2,bg='black').place(x=25,y=243)
    signup_pssw.bind('<FocusIn>',on_enter)
    signup_pssw.bind('<FocusOut>',on_leave)
    invalid=Label(signup_frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",10,"bold"),width=30)
    invalid.place(x=30,y=53)
    #------------------------------------SIGNUP ACCOUNT BACKEND--------------------------------------------------------------------------------------
    def signup_backend():
        user=str(signup_user.get())
        password=str(signup_pssw.get())
        flag=0 
        try:
            account_database()
            mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
            cursor=mydb.cursor()
            cursor.execute(f"create table if not exists SigninAccount (Name VARCHAR(30) PRIMARY KEY,Password VARCHAR(30))")
            cursor.execute(f"select Name,Password from SigninAccount")
            rows=cursor.fetchall()
            for row in rows:
                if row[0]==user:
                        flag=1
                else:
                    flag=0
            if flag==1:
                invalid.config(text="Account already exist")
            elif flag==0:
                cursor.execute(f"insert into SigninAccount (Name,Password) values ('{user}','{password}')")
                invalid.config(text="Account created successfully",fg="green")
            mydb.commit()
            cursor.close()
            mydb.close()
        except mysql.connector.Error as e:
            print(f"Error:{e}")
    #---------------------------------------------------------------------------
    signup_button=Button(signup_frame,width=30,pady=4,text='Sign Up',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=signup_backend)
    signup_button.place(x=35,y=300)
#---------------Hovering Color Change---------------------------------------
def changeOnHover(button,colorOnHover,colorOnLeave):
    button.bind("<Enter>",func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>",func=lambda e: button.config(background=colorOnLeave))
image_path1="A:\\Python\\Projects\\Automated Attendence System\\Take Attendence.jpg"
image_path2="A:\\Python\\Projects\\Automated Attendence System\\Holiday.png"
imagepath_p="A:\\Python\\Projects\\Automated Attendence System\\presentstudents.jpg"
imagepath_a="A:\\Python\\Projects\\Automated Attendence System\\absentstudents.png"
imagepath_pr="A:\\Python\\Projects\\Automated Attendence System\\presentstd.png"
imagepath_ar="A:\\Python\\Projects\\Automated Attendence System\\absentstd.png"
imagepath_signup="A:\\Python\\Projects\\Automated Attendence System\\signup.png"
#--------------------------------------MENU PAGE---------------------------------------------------------------------------------
def menu():
    signin=Toplevel(root)
    signin.title('Menu')
    signin.geometry('925x550')
    signin.config(bg="#fff")
    signin.resizable(False,False)
    signin_frame=Frame(signin,width=850,height=450,bg="white")
    signin_frame.place(x=30,y=30)
    def signin_destroy():
        if signin.winfo_exists():
            signin.destroy()
    menu_heading=Label(signin_frame,text="Menu",fg="#005694",bg="white",font=("Microsoft YaHei UI Light",21,"bold"))
    menu_heading.place(x=375,y=5)
    #--------------------------------------------------------------------------
    image_label1=Label(signin_frame,image='',width=40,height=17,bg="white")
    image_label1.place(x=580,y=90)
    image_label2=Label(signin_frame,image='',width=40,height=17,bg="white")
    image_label2.place(x=0,y=90)
    add_image_to_frame(image_label1,image_path1,230,250)
    add_image_to_frame(image_label2,image_path2,250,270)
    #-----------------------Take Attendence-----------------------------------------
    take_attnd=Button(signin_frame,width=30,pady=4,text='Take Attendence',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=lambda:[signin_destroy(),take_attendence()])
    take_attnd.place(x=290,y=90)
    mark_hol=Button(signin_frame,width=30,pady=4,text='Mark Holiday',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=holidays)
    mark_hol.place(x=290,y=170)
    attnd_rec=Button(signin_frame,width=30,pady=4,text='Attendence Record',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=lambda:[signin_destroy(),dashboard()])
    attnd_rec.place(x=290,y=250)
    std_details=Button(signin_frame,width=30,pady=4,text='Enter Student Details',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=student_details)
    std_details.place(x=290,y=330)
    changeOnHover(std_details,"#8FD437","#0097E8")
    changeOnHover(take_attnd,"#8FD437","#0097E8")
    changeOnHover(mark_hol,"#8FD437","#0097E8")
    changeOnHover(attnd_rec,"#8FD437","#0097E8")
    signin.mainloop()
#--------------------------------------SIGNIN ACCOUNT-------------------------------------------------------------------------------------
#########-----------Username
def on_enter(e):
    usr.delete(0,'end')
def on_leave(e):
    name=usr.get()
    if name=='':
        usr.insert(0,'Username')
usr=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
usr.place(x=30,y=100)
usr.insert(0,'Username')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=127)
usr.bind('<FocusIn>',on_enter)
usr.bind('<FocusOut>',on_leave)
#########---------Password
def on_enter(e):
    pssw.delete(0,'end')
def on_leave(e):
    name=pssw.get()
    if name=='':
        pssw.insert(0,'Password')
pssw=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
pssw.place(x=30,y=170)
pssw.insert(0,'Password')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=197)
pssw.bind('<FocusIn>',on_enter)
pssw.bind('<FocusOut>',on_leave)
no_account=Label(frame,text="Don't have an account?",fg='black',bg='white',font=("Microsoft YaHei UI Light",9))
no_account.place(x=50,y=310)
#######------Signup Button
sign_up=Button(frame,width=6,text='Sign Up',border=0,bg='white',fg="#0097E8",cursor='hand2',command=sign_up_page)
sign_up.place(x=190,y=310)
#----------------------------------------------------------------------------------------------------------------------
invalid=Label(frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",10,"bold"),width=20)
invalid.place(x=30,y=65)
#-------------------------------------SIGNIN ACCOUNT BACKEND--------------------------------------------------------------------------------------------
def signinaccount_backend():
    try:
        account_database()
        mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
        cursor=mydb.cursor()
        def table_exist():
            cursor.execute(f"SHOW TABLES LIKE 'SigninAccount'")
            return cursor.fetchone() is not None
        if table_exist():
            cursor.execute(f"select Name,Password from SigninAccount")
            rows=cursor.fetchall()
            for row in rows:
                if row[0]==str(usr.get()):
                    if row[1]==str(pssw.get()):
                        flag=0
                        break
                    else:
                        flag=1
                else:
                    flag=2
        else:
            flag=3
        if flag==1:
            invalid.config(text="Invalid password")
        elif flag==2:
            invalid.config(text="Invalid username")
        elif flag==3:
            invalid.config(text="No record found",fg="red")
        else:
            menu()
        mydb.commit()
        cursor.close()
        mydb.close()
    except mysql.connector.Error as e:
        print(f"Error:{e}")
#######------Signin Button
button=Button(frame,width=30,pady=4,text='Sign In',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=lambda:[signinaccount_backend()])
button.place(x=35,y=250)
#-------------------------------TAKE ATTENDENCE PAGE------------------------------------------------------------------------
def take_attendence():
    def ta_destroy():
        if ta.winfo_exists():
            ta.destroy()
    ta=Toplevel(root)
    ta.title('Take Attendence')
    ta.geometry('1125x600')
    ta.config(bg="#fff")
    ta_frame=Frame(ta,width=1200,height=600,bg="white")
    ta_frame.place(x=30,y=30)
    attnd_heading=Label(ta_frame,text="Attendence",fg="#005694",bg="white",font=("Microsoft YaHei UI Light",24,"bold"))
    attnd_heading.place(x=480,y=10)
    back_button=Button(ta,padx=7,pady=0,text="\u2190",bg='white',fg='black',border=0,font=("Microsoft YaHei UI Light",22),command=lambda:[ta_destroy(),menu()])
    back_button.place(x=10,y=-17)
    p_label=Label(ta,image='',bg='white',width=55,height=20)
    p_label.place(x=60,y=250)
    a_label=Label(ta,image='',bg='white',width=55,height=20)
    a_label.place(x=500,y=250)
    add_image_to_frame(p_label,imagepath_p,330,330)
    add_image_to_frame(a_label,imagepath_a,330,330)
    changeOnHover(back_button,"#ADADAD","#D4D4D4")
    #-----------------------------------------------------------------------------
    choose_course=Label(ta_frame,text="Choose a course:",fg='black',bg='white',font=("Microsoft YaHei UI Light",11,'bold'))
    choose_course.place(x=950,y=190)
    def show_selected(selected_value):
        pass
    courses=["Btech","MBA","BDes","BSc","MTech","BCA","BBA","BArch","BCom","BFA","MCA","BA","MA","MCom","MSc"]
    course_vr=StringVar(ta)
    course_vr.set("Choose a course")
    drop=ttk.Combobox(ta_frame,values=courses,textvariable=course_vr)
    drop.place(x=950,y=220)
    #--------------------------------------------------------
    choose_batch=Label(ta_frame,text="Choose batch:",fg='black',bg='white',font=("Microsoft YaHei UI Light",11,'bold'))
    choose_batch.place(x=950,y=105)
    def show_selected(selected_value):
        pass
    batches=["2019-2023","2020-2024","2021-2025","2022-2026","2023-2027","2024-2028","2025-2029","2026-2030","2027-2031","2028-2032"]
    batch_vr=StringVar(ta)
    batch_vr.set("Choose a batch")
    dropp=ttk.Combobox(ta_frame,values=batches,textvariable=batch_vr)
    dropp.place(x=950,y=135)
    #----------------------------------------------------------------------
    choose_section=Label(ta_frame,text="Choose a Section:",fg='black',bg='white',font=("Microsoft YaHei UI Light",11,'bold'))
    choose_section.place(x=950,y=285)
    def show_selected(selected_value):
        pass
    sections=["A1","A2","B1","B2","C1","C2","D1","D2","E1","E2","F1","F2","G1","G2","H1","H2","I1","I2","J1","J2"]
    section_vr=StringVar(ta)
    section_vr.set("Choose section")
    _dropp=ttk.Combobox(ta_frame,values=sections,textvariable=section_vr)
    _dropp.place(x=950,y=315)
    #------------------------------------------------------------------------
    choose_date=Label(ta_frame,text="Choose a Date:",fg='black',bg='white',font=("Microsoft YaHei UI Light",11,'bold'))
    choose_date.place(x=950,y=380)
    today=date.today()
    today_1=today-timedelta(days=1)
    today_2=today-timedelta(days=2)
    today_3=today-timedelta(days=3)
    today_4=today-timedelta(days=4)
    today_5=today-timedelta(days=5)
    today_6=today-timedelta(days=6)
    today_7=today-timedelta(days=7)
    today_8=today-timedelta(days=8)
    today_9=today-timedelta(days=9)
    today_10=today-timedelta(days=10)
    def show_selected(selected_value):
        pass
    dates=[str(today),str(today_1),str(today_2),str(today_3),str(today_4),str(today_5),str(today_6),str(today_7),str(today_8),str(today_9),str(today_10)]
    date_vr=StringVar(ta)
    date_vr.set("Choose Date")
    dropp_=ttk.Combobox(ta_frame,values=dates,textvariable=date_vr)
    dropp_.place(x=950,y=410)
    #---------------------------------------------------------------------------------------------
    attnd_method=Label(ta_frame,text="Take Attendence of:",fg='black',bg='white',font=("Microsoft YaHei UI Light",15,'bold'))
    attnd_method.place(x=40,y=90)
    check_box=Button(ta_frame,width=30,pady=4,text='Present Students',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=lambda:[check_entry_present(str(course_vr.get()),str(batch_vr.get()),str(date_vr.get()),str(section_vr.get()))])
    check_box.place(x=60,y=150)
    roll_no=Button(ta_frame,width=30,pady=4,text='Absent Students',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=lambda:[check_entry_absent(str(course_vr.get()),str(batch_vr.get()),str(date_vr.get()),str(section_vr.get()))])
    roll_no.place(x=550,y=150)
    changeOnHover(check_box,"#8FD437","#0097E8")
    changeOnHover(roll_no,"#8FD437","#0097E8")
    Frame(ta_frame,width=1,height=350,bg='black').place(x=880,y=110)
    #------------------------------------------------------------------------------------------------------
    invalid=Label(ta_frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",10,"bold"),width=20)
    invalid.place(x=950,y=75)
    def check_entry_present(c,b,d,s):
        if b not in batches:
            invalid.config(text="Invalid batch entry",fg="red")
        elif c not in courses:
            invalid.config(text="Invalid course entry",fg="red")
        elif s not in sections:
            invalid.config(text="Invalid section entry",fg="red")
        elif d not in dates:
            invalid.config(text="Invalid date entry",fg="red")
        else:
            invalid.config(text="")
            present_attnd(c,b,d,s)
    def check_entry_absent(c,b,d,s):
        if b not in batches:
            invalid.config(text="Invalid batch entry",fg="red")
        elif c not in courses:
            invalid.config(text="Invalid course entry",fg="red")
        elif s not in sections:
            invalid.config(text="Invalid section entry",fg="red")
        elif d not in dates:
            invalid.config(text="Invalid date entry",fg="red")
        else:
            invalid.config(text="")
            absent_attnd(c,b,d,s)

#--------------------------------PRESENT STUDENTS PAGE------------------------------------------------------------------------------------
today_date=date.today()
def present_attnd(c,b,d,s):
    ca=Toplevel(root)
    ca.title('Present Students')
    ca.geometry('625x600')
    ca.config(bg="#fff")
    ca.resizable(False,False)
    ca_frame=Frame(ca,width=600,height=600,bg="white")
    ca_frame.place(x=30,y=30)
    #--------------------------------------------------------------------
    prlabel=Label(ca_frame,image='',bg='white',width=38,height=7)
    prlabel.place(x=355,y=20)
    add_image_to_frame(prlabel,imagepath_pr,200,200)
    #--------------------------------------------------------------------
    cacourse_heading=Label(ca_frame,text=c,fg="#0097E8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    cacourse_heading.place(x=80,y=30)
    cabatch_heading=Label(ca_frame,text=f"({b})",fg="#0097E8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    cabatch_heading.place(x=185,y=30)
    section=Label(ca_frame,text="Section:",fg="black",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
    section.place(x=80,y=90)
    section_name=Label(ca_frame,text=s,fg="black",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
    section_name.place(x=155,y=90)
    date=Label(ca_frame,text="Date:",fg="black",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
    date.place(x=80,y=120)
    d_m_y=Label(ca_frame,text=d,fg="black",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
    d_m_y.place(x=140,y=120)
    rollno=Label(ca_frame,text="Roll No",fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"))
    rollno.place(x=90,y=180)
    name=Label(ca_frame,text="Student Name",fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"))
    name.place(x=235,y=180)
    def on_canvas_configure1(e):
        canvas1.configure(scrollregion=canvas1.bbox("all"))
    def on_scroll_v(*args):
        canvas1.yview(*args)
    canvas1 = Canvas(ca_frame, width=350, height=250, bg="white")
    canvas1.place(x=80, y=210)  
    data_frame1=Frame(canvas1,bg="red") 
    canvas1.create_window((0, 0), window=data_frame1, anchor='nw') 
    v_scroll = Scrollbar(ca_frame, orient='vertical', command=on_scroll_v)
    v_scroll.place(x=430, y=210, height=250)
    canvas1.config(yscrollcommand=v_scroll.set)
    canvas1.bind("<Configure>", on_canvas_configure1)
    invalid=Label(ca_frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",9,"bold"),width=25)
    invalid.place(x=75,y=155)
    #---------------------------------PRESENT STUDENT BACKEND------------------------------------------------------
    final_text=[]
    dates=f"{d}"
    table_name=str(f"{c}{s}{b}").lower()
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
        cursor=mydb.cursor()
        def table_exist(cursor,table_name):
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            return cursor.fetchone() is not None
        if table_exist(cursor,table_name):
            cursor.execute(f"SHOW COLUMNS FROM `{table_name}`")
            columns=[column[0] for column in cursor.fetchall()]
            if dates not in columns:          
                cursor.execute(f"alter table `{table_name}` add column `{dates}` VARCHAR(10)")      
            cursor.execute(f"select RollNo,StudentName from `{table_name}`")
            rows=cursor.fetchall()
            if rows:
                for row in rows:
                    final_text.append(f"{str(row[0]):<35s}{str(row[1]):<30s}")
            else:
                invalid.config(text="No record found")
        else:
            invalid.config(text="No record found")
    except mysql.connector.Error as e:
        print(f"Error:{e}")
    def on_checkbox_clicked(r):
        checkbox_vr[r].set(1)
    checkbox_vr=[IntVar() for _ in range(len(final_text))]
    for r,i in enumerate(final_text):        
        checkbox=Checkbutton(data_frame1,text=i,variable=checkbox_vr[r],background="white",onvalue=1,offvalue=0,command=lambda r=r:on_checkbox_clicked(r),width=50,anchor='w',font=("Microsoft YaHei UI Light",11,"bold"))
        checkbox.grid(row=r,column=0)
        if r%2==0:
            checkbox.config(background="#E3E3E3")
    def update_value():
        try:
            cursor.execute(f"select RollNo from `{table_name}`")
            rn=cursor.fetchall()
            if rn:
                for i,val in enumerate(rn):
                    if checkbox_vr[i].get()==1:
                        cursor.execute(f"update `{table_name}` set `{d}`='P' where RollNo={val[0]}")
                    else:
                        cursor.execute(f"update `{table_name}` set `{d}`='A' where RollNo={val[0]}")
                invalid.config(text="Record added successfully",fg="green")
            else:
                invalid.config(text="No record found")
            mydb.commit()
            cursor.close()
            mydb.close()
        except mysql.connector.Error as e:
            print(f"Error:{e}")
    #-------------------------------------------------------------------------------------------------------------
    submit=Button(ca_frame,width=20,pady=4,text='Submit',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=update_value)
    submit.place(x=240,y=480)
    changeOnHover(submit,"#8FD437","#0097E8")
#------------------------------------ABSENT STUDENT PAGE----------------------------------------------------------
def absent_attnd(c,b,d,s):
    aa=Toplevel(root)
    aa.title('Absent Students')
    aa.geometry('685x400')
    aa.config(bg="#fff")
    aa.resizable(False,False)
    aa_frame=Frame(aa,width=630,height=350,bg="white")
    aa_frame.place(x=30,y=30)
    acourse_heading=Label(aa_frame,text="Attendence",fg="#0097E8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    acourse_heading.place(x=230,y=20)
    aacourse_heading=Label(aa_frame,text=c,fg="#1FB8D0",bg="white",font=("Microsoft YaHei UI Light",16,"bold"))
    aacourse_heading.place(x=80,y=80)
    aabatch_heading=Label(aa_frame,text=f"({b})",fg="#1FB8D0",bg="white",font=("Microsoft YaHei UI Light",16,"bold"))
    aabatch_heading.place(x=150,y=80)
    a_section=Label(aa_frame,text="Section:",fg="black",bg="white",font=("Microsoft YaHei UI Light",10,"bold"))
    a_section.place(x=80,y=130)
    a_section_name=Label(aa_frame,text=s,fg="black",bg="white",font=("Microsoft YaHei UI Light",10,"bold"))
    a_section_name.place(x=155,y=130)
    a_date=Label(aa_frame,text="Date:",fg="black",bg="white",font=("Microsoft YaHei UI Light",10,"bold"))
    a_date.place(x=80,y=160)
    abs_d_m_y=Label(aa_frame,text=d,fg="black",bg="white",font=("Microsoft YaHei UI Light",10,"bold"))
    abs_d_m_y.place(x=140,y=160)
    #-----------------------------------------------------------------------------
    p_label=Label(aa_frame,image='',bg='white',width=38,height=3)
    p_label.place(x=345,y=60)
    add_image_to_frame(p_label,imagepath_ar,200,180)
    #--------------------------------------------------------------------------------------
    user_input=[]
    def on_enter(e):
        rollno.delete(0,'end')
    def on_leave(e):
        rn_name=rollno.get()
        if rn_name=='':
            rollno.insert(0,'Enter the Rollno')
    def on_entered_pressed(e):
        user_input.append(rollno.get())
        rollno.delete(0,'end')
    rollno=Entry(aa_frame,width=20,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",10))
    rollno.place(x=180,y=225)
    rollno.insert(0,'Enter the Rollno')
    Frame(aa_frame,width=150,height=2,bg='black').place(x=180,y=250)
    rollno.bind('<FocusIn>',on_enter)
    rollno.bind('<FocusOut>',on_leave)
    rollno.bind('<Return>',on_entered_pressed)
    inst=Label(aa_frame,text="(Press enter to add record successfully)",fg="black",bg="white",font=("Microsoft YaHei UI Light",8,"bold"))
    inst.place(x=300,y=235)
    #----------------ABSENT STUDENTS BACKEND--------------------------------------------------------------------------------------
    invalid=Label(aa_frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",9,"bold"),width=25)
    invalid.place(x=75,y=195)
    table_name=str(f"{c}{s}{b}")
    table_name.lower()
    dates=f"{d}"
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
        cursor=mydb.cursor()
        def table_exist(cursorr,tablename):
            cursorr.execute(f"SHOW TABLES LIKE '{tablename}'")
            return cursorr.fetchone() is not None
        if table_exist(cursor,table_name):
            cursor.execute(f"SHOW COLUMNS FROM `{table_name}`")
            columns=[column[0] for column in cursor.fetchall()]
            if dates not in columns:          
                cursor.execute(f"alter table `{table_name}` add column `{dates}` VARCHAR(10)")
            def update_value_a():
                try:
                    cursor.execute(f"update `{table_name}` set `{dates}`='P'")
                    user_input.sort()
                    for i in range(len(user_input)):
                        cursor.execute(f"select * from `{table_name}` where RollNo='{user_input[i]}'")
                        count=cursor.fetchone()
                        if count:
                            cursor.execute(f"update `{table_name}` set `{dates}`='A' where RollNo='{user_input[i]}'")
                            invalid.config(text="Record added successfully",fg="green")
                        else:
                            invalid.config(text="No record found",fg="red")
                    mydb.commit()
                    cursor.close()
                    mydb.close()
                except mysql.connector.Error as e:
                    print(f"Error:{e}")
        else:
            invalid.config(text="No record found",fg="red")
    except mysql.connector.Error as e:
        print(f"Error:{e}")
    #------------------------------------------------------
    submit_a=Button(aa_frame,width=30,pady=4,text='Submit',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=update_value_a)
    submit_a.place(x=180,y=270)
    changeOnHover(submit_a,"#8FD437","#0097E8")
#--------------------------STUDENT-----DETAILS---PAGE-------------------------------------------------------------------------------------------
def student_details():
    st=Toplevel(root)
    st.title('Student Details')
    st.geometry('500x500')
    st.config(bg="#fff")
    st.resizable(False,False)
    st_frame=Frame(st,width=450,height=450,bg="white")
    st_frame.place(x=20,y=30)
    menu_heading=Label(st_frame,text="Student Details",fg="#0097E8",bg="white",font=("Microsoft YaHei UI Light",21,"bold"))
    menu_heading.place(x=120,y=5)
    Frame(st_frame,width=1,height=275,bg='black').place(x=230,y=80)
    #-----------------------------------------------------------------
    imagepath="A:\\Python\\Projects\\Automated Attendence System\\studentdetails2.png"
    stdlabel=Label(st_frame,image='',bg='white',width=35,height=17)
    stdlabel.place(x=250,y=80)
    add_image_to_frame(stdlabel,imagepath,250,260)
    invalid=Label(st_frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",9,"bold"),width=25)
    invalid.place(x=30,y=45)
    #-----------------------------------------------------------------------
    def std_destroy():
        if st.winfo_exists():
            st.destroy()
    #------------------------------------------------
    def on_enter1(e):
        enter_course.delete(0,'end')
    def on_leave1(e):
        c_name=enter_course.get()
        if c_name=='':
            enter_course.insert(0,'Course; Ex:BTech')
    course=Label(st_frame,text="Enter the course:",fg="black",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
    course.place(x=50,y=185)
    enter_course=Entry(st_frame,width=20,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",10))
    enter_course.place(x=50,y=215)
    enter_course.insert(0,'Course; Ex:BTech')
    Frame(st_frame,width=150,height=2,bg='black').place(x=50,y=235)
    enter_course.bind('<FocusIn>',on_enter1)
    enter_course.bind('<FocusOut>',on_leave1)
    #--------------------------------------------------------------
    def on_enter2(e):
        enter_batch.delete(0,'end')
    def on_leave2(e):
        b_name=enter_batch.get()
        if b_name=='':
            enter_batch.insert(0,'Batch; Ex:2020_2024')
    batch=Label(st_frame,text="Enter the batch:",fg="black",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
    batch.place(x=50,y=85)
    enter_batch=Entry(st_frame,width=20,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",10))
    enter_batch.place(x=50,y=125)
    enter_batch.insert(0,'Batch; Ex:2020_2024')
    Frame(st_frame,width=150,height=2,bg='black').place(x=50,y=145)
    enter_batch.bind('<FocusIn>',on_enter2)
    enter_batch.bind('<FocusOut>',on_leave2)
    #---------------------------------------------------------------------------------
    def on_enter3(e):
        enter_section.delete(0,'end')
    def on_leave3(e):
        s_name=enter_section.get()
        if s_name=='':
            enter_section.insert(0,'Section')
    section=Label(st_frame,text="Enter the section:",fg="black",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
    section.place(x=50,y=265)
    enter_section=Entry(st_frame,width=20,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",10))
    enter_section.place(x=50,y=305)
    enter_section.insert(0,'Section')
    Frame(st_frame,width=150,height=2,bg='black').place(x=50,y=325)
    enter_section.bind('<FocusIn>',on_enter3)
    enter_section.bind('<FocusOut>',on_leave3)
    #------------------------------------------------------------------------------------------
    delete_data=Label(st_frame,text="Do you want to delete all data?",fg="black",bg="white",font=("Microsoft YaHei UI Light",8,"bold"))
    delete_data.place(x=50,y=360)
    #----------------------------FOLDERS---------------------------------------------
    def is_digit(b):
        for char in b:
            if char.isdigit() or char=='-':
                return True
        return False
    def alpha_(c):
        if c.isalpha():
            return True
        else:
            return False
    def alpha_digit_both(s):
        if s.isalnum() :
            return True
        else:
            return False
    def correct_data(b,c,s):
        table_n=f"{c}{s}{b}"
        if is_digit(b) and alpha_(c) and alpha_digit_both(s):
            invalid.config(text="")
            student_data(table_n)
        elif not is_digit(b):
            invalid.config(text="Invalid batch entry")
        elif not alpha_(c):
            invalid.config(text="Invalid course entry")
        elif not alpha_digit_both(s):
            invalid.config(text="Invalid section entry")
        else:
            invalid.config("Invalid data entries")
    #------------------------------------------------------------------------------------
    submit_st=Button(st_frame,width=30,pady=4,text='Submit',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=lambda :[correct_data(str(enter_batch.get()),str(enter_course.get()),str(enter_section.get())),std_destroy()])
    submit_st.place(x=60,y=400)
    changeOnHover(submit_st,"#8FD437","#0097E8")
#----------------------------------------STUDENT SECTION DATA BACKEND--------------------------------------------------
    def delete_std_sec():
        table_name=f"{str(enter_course.get())}{str(enter_section.get())}{str(enter_batch.get())}"
        table_name.lower()
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
            cursor=mydb.cursor()
            def table_exist(cursorr,tablename):
                cursorr.execute(f"SHOW TABLES LIKE '`{tablename}`'")
                return cursor.fetchone() is not None
            if table_exist(cursor,table_name):
                cursor.execute(f"drop table `{table_name}`")
                invalid.config(text="Record deleted successfully",fg="green")
            else:
                invalid.config(text="No record found",fg="red")
            mydb.commit()
            cursor.close()
            mydb.close()
        except mysql.connector.Error as e:
            print(f"Error:{e}")
    delete_itsec=Button(st_frame,text=f"Delete",fg="#0097E8",bg="white",border=0,cursor='hand2',font=("Microsoft YaHei UI Light",8,"bold"),command=delete_std_sec)
    delete_itsec.place(x=245,y=360)
#------------------------------------------------------------------------------------------------------
def student_data(f):
    sd=Toplevel(root)
    sd.title('Student Data')
    sd.geometry('500x500')
    sd.config(bg="#fff")
    sd_frame=Frame(sd,width=450,height=450,bg="white")
    sd_frame.place(x=30,y=30)
    menu_heading=Label(sd_frame,text="Student Details",fg="#0097E8",bg="white",font=("Microsoft YaHei UI Light",21,"bold"))
    menu_heading.place(x=120,y=5)
    #-------------------------------------------------------
    imagepath="A:\\Python\\Projects\\Automated Attendence System\\studentdetail1.png"
    stdlabel=Label(sd_frame,image='',bg='white',width=35,height=17)
    stdlabel.place(x=200,y=50)
    add_image_to_frame(stdlabel,imagepath,250,260)
    #-------------------------------------
    def on_enter(e):
        enter_name.delete(0,'end')
        enter_name.config(fg="black")
    def on_leave(e):
        d_name=enter_name.get()
        if d_name=='':
            enter_name.insert(0,'Enter name')
            enter_name.config(fg="red")
    name=Label(sd_frame,text="Enter name:",fg="black",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
    name.place(x=50,y=100)
    enter_name=Entry(sd_frame,width=20,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
    enter_name.place(x=50,y=140)
    enter_name.insert(0,'Name')
    Frame(sd_frame,width=150,height=2,bg='black').place(x=50,y=165)
    enter_name.bind('<FocusIn>',on_enter)
    enter_name.bind('<FocusOut>',on_leave)
    #------------------------------------------------------------------------------
    def on_enter(e):
        enter_rollno.delete(0,'end')
        enter_rollno.config(fg="black")
    def on_leave(e):
        r_name=enter_rollno.get()
        if r_name=='':
            enter_rollno.insert(0,'Enter rollno')
            enter_rollno.config(fg="red")
    rollno=Label(sd_frame,text="Enter Rollno:",fg="black",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
    rollno.place(x=50,y=200)
    enter_rollno=Entry(sd_frame,width=20,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
    enter_rollno.place(x=50,y=240)
    enter_rollno.insert(0,'Rollno')
    Frame(sd_frame,width=150,height=2,bg='black').place(x=50,y=265)
    enter_rollno.bind('<FocusIn>',on_enter)
    enter_rollno.bind('<FocusOut>',on_leave)
    #------------------------------------------------------------------------------------------
    delete_data=Label(sd_frame,text="Do you want to delete it?",fg="black",bg="white",font=("Microsoft YaHei UI Light",10,"bold"))
    delete_data.place(x=50,y=295)
    #----------------------------------------------------------------------------------------------------------
    invalid=Label(sd_frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",10,"bold"),width=25)
    invalid.place(x=10,y=70)
    def rollno_check(r):
        if r.isdigit():
            return 1
    def name_check(n):
        if n.isalpha():
            return 1
    def correct_data(r,n):
        if rollno_check(r) and name_check(n):
            invalid.config(text="")
            added_std_data()
        elif not rollno_check(r):
            invalid.config(text="Invalid roll number entry",fg="red")
        elif not name_check(n):
            invalid.config(text="Invalid name entry",fg="red")
        else:
            invalid.config(text="Invalid data entries",fg="red")
    def del_data(r,n):
        if rollno_check(r) and name_check(n):
            invalid.config(text="")
            delete_std()
        elif not rollno_check(r):
            invalid.config(text="Invalid roll number entry",fg="red")
        elif not name_check(n):
            invalid.config(text="Invalid name entry",fg="red")
        else:
            invalid.config(text="Invalid data entries",fg="red")
#-----------------STUDENT DETAILS BACKEND-----------------------------------------------------------------------------------------------
    def added_std_data():
        table_name=str(f)
        table_name.lower()
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
            cursor=mydb.cursor()
            cursor.execute(f"create table if not exists `{table_name}`(RollNo INT PRIMARY KEY,StudentName VARCHAR(20))")
            new_name=str(enter_name.get())
            new_rn=str(enter_rollno.get())
            cursor.execute(f"SELECT * FROM `{table_name}` WHERE RollNo = '{new_rn}'")
            existing_record = cursor.fetchone()
            if existing_record:
                invalid.config(text="Record already created")
            else:
                cursor.execute(f"insert into `{table_name}`(RollNo,StudentName) values ('{new_rn}','{new_name}')")
                cursor.execute(f"select * from `{table_name}` order by RollNo ASC")
                cursor.fetchall()
                invalid.config(text="Record added successfully",fg="green")
            mydb.commit()
            cursor.close()
            mydb.close()
        except mysql.connector.Error as e:
            print(f"Error:{e}")
#----------------------------------------------------------------------------------------------------------
    submit_sd=Button(sd_frame,width=30,pady=4,text='Submit',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=lambda:[correct_data(str(enter_rollno.get()),str(enter_name.get()))])
    submit_sd.place(x=60,y=350)
    changeOnHover(submit_sd,"#8FD437","#0097E8")
#-----------------------------------------------------------------------------------------------------------------------------
    def delete_std():
        table_name=str(f)
        table_name.lower()
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
            cursor=mydb.cursor()
            def table_exist(cursorr,tablename):
                cursorr.execute(f"SHOW TABLES LIKE '{tablename}'")
                return cursor.fetchone() is not None
            if table_exist(cursor,table_name):
                cursor.execute(f"select * from `{table_name}` where RollNo='{str(enter_rollno.get())}'")
                row=cursor.fetchone()
                if row:
                    cursor.execute(f"delete from `{table_name}` where RollNo='{str(enter_rollno.get())}'")
                    invalid.config(text="Record deleted successfully",fg="green")
                else:
                    invalid.config(text="No record found",fg="red")
            else:
                invalid.config(text="No record found",fg="red")
            mydb.commit()
            cursor.close()
            mydb.close()
        except mysql.connector.Error as e:
            print(f"Error:{e}")
    delete_it=Button(sd_frame,text=f"Delete",fg="#0097E8",bg="white",border=0,cursor='hand2',font=("Microsoft YaHei UI Light",10,"bold"),command=lambda:[del_data(str(enter_rollno.get()),str(enter_name.get()))])
    delete_it.place(x=232,y=292)
#--------------------------------------------------HOLIDAYS----------------------------------------------------------------------------
def holidays():
    h=Tk()
    h.title('Mark Holidays')
    h.geometry('300x300')
    h.config(bg="#fff")
    h_frame=Frame(h,width=260,height=260,bg="white")
    h_frame.place(x=20,y=20)
    def h_destroy():
        if h.winfo_exists():
            h.destroy()
    #------------------------------------------------TODAY-----------------------------------------------------------------------------------
    def today_holiday():
        today=date.today()
        current_date=f"{today.strftime("%d")}/{today.month}/{today.year}"
        table_name=f"holiday{today.year}"   
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
            cursor=mydb.cursor()
            cursor.execute(f"create table if not exists {table_name}(Date INT,Month INT,Dates VARCHAR(20),Number_of_Holidays INT)")
            cursor.execute(f"select * from {table_name} where Date='{today.strftime("%d")}' AND Month='{today.month}'")
            result=cursor.fetchall()
            if result:
                invalid.config(text="Record already exist",fg="red")
            else:
                cursor.execute(f"insert into {table_name}(Date,Month,Dates,Number_of_Holidays) values ('{today.strftime("%d")}','{today.month}','{current_date}','1')")
                invalid.config(text="Holiday marked successfully",fg="green")
            mydb.commit()
            cursor.close()
            mydb.close()
        except mysql.connector.Error as e:
            print(f"Error:{e}")
    #-----------------------------------------------------------------------------------
    cacourse_heading=Label(h_frame,text="Mark Holidays",fg="#005694",bg="white",font=("Microsoft YaHei UI Light",14,"bold"))
    cacourse_heading.place(x=50,y=10)
    invalid=Label(h_frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",8,"bold"),width=25)
    invalid.place(x=40,y=40)
    today_=Button(h_frame,width=20,pady=4,text='Today',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",10),command=today_holiday)
    today_.place(x=40,y=70)
    single_date=Button(h_frame,width=20,pady=4,text='Single Date',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",10),command=lambda:[h_destroy(),single_h_date()])
    single_date.place(x=40,y=140)
    no_days=Button(h_frame,width=20,pady=4,text='Number of Days',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",10),command=lambda:[h_destroy(),no_days_holiday()])
    no_days.place(x=40,y=210)
    changeOnHover(today_,"#8FD437","#0097E8")
    changeOnHover(single_date,"#8FD437","#0097E8")
    changeOnHover(no_days,"#8FD437","#0097E8")
#----------------------------------------SINGLE DAY-------------------------------------------------------------------------
def single_h_date():
    s=Tk()
    s.title('Mark Holiday')
    s.geometry('400x400')
    s.config(bg="#fff")
    s.resizable(False,False)
    s_frame=Frame(s,width=350,height=350,bg="white")
    s_frame.place(x=20,y=20)
    cacourse_heading=Label(s_frame,text="Mark Holidays",fg="#005694",bg="white",font=("Microsoft YaHei UI Light",14,"bold"))
    cacourse_heading.place(x=85,y=0)
    #--------------------------------------------------------------
    choose_date=Label(s_frame,text="Choose a Date:",fg='black',bg='white',font=("Microsoft YaHei UI Light",11,'bold'))
    choose_date.place(x=30,y=50)
    #-----------------------------------------------------------
    def show_selected(selected_value):
        pass
    dates_vr=StringVar(s)
    dates_vr.set("Date")
    dates=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',"31"]
    dateDrop=ttk.Combobox(s_frame,values=dates,textvariable=dates_vr)
    dateDrop.place(x=45,y=110)
    #--------------------------------------------------------------------
    def show_selected(selected_value):
        pass
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    month_vr=StringVar(s)
    month_vr.set("Month")
    m_drop=ttk.Combobox(s_frame,values=months,textvariable=month_vr)
    m_drop.place(x=45,y=180)
    #------------------------------------------------------------------------------------- 
    today=date.today()
    years=[f"{today.year}",f"{today.year-1}",f"{today.year-2}",f"{today.year-3}",f"{today.year-4}",f"{today.year-5}",f"{today.year-6}",f"{today.year-7}",f"{today.year-8}",f"{today.year-9}",f"{today.year-10}"]
    year_vr=StringVar(s)
    year_vr.set("Year")
    yrdrop=ttk.Combobox(s_frame,values=years,textvariable=year_vr)
    yrdrop.place(x=45,y=240)    
    #----------------------------------------------------------------------------------------------
    invalid=Label(s_frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",8,"bold"),width=25)
    invalid.place(x=45,y=80)
    def proper_date():
        odd_months=["January","March","May","July","August","October","December"]
        if month_vr.get() in odd_months:
            invalid.config(text="Holiday marked successfully",fg="green")
            single_day_backend()
        elif month_vr.get()=='February':
            if int(dates_vr.get())>28:
                invalid.config(text="Invalid date entry",fg="red")
            else:
                invalid.config(text="Holiday marked successfully",fg="green")
                single_day_backend()
        else:
            if int(dates_vr.get())>30:
                invalid.config(text="Invalid date entry",fg="red")
            else:
                invalid.config(text="Holiday marked successfully",fg="green")
                single_day_backend()
    #--------------------------------------------------------------------------------------------------------------------------------
    submit_s=Button(s_frame,width=30,pady=4,text='Submit',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=proper_date)
    submit_s.place(x=60,y=300)
    changeOnHover(submit_s,"#8FD437","#0097E8")
    #--------------------------------------SINGLE DAY BACKEND---------------------------------------------------------------------
    def single_day_backend():
        table_name=f"holiday{year_vr.get()}"
        date_object=datetime.strptime(month_vr.get(),"%B")
        month_no=date_object.month
        current_date=f"{dates_vr.get()}/{month_no}/{year_vr.get()}"
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
            cursor=mydb.cursor()
            cursor.execute(f"create table if not exists {table_name}(Date INT,Month INT,Dates VARCHAR(20),Number_of_Holidays INT)")
            cursor.execute(f"select * from {table_name} where Date='{dates_vr.get()}' AND Month='{month_no}'")
            result=cursor.fetchall()
            if result:
                invalid.config(text="Record already exist",fg="red")
            else:
                cursor.execute(f"insert into {table_name}(Date,Month,Dates,Number_of_Holidays) values ('{dates_vr.get()}','{month_no}','{current_date}','1')")
            mydb.commit()
            cursor.close()
            mydb.close()
        except mysql.connector.Error as e:
            print(f"Error:{e}")
#------------------------------NUMBER OF DAYS HOLIDAYS-----------------------------------------------------------------------------
def no_days_holiday():
    nh=Tk()
    nh.title('Mark Holiday')
    nh.geometry('400x400')
    nh.config(bg="#fff")
    nh.resizable(False,False)
    nh_frame=Frame(nh,width=350,height=350,bg="white")
    nh_frame.place(x=20,y=20)
    cacourse_heading=Label(nh_frame,text="Mark Holidays",fg="#005694",bg="white",font=("Microsoft YaHei UI Light",14,"bold"))
    cacourse_heading.place(x=85,y=0)
    from_date=Label(nh_frame,text="From:",fg='black',bg='white',font=("Microsoft YaHei UI Light",11,'bold'))
    from_date.place(x=20,y=30)
    to_date=Label(nh_frame,text="To:",fg='black',bg='white',font=("Microsoft YaHei UI Light",11,'bold'))
    to_date.place(x=170,y=30)
    invalid=Label(nh_frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",8,"bold"),width=25)
    invalid.place(x=40,y=240)
    #------------------------------------------------------------------------------------------------------------
    dates_vr1=StringVar(nh)
    dates_vr1.set("Date")
    dates_vr2=StringVar(nh)
    dates_vr2.set("Date")
    dateDrop1=ttk.Combobox(nh,values=list(range(1,32)),textvariable=dates_vr1)
    dateDrop1.grid(row=0,column=1,padx=5,pady=10)
    dateDrop1.place(x=35,y=90)
    dateDrop2=ttk.Combobox(nh,values=list(range(1,32)),textvariable=dates_vr2)
    dateDrop2.grid(row=0,column=1,padx=5,pady=10)
    dateDrop2.place(x=185,y=90)
    #----------------------------------------------------------------------------------------------------------------------------------
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    month_vr1=StringVar(nh)
    month_vr1.set("Month")
    month_vr2=StringVar(nh)
    month_vr2.set("Month")
    m_drop1=ttk.Combobox(nh,values=months,textvariable=month_vr1)
    m_drop1.grid(row=0,column=1,padx=5,pady=10)
    m_drop1.place(x=35,y=160)
    m_drop2=ttk.Combobox(nh,values=months,textvariable=month_vr2)
    m_drop2.grid(row=0,column=1,padx=5,pady=10)
    m_drop2.place(x=185,y=160)
    #------------------------------------------------------------------------------------------------------------------------------
    today=date.today()
    years=[f"{today.year}",f"{today.year-1}",f"{today.year-2}",f"{today.year-3}",f"{today.year-4}",f"{today.year-5}",f"{today.year-6}",f"{today.year-7}",f"{today.year-8}",f"{today.year-9}",f"{today.year-10}"]
    year_vr1=StringVar(nh)
    year_vr1.set("Year")
    year_vr2=StringVar(nh)
    year_vr2.set("Year")
    yrdrop1=ttk.Combobox(nh,values=years,textvariable=year_vr1)
    yrdrop1.grid(row=0,column=1,padx=5,pady=10)
    yrdrop1.place(x=35,y=230)
    yrdrop2=ttk.Combobox(nh,values=years,textvariable=year_vr2)
    yrdrop2.grid(row=0,column=1,padx=5,pady=10)
    yrdrop2.place(x=185,y=230)
    #-----------------------------------------------------------------------------------------------------------------------------
    def proper_no_date():
        odd_months=["January","March","May","July","August","October","December"]
        if month_vr1.get() in odd_months:
            invalid.config(text="Holiday marked successfully",fg="green")
            no_day_backend()
        if month_vr2.get() in odd_months:
            invalid.config(text="Holiday marked successfully",fg="green")
            no_day_backend()
        elif month_vr1.get()=='February' or month_vr2.get()=='February':
            if int(dates_vr1.get())>28 or int(dates_vr2.get()>28):
                invalid.config(text="Invalid data entry",fg="red")
            else:
                invalid.config(text="Holiday marked successfully",fg="green")
                no_day_backend()
        else:
            if int(dates_vr1.get())>30 or int(dates_vr2.get())>30:
                invalid.config(text="Invalid data entry",fg="red")
            else:
                invalid.config(text="Holiday marked successfully",fg="green")
                no_day_backend()
    #---------------------------------------------------------------------------------------------------------------------------------------
    submit_s=Button(nh_frame,width=20,pady=4,text='Submit',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",12),command=proper_no_date)
    submit_s.place(x=60,y=275)
    changeOnHover(submit_s,"#8FD437","#0097E8")
    #-----------------------------------------NUMBER OF HOLIDAYS BACKEND------------------------------------------------------------------------------------
    def no_day_backend():
        table_name1=f"holiday{year_vr1.get()}"
        table_name2=f"holiday{year_vr2.get()}"
        date_object1=datetime.strptime(month_vr1.get(),"%B")
        date_object2=datetime.strptime(month_vr2.get(),"%B")
        month_no1=date_object1.month
        month_no2=date_object2.month
        current_date1=f"{dates_vr1.get()}/{month_no1}/{year_vr1.get()}"
        current_date2=f"{dates_vr2.get()}/{month_no2}/{year_vr2.get()}"
        if(int(year_vr1.get())>int(year_vr2.get())):
            invalid.config(text="Invalid data entry",fg="red")
        else:
            if(int(year_vr1.get())==int(year_vr2.get())):
                datetime1=datetime(int(year_vr1.get()),int(month_no1),int(dates_vr1.get()))
                datetime2=datetime(int(year_vr2.get()),int(month_no2),int(dates_vr2.get()))
                time_difference=datetime2-datetime1
                days_difference=time_difference.days
                n_d=int(f"{dates_vr1.get()}")
                c_d=f"{current_date1}-{current_date2}"
                try:
                    mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
                    cursor=mydb.cursor()
                    cursor.execute(f"create table if not exists {table_name1}(Date INT,Month INT,Dates VARCHAR(100),Number_of_Holidays INT)")
                    cursor.execute(f"select * from {table_name1} where Date='{n_d}' AND Month='{month_no1}'")
                    result=cursor.fetchall()
                    if result:
                        print(result)
                        invalid.config(text="Record already exist",fg="red")
                    else:
                        cursor.execute(f"insert into {table_name1}(Date,Month,Dates,Number_of_Holidays) values ('{n_d}','{month_no1}','{c_d}','{days_difference}')")
                    mydb.commit()
                    cursor.close()
                    mydb.close()
                except mysql.connector.Error as e:
                    print(f"Error:{e}")
            else:
                datetime1=datetime(int(year_vr1.get()),int(month_no1),int(dates_vr1.get()))
                datetime2=datetime(int(year_vr2.get()),int(month_no2),int(dates_vr2.get()))
                lastdate1=datetime(int(year_vr1.get()),12,31)
                lastdate2=datetime(int(year_vr2.get()),1,1)
                time_difference1=lastdate1-datetime1
                time_difference2=datetime2-lastdate2
                days_difference1=time_difference1.days
                days_difference2=time_difference2.days
                m_last_day=f"31/12/{year_vr1.get()}"
                m_first_day=f"1/1/{year_vr2.get()}"
                n_d1=int(f"{dates_vr1.get()}")
                n_d2=1
                c_d1=f"{current_date1}-{m_last_day}"
                c_d2=f"{m_first_day}-{current_date2}"
                try:
                    mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
                    cursor=mydb.cursor()
                    cursor.execute(f"create table if not exists {table_name1}(Date INT,Month INT,Dates VARCHAR(100),Number_of_Holidays INT)")
                    cursor.execute(f"select * from {table_name1} where Date='{n_d1}' AND Month='{month_no1}'")
                    result1=cursor.fetchall()
                    if result1:
                        invalid.config(text="Record already exist",fg="red")
                    else:
                        cursor.execute(f"insert into {table_name1}(Date,Month,Dates,Number_of_Holidays) values ('{n_d1}','{month_no1}','{c_d1}','{days_difference1}')")
                    cursor.execute(f"create table if not exists {table_name2}(Date INT,Month INT,Dates VARCHAR(100),Number_of_Holidays INT)")
                    cursor.execute(f"select * from {table_name2} where Date='{n_d2}' AND Month='{month_no2}'")
                    result2=cursor.fetchall()
                    if result2:
                        invalid.config(text="Record already exist",fg="red")
                    else:
                        cursor.execute(f"insert into {table_name2}(Date,Month,Dates,Number_of_Holidays) values ('{n_d2}','{month_no2}','{c_d2}','{days_difference2}')")
                    mydb.commit()
                    cursor.close()
                    mydb.close()
                except mysql.connector.Error as e:
                    print(f"Error:{e}")
#--------------------------------------------------DASHBOARD----------------------------------------------------------------------------------
def dashboard():
    d=Tk()
    d.title('Dashboard')
    d.geometry('700x550')
    d.config(bg="#fff")
    d_frame=Frame(d,width=1230,height=600,bg="white")
    d_frame.place(x=20,y=20)
    def d_destroy():
        if d.winfo_exists():
            d.destroy()
    #----------------------------------------------------------------------------------------------------------------------
    dashboard_heading=Label(d_frame,text="Dashboard",fg="#005694",bg="white",font=("Microsoft YaHei UI Light",26,"bold"))
    dashboard_heading.place(x=520,y=10)
    back_button=Button(d,padx=7,pady=0,text="\u2190",bg='white',fg='black',border=0,font=("Microsoft YaHei UI Light",22),command=lambda:[d_destroy(),menu()])
    back_button.place(x=10,y=-17)
    changeOnHover(back_button,"#ADADAD","#D4D4D4")
    #-------------------------------------------------------------------------------------------
    br_vr=StringVar(d)
    branch=Label(d_frame,text="Branch:",fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"))
    branch.place(x=25,y=75)
    branches=["Btech","MBA","B.Des","BSc","M.Tech","BCA","BBA","B.Arch","B.Com","BFA","MCA","BA","MA","M.Com","MSc"]
    branch_choice=ttk.Combobox(d_frame,values=branches,textvariable=br_vr)
    branch_choice.grid(row=0,column=1,padx=10,pady=20)
    branch_choice.place(x=95,y=80)
    #--------------------------------------------------------------------------------------------------
    s_vr=StringVar(d)
    section=Label(d_frame,text="Section:",fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"))
    section.place(x=275,y=75)
    sections=["A1","A2","B1","B2","C1","C2","D1","D2","E1","E2","F1","F2","G1","G2","H1","H2","I1","I2","J1","J2"]
    section_choice=ttk.Combobox(d_frame,values=sections,textvariable=s_vr)
    section_choice.grid(row=0,column=1,padx=10,pady=20)
    section_choice.place(x=345,y=80)
    #---------------------------------------------------------------------------------------------------------------
    ba_vr=StringVar(d)
    batch=Label(d_frame,text="Batch:",fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"))
    batch.place(x=525,y=75)
    batches=["2019-2023","2020-2024","2021-2025","2022-2026","2023-2027","2024-2028","2025-2029","2026-2030","2027-2031","2028-2032"]
    batch_choice=ttk.Combobox(d_frame,values=batches,textvariable=ba_vr)
    batch_choice.grid(row=0,column=1,padx=10,pady=20)
    batch_choice.place(x=585,y=80)
    #-------------------------------------------------------------------------------------------------------
    def on_canvas_configure1(e):
        canvas1.configure(scrollregion=canvas1.bbox("all"))
    def on_canvas_configure2(e):
        canvas2.configure(scrollregion=canvas2.bbox("all"))
    def on_canvas_configure3(e):
        canvas3.configure(scrollregion=canvas3.bbox("all"))
    def on_canvas_configure6(e):
        canvas6.configure(scrollregion=canvas6.bbox("all"))
    def on_scroll_v(*args):
        canvas1.yview(*args)
        canvas2.yview(*args)
        canvas6.yview(*args)
    def on_scroll_h(*args):
        canvas1.xview(*args)
        canvas3.xview(*args)
    canvas1 = Canvas(d, width=550, height=300, bg="white")
    canvas1.place(x=265, y=220)
    canvas2 = Canvas(d, width=250, height=300, bg="white")
    canvas2.place(x=640, y=220)
    canvas3 = Canvas(d, width=550, height=50, bg="white")
    canvas3.place(x=265, y=165)
    canvas4 = Canvas(d, width=250, height=50, bg="white")
    canvas4.place(x=640, y=165)
    canvas5 = Canvas(d, width=235, height=50, bg="white")
    canvas5.place(x=30, y=165)
    canvas6 = Canvas(d, width=235, height=300, bg="white")
    canvas6.place(x=30, y=220)
    data_frame1=Frame(canvas1,bg="white")
    data_frame2=Frame(canvas2,bg="white")
    data_frame3=Frame(canvas3,bg="white")
    data_frame4=Frame(canvas4,bg="white")
    data_frame5=Frame(canvas5,bg="white")
    data_frame6=Frame(canvas6,bg="white")
    canvas1.create_window((0, 0), window=data_frame1, anchor='nw')
    canvas2.create_window((0, 0), window=data_frame2, anchor='nw')
    canvas3.create_window((0, 0), window=data_frame3, anchor='nw')
    canvas4.create_window((0, 0), window=data_frame4, anchor='nw')
    canvas5.create_window((0, 0), window=data_frame5, anchor='nw')
    canvas6.create_window((0, 0), window=data_frame6, anchor='nw')
    h_scroll = Scrollbar(d, orient='horizontal', command=on_scroll_h)
    v_scroll = Scrollbar(d, orient='vertical', command=on_scroll_v)
    h_scroll.place(x=270, y=525, width=370)
    v_scroll.place(x=885, y=220, height=300)
    canvas1.config(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
    canvas2.config(yscrollcommand=v_scroll.set)
    canvas3.config(xscrollcommand=h_scroll.set)
    canvas6.config(yscrollcommand=v_scroll.set)
    canvas1.bind("<Configure>", on_canvas_configure1)
    canvas2.bind("<Configure>", on_canvas_configure2)
    canvas3.bind("<Configure>", on_canvas_configure3)
    canvas6.bind("<Configure>", on_canvas_configure6)
    #---------------------------------------------------------------------------------------------------------------------------------
    def on_enter(e):
            search_data.delete(0,'end')
            search_data.config(fg="black")
    def on_leave(e):
        roll_name=search_data.get()
        if roll_name =='':
            search_data.insert(0,'Enter rollno')
            search_data.config(fg="red")
    search_data=Entry(d_frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
    search_data.place(x=920,y=100)
    search_data.insert(0,'Enter Rollno')
    Frame(d_frame,width=200,height=2,bg='black').place(x=920,y=120)
    search_data.bind('<FocusIn>',on_enter)
    search_data.bind('<FocusOut>',on_leave)
    #-------------------------------------------------------------------------------------------------------
    criteria=Label(d_frame,text="Criteria",fg="#1FB8D0",bg="white",font=("Microsoft YaHei UI Light",16,"bold"))
    criteria.place(x=1000,y=150)
    def on_enter1(e):
            search_criteria.delete(0,'end')
    def on_leave1(e):
        crit_name=search_criteria.get()
        if crit_name =='':
            search_criteria.insert(0,'Enter Criteria to Filter')
    search_criteria=Entry(d_frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
    search_criteria.place(x=920,y=190)
    search_criteria.insert(0,'Enter Criteria to Filter')
    Frame(d_frame,width=170,height=2,bg='black').place(x=920,y=210)
    search_criteria.bind('<FocusIn>',on_enter1)
    search_criteria.bind('<FocusOut>',on_leave1)
    canvas_crit = Canvas(d, width=315, height=140, bg="white")
    canvas_crit.place(x=920, y=280)
    v_scroll_crit = Scrollbar(d, orient='vertical', command=canvas_crit.yview)
    v_scroll_crit.place(x=1235, y=280, height=140)
    data_frame_crit=Frame(canvas_crit,bg="white")
    canvas_crit.create_window((0, 0), window=data_frame_crit, anchor='nw')
    canvas_crit.config(yscrollcommand=v_scroll_crit.set)
    def on_canvas_configure(e):
        canvas_crit.configure(scrollregion=canvas_crit.bbox("all"))
    canvas_crit.bind("<Configure>", on_canvas_configure)
    headings=['Roll No','Name','Percentage']
    i=900
    for data in headings:
        dd=Label(d_frame,text=data,fg="black",bg="white",font=("Microsoft YaHei UI Light",10,"bold"),width=10)
        dd.place(x=i,y=230)
        i=i+100
    #-------------------------------DASHBOARD BACKEND-------------------------------------------------------------------------------
    def dashboard_atten_backend():
        tablename=f"{str(br_vr.get())}{str(s_vr.get())}{str(ba_vr.get())}"
        tablename.lower()
        absent_no=0
        present_no=0
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
            cursor=mydb.cursor()
            def table_exist(cursorr,table_name):
                cursorr.execute(f"SHOW TABLES LIKE '{table_name}'")
                return cursor.fetchone() is not None
            total=0
            if table_exist(cursor,tablename):
                clear_frame(data_frame1)
                cursor.execute(f"SELECT * FROM `{tablename}`")
                rows=cursor.fetchall()
                cursor.execute(f"SHOW COLUMNS FROM `{tablename}`")
                columns=[column[0] for column in cursor.fetchall()]
                columns.pop(0)
                columns.pop(0)
                sorted_dates = sorted(map(lambda x: datetime.strptime(x, '%Y-%m-%d'), columns))
                sorted_column = [date.strftime('%Y-%m-%d') for date in sorted_dates]
                cursor.execute("create table Temp(RollNo INT PRIMARY KEY,StudentName VARCHAR(20))")
                cursor.execute(f"insert into Temp(RollNo,StudentName) select RollNo,StudentName from `{tablename}`")
                for data in sorted_column:
                    cursor.execute(f"alter table Temp add column `{data}` VARCHAR(10)")
                    cursor.execute(f"update Temp set `{data}`=(select `{data}` from `{tablename}` LIMIT 1)")
                    cursor.execute(f"update Temp set `{data}`='Nill' where `{data}` is NULL")
                cursor.execute(f"SHOW COLUMNS FROM Temp")
                columns=[column[0] for column in cursor.fetchall()]
                for idx,i in enumerate(columns):
                    if idx==0 or idx==1:
                        data=Label(data_frame5,text=i,fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"),width=10)
                        data.grid(row=0,column=idx,padx=4,pady=15)
                    else:

                        data=Label(data_frame3,text=i,fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"),width=10)
                        data.grid(row=0,column=idx,padx=7,pady=15)
                for idx1,row in enumerate(rows):
                    for idx2,i in enumerate(row):
                        if idx2==0 or idx2==1:
                            data=Label(data_frame6,text=i,fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"),width=10)
                            data.grid(row=idx1,column=idx2,padx=5,pady=10)
                        else:
                            data=Label(data_frame1,text=i,fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"),width=10)
                            data.grid(row=idx1+1,column=idx2,padx=5,pady=10)
                            if i=='A':
                                absent_no=absent_no+1
                            elif i=='P':
                                present_no=present_no+1
                    total=present_no+absent_no
                    data_p=Label(data_frame2,text=present_no,fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"),width=10)
                    data_p.grid(row=idx1+1,column=0,padx=10,pady=10)
                    data_a=Label(data_frame2,text=absent_no,fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"),width=10)
                    data_a.grid(row=idx1+1,column=1,padx=10,pady=10)
                    absent_no=0
                    present_no=0
                pa_column=['Total Present','Total Absent']
                for idx,i in enumerate(pa_column):
                    data=Label(data_frame4,text=i,fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"),width=10)
                    data.grid(row=0,column=idx,padx=10,pady=20)
                d.update_idletasks()
                req_width1=data_frame1.winfo_reqwidth()
                req_height1=data_frame1.winfo_reqheight()
                req_height2=data_frame2.winfo_reqheight()
                canvas1.configure(scrollregion=(0, 0, req_width1, req_height1))
                canvas2.configure(scrollregion=(0, 0, 0, req_height2))
                canvas3.configure(scrollregion=(0, 0, req_width1,0))
                canvas6.configure(scrollregion=(0, 0, 0, req_height2))
                cursor.execute("DROP TABLE IF EXISTS Temp")
                mydb.commit()
                cursor.close()
                mydb.close()
            else:
                invalid=Label(data_frame1,text="No records found",fg="red",bg="white",font=("Microsoft YaHei UI Light",10,"bold"),width=25)
                invalid.grid(row=0,column=0,padx=25,pady=20)
        except mysql.connector.Error as e:
            print(f"Error:{e}")
        data=Label(d_frame,text=f"Total Lectures: {total}",fg="black",bg="white",font=("Microsoft YaHei UI Light",11,"bold"))
        data.place(x=65,y=110)
    submit_s=Button(d_frame,width=20,pady=2,text='Show Data',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",8),command=dashboard_atten_backend)
    submit_s.place(x=760,y=80)
    changeOnHover(submit_s,"#8FD437","#0097E8")
    #-------------------------------------------------------------------------------------------------------------------------------
    invalid=Label(d_frame,text="",fg="red",bg="white",font=("Microsoft YaHei UI Light",9,"bold"),width=25)
    invalid.place(x=920,y=80)
    def search_data_record():
        tablename=f"{str(br_vr.get())}{str(s_vr.get())}{str(ba_vr.get())}"
        tablename.lower()
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
            cursor=mydb.cursor()
            def table_exist(cursorr,table_name):
                cursorr.execute(f"SHOW TABLES LIKE '{table_name}'")
                return cursor.fetchone() is not None
            if table_exist(cursor,tablename):
                invalid.config(text="")
                def is_digit(s):
                    return s.isdigit()
                if is_digit(search_data.get()):
                    invalid.config(text="")
                    search=Toplevel(d)
                    search.title('Student Data')
                    search.geometry('400x500')
                    search.config(bg="#fff")
                    search.resizable(False,False)
                    search_frame=Frame(search,width=450,height=400,bg="white")
                    search_frame.place(x=40,y=50)
                    cursor.execute(f"select * from `{tablename}` where RollNo='{search_data.get()}'")
                    rows=cursor.fetchall()
                    for row in rows:
                        absent=0
                        present=0
                        for idx,i in enumerate(row):
                            if idx==0 or idx==1:
                                std_d=Label(search_frame,text=f"{row[1]}",fg="#1FB8D0",bg="white",font=("Microsoft YaHei UI Light",22,"bold"))
                                std_d.place(x=110,y=10)
                                std_d=Label(search_frame,text=f"RollNo: {row[0]}",fg="black",bg="white",font=("Microsoft YaHei UI Light",15,"bold"))
                                std_d.place(x=30,y=65)
                                std_d=Label(search_frame,text=f"Section: {s_vr.get()}",fg="black",bg="white",font=("Microsoft YaHei UI Light",15,"bold"))
                                std_d.place(x=30,y=105)
                                std_d=Label(search_frame,text=f"Branch: {br_vr.get()}",fg="black",bg="white",font=("Microsoft YaHei UI Light",15,"bold"))
                                std_d.place(x=30,y=145)
                                std_d=Label(search_frame,text=f"Batch: {ba_vr.get()}",fg="black",bg="white",font=("Microsoft YaHei UI Light",15,"bold"))
                                std_d.place(x=30,y=185)
                            else:
                                if i=='A':
                                    absent=absent+1
                                else:
                                    present=present+1
                        total=present+absent
                        percentage=(present/total)*100
                        percentage=round(percentage,2)
                        std_d=Label(search_frame,text=f"Total Lecture: {total}",fg="black",bg="white",font=("Microsoft YaHei UI Light",15,"bold"))
                        std_d.place(x=30,y=225)
                        std_d=Label(search_frame,text=f"Total Present: {present}",fg="black",bg="white",font=("Microsoft YaHei UI Light",15,"bold"))
                        std_d.place(x=30,y=265)
                        std_d=Label(search_frame,text=f"Total Absent: {absent}",fg="black",bg="white",font=("Microsoft YaHei UI Light",15,"bold"))
                        std_d.place(x=30,y=305)
                        std_d=Label(search_frame,text=f"Percentage: {percentage}%",fg="black",bg="white",font=("Microsoft YaHei UI Light",15,"bold"))
                        std_d.place(x=30,y=345)
                else:
                    invalid.config(text="Invalid rollno")
            else:
                invalid.config(text="Invalid details of student")
        except mysql.connector.Error as e:
            print(f"Error:{e}")
    search_button=Button(d_frame,width=15,pady=2,text='Search',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",8),command=search_data_record)
    search_button.place(x=1135,y=100)
    changeOnHover(search_button,"#8FD437","#0097E8")
    #-----------------------------------------------------------------------------------------------------------------------------
    def clear_frame(frame):
            for widget in frame.winfo_children():
                widget.destroy()
    #-------------------------------------------------------------------------
    def criteria_():
        tablename=f"{str(br_vr.get())}{str(s_vr.get())}{str(ba_vr.get())}"
        tablename.lower()
        final_list=[]
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
            cursor=mydb.cursor()
            def table_exist(cursorr,table_name):
                cursorr.execute(f"SHOW TABLES LIKE '{table_name}'")
                return cursor.fetchone() is not None
            if table_exist(cursor,tablename):
                def is_digit(s):
                    return s.isdigit()
                if is_digit(search_criteria.get()):
                    cursor.execute(f"select * from `{tablename}`")
                    rows=cursor.fetchall()
                    for row in rows:
                        absent=0
                        present=0
                        for i in row:
                            if i=='A':
                                absent=absent+1
                            elif i=='P':
                                present=present+1
                        total=present+absent
                        percentage=(present/total)*100
                        percentage=round(percentage,2)
                        if percentage<float(search_criteria.get()):
                            t=(f'{row[0]}',f'{row[1]}',f'{percentage}')
                            final_list.append((t))
                    if final_list:
                        for idx1,row in enumerate(final_list):
                            for idx2,data in enumerate(row):
                                crit_data=Label(data_frame_crit,text=data,fg="black",bg="white",font=("Microsoft YaHei UI Light",9,"bold"),width=10)
                                crit_data.grid(row=idx1,column=idx2,padx=5,pady=8)
                    else:
                        crit_data=Label(data_frame_crit,text="No records found",fg="red",bg="white",font=("Microsoft YaHei UI Light",9,"bold"))
                        crit_data.grid(row=0,column=0,padx=5,pady=8)
                else:
                    crit_data=Label(data_frame_crit,text="Enter valid criteria",fg="red",bg="white",font=("Microsoft YaHei UI Light",9,"bold"))
                    crit_data.grid(row=0,column=0,padx=5,pady=8)
            else:
                crit_data=Label(data_frame_crit,text="No records found",fg="red",bg="white",font=("Microsoft YaHei UI Light",9,"bold"))
                crit_data.grid(row=0,column=0,padx=5,pady=2)
                crit_data=Label(data_frame_crit,text="(Enter the correct details of student)",fg="red",bg="white",font=("Microsoft YaHei UI Light",9,"bold"))
                crit_data.grid(row=1,column=0,padx=5,pady=2)
        except mysql.connector.Error as e:
            print(f"Error:{e}")
    crit_button=Button(d_frame,width=15,pady=2,text='Show Data',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",8),command=lambda:[clear_frame(data_frame_crit),criteria_()])
    crit_button.place(x=1120,y=190)
    changeOnHover(crit_button,"#8FD437","#0097E8")
    #--------------------------------------------------------------------------------------------------------------------------------
    today=date.today()
    holidays=Label(d_frame,text="Holidays",fg="#1FB8D0",bg="white",font=("Microsoft YaHei UI Light",13,"bold"))
    holidays.place(x=1000,y=415)
    holidays=Label(d_frame,text=f"Holidays marked in year {today.year}",fg="black",bg="white",font=("Microsoft YaHei UI Light",8,"bold"))
    holidays.place(x=915,y=440)
    #-----------------------------------------------------------------------------------
    def changeyear():
        def on_enter(e):
            enter_year.delete(0,'end')
            enter_year.config(fg="black")
        def on_leave(e):
            year=enter_year.get()
            if year =='':
                enter_year.insert(0,'Enter the year')
                enter_year.config(fg="red")
        enter_year=Entry(d_frame,width=17,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",9))
        enter_year.place(x=930,y=460)
        enter_year.insert(0,'Enter Year; Ex:2022')
        Frame(d_frame,width=140,height=1,bg='black').place(x=930,y=480)
        enter_year.bind('<FocusIn>',on_enter)
        enter_year.bind('<FocusOut>',on_leave)
        def list_of_holidays():
            try:
                tablename=f"holiday{enter_year.get()}"
                mydb=mysql.connector.connect(host='localhost',user='root',port='3306',password='123456ds',database='Attendence_System')
                cursor=mydb.cursor()
                def table_exist(cursorr,table_name):
                    cursorr.execute(f"SHOW TABLES LIKE '{table_name}'")
                    return cursor.fetchone() is not None
                if table_exist(cursor,tablename):
                    canvas_holi = Canvas(d, width=315, height=80, bg="white")
                    canvas_holi.place(x=920, y=540)
                    v_scroll_holi = Scrollbar(d, orient='vertical', command=canvas_holi.yview)
                    v_scroll_holi.place(x=1235, y=540, height=80)
                    data_frame_holi=Frame(canvas_holi,bg="white")
                    canvas_holi.create_window((0, 0), window=data_frame_holi, anchor='nw')
                    canvas_holi.config(yscrollcommand=v_scroll_holi.set)
                    def on_canvas_configure(e):
                        canvas_holi.configure(scrollregion=canvas_holi.bbox("all"))
                    canvas_holi.bind("<Configure>", on_canvas_configure)
                    headings=['Date','Number Of Holidays']
                    i=935
                    for data in headings:
                        dd=Label(d_frame,text=data,fg="black",bg="white",font=("Microsoft YaHei UI Light",8,"bold"))
                        dd.place(x=i,y=500)
                        i=i+110
                    cursor.execute(f"select * from {tablename}")
                    rows=cursor.fetchall()
                    for idx1,row in enumerate(rows):
                        for idx2,i in enumerate(row):
                            if idx2==2 or idx2==3:
                                holi_data=Label(data_frame_holi,text=i,fg="black",bg="white",font=("Microsoft YaHei UI Light",9,"bold"),width=16)
                                holi_data.grid(row=idx1,column=idx2-2,padx=5,pady=8)
                    cursor.close()
                    mydb.close()
            except mysql.connector.Error as e:
                print(f"Error:{e}")
        done_button=Button(d_frame,width=12,pady=2,text='Done',bg='#0097E8',fg='white',border=0,font=("Microsoft YaHei UI Light",8),command=list_of_holidays)
        done_button.place(x=1100,y=460)
    change_year=Button(d_frame,text=f"Change Year?",fg="#0097E8",bg="white",border=0,cursor='hand2',font=("Microsoft YaHei UI Light",8,"bold"),command=changeyear)
    change_year.place(x=1100,y=440)
root.mainloop()