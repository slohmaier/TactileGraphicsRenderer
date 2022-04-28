import sys
from PySide6.QtWidgets import QMainWindow, QGridLayout, QLabel, QApplication

class TactileSchematics(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self._grid = QGridLayout()
        self.setLayout(self._grid)
        self._grid.addWidget(QLabel(self.tr('HELLO')))

if __name__ == '__main__':
    app = QApplication([])
    window = TactileSchematics()
    window.show()
    sys.exit(app.exec())
