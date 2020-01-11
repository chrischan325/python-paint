import sys, pygame
from pygame.math import Vector2

pygame.init()
win = pygame.display.set_mode((1000, 700))
white = [255, 255, 255]
win.fill(white)
pygame.display.set_caption('Python_Paint')

w, h = pygame.display.get_surface().get_size()
paint = False
last_pos = (0, 0)
x = 50
y = 400
width = 35
height = 35
radius = 1
run = True
gray = [158, 128, 158]
black = [0, 0, 0]
colour = [0, 0, 0]
green = [0, 255, 0]
red = [255, 0, 0]
aqua = [0, 128, 128]
orange = [255, 165, 0]
yellow = [255, 255, 0]
navy = [0, 0, 128]
purple = [128, 0, 128]
brown = [139, 69, 19]


def fill(screen, color, start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + int(i) / distance * dx)
        y = int(start[1] + int(i) / distance * dy)
        pygame.draw.circle(screen, color, (x, y), radius)


bar = pygame.draw.rect(win, gray, [0, 0, 220, 700])
red_rect = pygame.draw.rect(win, red, [50, 100, width, height])
green_rect = pygame.draw.rect(win, green, [90, 100, width, height])
aqua_rect = pygame.draw.rect(win, aqua, [130, 100, width, height])
orange_rect = pygame.draw.rect(win, orange, [50, 140, width - 2, height - 2])
yellow_rect = pygame.draw.rect(win, yellow, [90, 140, width - 2, height - 2])
black_rect = pygame.draw.rect(win, black, [130, 140, width - 2, height - 2])
navy_rect = pygame.draw.rect(win, navy, [50, 180, width - 2, height - 2])
purple_rect = pygame.draw.rect(win, purple, [90, 180, width - 2, height - 2])
brown_rect = pygame.draw.rect(win, brown, [130, 180, width - 2, height - 2])


pygame.draw.line(win, black, [20, 280], [200, 280], 2)
scroll = pygame.draw.rect(win, black, [20, 272, 8, 18])
save = pygame.draw.rect(win, white, [65, 330, 85, height])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


while run:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bar.left + 220 > mouse[0] > bar.left and bar.top + 700 > mouse[1] > bar.top:
                paint = False
            else:
                paint = True
                w, z = pygame.mouse.get_pos()
                pygame.draw.circle(win, colour, pygame.mouse.get_pos(), radius)
                pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            paint = False
        if event.type == pygame.MOUSEMOTION:
            if bar.left + 220 > mouse[0] > bar.left and bar.top + 700 > mouse[1] > bar.top:
                paint = False
            if paint:
                w, z = pygame.mouse.get_pos()
                pygame.draw.circle(win, colour, pygame.mouse.get_pos(), radius)
                fill(win, colour, pygame.mouse.get_pos(), last_pos)
            last_pos = pygame.mouse.get_pos()
            pygame.display.update()
        if red_rect.left + width > mouse[0] > red_rect.left and red_rect.top + height > mouse[1] > red_rect.top:
            pygame.draw.rect(win, black, [red_rect.left - 2, red_rect.top - 2, width + 1, height + 2], 2)
            if click[0] == 1:
                colour = red
        else:
            pygame.draw.rect(win, gray, [red_rect.left - 2, red_rect.top - 2, width + 1, height + 2], 2)
        if aqua_rect.left + width > mouse[0] > aqua_rect.left and aqua_rect.top + height > mouse[1] > aqua_rect.top:
            pygame.draw.rect(win, black, [aqua_rect.left - 2, aqua_rect.top - 2, width + 1, height + 2], 2)
            if click[0] == 1:
                colour = aqua
        else:
            pygame.draw.rect(win, gray, [aqua_rect.left - 2, aqua_rect.top - 2, width + 1, height + 2], 2)
        if green_rect.left + width > mouse[0] > green_rect.left and green_rect.top + height > mouse[1] > green_rect.top:
            pygame.draw.rect(win, black, [green_rect.left - 2, green_rect.top - 2, width + 1, height + 2], 2)
            if click[0] == 1:
                colour = green
        else:
            pygame.draw.rect(win, gray, [green_rect.left - 2, green_rect.top - 2, width + 1, height + 2], 2)
        if orange_rect.left + width > mouse[0] > orange_rect.left and orange_rect.top + height > mouse[
            1] > orange_rect.top:
            pygame.draw.rect(win, black, [orange_rect.left - 2, orange_rect.top - 2, width + 1, height + 1], 2)
            if click[0] == 1:
                colour = orange
        else:
            pygame.draw.rect(win, gray, [orange_rect.left - 2, orange_rect.top - 2, width + 1, height + 1], 2)
        if yellow_rect.left + width > mouse[0] > yellow_rect.left and yellow_rect.top + height > mouse[
            1] > yellow_rect.top:
            pygame.draw.rect(win, black, [yellow_rect.left - 2, yellow_rect.top - 2, width + 1, height + 1], 2)
            if click[0] == 1:
                colour = yellow
        else:
            pygame.draw.rect(win, gray, [yellow_rect.left - 2, yellow_rect.top - 2, width + 1, height + 1], 2)
        if black_rect.left + width > mouse[0] > black_rect.left and black_rect.top + height > mouse[1] > black_rect.top:
            pygame.draw.rect(win, white, [black_rect.left - 2, black_rect.top - 2, width + 1, height + 1], 2)
            if click[0] == 1:
                colour = black
        else:
            pygame.draw.rect(win, gray, [black_rect.left - 2, black_rect.top - 2, width + 1, height + 1], 2)
        if navy_rect.left + width > mouse[0] > navy_rect.left and navy_rect.top + height > mouse[1] > navy_rect.top:
            pygame.draw.rect(win, black, [navy_rect.left - 2, navy_rect.top - 2, width + 1, height + 1], 2)
            if click[0] == 1:
                colour = navy
        else:
            pygame.draw.rect(win, gray, [navy_rect.left - 2, navy_rect.top - 2, width + 1, height + 1], 2)
        if purple_rect.left + width > mouse[0] > purple_rect.left and purple_rect.top + height > mouse[
            1] > purple_rect.top:
            pygame.draw.rect(win, black, [purple_rect.left - 2, purple_rect.top - 2, width + 1, height + 1], 2)
            if click[0] == 1:
                colour = purple
        else:
            pygame.draw.rect(win, gray, [purple_rect.left - 2, purple_rect.top - 2, width + 1, height + 1], 2)
        if brown_rect.left + width > mouse[0] > brown_rect.left and brown_rect.top + height > mouse[1] > brown_rect.top:
            pygame.draw.rect(win, black, [brown_rect.left - 2, brown_rect.top - 2, width + 1, height + 1], 2)
            if click[0] == 1:
                colour = brown
        else:
            pygame.draw.rect(win, gray, [brown_rect.left - 2, brown_rect.top - 2, width + 1, height + 1], 2)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("save", smallText)
        textRect.center = ((65 + (85 / 2)), (330 + (height / 2)))
        win.blit(textSurf, textRect)

        if save.left + 65 > mouse[0] > save.left and save.top + height > mouse[1] > save.top:
            if click[0] == 1:
                pygame.image.save(win, "image.jpg")
                print("the image has been saved")

pygame.quit()
