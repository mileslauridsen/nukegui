# imports
import sys

try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except:
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *

from nukeguiUI import NukeguiUI


# class and defs
class NukeguiCore(NukeguiUI):
    def __init__(self):
        super(NukeguiCore, self).__init__()

        self.tool01_button.clicked.connect(self.tool01_action)
        self.tool02_button.clicked.connect(self.tool02_action)


    def tool01_action(self):
        print "tool01"


    def tool02_action(self):
        print "tool02"


def start():
    start.panel = NukeguiCore()
    start.panel.show()


app = QApplication(sys.argv)
panel = NukeguiCore()
panel.show()
app.exec_()
