from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import cv2
import webbrowser
class windown:
	screen=Tk()
	def __init__(self):
		self.screen.title('Gửi mail')
		scrW=self.screen.winfo_screenwidth()
		scrH=self.screen.winfo_screenheight()
		self.screen.geometry('1000x600+%d+%d'%(scrW/2-500,scrH/2-300))
		self.screen.configure(bg='#ffd5cc')
		self.screen.resizable(False, False)
		self.cv=Canvas(self.screen,height=600,width=1000,bg='#cceaff').place(x=0,y=0)
class content_mail:
	def __init__(self,wd):
		self.parent=wd
		img = ImageTk.PhotoImage(Image.open("source/control.png"))
		self.label1 = Label(self.parent.cv,image=img)
		self.label1.image = img
		self.label1.place(x=0, y=0)
		self.label_content=Label(self.parent.cv,text="Please enter your email: ").place(x=130,y=170)
		self.AddEnt=Entry(wd.cv,font="Times 20 bold",width=50)
		self.AddEnt.place(x=130,y=200)
		self.label_content=Label(self.parent.cv,text="Please enter your password: ").place(x=130,y=250)
		self.PassEnt=Entry(wd.cv,font="Times 20 bold",width=50, show="*")
		self.PassEnt.place(x=130,y=280)
		self.Submit=Button(wd.cv,
        text='Đăng nhập',
        bg='#ffecb4',
        fg='black',
        command=self.get_result,
        font='Times 15 bold',
        height=1,
        width=20,
        ).place(x=130,y=350)
		self.Submit=Button(wd.cv,
        text='Đăng ký',
        bg='#ffecb4',
        fg='black',
        command=self.open_fun,
        font='Times 15 bold',
        height=1,
        width=20,
        ).place(x=420,y=350)
	def get_result(self):
		mail=self.AddEnt.get()
		password=self.PassEnt.get()
		print('mail: ',mail)
		print('password: ',password)
		return mail,password
	def open_fun(self):
		webbrowser.open('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
#-----------------------------------------
# WD=windown()
# gui_mail=content_mail(WD)
# WD.screen.mainloop()
