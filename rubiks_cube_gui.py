from rubiks_cube import *
import pygame
pygame.init()

wsx = 1280
wsy = 720

window = pygame.display.set_mode((wsx,wsy))
pygame.display.set_caption('My Cube')

def run_cube():
    run = True
    mycube = Cube(cube_pieces)
    
    while run:
        pygame.time.delay(200)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            mycube.rotate_cube('y')

        elif keys[pygame.K_DOWN]:
            mycube.rotate_cube('y')
            mycube.rotate_cube('y')
            mycube.rotate_cube('y')

        elif keys[pygame.K_LEFT]:
            mycube.rotate_cube('x')

        elif keys[pygame.K_RIGHT]:
            mycube.rotate_cube('x')
            mycube.rotate_cube('x')
            mycube.rotate_cube('x')

        elif keys[pygame.K_r]:
            mycube.rotate('R', keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT])

        elif keys[pygame.K_l]:
            mycube.rotate('L', keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT])

        elif keys[pygame.K_u]:
            mycube.rotate('U', keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT])

        elif keys[pygame.K_d]:
            mycube.rotate('D', keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT])

        elif keys[pygame.K_f]:
            mycube.rotate('F', keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT])

        elif keys[pygame.K_b]:
            mycube.rotate('B', keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT])
        
            
        redraw_pieces('z', mycube.pieces)
        pygame.display.update()

def redraw_pieces(axis,pieces):
    colors = {'red':(255,0,0), 'blue':(0,0,255), 'yellow':(255,255,0), 'green': \
              (0,255,0), 'orange': (255,165,0), 'white':(255,255,255)}
    size = 60
    seperation = size / 6
        
    for k in pieces:
        displace_x = k.get_coordinate('x')
        displace_y = k.get_coordinate('y')

        if k.get_coordinate(axis) == -1:
            color = k.get_colour(axis)
            curr_piece = pygame.Surface((size,size))
            curr_piece.fill(colors[color])
            window.blit(curr_piece,\
                        ((displace_x - (-1))*(size + seperation) - (size * 1.5 + seperation) + (wsx / 2)\
                        ,((displace_y - (-1))*(size + seperation) - (size * 1.5 + seperation) + (wsy / 2))))
run_cube()

    
