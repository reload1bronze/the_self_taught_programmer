from the_self_taught_programmer.ch14_war_cardgame.deck import Deck
from the_self_taught_programmer.ch14_war_cardgame.player import Player


class Game:
    def __init__(self):
        name1 = input("p1 name: ")
        name2 = input("p2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {}, {} drew {}."
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        card = self.deck.cards
        print("beginning War!")
        while len(card) >= 2:
            m = "q to quit. Any key to play:"
            response = input(m)
            if response == 'q':
                break
            # p1c = card.pop()
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("War is over. {}".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return "{} wins".format(p1.name)
        if p1.wins < p2.wins:
            return "{} wins".format(p2.name)
        else:
            return "It was a tie!"


game = Game()
game.play_game()
