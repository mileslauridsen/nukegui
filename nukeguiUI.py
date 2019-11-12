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
        #send_layout.addLayout(send_layout_right)

        # Buttons
        self.tool01_button = QPushButton("tool01")
        self.tool02_button = QPushButton("tool02")

        tools_layout.addWidget(self.tool01_button)
        tools_layout.addWidget(self.tool02_button)

        # received_layout = QHBoxLayout()
        # received_layout_left = QVBoxLayout()
        # received_layout_left.addWidget(history_label)
        # received_layout_left.addWidget(self.history_table_widget)
        # received_action_layout = QHBoxLayout()
        # received_action_layout.addWidget(self.paste_push_button)
        # received_action_layout.addWidget(self.received_close_push_button)
        # received_layout_left.addLayout(received_action_layout)
        #
        # received_layout_right = QVBoxLayout()
        # received_layout_right.addWidget(notes_label)
        # received_layout_right.addWidget(self.received_notes_text_edit)

        # received_layout.addLayout(received_layout_left)
        # received_layout.addLayout(received_layout_right)

        self.tools_main_widget.setLayout(tools_layout)
        # self.received_main_widget.setLayout(received_layout)

        self.addTab(self.tools_main_widget, "Tools")
