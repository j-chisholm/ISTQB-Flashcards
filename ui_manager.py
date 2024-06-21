# UI Manager
# Handles events and displaying the window

import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

class UIManager:

    def __init__(self):
        pass

    # defines window parameters and show window
    def window(self):
        app = QApplication(sys.argv)

        # define window parameters
        win = QMainWindow()
        win.setGeometry(0, 0, 640, 480)
        win.setWindowTitle("CTFL Flash Cards")

        # display window
        win.show()

        # close the application and exit
        sys.exit(app.exec())

ui = UIManager()
ui.window()