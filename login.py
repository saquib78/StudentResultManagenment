from tkinter import *
from tkinter import messagebox,ttk
import sqlite3
import os
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1200x700+0+0")

        # ---- Background Colors -----
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        #----- Frame ----
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=200,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        email = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="white",fg="black").place(x=250, y=150)
        self.txt1_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt1_email.place(x=250, y=180,width=350,height=35)

        pass_ = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white",fg="black").place(x=250, y=250)
        self.txt1_pass_ = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt1_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg=Button(login_frame,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2",command=self.register_window).place(x=250,y=340)
        btn_forget = Button(login_frame, text="Forget Password", font=("times new roman", 14), bg="white", bd=0,fg="red", cursor="hand2", command=self.forget_password_window).place(x=450, y=340)

        btn_login = Button(login_frame, text="Login", font=("times new roman", 20,"bold"), fg="white",bg="#B00857",cursor="hand2",command=self.login).place(x=300, y=400,width=180,height=40)


    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt1_pass_.delete(0,END)
        self.txt1_email.delete(0,END)


    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get() == "" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)

        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer =?",( self.txt1_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select Correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_new_pass.get(),self.txt1_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=self.root)

    def forget_password_window(self):
        if self.txt1_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt1_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("450x425+450+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white",fg="red").place(x=0, y=10, relwidth=1)

                    # ------ Row 3

                    question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=100, y=100)
                    self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly',justify=CENTER)
                    self.cmb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                    self.cmb_quest.place(x=100, y=130, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=100, y=180)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_answer.place(x=100, y=210, width=250)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=100, y=260)
                    self.txt_new_pass = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_new_pass.place(x=100, y=290, width=250)

                    btn_change_password = Button(self.root2, text="Reset Password",command=self.forget_password, bg="green", fg="white",font=("times new roman", 15, "bold")).place(x=150, y=340)

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to : {str(es)}",parent=self.root)



    def register_window(self):
        self.root.destroy()
        import register


    def login(self):
        if self.txt1_email.get()=="" or self.txt1_pass_.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt1_email.get(),self.txt1_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome : {self.txt1_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to : {str(es)}",parent=self.root)




root=Tk()
obj=Login_window(root)
root.mainloop()