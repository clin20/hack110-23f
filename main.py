import sys, pygame

# screen size
size = width, height = 640, 480

# constants
LIGHT_BLUE = (51, 153, 255)

# screen and clock objects
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
score = 0

# bird
bird = pygame.image.load("assets/bird.png")
bird = pygame.transform.scale_by(bird, .1).convert_alpha()
screen.blit(bird, (width / 2, height / 2))

# obstacle rectangle objects
pipe_1_top = pygame.image.load("assets/pipe.png").convert()
pipe_1_top = pygame.transform.scale_by(pipe_1_top, .3).convert_alpha()
screen.blit(bird, (width / 2, height))

# obstacle_top: pygame.Rect = pygame.Rect(0, -25, width, height/2)
# obstacle_bottom: pygame.Rect = pygame.Rect(0, height - 175, width, height/2)
# obstacle_list: list[pygame.Rect] = [obstacle_top, obstacle_bottom]


def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    bird_y = int(height / 2)
    
    while True:
        # set frame rate
        time_delta = clock.tick(20)

        # TODO: background imagery
        # fill background with solid color
        screen.fill(LIGHT_BLUE)

        # falling bird
        bird_y += 4

        # pygame boilerplate for handling keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # pygame.transform.rotate(bird, 25)
                # TODO: fly animation
                bird_y -= 30 
                screen.blit(bird, (width / 2, bird_y))
                pygame.display.flip()

        # TODO: obstacle collision
        # for obstacle in obstacle_list:
        #     if bird.colliderect(obstacle):
        #         print("whomp whomp.")
        #         sys.exit()

        # re-render
        screen.blit(bird, (width / 2, bird_y))
        screen.blit(pipe_1_top, (width / 2, height / 2 + 40))
        pygame.display.flip()


if __name__ == '__main__':
    main()