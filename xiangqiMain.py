import pygame
from xiangqiMoves import *
pygame.init()

scale = 1
WIDTH = 1000 * scale
HEIGHT = 720 * scale
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Xiangqi Time')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
board_color = (255, 198, 153)

# need to be defined outside of load_pieces as draw_pieces() uses them
piece_size = HEIGHT * 3/40
small_piece_size = piece_size * 3/4
black_images = []
small_black_images = []
red_images = []
small_red_images= []
piece_list = ['advisor', 'cannon', 'elephant', 'general', 'knight', 'pawn', 'rook'] # needed for draw_pieces and draw_captured
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

def piece_adjust(input): # used for draw_pieces
    return input * HEIGHT/10 + HEIGHT/80
def line_pos(input): # used for both draw_board() and draw_valid()
    return input * HEIGHT/10 + HEIGHT/20

# load in game pieces
def load_pieces():
    black_types = ['Black Advisor', 'Black Cannon', 'Black Elephant', 'Black General', 'Black Knight', 'Black Pawn', 'Black Rook']
    red_types = ['Red Advisor', 'Red Cannon', 'Red Elephant', 'Red General', 'Red Knight', 'Red Pawn', 'Red Rook']

    for i in range(len(black_types)):
        black_images.append(pygame.image.load('assets/xiangqi_images/' + black_types[i] + '.png')) 
        black_images[i] = pygame.transform.scale(black_images[i], (piece_size, piece_size))
        small_black_images.append(pygame.transform.scale(black_images[i], (small_piece_size, small_piece_size)))

        red_images.append(pygame.image.load('assets/xiangqi_images/' + red_types[i] + '.png')) 
        red_images[i] = pygame.transform.scale(red_images[i], (piece_size, piece_size))
        small_red_images.append(pygame.transform.scale(red_images[i], (small_piece_size, small_piece_size)))

def draw_pieces():
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        black_coord = (piece_adjust(black_locations[i][0]), piece_adjust((black_locations[i][1])))
        screen.blit(black_images[index], (black_coord))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.circle(screen, 'blue', (line_pos(black_locations[i][0]), line_pos(black_locations[i][1])), 0.57*piece_size, width=5)

    for i in range(len(red_pieces)):
        index = piece_list.index(red_pieces[i])
        red_coord = (piece_adjust(red_locations[i][0]), piece_adjust((red_locations[i][1])))
        screen.blit(red_images[index], (red_coord))
        if turn_step < 2:
            if selection == i:
                    pygame.draw.circle(screen, 'red', (line_pos(red_locations[i][0]), line_pos(red_locations[i][1])), 0.57*piece_size, width=5)

def draw_board():
    # horizontal lines
    for i in range(10):
        pygame.draw.line(screen, 'black', (line_pos(0), line_pos(i)), (line_pos(8), line_pos(i)), 2)

    # vertical lines
    pygame.draw.line(screen, 'black', (line_pos(0), line_pos(0)), (line_pos(0), line_pos(9)), 2)
    pygame.draw.line(screen, 'black', (line_pos(8), line_pos(0)), (line_pos(8), line_pos(9)), 2)
    for j in range(1, 8):
        pygame.draw.line(screen, 'black', (line_pos(j), line_pos(0)), (line_pos(j), line_pos(4)), 2)
        pygame.draw.line(screen, 'black', (line_pos(j), line_pos(5)), (line_pos(j), line_pos(9)), 2)

    # diagonal lines
    pygame.draw.line(screen, 'black', (line_pos(3), line_pos(0)), (line_pos(5), line_pos(2)), 2)
    pygame.draw.line(screen, 'black', (line_pos(5), line_pos(0)), (line_pos(3), line_pos(2)), 2)
    pygame.draw.line(screen, 'black', (line_pos(3), line_pos(9)), (line_pos(5), line_pos(7)), 2)
    pygame.draw.line(screen, 'black', (line_pos(5), line_pos(9)), (line_pos(3), line_pos(7)), 2)

    status_text = ['Red: Select a Piece!', 'Red: Select a Destination!',
                    'Black: Select a Piece!', 'Black: Select a Destination!']
    status_color = [(254, 71, 10), (77, 163, 253)]
    if not gameOver:
        screen.blit(medium_font.render(status_text[turn_step], True, status_color[turn_step//2]), (0.1*WIDTH, 0.48*HEIGHT))

# function to check all pieces valid on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        match piece:
            case 'pawn':
                moves_list = check_pawn(location, turn, black_locations, red_locations)
            case 'rook':
                moves_list = check_rook(location, turn, black_locations, red_locations)
            case 'knight':
                moves_list = check_knight(location, turn, black_locations, red_locations)
            case 'advisor':
                moves_list = check_advisor(location, turn, black_locations, red_locations)
            case 'cannon':
                moves_list = check_cannon(location, turn, black_locations, red_locations)
            case 'elephant':
                moves_list = check_elephant(location, turn, black_locations, red_locations)
            case 'general':
                moves_list = check_general(location, turn, black_locations, red_locations)
        all_moves_list.append(moves_list)
    return all_moves_list

# check for valid moves for selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = red_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        circle_center = (line_pos(moves[i][0]), line_pos(moves[i][1]))
        pygame.draw.circle(screen, color, circle_center, 7)

# draw captured pieces
def draw_captured():
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_red_images[index], ((0.68 + 0.07*(i//4))*WIDTH, (i+1-4*(i//4))*0.1*HEIGHT))
    for i in range(len(captured_pieces_red)):
        captured_piece = captured_pieces_red[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], ((0.68 + 0.07*(i//4))*WIDTH, HEIGHT-(i+1-4*(i//4))*0.1*HEIGHT))

def draw_check():
    if 'general' in red_pieces:
        general_index = red_pieces.index('general')
        general_location = red_locations[general_index]
        for i in range(len(black_options)):
            if general_location in black_options[i]:
                if counter < 15:
                    pygame.draw.circle(screen, 'dark red', [line_pos(red_locations[general_index][0]),
                                                              line_pos(red_locations[general_index][1])], 0.67*piece_size, width=5)
    if 'general' in black_pieces:
        general_index = black_pieces.index('general')
        general_location = black_locations[general_index]
        for i in range(len(red_options)):
            if general_location in red_options[i]:
                if counter < 15:
                    pygame.draw.circle(screen, 'dark blue', [line_pos(black_locations[general_index][0]),
                                                               line_pos(black_locations[general_index][1])], 0.67*piece_size, width=5)

def draw_game_over():
    winner_color = [(47, 253, 141), (12, 157, 72)]
    if winner == 'Red':
        winner_color.reverse()
    pygame.draw.rect(screen, winner_color[0], [line_pos(2.5), line_pos(4), WIDTH * 0.22, HEIGHT/10])
    screen.blit(font.render(f'{winner} won the game!', True, winner_color[1]), (line_pos(2.67), line_pos(4.1)))
    screen.blit(font.render('Press Enter to restart', True, winner_color[1]), (line_pos(2.67), line_pos(4.7)))

# main game loop
run = True
black_options = check_options(black_pieces, black_locations, 'black')
red_options = check_options(red_pieces, red_locations, 'red')

while run:
    timer.tick(fps)
    screen.fill(board_color)
    if counter <= 30:
        counter += 1
    else:
        counter = 0
    load_pieces()
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()

    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not gameOver:
            x_coord = round((event.pos[0] - HEIGHT/80) / (HEIGHT/10))
            y_coord = round((event.pos[1] - HEIGHT/80) / (HEIGHT/10))
            click_coords = (x_coord, y_coord)

            # red's turn
            if turn_step <= 1:
                if click_coords in red_locations:
                    selection = red_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    red_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_red.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'general':
                            winner = 'Red'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    red_options = check_options(red_pieces, red_locations, 'red')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

        # black's turn
        if turn_step > 1:
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in red_locations:
                        red_piece = red_locations.index(click_coords)
                        captured_pieces_black.append(red_pieces[red_piece])
                        if red_pieces[red_piece] == 'general':
                            winner = 'Black'
                        red_pieces.pop(red_piece)
                        red_locations.pop(red_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    red_options = check_options(red_pieces, red_locations, 'red')
                    turn_step = 0
                    selection = 100
                    valid_moves = []

        if event.type == pygame.KEYDOWN and gameOver: # GOOD/BIG PROBLEM
            if event.key == pygame.K_RETURN:
                black_options = check_options(black_pieces, black_locations, 'black')
                red_options = check_options(red_pieces, red_locations, 'red')
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

    if winner != '': # was in event loop?
        gameOver = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()