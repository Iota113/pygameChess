def initialize():
    counter = 0
    winner = ''
    gameOver = False
    turn_step = 0
    selection = 100
    valid_moves = []
    black_pieces = ['rook', 'knight', 'elephant', 'advisor', 'general', 'advisor', 'elephant', 
              'knight', 'rook', 'cannon', 'cannon', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (8, 0), (1, 2), (7, 2), (0, 3), (2, 3), (4, 3), (6, 3), (8, 3)]
    red_pieces = ['rook', 'knight', 'elephant', 'advisor', 'general', 'advisor', 'elephant', 
              'knight', 'rook', 'cannon', 'cannon', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    red_locations = [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9),
                   (8, 9), (1, 7), (7, 7), (0, 6), (2, 6), (4, 6), (6, 6), (8, 6)]
    captured_pieces_black = []
    captured_pieces_red = []