def save_pattern(board, filename='patterns.txt'):
    with open(filename, 'w') as f:
        for x, y in board.live:
            f.write(f"{x},{y}\n")

def load_pattern(board, filename='patterns.txt'):
    try:
        with open(filename) as f:
            board.live = {tuple(map(int, line.strip().split(','))) for line in f if line.strip() and not line.startswith('#')}
    except FileNotFoundError:
        pass
