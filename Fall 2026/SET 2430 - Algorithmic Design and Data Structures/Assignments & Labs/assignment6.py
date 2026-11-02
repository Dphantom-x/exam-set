# Assignment 6 - Dice Battle Simulator
import random
from collections import deque

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.history = []
        self.q = deque()
        self.stack = []

    def score(self):
        return sum(self.q)

    def roll(self):
        val = random.randint(1, 6)
        self.history.append(val)

        if val == 6:
            self.stack.append(val)
        elif val == 1:
            if self.q:
                self.q.popleft()
        else:
            self.q.append(val)

        return val


def play_game():
    p = Player("Player")
    turn = 0

    while p.score() < 30:
        turn += 1
        val = p.roll()
        print(f"Turn {turn}: Rolled {val} | Queue: {list(p.q)} | Score: {p.score()}")

    print(f"\nGame Over! {p.name} reached {p.score()} points in {turn} turns.")
    print(f"Complete history: {p.history}")
    print(f"Stack (banked 6s): {p.stack}")


# Bonus: Two-player mode
def play_two_player():
    p1 = Player("Player 1")
    p2 = Player("Player 2")
    turn = 0

    while True:
        turn += 1

        # player 1 turn
        r1 = p1.roll()
        print(f"Turn {turn} - {p1.name}: Rolled {r1} | Queue: {list(p1.q)} | Score: {p1.score()}")
        if p1.score() >= 30:
            print(f"\n{p1.name} wins in {turn} turns with {p1.score()} points!")
            break

        # player 2 turn
        r2 = p2.roll()
        print(f"Turn {turn} - {p2.name}: Rolled {r2} | Queue: {list(p2.q)} | Score: {p2.score()}")
        if p2.score() >= 30:
            print(f"\n{p2.name} wins in {turn} turns with {p2.score()} points!")
            break

    print(f"\n{p1.name} history: {p1.history}")
    print(f"{p2.name} history: {p2.history}")


# Big-O Analysis:
# 1. Adding to history list: O(1) amortized (appending to dynamic array)
# 2. Queue add/remove: O(1) (deque append and popleft operate in constant time)
# 3. Pushing onto stack: O(1) amortized (list append adds to the top)
# 4. Calculating current score: O(k) where k is the queue size (sum of queue elements)


if __name__ == '__main__':
    play_game()
