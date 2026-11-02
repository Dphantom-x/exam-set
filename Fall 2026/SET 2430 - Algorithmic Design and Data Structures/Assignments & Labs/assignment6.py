# Assignment 6 - Dice Battle Simulator
import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def total(self):
        return sum(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None


class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.history = []
        self.q = Queue()
        self.stack = Stack()

    def score(self):
        return self.q.total()

    def roll(self):
        val = random.randint(1, 6)
        self.history.append(val)

        if val == 6:
            self.stack.push(val)
        elif val == 1:
            if not self.q.is_empty():
                self.q.dequeue()
        else:
            self.q.enqueue(val)

        return val


def play_game():
    p = Player("Player")
    turn = 0

    while p.score() < 30:
        turn += 1
        val = p.roll()
        print(f"Turn {turn}: Rolled {val} | Queue: {p.q.items} | Score: {p.score()}")

    print(f"\nGame Over! {p.name} reached {p.score()} points in {turn} turns.")
    print(f"Complete history: {p.history}")
    print(f"Stack (banked 6s): {p.stack.items}")


# Bonus: Two-player mode
def play_two_player():
    p1 = Player("Player 1")
    p2 = Player("Player 2")
    turn = 0

    while True:
        turn += 1

        # player 1 turn
        r1 = p1.roll()
        print(f"Turn {turn} - {p1.name}: Rolled {r1} | Queue: {p1.q.items} | Score: {p1.score()}")
        if p1.score() >= 30:
            print(f"\n{p1.name} wins in {turn} turns with {p1.score()} points!")
            break

        # player 2 turn
        r2 = p2.roll()
        print(f"Turn {turn} - {p2.name}: Rolled {r2} | Queue: {p2.q.items} | Score: {p2.score()}")
        if p2.score() >= 30:
            print(f"\n{p2.name} wins in {turn} turns with {p2.score()} points!")
            break

    print(f"\n{p1.name} history: {p1.history}")
    print(f"{p2.name} history: {p2.history}")


# Big-O Analysis:
# 1. Adding to history list: O(1) amortized
# 2. Adding to queue: O(1) amortized, removing from queue: O(n)
# 3. Pushing onto stack: O(1) amortized
# 4. Calculating current score: O(k) where k is the queue size


if __name__ == '__main__':
    play_game()
