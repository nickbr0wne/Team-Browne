import pygame
import src.model as model
from src.constant import WIDTH
import src.view as view
from src.utility import has_won, has_drawn

# Initializing Pygame
pygame.init()

# Images
BACK_IMAGE = pygame.transform.scale(pygame.image.load("assets/background.png"), (500, 500))
X_IMAGE = pygame.transform.scale(pygame.image.load("assets/chewbacca.png"), (150, 150))
O_IMAGE = pygame.transform.scale(pygame.image.load("assets/porg.png"), (150, 150))

chewwie = pygame.mixer.Sound("assets/chewbacca1.wav")
porg = pygame.mixer.Sound("assets/porg1.wav")


# Fonts
END_FONT = pygame.font.SysFont("assets/starwars.ttf", 40)


# Screen
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("***   Tic-Tac-Toe   ***")


def main():
    global x_turn, o_turn, images, draw

    images = []
    draw, run = False, True
    x_turn, o_turn = True, False
    game_array = model.initialize_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_turn, o_turn, images = view.click(game_array, X_IMAGE, chewwie, O_IMAGE, porg, x_turn, o_turn, images)

        model.render(win, BACK_IMAGE, images)

        if has_won(game_array, win, BACK_IMAGE, END_FONT) or has_drawn(game_array, win, BACK_IMAGE, END_FONT):
            run = False


while True:
    if __name__ == '__main__':
        main()