from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPicture, QPixmap
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout(parent)

        picture_1 = QPixmap("cat_1.png")

        scaled_pixmap = picture_1.scaledToWidth(900, Qt.TransformationMode.FastTransformation)
        scaled_pixmap_smooth = picture_1.scaledToWidth(900, Qt.TransformationMode.SmoothTransformation)

        label_1 = QLabel(self)
        label_1.setPixmap(scaled_pixmap)
        label_2 = QLabel(self)
        label_2.setPixmap(scaled_pixmap_smooth)

        layout.addWidget(label_1, 0, 0)
        layout.addWidget(label_2, 0, 1)

        self.setLayout(layout)