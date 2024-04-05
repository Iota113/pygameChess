import pygame

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

turn_step = 0
selection = 100
valid_moves = []

# need to be defined outside of load_pieces as draw_pieces() uses them
piece_size = HEIGHT * 3/40
small_piece_size = piece_size * 3/4
black_images = []
small_black_images = []
red_images = []
small_red_images= []

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

piece_list = ['advisor', 'cannon', 'elephant', 'general', 'knight', 'pawn', 'rook'] # maybe can put in draw_pieces?

def piece_adjust(input): # used for draw_pieces
    return input * HEIGHT/10 + HEIGHT/80
def line_pos(input): # used for both draw_board() and draw_valid()
    return input * HEIGHT/10 + HEIGHT/20

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

    status_text = ['Red: Select a Piece to Move!', 'Red: Select a Destination!',
                    'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(medium_font.render(status_text[turn_step], True, 'black'), (0.042*WIDTH, 0.48*HEIGHT))

def check_pawn(position, color):
    moves_list = []
    if color == 'black':
        if (position[0], position[1] + 1) not in black_locations and position[1] + 1 <= 9:
            moves_list.append((position[0], position[1] + 1))
        if position[1] >= 5:
            if (position[0] + 1, position[1]) not in black_locations and position[0] + 1 <= 8:
                moves_list.append((position[0] + 1, position[1]))
            if (position[0] - 1, position[1]) not in black_locations and position[0] - 1 >= 0:
                moves_list.append((position[0] - 1, position[1]))
    elif color == "red":
        if (position[0], position[1] - 1) not in red_locations and position[1] - 1 >= 0:
            moves_list.append((position[0], position[1] - 1))
        if position[1] <= 4:
            if (position[0] + 1, position[1]) not in red_locations and position[0] + 1 <= 8:
                moves_list.append((position[0] + 1, position[1]))
            if (position[0] - 1, position[1]) not in red_locations and position[0] - 1 >= 0:
                moves_list.append((position[0] - 1, position[1]))
    return moves_list

def check_rook(position, color):
    moves_list = []
    if color == 'black':
        friends_list, enemies_list = black_locations, red_locations
    else:
        friends_list, enemies_list = red_locations, black_locations

    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x, y = -1, 0
        elif i == 1:
            x, y = 1, 0
        elif i == 2:
            x, y = 0, 1
        elif i == 3:
            x, y = 0, -1
        while path: 
            if (position[0] + chain * x, position[1] + chain * y) not in friends_list and 0 <= position[0] + chain * x <= 8 and 0 <= position[1] + chain * y <= 9:
                moves_list.append((position[0] + chain * x, position[1] + chain * y))
                if (position[0] + chain * x, position[1] + chain * y) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
        
    return moves_list

def check_knight(position, color):
    moves_list = []
    if color == 'black':
        friends_list = black_locations
    else:
        friends_list = red_locations

    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]
    blockages = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        blockage = (position[0] + blockages[i//2][0], position[1] + blockages[i//2][1])
        if target not in friends_list and 0 <= target[0] <= 8 and 0 <= target[1] <= 9 and blockage not in (red_locations + black_locations):
            moves_list.append(target)
    return moves_list

def check_advisor(position, color):
    moves_list = []
    if color == 'black':
        friends_list = black_locations
        box = [(3, 0), (5, 0), (3, 2), (5,2), (4, 1)]
    else:
        friends_list = red_locations
        box = [(3, 9), (3, 7), (5, 9), (5,7), (4, 8)]
    
    targets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(4):
        coord = (position[0] + targets[i][0], position[1] + targets[i][1]) 
        if coord not in friends_list and coord in box:
            moves_list.append(coord)

    return moves_list

def check_cannon(position, color):
    moves_list = []
    if color == 'black':
        friends_list, enemies_list = black_locations, red_locations
    else:
        friends_list, enemies_list = red_locations, black_locations

    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x, y = -1, 0
        elif i == 1:
            x, y = 1, 0
        elif i == 2:
            x, y = 0, 1
        elif i == 3:
            x, y = 0, -1
        while path:
            if 0 <= position[0] + chain * x <= 8 and 0 <= position[1] + chain * y <= 9:
                if (position[0] + chain * x, position[1] + chain * y) not in (friends_list + enemies_list):
                    moves_list.append((position[0] + chain * x, position[1] + chain * y))
                    chain += 1
                else:
                    for j in range(1, 9):
                        if (position[0] + (chain + j) * x, position[1] + (chain + j) * y) in enemies_list:
                            moves_list.append((position[0] + (chain + j) * x, position[1] + (chain + j) * y))
                            break
                    path = False
            else: 
                path = False

 
    return moves_list

def check_elephant(position, color):
    moves_list = []
    if color == 'black':
        friends_list = black_locations
        box = [(2, 0), (0, 2), (2, 4), (4, 2), (6, 0), (8, 2), (6, 4)]
    else:
        friends_list = red_locations
        box = [(2, 9), (0, 7), (2, 5), (4, 7), (6, 9), (8, 7), (6, 5)]
    
    targets = [(2, 2), (-2, -2), (2, -2), (-2, 2)]
    blockages = [(0.5*x, 0.5*y) for (x,y) in targets]
    for i in range(4):
        coord = (position[0] + targets[i][0], position[1] + targets[i][1]) 
        blockage = (position[0] + blockages[i][0], position[1] + blockages[i][1]) 
        if coord not in friends_list and coord in box and blockage not in (red_locations + black_locations):
            moves_list.append(coord)

    return moves_list


def check_general(position, color):
    moves_list = []
    if color == 'black':
        friends_list = black_locations
        box = [(3, 0), (4, 0), (5, 0), (3, 1), (4, 1), (5, 1), (3, 2), (4, 2), (5, 2)]
    else:
        friends_list = red_locations
        box = [(3, 9), (4, 9), (5, 9), (3, 8), (4, 8), (5, 8), (3,7), (4,7), (5,7)]
    
    targets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(4):
        coord = (position[0] + targets[i][0], position[1] + targets[i][1]) 
        if coord not in friends_list and coord in box:
            moves_list.append(coord)

    return moves_list

# function to check all pieces valid on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        match piece:
            case 'pawn':
                moves_list = check_pawn(location, turn)
            case 'rook':
                moves_list = check_rook(location, turn)
            case 'knight':
                moves_list = check_knight(location, turn)
            case 'advisor':
                moves_list = check_advisor(location, turn)
            case 'cannon':
                moves_list = check_cannon(location, turn)
            case 'elephant':
                moves_list = check_elephant(location, turn)
            case 'general':
                moves_list = check_general(location, turn)
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

# main game loop
black_options = check_options(black_pieces, black_locations, 'black')
red_options = check_options(red_pieces, red_locations, 'red')
run = True
while run:
    timer.tick(fps)
    screen.fill(board_color)
    load_pieces()
    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
                        red_pieces.pop(red_piece)
                        red_locations.pop(red_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    red_options = check_options(red_pieces, red_locations, 'red')
                    turn_step = 0
                    selection = 100
                    valid_moves = []

    pygame.display.flip()
pygame.quit()