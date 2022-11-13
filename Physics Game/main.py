import pygame,sys,pymunk


def create_apple(space,pos):   #created a physical body
    body =  pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC) #AN ATOM influenced by physics, (mass, inertia, body type)
    body.position = pos 
    shape = pymunk.Circle(body, 65) #radius of body of apple
    space.add(body,shape)

    return shape



def draw_apples(apples): #drawing it in pygame
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center = (pos_x, pos_y))
        screen.blit(apple_surface, apple_rect)


def static_ball(space,pos):
    body = pymunk.Body(body_type= pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body,shape)
    return shape

def draw_static_ball(balls): #draw with pygame
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (255,255,255),(pos_x,pos_y),50)





pygame.init()  #initiating pygame
screen = pygame.display.set_mode((800,800)) # creating the display surface space
clock = pygame.time.Clock() #game clock
space = pymunk.Space()
space.gravity = (0,300)  #gravity x and y axis
apple_surface = pygame.image.load('apple.png')
apples = []


balls = []
balls.append(static_ball(space,(500,500)))
balls.append(static_ball(space,(250,600)))



while True: #Game Loop
    for event in pygame.event.get(): #validating for user input
        if event.type == pygame.QUIT: #input to close the game
            pygame.quit()
            sys.exit()

        if event.type== pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))


    screen.fill((0,0,0))  #background color
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1/50)            #upfate the simulation, how fast: 0.02
    pygame.display.update()    #rendering the frame
    clock.tick(120)            #limiting the frames per second to 120
