from random import shuffle

from the_self_taught_programmer.ch14_war_cardgame.card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        # pop() 메소드는 리스트의 마지막 요소를 삭제하고 그 값을 반환함
        return self.cards.pop()

