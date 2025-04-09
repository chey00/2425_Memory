from PyQt6.QtWidgets import QWidget, QGridLayout

from MemoryCard import MemoryCard


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout(parent)

        memory_card_1 = MemoryCard("cat_1.png")
        memory_card_2 = MemoryCard("cat_2.png")
        memory_card_3 = MemoryCard("cat_3.png")
        memory_card_4 = MemoryCard("cat_4.png")

        layout.addWidget(memory_card_1, 0, 0)
        layout.addWidget(memory_card_2, 0, 1)
        layout.addWidget(memory_card_3, 0, 2)
        layout.addWidget(memory_card_4, 0, 3)

        self.setLayout(layout)
