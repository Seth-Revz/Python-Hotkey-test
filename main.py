import sys
import keyboard
import hotkeys

from PyQt5 import QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
MainWindow.show()

keyboard.add_hotkey("F5", lambda: keyboard.call_later(hotkeys.execPatch), suppress=True)
keyboard.add_hotkey("F6", lambda: keyboard.call_later(hotkeys.colorblindFix), suppress=True)
keyboard.add_hotkey("F7", lambda: keyboard.call_later(hotkeys.reload), suppress=True)
#keyboard.add_hotkey("F8", lambda: keyboard.call_later(hotkeys.readOnlyReload), suppress=True)
keyboard.add_hotkey('end', lambda: app.exit(), suppress=True)

app.exec()
