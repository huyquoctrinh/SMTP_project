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
	self.mail=""
	self.passw=""
	def log_out(self):
		self.label_suc.destroy()
		self.logButton.destroy()
		self.login_tab()
	def login_tab(self):
		img = ImageTk.PhotoImage(Image.open("source/control.png"))
		self.label1 = Label(self.parent.cv,image=img)
		self.label1.image = img
		self.label1.place(x=0, y=0)
		self.label_content=Label(self.parent.cv,text="Please enter your email: ")
		self.label_content.place(x=130,y=170)
		self.AddEnt=Text(self.parent.cv,font="Times 20 bold",width=50,height=1)
		self.AddEnt.place(x=130,y=200)
		self.label_content_1=Label(self.parent.cv,text="Please enter your password: ")
		self.label_content_1.destroy()
		self.PassEnt=Text(self.parent.cv,font="Times 20 bold",width=50,height=1)
		self.PassEnt.place(x=130,y=280)
		self.Submit=Button(self.parent.cv,text='Đăng nhập',bg='#ffecb4',fg='black',command=self.get_result,font='Times 15 bold',height=1,width=20)
		self.Submit.place(x=130,y=350)
		self.regis=Button(self.parent.cv,text='Đăng ký',bg='#ffecb4',fg='black',command=self.open_fun,font='Times 15 bold',height=1,width=20)
		self.regis.place(x=420,y=350)
	def child_tab(self):
		self.label_suc=Label(self.parent.cv,text="Chúc mừng bạn đã đăng nhập thành công: ")
		self.label_suc.place(x=130,y=170)
		self.logButton=Button(self.parent.cv,text='Log out',bg='#ffecb4',fg='black',command=self.log_out,font='Times 15 bold',height=1,width=20)
		self.logButton.place(x=420,y=350)
	def destroy(self):
		self.label1.destroy()
		self.label_content.destroy()
		self.AddEnt.destroy()
		self.label_content_1.destroy()
		self.PassEnt.destroy()
		self.Submit.destroy()
		self.regis.destroy()
	def get_result(self):
		self.mail=self.AddEnt.get("1.0",'end-1c')
		self.passw=self.PassEnt.get("1.0",'end-1c')
		print('mail: ',self.mail)
		print('password: ',self.passw)
		#self.destroy()
		#self.child_tab()
	def open_fun(self):
		webbrowser.open('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
	def __init__(self,wd):
		self.parent=wd
		self.login_tab()

#-----------------------------------------
WD=windown()
gui_mail=content_mail(WD)
WD.screen.mainloop()
#----------------------------------------
#success(KQ)
#KQ.screen.mainloop()
