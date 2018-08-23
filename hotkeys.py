import keyboard
import time
#import subprocess
import win32gui
from main import MainWindow

def execPatch():
    handle = win32gui.FindWindow(0, "Borderlands 2 (32-bit, DX9)")
    if (handle):
        win32gui.SetForegroundWindow(handle)
        keyboard.send('`')
        keyboard.send('e')
        keyboard.send('x')
        keyboard.send('e')
        keyboard.send('c')
        keyboard.send('space')
        keyboard.send('p')
        keyboard.send('a')
        keyboard.send('t')
        keyboard.send('c')
        keyboard.send('h')
        keyboard.send('.')
        keyboard.send('t')
        keyboard.send('x')
        keyboard.send('t')
        keyboard.send('enter')
        keyboard.send('`')
    else:
        MainWindow.errorMsg("open")

def colorblindFix():
    handle = win32gui.FindWindow(0, "Borderlands 2 (32-bit, DX9)")
    if (handle):
        keyboard.send('escape')
        time.sleep(.02)
        keyboard.send('down'); keyboard.send('down')
        keyboard.send('enter')
        time.sleep(.035)
        keyboard.send('down'); keyboard.send('down')
        keyboard.send('enter')
        time.sleep(.02)
        keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
        keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
        keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
        keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
        keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
        keyboard.send('down')
        keyboard.send('right'); keyboard.send('right')
        time.sleep(.05)
        keyboard.send('escape'); keyboard.send('escape'); keyboard.send('escape')
    else:
        MainWindow.errorMsg("open")

def reload():
    handle = win32gui.FindWindow(0, "Borderlands 2 (32-bit, DX9)")
    if (handle):
        keyboard.send('escape')
        time.sleep(.02)
        keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
        keyboard.send('enter')
        time.sleep(.05)
        keyboard.send('up')
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('enter')
        time.sleep(.05)
        keyboard.send('enter')
    else:
        MainWindow.errorMsg("open")

'''
def readOnlyReload():
    handle = win32gui.FindWindow(0, "Borderlands 2 (32-bit, DX9)")
    if (handle):
        keyboard.send('escape')
        time.sleep(.02)
        keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
        keyboard.send('enter')
        time.sleep(.05)
        keyboard.send('up')
        keyboard.send('enter')
        time.sleep(1.8)
        keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
    else:
        MainWindow.errorMsg("open")
'''

''' Used for testing
def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst

def setActiveWindow():
    appwindows = get_app_list()
    for i in appwindows:
        print(i)
'''