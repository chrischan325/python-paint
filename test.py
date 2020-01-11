import pygame

pygame.init()
win = pygame.display.set_mode((1000, 700))
white = [255, 255, 255]
black = [0, 0, 0]
win.fill(white)

run = True
save = pygame.draw.rect(win, black, [65, 330, 85, 35], 2)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Save", smallText)
        textRect.center = ((65 + (85 / 2)), (330 + (35 / 2)))
        win.blit(textSurf, textRect)
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(15)

pygame.quit()
