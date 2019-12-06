# code adapted from https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3
import random
# import tabulate
import pandas as pd
# import collections


class Card:
    """Define the suit and value of the card"""
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return f"{self.value}{self.suit}"


class Deck:
    """Define the deck of 52 cards"""
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """Build the deck of cards"""
        for s in ["♠", "♥", "♣", "♦"]:
            for v in range(2, 11):
                self.cards.append(Card(s, v))
            for f in ["K", "Q", "J", "A"]:
                self.cards.append(Card(s, f))

    def shuffle(self):
        """Shuffle the deck of cards"""
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        """Draw a single card"""
        return self.cards.pop()


class Trials:
    """Chose the number of trials"""
    def __init__(self):
        self.hand = []
        self.n = 0

    def __str__(self):
        return self.hand

    def draw(self, deck, n_max):
        """Draw a card and then replace and shuffle"""
        while self.n < self.n_max:
            deck = Deck()
            deck.shuffle()
            self.hand.append(f"{deck.drawCard()}")
            self.n += 1
        print(self.hand)
        return self

    def count(self, n_max):
        """Count the number of cards of each type and
        output the results to a csv file
        """
        deck = Deck()
        self.draw(deck, n_max)
        total = []
        stack = list(dict.fromkeys(self.hand))
        for card in stack:
            count = self.hand.count(card)
            percent = count * 100/self.n_max
            total.append([card, count, percent])
        # print(tabulate.tabulate(total,
        #                         headers=["Card", " Count", "% Frequency"],
        #                         tablefmt="fancy_grid"))
        df = pd.DataFrame([[i[0], i[1], i[2]] for i in total],
                  columns=['Cards', 'Count', '% Frequency'])

        df.to_csv('file.csv', index=False)

    def count_input(self):
        """Ask the user how many trials they want to run"""
        self.n_max = int(input("How many cards would you like to draw? "))
        while True:
            try:
                self.count(self.n_max)
                break
            except ValueError:
                print("Invalid input, try again.")


t = Trials()
t.count_input()
