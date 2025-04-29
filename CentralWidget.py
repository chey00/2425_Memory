from PyQt6.QtCore import pyqtSlot, QTimer
from PyQt6.QtWidgets import QWidget, QGridLayout

from MemoryCard import MemoryCard

import random as rnd


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)
        self.timer = QTimer()

        self.first_card = None
        self.second_card = None

        layout = QGridLayout(parent)

        memory_cards = [MemoryCard("cat_1.png"), MemoryCard("cat_1.png"), MemoryCard("cat_2.png"),
                        MemoryCard("cat_2.png"), MemoryCard("cat_3.png"), MemoryCard("cat_3.png"),
                        MemoryCard("cat_4.png"), MemoryCard("cat_4.png")]

        rnd.shuffle(memory_cards)

        counter = 0
        for card in memory_cards:
            card.card_pressed.connect(self.card_listener)

            layout.addWidget(card, counter // 4, counter % 4)
            counter += 1

        self.setLayout(layout)

    @pyqtSlot()
    def card_listener(self):
        if self.first_card is None:
            self.first_card = self.sender()
            self.first_card.setDisabled(True)
        else:
            self.second_card = self.sender()

            if self.second_card.ident == self.first_card.ident:
                self.second_card.setDisabled(True)
                print("Paar gefunden")
            else:
                self.first_card.setDisabled(False)

                self.setDisabled(True)
                self.timer.singleShot(5 * 1000, self.flip_cards)

    @pyqtSlot()
    def flip_cards(self):
        self.first_card.flip_card()
        self.first_card = None

        self.second_card.flip_card()
        self.second_card = None

        self.setDisabled(False)
