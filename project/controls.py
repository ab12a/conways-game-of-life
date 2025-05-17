import pygame
from utils import save_pattern, load_pattern

CELL_SIZE = 20

def handle_events(view):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, view.paused
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                view.paused = not view.paused
            elif event.key == pygame.K_c:
                view.board.clear()
            elif event.key == pygame.K_r:
                view.board.random_fill()
            elif event.key == pygame.K_n and view.paused:
                view.board.next_gen()
            elif event.key == pygame.K_s:
                save_pattern(view.board)
            elif event.key == pygame.K_l:
                load_pattern(view.board)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if view.paused:
                x, y = pygame.mouse.get_pos()
                grid_x = x // CELL_SIZE
                grid_y = y // CELL_SIZE
                if 0 <= grid_x < view.board.width and 0 <= grid_y < view.board.height:
                    view.board.toggle(grid_x, grid_y)
    return True, view.paused