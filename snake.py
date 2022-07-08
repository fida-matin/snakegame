import pygame       # import game interface
# import time         import time for delays
import random       # import random for placing food
# create snake game
pygame.init()
# initialise colours
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
brown = (85, 0, 0)
# initialise box
displayWidth = 600
displayHeight = 400
# create screen
dis = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Snake Game by Fida')

# use clock to differentiate inputs and determine speed
clock = pygame.time.Clock()

snakeSpeed = 15     # speed of snake
snakeBlock = 10     # determines the increment of snake movement as well as dimension of snake

# set font for messages
fontStyle = pygame.font.SysFont("bahnschrift", 40)
scoreFont = pygame.font.SysFont("bahnschrift", 25)


# score tracker
def keep_score(score, colour):
    val = scoreFont.render("Your Score: " + str(score), True, colour)
    dis.blit(val, [0, 0])


# create tail for snake
def sneakysnake(block, snakeList):
    for bit in snakeList:
        pygame.draw.rect(dis, green, [bit[0], bit[1], block, block])


# set up for writing messages on screen
def message(msg, colour):
    chat = fontStyle.render(msg, True, colour)
    dis.blit(chat, [10, displayHeight/2.5])


def looper():
    game_over = False
    game_close = False
    # x and y keep track of the snake location
    x = displayWidth / 2
    y = displayHeight / 2
    # keeps track of the change in location
    x_change = 0
    y_change = 0

    snakeList = []
    snakeLength = 1

    foodX = round(random.randrange(0, displayWidth - snakeBlock) / 10.0) * 10.0
    foodY = round(random.randrange(0, (displayHeight-25) - snakeBlock) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(green)
            message("Game Over! Press Q -Quit or C -Play Again", black)
            keep_score(snakeLength - 1, blue)
            pygame.display.update()

            for event in pygame.event.get():
                # check for quit
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                # check for option user picked
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        looper()

        for event in pygame.event.get():
            # check for quit
            if event.type == pygame.QUIT:
                game_over = True
            # keyboard response if-statements
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -snakeBlock  # move left by 10
                    y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = snakeBlock  # move right by 10
                    y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    x_change = 0
                    y_change = -snakeBlock  # move up by 10
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x_change = 0
                    y_change = snakeBlock   # move down by 10

        # if x or y is outside of display finish game
        if x >= displayWidth or x < 0 or y >= displayHeight or y < 25:
            game_close = True
        # add all changes to location coordinates
        x += x_change
        y += y_change
        dis.fill(blue)  # fill screen as blue
        # entered as [x-coordinate, y-coordinate, width, length]
        # draw food as brown
        pygame.draw.rect(dis, brown, [foodX, foodY, snakeBlock, snakeBlock])
        pygame.draw.rect(dis, black, [0, 25, displayWidth, displayHeight - 25], 4)

        # create head of snake
        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        # add head of snake to rest of body
        snakeList.append(snakeHead)
        # if snake length is shorter than list, snake if just moving not getting bigger
        if len(snakeList) > snakeLength:
            del snakeList[0]
        # check if head is hitting any other part of snake
        for bit in snakeList[:-1]:
            if bit == snakeHead:
                game_close = True

        # draw full snake every time
        sneakysnake(snakeBlock, snakeList)
        # display score
        keep_score(snakeLength - 1, yellow)

        # update display
        pygame.display.update()

        if x == foodX and y == foodY:
            foodX = round(random.randrange(0, displayWidth - snakeBlock) / 10.0) * 10.0
            foodY = round(random.randrange(0, displayHeight - snakeBlock) / 10.0) * 10.0
            snakeLength += 1

        # clock ticks over so more input can be taken in
        clock.tick(snakeSpeed)

    pygame.quit()
    quit()


# runs the actual game
looper()
