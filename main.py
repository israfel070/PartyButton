import sys, pygame.mixer, random
from pygame.locals import *

display_width = 1136
display_height = 640

button_width = (250, 250)

text_size = 200

wait_duration = 100

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 53, 94)
Watermelon = (253, 91, 120)
Orange = (255, 96, 55)
Tangerine = (255, 153, 102)
Carrot = (255, 153, 51)
Sunglow = (255, 204, 51)
Lemon = (255, 255, 102)
Lime = (204, 255, 0)
Green = (102, 255, 102)
Mint = (170, 240, 209)
Blue = (80, 191, 230)
Pink = (255, 110, 255)
Rose = (238, 52, 210)
Purple = (255, 0, 204)

colors = [Red, Watermelon, Orange, Tangerine, Carrot, Sunglow, Lemon,
          Lime, Green, Mint, Blue, Pink, Rose, Purple]

done = False

FPS = 60

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('celebration.mp3')

pygame.display.set_caption('Party Button')


gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
gameDisplay.fill(White)


button_img = pygame.image.load('redbutton.png')
button_img = pygame.transform.scale(button_img, button_width)
button_rect = button_img.get_rect(center=gameDisplay.get_rect().center)
gameDisplay.blit(button_img, button_rect)
pygame.display.update()


def random_color():
    random_fill = random.choice(colors)
    gameDisplay.fill(random_fill)


def party_time():
    while not done:
        random_color()
        font = pygame.font.SysFont('Franklin Gothic', text_size, False, False)
        text = font.render("PARTY MODE!", False, White)
        text_rect = text.get_rect(center=(display_width / 2, display_height / 2))
        gameDisplay.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(wait_duration)


def button_click():
    pygame.mixer.music.play()
    party_time()


while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            button_rect = Rect((display_width/2), (display_height/2), (display_width/2), (display_height/2))
            if button_rect.collidepoint(x,y):
                button_click()
