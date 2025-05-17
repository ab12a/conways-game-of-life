
import random

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.live = set()

    def toggle(self, x, y):
        self.live ^= {(x, y)}

    def random_fill(self):
        self.live = {(x, y) for x in range(self.width) for y in range(self.height) if random.random() < 0.2}

    def clear(self):
        self.live = set()

    def next_gen(self):
        from collections import Counter
        counts = Counter((nx, ny)
            for (x, y) in self.live
            for nx in range(x-1, x+2)
            for ny in range(y-1, y+2)
            if (nx, ny) != (x, y))

        self.live = {pt for pt, c in counts.items() if c == 3 or (c == 2 and pt in self.live)}
