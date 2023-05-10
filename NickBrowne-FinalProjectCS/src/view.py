import pygame
import math
from src.constant import WIDTH, ROWS


def click(game_array, X_IMAGE, chewwie, O_IMAGE, porg, x_turn, o_turn, images):

    x_t, o_t, img = x_turn, o_turn, images

    # Mouse position
    m_x, m_y = pygame.mouse.get_pos()

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char, can_play = game_array[i][j]

            # Distance between mouse and the centre of the square
            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

            # If it's inside the square
            if dis < WIDTH // ROWS // 2 and can_play:
                if x_t:  # If it's X's turn
                    img.append((x, y, X_IMAGE))
                    pygame.mixer.Sound.play(chewwie)
                    pygame.mixer.music.stop()

                    x_t = False
                    o_t = True
                    game_array[i][j] = (x, y, 'Chewbacca', False)

                elif o_t:  # If it's O's turn
                    img.append((x, y, O_IMAGE))
                    pygame.mixer.Sound.play(porg)
                    pygame.mixer.music.stop()
                    x_t = True
                    o_t = False
                    game_array[i][j] = (x, y, 'Porg', False)

    x_turn, o_turn, images = x_t, o_t, img
    return x_turn, o_turn, images