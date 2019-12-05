# code adapted from https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3
import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return f"{self.value}{self.suit}"

    # def show(self):
    #     print(f"{self.value}{self.suit}")

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["♠", "♥", "♣", "♦"]:
            for v in range(2,11):
                self.cards.append(Card(s, v))
            for f in ["K", "Q", "J", "A"]:
                self.cards.append(Card(s, f))

    # def show(self):
    #     for c in self.cards:
    #         c.show()

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Trials:
    def __init__(self):
        self.hand = []
        self.n = 0
        self.n_max = 20

    def __str__(self):
        return self.hand

    def draw(self, deck):
        while self.n <= self.n_max:
            self.hand.append(f"{deck.drawCard()}")
            self.n += 1
        print(self.hand)
        return self

    def count(self):
        total = []
        for card in self.hand:
            percent = self.hand.count(card) * 100/self.n_max
            total.append([card, percent])
        print(total)



deck = Deck()
deck.shuffle()
# deck.show()
# card = deck.drawCard()
# card.show()
t = Trials()
t.draw(deck)
t.count()
