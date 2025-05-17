from board import Board

def test_blinker():
    b = Board(5, 5)
    b.live = {(2, 1), (2, 2), (2, 3)}
    b.next_gen()
    assert b.live == {(1, 2), (2, 2), (3, 2)}
    b.next_gen()
    assert b.live == {(2, 1), (2, 2), (2, 3)}
