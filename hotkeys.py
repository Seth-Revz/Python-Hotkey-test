import keyboard
import time

def execPatch():
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

def colorblindFix():
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

def reload():
    keyboard.send('escape')
    time.sleep(.02)
    keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
    keyboard.send('enter')
    time.sleep(.05)
    keyboard.send('up')
    keyboard.send('enter')
    time.sleep(3)
    keyboard.send('enter')
    time.sleep(.05)
    keyboard.send('enter')

'''
def readOnlyReload():
    keyboard.send('escape')
    time.sleep(.02)
    keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
    keyboard.send('enter')
    time.sleep(.05)
    keyboard.send('up')
    keyboard.send('enter')
    time.sleep(1.8)
    keyboard.send('down'); keyboard.send('down'); keyboard.send('down'); keyboard.send('down')
'''

keyboard.add_hotkey("F5", lambda: keyboard.call_later(execPatch), suppress=True)
keyboard.add_hotkey("F6", lambda: keyboard.call_later(colorblindFix), suppress=True)
keyboard.add_hotkey("F7", lambda: keyboard.call_later(reload), suppress=True)
#keyboard.add_hotkey("F8", lambda: keyboard.call_later(readOnlyReload), suppress=True)

keyboard.wait('end')