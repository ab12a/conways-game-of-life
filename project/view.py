import pygame
from controls import handle_events
from utils import save_pattern, load_pattern

CELL_SIZE = 20
COLOR_BG = (30, 30, 30)
COLOR_GRID = (50, 50, 50)
COLOR_ALIVE = (0, 200, 0)

class GameView:
    def __init__(self, board, fps=10):
        self.board = board
        self.fps = fps
        pygame.init()
        self.screen = pygame.display.set_mode((board.width * CELL_SIZE, board.height * CELL_SIZE))
        pygame.display.set_caption("Conway's Game of Life")
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = True

    def draw(self):
        self.screen.fill(COLOR_BG)
        for x in range(self.board.width):
            for y in range(self.board.height):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)
                if (x, y) in self.board.live:
                    pygame.draw.rect(self.screen, COLOR_ALIVE, rect)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.running, self.paused = handle_events(self)
            if not self.paused:
                self.board.next_gen()
            self.draw()
            self.clock.tick(self.fps)
