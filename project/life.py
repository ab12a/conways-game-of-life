
import argparse
from board import Board
from view import GameView

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int, default=60)
    parser.add_argument('--height', type=int, default=30)
    parser.add_argument('--fps', type=int, default=10)
    args = parser.parse_args()

    board = Board(args.width, args.height)
    view = GameView(board, fps=args.fps)
    view.run()

if __name__ == '__main__':
    main()