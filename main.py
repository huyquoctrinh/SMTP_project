from sender import *
from receiver import *
from ui_login import * 

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import cv2

from utils import *




# sender = Sender("thaovo2962002@gmail.com","a2k46pbc")

# receiver = Receiver ("thaovo2962002@gmail.com","a2k46pbc")
# subject, content = receiver.get_mail()
# print(content)
subject = "list_process"
pid = None 
name_prog = ""
path = ""
dst = ""

if subject == "mac_address":
    mac_add = mac_address()

elif subject == "capture_screen":
    capture_screen()

elif subject == "list_app":
    l1,l2,l3 = list_apps()
    print(l1,l2,l3)

elif subject == "list_process":
    l1,l2,l3 = list_processes()
    print(l1,l2,l3)
elif subject == "kill":
    r = kill(pid)

elif subject == "start":
    start(name_prog)

elif subject == "showTree":
    listT = showTree()
    print(listT)
elif subject == "list_dir":
    listD = sendListDirs()
    print(listD)
elif subject == "delete_file":
    delFile(path)

elif subject == "copy_file":
    copyFile(path,dst)
