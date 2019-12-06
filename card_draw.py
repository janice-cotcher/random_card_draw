# code adapted from https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3
import random
import tabulate
# import collections


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return f"{self.value}{self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["♠", "♥", "♣", "♦"]:
            for v in range(2, 11):
                self.cards.append(Card(s, v))
            for f in ["K", "Q", "J", "A"]:
                self.cards.append(Card(s, f))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Trials:
    def __init__(self):
        self.hand = []
        self.n = 0

    def __str__(self):
        return self.hand

    def draw(self, deck, n_max):
        while self.n < self.n_max:
            deck = Deck()
            deck.shuffle()
            self.hand.append(f"{deck.drawCard()}")
            self.n += 1
        print(self.hand)
        return self

    def count(self, n_max):
        deck = Deck()
        self.draw(deck, n_max)
        total = []
        stack = list(dict.fromkeys(self.hand))
        for card in stack:
            count = self.hand.count(card)
            percent = count * 100/self.n_max
            total.append([card, count, percent])
        print(tabulate.tabulate(total,
                                headers=["Card", " Count", "% Frequency"],
                                tablefmt="fancy_grid"))

    def count_input(self):
        self.n_max = int(input("How many cards would you like to draw? "))
        while True:
            try:
                self.count(self.n_max)
                break
            except ValueError:
                print("Invalid input, try again.")


t = Trials()
t.count_input()
