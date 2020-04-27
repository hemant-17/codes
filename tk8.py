from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1350x700+0+0")

        # variables
        self.uname = StringVar()
        self.password = StringVar()

        self.bg_icon = ImageTk.PhotoImage(file="bg3.jpg")

        image = Image.open("lo2.jpg")
        image = image.resize((400, 100), Image.ANTIALIAS)
        self.lg_icon = ImageTk.PhotoImage(image)
        #image.close()

        image12 = Image.open("pass.png")
        image12 = image.resize((40, 50), Image.ANTIALIAS)
        self.user_icon = ImageTk.PhotoImage(image12)
        #image12.close()

        l1 = Image.open("pass.png")
        l1 = image.resize((40, 50), Image.ANTIALIAS)
        self.pass_icon = ImageTk.PhotoImage(l1)


        bg_lbl = Label(self.root,image=self.bg_icon).pack()

        title = Label(self.root,text="Login",font="Helvetica 40 bold ", bg="black",fg="white",borderwidth=6 , relief=SUNKEN)
        title.place(x=0,y=0,relwidth=1)

        log_fr = Frame(self.root,bg="white")
        log_fr.place(x=450,y=200)

        log_lbl = Label(log_fr,image=self.lg_icon).grid(row=0,columnspan=2,pady=20)

        lbl_user = Label(log_fr,text="Username",image=self.user_icon,compound=LEFT,font="Helvetica 15 bold").grid(row=1,column=0,padx=20,pady=10)
        txt_user = Entry(log_fr,bd=5,textvariable= self.uname,relief=GROOVE,font="Helvetica 10").grid(row=1,column=1,padx=20)
        lbl_pass = Label(log_fr,text="Password",image=self.pass_icon,compound=LEFT,font="Helvetica 15 bold").grid(row=2,column=0,padx=20,pady=10)
        txt_pass = Entry(log_fr,bd=5,textvariable= self.password,relief=GROOVE,font="Helvetica 10").grid(row=2,column=1,padx=20)

        btn = Button(log_fr,text="Login",width=15,font="Helvetica 15 bold ",bg="black",fg="white",command=self.login1).grid(row=3,column=1,pady=10)


    def login1(self):
            if self.uname.get()== "" or self.password =="":
                messagebox.showerror("ERROR","Fields are Mandatory!!")

            elif self.uname.get() == "hemant" and self.password =="1234":
                messagebox.showinfo("Welcome",f"Login is suucessful{self.uname.get()}")

            else:
                messagebox.showerror("ERROR","Invalid Username and password!!")





root = Tk()
obj = Login(root)
root.mainloop()