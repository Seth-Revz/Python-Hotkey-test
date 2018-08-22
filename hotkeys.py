import keyboard

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

keyboard.add_hotkey("F5", lambda: execPatch(), suppress=True)

keyboard.wait()