import os
import sys
import louis

from PySide6.QtWidgets import QMainWindow, QGridLayout, QLabel, QApplication, QWidget
from PySide6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QComboBox, QSpacerItem
from PySide6.QtWidgets import QFontComboBox, QSizePolicy

def create_hspacer() -> QSpacerItem:
    return QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

class TactileSchematics(QMainWindow):
    def __init__(self, louisDataPath) -> None:
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
        hbox.addItem(create_hspacer())
        self._grid.addLayout(hbox, row, 1)
        row += 1

        self._grid.addWidget(QLabel(self.tr('Translation Table:')), row, 0)
        hbox = QHBoxLayout()
        self._tables = QComboBox()
        for tableFile in os.listdir(os.path.join(louisDataPath, 'liblouis', 'tables')):
            self._tables.addItem(tableFile)
        hbox.addWidget(self._tables)
        hbox.addItem(create_hspacer())
        self._grid.addLayout(hbox, row, 1)
        row += 1
    
    def _chooseFile(self):
        pass

if __name__ == '__main__':
    dataPath = os.path.dirname(__file__).encode('utf-8')
    if dataPath != louis.liblouis.lou_setDataPath(dataPath):
        raise Exception('Cannot configure liblouis!')

    app = QApplication([])
    window = TactileSchematics(dataPath.decode('utf-8'))
    window.show()
    sys.exit(app.exec())
