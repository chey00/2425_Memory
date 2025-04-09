from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class MemoryCard(QLabel):
    def __init__(self, file_name, parent=None):
        super(MemoryCard, self).__init__(parent)

        pixmap = QPixmap(file_name).scaledToWidth(400)

        self.setPixmap(pixmap)
