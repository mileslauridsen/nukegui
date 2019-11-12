# Imports
try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except:
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *


class NukeguiUI(QTabWidget):
    def __init__(self):
        super(NukeguiUI, self).__init__()

        self.setWindowTitle("Miles Tools")
        self.resize(500, 600)
        self.setMinimumSize(500,600)

        # Widgets
        self.tools_main_widget = QWidget()

        # Layout
        tools_layout = QHBoxLayout()
        tools_layout_left = QVBoxLayout()

        tools_layout.addLayout(tools_layout_left)

        # Buttons
        self.tool01_button = QPushButton("tool01")
        self.tool02_button = QPushButton("tool02")

        tools_layout.addWidget(self.tool01_button)
        tools_layout.addWidget(self.tool02_button)

        self.tools_main_widget.setLayout(tools_layout)

        self.addTab(self.tools_main_widget, "Tools")
