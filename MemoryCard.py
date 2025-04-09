from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class MemoryCard(QLabel):
    def __init__(self, file_name, parent=None):
        super(MemoryCard, self).__init__(parent)

        self.__shows_back = True

        self.__ident = file_name

        self.__pixmap_back = QPixmap("card_back.png").scaledToWidth(400, Qt.TransformationMode.SmoothTransformation)
        self.__pixmap_front = QPixmap(file_name).scaledToWidth(400, Qt.TransformationMode.SmoothTransformation)

        self.setPixmap(self.__pixmap_back)

    def mousePressEvent(self, event):
        if self.__shows_back:
            self.__shows_back = False

            self.setPixmap(self.__pixmap_front)
        else:
            self.__shows_back = True

            self.setPixmap(self.__pixmap_back)
