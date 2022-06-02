import uuid
from PIL import ImageGrab
import io
import os 
import  pickle, psutil, struct
from shutil import copyfile 
import cv2 

def mac_address():
    return hex(uuid.getnode())

def capture_screen():
    img = ImageGrab.grab()
    img.save("save_img.png")

def list_apps():
    ls1 = list()
    ls2 = list()
    ls3 = list()

    cmd = 'powershell "gps | where {$_.mainWindowTitle} | select Description, ID, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}'
    proc = os.popen(cmd).read().split('\n')
    tmp = list()
    for line in proc:
        if not line.isspace():
            tmp.append(line)
    tmp = tmp[3:]
    for line in tmp:
        try:
            arr = line.split(" ")
            if len(arr) < 3:
                continue
            if arr[0] == '' or arr[0] == ' ':
                continue

            name = arr[0]
            threads = arr[-1]
            ID = 0
            # interation
            cur = len(arr) - 2
            for i in range (cur, -1, -1):
                if len(arr[i]) != 0:
                    ID = arr[i]
                    cur = i
                    break
            for i in range (1, cur, 1):
                if len(arr[i]) != 0:
                    name += ' ' + arr[i]
            ls1.append(name)
            ls2.append(ID)
            ls3.append(threads)
        except:
            pass
    return ls1, ls2, ls3

def list_processes():
    ls1 = list()
    ls2 = list()
    ls3 = list()
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            name = proc.name()
            pid = proc.pid
            threads = proc.num_threads()
            ls1.append(str(name))
            ls2.append(str(pid))
            ls3.append(str(threads))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return ls1, ls2, ls3

def kill(pid):
    cmd = 'taskkill.exe /F /PID ' + str(pid)
    try:
        a = os.system(cmd)
        if a == 0:
            return 1
        else:
            return 0
    except:
        return 0
    
def start(name):
    os.system(name)
    return

def showTree():
    listD = []
    for c in range(ord('A'), ord('Z') + 1):
        path = chr(c) + ":\\"
        if os.path.isdir(path):
            listD.append(path)
    return listD

def sendListDirs(path):
    if not os.path.isdir(path):
        return False, []
    listT = []
    listD = os.listdir(path)
    for d in listD:
        listT.append((d, os.path.isdir(path + "\\" + d)))
    return True, listT

def delFile(path):
    if not os.path.isdir(path):
        return False,path 
    os.remove(path)
    return True, path

def copyFile(path,dst):
    if not os.path.isdir(path):
        return False,path 
    copyfile(path,dst)
    return True, dst 

def webcam():
    cam = cv2.VideoCapture(0)
    s, img = cam.read() 
    cv2.imwrite("webcam.png",img)