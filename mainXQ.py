import pygame

pygame.init()
scale = 1
WIDTH = 1000 * scale
HEIGHT = 720 * scale
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Xiangqi')
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

# load in game pieces
piece_size = HEIGHT * 3/40
small_piece_size = piece_size * 3/4
black_advisor = pygame.image.load('assets/xiangqi_images/Black Advisor.png')
black_advisor = pygame.transform.scale(black_advisor, (piece_size, piece_size))
black_advisor_small = pygame.transform.scale(black_advisor, (small_piece_size, small_piece_size))
black_cannon = pygame.image.load('assets/xiangqi_images/Black Cannon.png')
black_cannon = pygame.transform.scale(black_cannon, (piece_size, piece_size))
black_cannon_small = pygame.transform.scale(black_cannon, (small_piece_size, small_piece_size))
black_elephant = pygame.image.load('assets/xiangqi_images/Black Elephant.png')
black_elephant = pygame.transform.scale(black_elephant, (piece_size, piece_size))
black_elephant_small = pygame.transform.scale(black_elephant, (small_piece_size, small_piece_size))
black_general = pygame.image.load('assets/xiangqi_images/Black General.png')
black_general = pygame.transform.scale(black_general, (piece_size, piece_size))
black_general_small = pygame.transform.scale(black_general, (small_piece_size, small_piece_size))
black_knight = pygame.image.load('assets/xiangqi_images/Black Knight.png')
black_knight = pygame.transform.scale(black_knight, (piece_size, piece_size))
black_knight_small = pygame.transform.scale(black_knight, (small_piece_size, small_piece_size))
black_pawn = pygame.image.load('assets/xiangqi_images/Black Pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (piece_size, piece_size))
black_pawn_small = pygame.transform.scale(black_pawn, (small_piece_size, small_piece_size))
black_rook = pygame.image.load('assets/xiangqi_images/Black Rook.png')
black_rook = pygame.transform.scale(black_rook, (piece_size, piece_size))
black_rook_small = pygame.transform.scale(black_rook, (small_piece_size, small_piece_size))

red_advisor = pygame.image.load('assets/xiangqi_images/Red Advisor.png')
red_advisor = pygame.transform.scale(red_advisor, (piece_size, piece_size))
red_advisor_small = pygame.transform.scale(red_advisor, (small_piece_size, small_piece_size))
red_cannon = pygame.image.load('assets/xiangqi_images/Red Cannon.png')
red_cannon = pygame.transform.scale(red_cannon, (piece_size, piece_size))
red_cannon_small = pygame.transform.scale(red_cannon, (small_piece_size, small_piece_size))
red_elephant = pygame.image.load('assets/xiangqi_images/Red Elephant.png')
red_elephant = pygame.transform.scale(red_elephant, (piece_size, piece_size))
red_elephant_small = pygame.transform.scale(red_elephant, (small_piece_size, small_piece_size))
red_general = pygame.image.load('assets/xiangqi_images/Red General.png')
red_general = pygame.transform.scale(red_general, (piece_size, piece_size))
red_general_small = pygame.transform.scale(red_general, (small_piece_size, small_piece_size))
red_knight = pygame.image.load('assets/xiangqi_images/Red Knight.png')
red_knight = pygame.transform.scale(red_knight, (piece_size, piece_size))
red_knight_small = pygame.transform.scale(red_knight, (small_piece_size, small_piece_size))
red_pawn = pygame.image.load('assets/xiangqi_images/Red Pawn.png')
red_pawn = pygame.transform.scale(red_pawn, (piece_size,piece_size))
red_pawn_small = pygame.transform.scale(red_pawn, (small_piece_size, small_piece_size))
red_rook = pygame.image.load('assets/xiangqi_images/Red Rook.png')
red_rook = pygame.transform.scale(red_rook, (piece_size, piece_size))
red_rook_small = pygame.transform.scale(red_rook, (small_piece_size, small_piece_size))


black_images= [black_advisor, black_cannon, black_elephant, black_general, black_knight,
               black_pawn, black_rook]
small_black_images= [black_advisor_small, black_cannon_small, black_elephant_small, black_general, 
                     black_knight_small, black_pawn_small, black_rook_small]
red_images= [red_advisor, red_cannon, red_elephant, red_general, red_knight,
            red_pawn, red_rook]
small_red_images= [red_advisor_small, red_cannon_small, red_elephant_small, red_general, 
                   red_knight_small, red_pawn_small, red_rook_small]

piece_list = ['advisor', 'cannon', 'elephant', 'general', 'knight', 'pawn', 'rook']

def draw_pieces():
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        screen.blit(black_images[index], (black_locations[i][0] * HEIGHT/10 + HEIGHT/80, black_locations[i][1] * HEIGHT/10 + HEIGHT/80))

    for i in range(len(red_pieces)):
        index = piece_list.index(red_pieces[i])
        screen.blit(red_images[index], (red_locations[i][0] * HEIGHT/10 + HEIGHT/80, red_locations[i][1] * HEIGHT/10 + HEIGHT/80))

def draw_board():
    row = 0
    column = 0
    for i in range(10):
        # horizontal lines
        pygame.draw.line(screen, 'black', (HEIGHT/19, i * HEIGHT/10 + HEIGHT/20), (8 * HEIGHT/10 + HEIGHT/20, i * HEIGHT/10 + HEIGHT/20), 2)

    # vertical lines
    pygame.draw.line(screen, 'black', (HEIGHT/20, HEIGHT/25), (HEIGHT/20, 9 * HEIGHT/10 + HEIGHT/20), 2)
    pygame.draw.line(screen, 'black', (8 * HEIGHT/10 + HEIGHT/20, HEIGHT/25), (8 * HEIGHT/10 + HEIGHT/20, 9 * HEIGHT/10 + HEIGHT/20), 2)
    for j in range(1, 8):
        pygame.draw.line(screen, 'black', (j * HEIGHT/10 + HEIGHT/20, HEIGHT/25), (j * HEIGHT/10 + HEIGHT/20, 4 * HEIGHT/10 + HEIGHT/20), 2)
        pygame.draw.line(screen, 'black', (j * HEIGHT/10 + HEIGHT/20, 5 * HEIGHT/10 + HEIGHT/20), (j * HEIGHT/10 + HEIGHT/20, 9 * HEIGHT/10 + HEIGHT/15), 2)


# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill(board_color)
    draw_board()
    draw_pieces()

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()