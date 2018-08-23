import sys
import keyboard
import hotkeys
from Gui import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    
    keyboard.add_hotkey("F5", lambda: keyboard.call_later(hotkeys.execPatch), suppress=True)
    keyboard.add_hotkey("F6", lambda: keyboard.call_later(hotkeys.colorblindFix), suppress=True)
    keyboard.add_hotkey("F7", lambda: keyboard.call_later(hotkeys.reload), suppress=True)
    #keyboard.add_hotkey("F8", lambda: keyboard.call_later(hotkeys.readOnlyReload), suppress=True)
    keyboard.add_hotkey('end', lambda: app.exit(), suppress=True)
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    app.exec()