import sys, pygame, random

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
pipe_1 = pygame.image.load("assets/pipe.png").convert()
pipe_1 = pygame.transform.scale_by(pipe_1, .3).convert_alpha()

pipe_2 = pygame.image.load("assets/pipe.png").convert()
pipe_2 = pygame.transform.scale_by(pipe_1, .3).convert_alpha()
pipe_2 = pygame.transform.rotate(pipe_1, 180).convert_alpha()


screen.blit(bird, (width / 2, height))

# obstacle_top: pygame.Rect = pygame.Rect(0, -25, width, height/2)
# obstacle_bottom: pygame.Rect = pygame.Rect(0, height - 175, width, height/2)
# obstacle_list: list[pygame.Rect] = [obstacle_top, obstacle_bottom]


def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    bird_y = int(height / 2)
    pipe_old_y = height - (height / 2)
    pipe_x = int(width)
    # pipes = [pipe_1_top]

    while True:
        # set frame rate
        time_delta = clock.tick(20)

        #  TODO: generate pipes

        # TODO: background imagery
        # fill background with solid color
        screen.fill(LIGHT_BLUE)

        # falling bird
        bird_y += 4

        # moving pipes
        pipe_x -= 3

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
        pipe_old_y  = generate_pipes(pipe_old_y)
        # re-render
        screen.blit(bird, (width / 2, bird_y))
        screen.blit(pipe_1, (pipe_x, height / 2 + 40))
        screen.blit(pipe_2, (pipe_x, height / 2 + 40 - height))

        pygame.display.flip()


def generate_pipes(previous_pipe):
    """generate one top and bottom pipe, given the center y coordinate/passageway of previous pipe"""
    bottom = pygame.image.load("assets/pipe.png").convert()
    bottom = pygame.transform.scale_by(bottom, .3).convert_alpha()

    top  = pygame.image.load("assets/pipe.png").convert()
    top = pygame.transform.scale_by(top, .3).convert_alpha()
    top = pygame.transform.rotate(top, 180).convert_alpha()

    y = random.randint(previous_pipe - 30, previous_pipe + 30)
    screen.blit(top, (width, y))
    pygame.display.flip()
    return y


if __name__ == '__main__':
    main()