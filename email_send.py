from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import smtplib
from tkinter.scrolledtext import ScrolledText

root=tk.Tk()
root.title('Email Sender')
root.geometry('400x300')
root.maxsize(400,300)
root.minsize(400,300)


def Login():
    em=email.get()
    pa=password.get()
    
    if '@gmail.com' not in em or em =='':
        messagebox.showerror('Login error','Please write the valid Email')
        
    elif pa =='':
        messagebox.showerror('Login error',"Password shouldn't be Empty")
        
    else:
        try:
            s=smtplib.SMTP('smtp.gmail.com',587)
            
            s.starttls()
            s.login(em,pa)
            
            
            messagebox.showinfo('Login Success','You have logged to Gmail Successfully')
            root=tk.Tk()
            root.geometry('500x400')
            
        
            def Logout():
                s.quit()
                root.destroy()
                
            header1=Label(root,bg='orange',width=300,height=2)
            header1.place(x=0,y=0)
            h2=Label(root,text='Email Sender',bg='orange',fg='black',font=('verdana',10,'bold'))
            h2.place(x=175,y=5)
            logout=Button(root,text='Logout',padx=20,bg='orange',relief=RIDGE,borderwidth=1,font=('verdana',10,'bold'),cursor='hand2',command=Logout)
            logout.place(x=390,y=38)
            r=Label(root,text='Recepentent Address',font=('verdana',10,'bold'))
            r.place(x=130,y=130)
            recipetent=Entry(root,width=30,relief=RIDGE,borderwidth=3)
            recipetent.place(x=130,y=150)
            st=Label(root,text='Subject',font=('verdana',10,'bold'))
            st.place(x=130,y=190)
            subject=Entry(root,width=30,relief=RIDGE,borderwidth=3)
            subject.place(x=130,y=210)
            m=Label(root,text='message',font=('verdana',10,'bold'))
            m.place(x=130,y=250)
            message=ScrolledText(root,width=40,height=5,relief=RIDGE,borderwidth=3)
            message.place(x=130,y=270)
            
            def Send():
                r=recipetent.get()
                st=subject.get()
                m=message.get()

                if '@gmail.com' not in r or r =='':
                    messagebox.showerror('Sending error','Please write the valid Email')
                elif m=='':
                    messagebox.showerror('Sending error',"Message shouldn't be empty")

                else:
                    s.sendmail(r,e,f"subject:{st}\n\n {m}")
                    messagebox.showinfo('Success','Your message has been send successfully')
                
            send=Button(root,text='send',padx=30,relief=RIDGE,borderwidth=1,bg='orange',font=('verdana',10,'bold'),cursor='hand2',command=Send)
            send.place(x=350,y=360)
            root.mainloop()
        except e:
            print(e)
            messagebox.showerror('Login Error','check id and password again')
                           
    
    

    
header=Label(root,bg='orange',width=300,height=2)
header.place(x=0,y=0)
h1=Label(root,text='Email Sender',bg='orange',fg='black',font=('verdana',13,'bold'))
h1.place(x=135,y=5)
img=ImageTk.PhotoImage(Image.open('gmail.jpg'))
logo=Label(root,image=img,borderwidth=0)
logo.place(x=80,y=38)
e=Label(root,text='Email Address',font=('verdana',10,'bold'))
e.place(x=100,y=130)
email=Entry(root,width=30,relief=RIDGE,borderwidth=3)
email.place(x=100,y=150)
p=Label(root,text='Password',font=('verdana',10,'bold'))
p.place(x=100,y=190)
password=Entry(root,width=30,relief=RIDGE,borderwidth=5)
password.place(x=100,y=210)
login=Button(root,text='Login',padx=30,bg='orange',relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor='hand2',command=Login)
login.place(x=135,y=240)
root.mainloop()


