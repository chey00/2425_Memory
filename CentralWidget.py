from PyQt6.QtWidgets import QWidget, QGridLayout

from MemoryCard import MemoryCard

import random as rnd


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout(parent)

        memory_cards = [MemoryCard("cat_1.png"), MemoryCard("cat_1.png"), MemoryCard("cat_2.png"),
                        MemoryCard("cat_2.png")]
        # memory_cards.append(MemoryCard("cat_3.png"))
        # memory_cards.append(MemoryCard("cat_3.png"))
        # memory_cards.append(MemoryCard("cat_4.png"))
        # memory_cards.append(MemoryCard("cat_4.png"))

        rnd.shuffle(memory_cards)

        counter = 0
        for card in memory_cards:
            layout.addWidget(card, counter // 4, counter % 4)
            counter += 1

        self.setLayout(layout)
