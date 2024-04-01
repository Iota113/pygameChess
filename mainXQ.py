import pygame

pygame.init()
scale = 1
WIDTH = 1000 * scale
HEIGHT = 900 * scale
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Xiangqi')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

black_pieces = ['rook', 'knight', 'elephant', 'advisor', 'general', 'advisor', 'elephant', 
              'knight', 'rook', 'cannon', 'cannon', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (8, 0), (1, 2), (7, 2), (0, 4), (2, 4), (4, 4), (6, 4), (8, 4)]
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
black_advisor = pygame.image.load('assets/xiangqi_images/Black Advisor.png')
black_advisor = pygame.transform.scale(black_advisor, (80, 80))
black_advisor_small = pygame.transform.scale(black_advisor, (45, 45))
black_cannon = pygame.image.load('assets/xiangqi_images/Black Cannon.png')
black_cannon = pygame.transform.scale(black_cannon, (80, 80))
black_cannon_small = pygame.transform.scale(black_cannon, (45, 45))
black_elephant = pygame.image.load('assets/xiangqi_images/Black Elephant.png')
black_elephant = pygame.transform.scale(black_elephant, (80, 80))
black_elephant_small = pygame.transform.scale(black_elephant, (45, 45))
black_general = pygame.image.load('assets/xiangqi_images/Black General.png')
black_general = pygame.transform.scale(black_general, (80, 80))
black_general_small = pygame.transform.scale(black_general, (45, 45))
black_knight = pygame.image.load('assets/xiangqi_images/Black Knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/xiangqi_images/Black Pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (80,80))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
black_rook = pygame.image.load('assets/xiangqi_images/Black Rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

red_advisor = pygame.image.load('assets/xiangqi_images/Red Advisor.png')
red_advisor = pygame.transform.scale(red_advisor, (80, 80))
red_advisor_small = pygame.transform.scale(red_advisor, (45, 45))
red_cannon = pygame.image.load('assets/xiangqi_images/Red Cannon.png')
red_cannon = pygame.transform.scale(red_cannon, (80, 80))
red_cannon_small = pygame.transform.scale(red_cannon, (45, 45))
red_elephant = pygame.image.load('assets/xiangqi_images/Red Elephant.png')
red_elephant = pygame.transform.scale(red_elephant, (80, 80))
red_elephant_small = pygame.transform.scale(red_elephant, (45, 45))
red_general = pygame.image.load('assets/xiangqi_images/Red General.png')
red_general = pygame.transform.scale(red_general, (80, 80))
red_general_small = pygame.transform.scale(red_general, (45, 45))
red_knight = pygame.image.load('assets/xiangqi_images/Red Knight.png')
red_knight = pygame.transform.scale(red_knight, (80, 80))
red_knight_small = pygame.transform.scale(red_knight, (45, 45))
red_pawn = pygame.image.load('assets/xiangqi_images/Red Pawn.png')
red_pawn = pygame.transform.scale(red_pawn, (80,80))
red_pawn_small = pygame.transform.scale(red_pawn, (45, 45))
red_rook = pygame.image.load('assets/xiangqi_images/Red Rook.png')
red_rook = pygame.transform.scale(red_rook, (80, 80))
red_rook_small = pygame.transform.scale(red_rook, (45, 45))

black_images= [black_advisor, black_cannon, black_elephant, black_general, black_knight,
               black_pawn, black_rook]
small_black_images= [black_advisor_small, black_cannon_small, black_elephant_small, black_general, 
                     black_knight_small, black_pawn_small, black_rook_small]
red_images= [red_advisor, red_cannon, red_elephant, red_general, red_knight,
            red_pawn, red_rook]
small_red_images= [red_advisor_small, red_cannon_small, red_elephant_small, red_general, 
                   red_knight_small, red_pawn_small, red_rook_small]

piece_list = ['advisor', 'cannon', 'elephant', 'general', 'knight', 'pawn', 'rook']

def draw_board():
    for i in range()



# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill((255, 198, 153))

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()