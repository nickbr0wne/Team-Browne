from src.constant import WIDTH, ROWS, GRAY
import pygame


def initialize_grid():
    dis_to_cen = WIDTH // ROWS // 2
    # Initializing the array
    game_array = [[None] * ROWS for _ in range(ROWS)]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_cen * (2 * j + 1)
            y = dis_to_cen * (2 * i + 1)

            # Adding centre coordinates
            game_array[i][j] = (x, y, "", True)

    return game_array


def draw_grid(win):

    gap = WIDTH // ROWS
    # Starting points
    x = 0
    y = 0

    for i in range(ROWS):
        x = i * gap

        pygame.draw.line(win, GRAY, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(win, GRAY, (0, x), (WIDTH, x), 3)


def render(win, BACK_IMAGE, images):
    win.blit(BACK_IMAGE, (0, 0))
    draw_grid(win)

    # Drawing X's and O's
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()
