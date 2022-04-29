import sys

from PySide6.QtWidgets import QMainWindow, QGridLayout, QLabel, QApplication, QWidget
from PySide6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QComboBox, QSpacerItem
from PySide6.QtWidgets import QFontComboBox

def create_hspacer() -> QSpacerItem:
    return QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

class TactileSchematics(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        widget = QWidget()
        self._grid = QGridLayout(widget)
        self.setCentralWidget(widget)
        row = 0

        self._grid.addWidget(QLabel(self.tr('Input-File:')), row, 0)
        hbox = QHBoxLayout()
        self._filePath = QLineEdit(self.tr('Choose File ...'))
        self._filePath.setReadOnly(True)
        hbox.addWidget(self._filePath)
        button = QPushButton(self.tr('Choose File'))
        button.clicked.connect(self._chooseFile)
        hbox.addWidget(button)
        self._grid.addLayout(hbox, row, 1)
        row += 1

        self._grid.addWidget(QLabel(self.tr('Select-Font:')), row, 0)
        hbox = QHBoxLayout()
        self._fonts = QComboBox()
        fc = QFontComboBox()
        i = 0
        while fc.itemText(i):
            if fc.itemText(i).lower().find('braille') != -1:
                self._fonts.addItem(fc.itemText(i))
            i += 1
        hbox.addWidget(self._fonts)
        self._grid.addLayout(hbox, row, 1)
        row += 1
    
    def _chooseFile(self):
        pass

if __name__ == '__main__':
    app = QApplication([])
    window = TactileSchematics()
    window.show()
    sys.exit(app.exec())
