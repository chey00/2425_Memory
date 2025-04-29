from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class MemoryCard(QLabel):
    card_pressed = pyqtSignal()

    def __init__(self, file_name, parent=None):
        super(MemoryCard, self).__init__(parent)

        self.__shows_back = True

        self.ident = file_name

        self.__pixmap_back = QPixmap("card_back.png").scaledToWidth(400, Qt.TransformationMode.SmoothTransformation)
        self.__pixmap_front = QPixmap(file_name).scaledToWidth(400, Qt.TransformationMode.SmoothTransformation)

        self.setPixmap(self.__pixmap_back)

    def mousePressEvent(self, event):
        self.flip_card()

        self.card_pressed.emit()

    def flip_card(self):
        if self.__shows_back:
            self.__shows_back = False

            self.setPixmap(self.__pixmap_front)
        else:
            self.__shows_back = True

            self.setPixmap(self.__pixmap_back)
